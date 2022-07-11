import requests

response=requests.get("https://www.usom.gov.tr/url-list.txt", verify=False)
file=open("usom.txt", "w", encoding="utf-8")
file.write(str(response.content))
file.close()

