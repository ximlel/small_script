#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 11:44:35 2018

A web crawlers to batch download mp3 on http://www.ysts8.com.

@author: leixin
"""
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import requests

INIT=1
N=121
NAME_IN_URL='play_20766_47_1'

if not os.path.exists(NAME_IN_URL):
    os.makedirs(NAME_IN_URL)
os.chdir(NAME_IN_URL)
head = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36'}
'''
html = requests.get(url_s,headers=head)
with open('a.html','wb') as f:
    f.write(html.content) 
from bs4 import BeautifulSoup
bsObj=BeautifulSoup(html.content,'lxml')
print(bsObj.image)
'''
driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
#driver = webdriver.Firefox()
down_url = ['0']*(N-INIT+1)
i=INIT
while i<=N:
    url='http://www.ysts8.com/'+NAME_IN_URL+'_'+str(i)+'.html'
    driver.get(url)
    driver.switch_to.frame('play')
    source=driver.page_source
#    with open(str(i+1)+'.html','wt') as f:
#        f.write(source)
#    url_str = re.search(r"url[0-9a-zA-Z\_]+ = '(.*)';\n",source)
#    if url_str:
#        exec(url_str.group(0))
#    murl_str = re.search(r"murl[0-9a-zA-Z\_]+ = '(.*)';\n",source)
#    if murl_str:
#        exec(murl_str.group(0))
#    mp3_str = re.search(r"mp3:'(.*)'\n",source)
#    exec(mp3_str.group(0).replace('mp3:',''))
#    from selenium.webdriver.support.ui import WebDriverWait
#    wait = WebDriverWait(driver,10)
#    wait.until(lambda driver: driver.find_element_by_id('jp_audio_0'))
    try:
        down = driver.find_element_by_id('jp_audio_0')
    except NoSuchElementException:
#        print('No jp_audio_0 in object ',i,'!')
        continue
    else:
        down_url[i-INIT] = str(down.get_attribute('src'))
        if len(down_url[i-INIT])>1:
            print('URL'+str(i)+': '+down_url[i-INIT])
            i+=1
driver.close()
for i in range(INIT,N+1):
    mp3_down = requests.get(down_url[i-INIT],headers=head)
    #mp3_down.urlretrieve(down_url[i-INIT],str(i)+'.mp3')
    with open(str(i)+'.mp3','wb') as f:
        f.write(mp3_down.content)
        print('Creat: '+str(i)+'.mp3!')
