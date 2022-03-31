"""
JSON_request -

协议 - 通信双方需要遵守的规则
HTTP/HTTPS ---> 通过URL访问网络资源协议  --- Hyper-Text Transfer Protocol (超文本传输协议)

请求(request) - 响应(respond)
Author : wangyiwen03
Date : 2022/3/10
"""
import json

import requests

resp = requests.get(
    url='http://api.tianapi.com/esports/index',
    params={'key': '797f584a50b9229025e278ad0e91a242', 'num': 20}
)

news_dict = resp.json()
news_list = news_dict['newslist']
for news in news_list:
    print(news['title'])
    print(news['url'])
