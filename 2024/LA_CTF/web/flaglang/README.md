# flaglang
> Do you speak the language of the flags?

By inspecting `src/countries.yaml`, it is obvious that the flag is
the first few line of the file.
```yaml
%YAML 1.1
---
Flagistan:
  iso: FL
  msg: "<REDACTED>"
  password: "<REDACTED>"
  deny: [...]
```
Then I look into `src/app.js`, there is no way for me to get `password`. However I can get `msg` with the following entry.
```js
app.get('/view', (req, res) => {
  if (!req.query.country) {
    res.status(400).json({ err: 'please give a country' });
    return;
  }
  if (!countries.has(req.query.country)) {
    res.status(400).json({ err: 'please give a valid country' });
    return;
  }
  const country = countryData[req.query.country];
  const userISO = req.signedCookies.iso;
  if (country.deny.includes(userISO)) {
    res.status(400).json({ err: `${req.query.country} has an embargo on your country` });
    return;
  }
  res.status(200).json({ msg: country.msg, iso: country.iso });
});
```

### Goal:
- pass three check
  - `req.query.country` not empty and it is in `countries`
    - The only country that match is `Flagistan`
  - `countryData["Flagistan"].deny` does not include `req.signedCookies.iso`
  
## Solve
To solve the question, we only need to send a request with query, and not carrying any cookies.

It can be done by typing the following command:

`curl https://flaglang.chall.lac.tf/view?country=Flagistan`

The flag will then be printed on the terminal