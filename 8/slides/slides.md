---
marp: true
theme: gaia
---
# Session 8
## Advanced Web Development
---
## Agenda
* Revisit Authentication
* Authorization
    * Permissions & roles
* What if you really want to store passwords?
    * Encryption vs Hashing
---

## Token Authentication
Delegate responsibilities to 3rd party.

![](authenticate.png)

---
![](authenticate1.png)

---

![](authenticate2.png)

---

https://ms10596.us.auth0.com/
authorize?audience=sunday
&response_type=token
&client_id=MMFAWwCM4zHFY4WWHqE2i6enUdoiyzaD
&redirect_uri=http://127.0.0.1:8100/tabs/user-page

---

Hashing | Encryption
--- | ---
 Cannot be decoded | Can be decoded using a key    
 To attack: Rainbow table | To attack: Brute Force
 SHA256, MD5 | DES, AES, 3DES, bcrypt, scrypt


Symmetric | Asymettric Encryption
--- | ---
 Needs only one key to encode & decode | Needs public key to encrypt and private key to decrypt or vice versa.
---

![bg 75%](../../udacity.gif)

> [_](https://docs.google.com/forms/d/e/1FAIpQLSe22HYBxvujLSY6nrvu_poLv4FBDS1allyPqJn18DhnSNep6A/viewform?usp=sf_link)