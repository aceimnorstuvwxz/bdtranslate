#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 ch3n.co


import httplib
import md5
import urllib
import random
import json

def translate(appid, secretKey, fromLang, toLang, srcString):

    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = srcString
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)

    sign = appid+q+str(salt)+secretKey
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
 
    trRet = ''
    try:
        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        ret =  response.read()
        jobj = json.loads(ret)
        trRet = jobj['trans_result'][0]['dst']
        
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
    
    return trRet


if __name__ == "__main__":
    appid = '20170221000039563'
    secretKey = 'nIyk6j2N4pOIc3PpE9tY'
    fromLang = 'en'
    toLang = 'zh'
    print translate(appid, secretKey, fromLang, toLang, "Prisident reject to lough out loudly, interesting!")

