YOUR_DOMAIN = ""
API_IDENTIFIER = ""
YOUR_CLIENT_ID = ""
YOUR_CALLBACK_URI = "http://127.0.0.1:8100/tabs/user-page"

url = f"""https://{YOUR_DOMAIN}/\
authorize?audience={API_IDENTIFIER}\
&response_type=token\
&client_id={YOUR_CLIENT_ID}\
&redirect_uri={YOUR_CALLBACK_URI}"""


print(url)
