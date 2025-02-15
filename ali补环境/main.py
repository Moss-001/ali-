#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：ALI补环镜 
@File    ：main.py
@IDE     ：VScode 
@Author  ：liyuda
@Date    ：2025/2/11 18:43 
'''
import requests
import time
import re
import json
import subprocess
from loguru import logger
times = 0
for i in range(10):
    session = requests.session()
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    params = {
        'serviceType': '01',
        'bussTypeln': '',
        'phone': '',
        'channelKey': 'sxwx',
        'joinSign': '',
    }
    response = session.get('https://upay.10010.com/upay-wap/', params=params, headers=headers)
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://upay.10010.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }
    t = "FFFF0N0N000000009296:"+str(int(time.time()))+":0.4619966069361052"
    url = "https://cf.aliyun.com/nocaptcha/initialize.jsonp"
    params = {
        "a": "FFFF0N0N000000009296",
        "t": t,
        "scene": "nc_other_h5",
        "lang": "cn",
        "v": "v1.3.21",
        "href": "https://upay.10010.com/upay-wap/",
        "comm": {},
        "callback": "initializeJsonp_015518708121417046"
    }
    response = session.get(url, headers=headers, params=params)

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://upay.10010.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }
    result = subprocess.run(['node', 'test.js'], capture_output=True, text=True,encoding='utf-8')
    n = result.stdout
    logger.info(n)
    url = "https://cf.aliyun.com/nocaptcha/analyze.jsonp"
    params = {
        "a": "FFFF0N0N000000009296",
        "t":t,
        "n": n,
        "p": {"key1":"code200","ncbtn":"71.57292175292969|411.84375|53.72916793823242|23.875|411.84375|435.71875|71.57292175292969|125.30208969116211",
            "umidToken":"T2gAWxCRKe0-hJjZl49GtGbis8CK8NjvoIrgLv3KTDppj6F3iduWRP2QEacpgtBsrYU=","ncSessionID":"779f1eba1ce","et":"1"}
    ,
        "scene": "nc_other_h5",
        "asyn": "0",
        "lang": "cn",
        "v": "1",
        "callback": "jsonp_04511053710993753"
    }
    response = session.get(url, headers=headers, params=params)
    jsonp_response = response.text
    match = re.search(r'\((\{.*\})\)', jsonp_response)
    if match:
        json_data = match.group(1)
        parsed_data = json.loads(json_data)
        code = parsed_data['result']['code']
        if(code == 0):
            times += 1
            logger.success(jsonp_response)
            logger.success("成功次数: {}", times)
            