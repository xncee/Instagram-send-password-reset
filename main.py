import os, uuid, string, random
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
class Xnce():
    def __init__(self):
        print("""
██╗  ██╗███╗   ██╗ ██████╗███████╗
╚██╗██╔╝████╗  ██║██╔════╝██╔════╝
 ╚███╔╝ ██╔██╗ ██║██║     █████╗
 ██╔██╗ ██║╚██╗██║██║     ██╔══╝
██╔╝ ██╗██║ ╚████║╚██████╗███████╗
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝
              Instagram: @xnce / @ro1c\n""")
        self.target = input("[+] Target: ")
        if self.target[0]=="@":
            print("[-] Enter User Without '@' ")
            input()
            exit()
        self.lookup()
        self.send_password_reset()
    def lookup(self):
        head = {"user-agent": f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; en_GB;)",}
        data = {
            "phone_id": uuid.uuid4(),
            "q": self.target,
            "guid": uuid.uuid4(),
            "device_id": uuid.uuid4(),
            "android_build_type":"release",
            "waterfall_id": uuid.uuid4(),
            "directly_sign_in":"true",
            "is_wa_installed":"false"
        }
        req = requests.post("https://i.instagram.com/api/v1/users/lookup/", headers=head, data=data)
        if "email_sent" in req.text and "user_id_na" not in req.text:
            self.user_id = req.json()["user"]["pk"]
            self.data = {
                "_csrftoken": "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=32)),
                "user_id": self.user_id,
                "guid": uuid.uuid4(),
                "device_id": uuid.uuid4()
            }
        elif "user_id_na" in req.text:
            self.data = {
                "_csrftoken": "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=32)),
                "user_email": self.target,
                "guid": uuid.uuid4(),
                "device_id": uuid.uuid4()
            }
        else:
            print(f"[-] {req.text} {req.status_code}")
            input()
            exit()
    
    def send_password_reset(self):
        head = {"user-agent": f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; en_GB;)"}
        req = requests.post("https://i.instagram.com/api/v1/accounts/send_password_reset/", headers=head, data=self.data)
        #print(req.text, req.status_code)
        if "obfuscated_email" in req.text: 
            print(f"[+] {req.text}")
            input()
            exit()
        else:
            print(f"[-] {req.text}")
            input()
            exit()
Xnce()
