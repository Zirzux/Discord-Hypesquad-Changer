import requests 

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
with open('bios.txt','r') as handle:
        bios = handle.readlines()
        for x in bios:
            bios = x.rstrip()
          
def squad():
    houseid = input("[>] Choices - 1, 2, 3\n[>] House Id > ")

    json = {
        "house_id": f'{houseid}'
    }
    headers = {
        "Authorization": token
    }

    squadresponse = requests.post('https://discord.com/api/v9/hypesquad/online', headers=headers, json=json)
    print(f"[!] Changing Hypesquad For {token}")

    if squadresponse.status_code == '200':
        print("[-] Error Changing Hypesquad")
    else:
        print("[!] Hypesquad Changed!")
squad()
