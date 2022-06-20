#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import random

print("正在加载聊天机器人...")
API_KEY = 'fcsQcF9yHoayIPSIFMXqfGlP'
SECRET_KEY = 'YQaBzgiBSGqlcjGHioIW6KGWg78n5CdG'
APPID = 26490425
ROBOT_ID = 'S71244'
SKILL_ID = '1204023'

host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(API_KEY, SECRET_KEY)
response = requests.get(host)
access_token = response.json()['access_token']

url = 'https://aip.baidubce.com/rpc/2.0/unit/service/v3/chat?access_token=' + access_token
log_id = str(random.randint(1000000, 9999999))
session_id = ''

print("加载成功！说点什么以唤醒机器人。")
while True:
    question = input()
    if (question == ""):
        break
    post_data = {
        'version': '3.0',
        'service_id': ROBOT_ID,
        'session_id': session_id,
        'log_id': log_id,
        'request': {'terminal_id': '88888', 'query': question}
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(post_data), headers=headers)
    print(response.json()['result']['responses'][0]['actions'][0]['say'])
    session_id = response.json()['result']['session_id']
