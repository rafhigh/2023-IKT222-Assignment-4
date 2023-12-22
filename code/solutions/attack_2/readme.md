# Attack 2 - SQL injection

In this attack I performed a SQL injection which essentially means that I injected code into an input field in the form of a query language. This is in order to gain unauthorized access to Jonas Dahl's internal user page on the website without having to know the password.

I execute the attack by entering the username "jonas.dahl" and the following query input into the form for the password.
```python
' OR '1'='1
```
This essentially exploits a weakness where the user input is not properly validated and allows us to modify the query code line used to check if the inputted password is correct.