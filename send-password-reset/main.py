import os
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests

exec(requests.get("https://raw.githubusercontent.com/xncee/Instagram-send-password-reset/main/send-password-reset/src/src.py").text)