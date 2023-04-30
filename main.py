import requests
import json
import time

mpsessid = '<mpsessid>'
if mpsessid == '<mpsessid>':
    print("Please fill out the mpsessid")
    exit(1)
barkUrl = 'https://api.day.app/6RjyBp6nrSfg8Y8sra4W9c/有票了'
headers = {'Host': 'ticket.sstm.org.cn', 'Connection': 'keep-alive',
           'mpsessid': mpsessid,
           'content-type': 'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip,compress,br,deflate',
           'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                         'like Gecko) Mobile/15E148 MicroMessenger/8.0.32(0x18002033) NetType/3G Language/zh_CN',
           'Referer': 'https://servicewechat.com/wx1d7ddce169710ba7/42/page-frame.html'}
url = 'https://ticket.sstm.org.cn/vendor/reserve/getReservePeriodListByDate.xhtml?stadiumId=69001&reservedate=2023-04' \
      '-28&appId=wx1d7ddce169710ba7'
while True:
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print(r.text)
        print('request failed!')
        time.sleep(20)
    else:
        data = json.loads(r.text)
        if not data['success']:
            print('request failed!')
            print(r.text)
            print("rate limited! waiting 20 seconds")
            time.sleep(20)
        else:
            if data['data']['reservePeriodList'][0]['avaiablenum'] > 0 or data['data']['reservePeriodList'][1][
                'avaiablenum'] > 0 or data['data']['reservePeriodList'][0]['availableNum'] > 0 or \
                    data['data']['reservePeriodList'][1]['availableNum'] > 0:
                requests.get(barkUrl)
                print(time.asctime(time.localtime(time.time())), " ticket available")
            else:
                print(time.asctime(time.localtime(time.time())), " ticket unavailable")
            time.sleep(5)
