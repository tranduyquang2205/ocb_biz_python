import requests

session = requests.Session()

if not session.cookies:
    print("No cookies yet",session.cookies)
else:
    print("Cookies exist")
