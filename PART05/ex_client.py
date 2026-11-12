import json, urllib.request, urllib.error
URL = "http://127.0.0.1:8000"
for path in ("/status", "/start", "/status", "/hello"):
    try:
        r = urllib.request.urlopen(URL + path)
        text = r.read().decode()
        print(path, r.status, text)
    except urllib.error.HTTPError as e:
        print(path, e.code, "오류")
s = json.loads(urllib.request.urlopen(URL + "/status").read())
print("지금 모드:", s["mode"])
