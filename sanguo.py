import requests
import json
from datetime import datetime
import time
from random import randint


'''
authorization: Bearer 替换成你的，安卓reqable或者ios-stream都可以抓
'''

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b11)XWEB/9185",
        'Content-Type': "application/json",
        'current-uri': "subPackages/index/welfare/welfare",
        'AppVersion-Code': "",
        'Authorization': "替换成你的，安卓reqable或者ios-stream都可以抓",
        'App-System': "weixin",
        'xweb_xhr': "1",
        'platform': "weixin",
        'client-Id': "",
        'App-Version': "",
        'Sec-Fetch-Site': "cross-site",
        'Sec-Fetch-Mode': "cors",
        'Sec-Fetch-Dest': "empty",
        'Referer': "https://servicewechat.com/wxd67100c9bcf72279/550/page-frame.html",
        'Accept-Language': "zh-CN,zh;q=0.9"
        }

class sanguosha:
    def __init__(self, headers):
        self.headers = headers
        # print(self.headers)
        
    def sign_in(self):
        print('sign_in')
        url = "https://wxforum.sanguosha.cn/api/user/signIn"
        payload = json.dumps({})
        response = requests.post(url, data=payload, headers=self.headers)
        data = json.loads(response.text).get('msg')
        print(f'签到{data}')

    def get_topic(self):
        print('get_topic')
        url = "https://wxforum.sanguosha.cn/api/topics"
        params = {
        'page': "1",
        'category_id': "1"
        }
        response = requests.get(url, params=params, headers=self.headers)
        data = json.loads(response.text)
        res = data.get('msg')
        data = data.get('data')
        topic_list = [i.get('id') for i in data]
        print(f'获取帖子:{res},共计{len(topic_list)}个帖子')
        return topic_list
    
    def reply(self,topic_list):
        print('reply')
        for topic_id in topic_list:
            url = f"https://wxforum.sanguosha.cn/api/topics/{topic_id}/replies"
            currentDateAndTime = datetime.now()
            currentTime = currentDateAndTime.strftime("%H:%M:%S")
            payload = {
            "contents": currentTime,
            "vote_option": ""
            }
            
            payload = json.dumps(payload)
            response = requests.post(url, data=payload, headers=self.headers)
            data = json.loads(response.text)
            print(f'回帖:',data.get('msg'),data.get('data'),data.get('message'))
            time.sleep(randint(60,90))
    
    def like(self,topic_list):
        for topic in topic_list:
            url = f"https://wxforum.sanguosha.cn/api/topics/{topic}/likes"
            payload = json.dumps({})
            response = requests.post(url, data=payload, headers=self.headers)
            data = json.loads(response.text)
            print(f'点赞:',data.get('msg'),data.get('data'))
            time.sleep(randint(2,10))

    def main(self):
        self.sign_in()
        topic_list = self.get_topic()
        self.reply(topic_list[:15])
        self.like(topic_list[:15])
        

if __name__ == "__main__":
    s = sanguosha(headers)
    s.main()