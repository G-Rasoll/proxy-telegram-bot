import requests
import json
import random
import datetime

def tarikh():
    tarikh = datetime.date.today()
    return tarikh

def api_proxy():

    req = requests.get("http://api.codebazan.ir/mtproto/json/")
    req_result = req.json()['Result']
    random_num = random.randint(1, 35)
    d = req_result[random_num]
    proxy = ('🔸{}\n\nhttps://t.me/proxy?server={}&port={}&secret={}\n\n'.format("<b>"+"Telegram Still Alive"+"</b>",d['server'],d['port'],d['secret']))
    return proxy
