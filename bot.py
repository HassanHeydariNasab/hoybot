#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import os
import telepot
from telepot.delegate import per_chat_id, create_open
import re
from random import choice
#from peewee import *
import BeautifulSoup
#from hazm import *
import urllib2
import subprocess
from time import sleep
#print a
class Babilo(telepot.helper.ChatHandler):
    def __init__(self, seed_tuple, timeout):
        super(Babilo, self).__init__(seed_tuple, timeout)
        
    def on_message(self, msg):
        if msg.has_key(u'document'):
            self.sender.downloadFile(msg[u'document'][u'file_id'], file_path="~/dl")
        m = msg['text'].split(' ')
        mr = msg['text']
        fn = msg['from']['first_name']
        if m[0] == u'/start':
            r = u'سلام به تو که اسمتو گذاشتی ' + unicode(fn)
        elif m[0] == u'mojose':
            r = msg
        elif m[0] == u'dimodo' and m[1] == u'source':
            f = open("bot.py", 'r')
            self.sender.sendDocument(f)
        elif m[0] == u'dimodo' and m[1] == u'k':
            process = subprocess.Popen(['/bin/bash'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            process.stdin.write('(sleep 5 && ./bot_killer.sh)&\n')
            sleep(2)
            process.kill()
            #print process.stdout.readline()
        elif m[0] == u'dimodo':
            process = subprocess.Popen(['/bin/bash'], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,bufsize = 1, universal_newlines = True)
            process.stdin.write(mr[6:]+';echo nenio!\n')
            r = process.stdout.readline()
            process.kill()
            if r == "":
                r = "error!"
            if len(r) > 4000:
                r = u'too long!'
        elif m[0] == u'هوی':
            if re.search(u'تخم|کیر|کسخل|کون|کون|الاغ|الاق|خر|جنده\
            |گای|پستون|ممه|گوز|شاش|جیش|قبحه|جلق|جق|سگ|گائ|گاتو|گامو|فاک|ساک|fuck|کوس|کوص|کص|سکس|پورن|porn|الکسیس\
            |گاشو', mr) \
            or re.search('رید ', mr) or u'گا' in m or u'شق' in m \
            or u'منی' in m:
                r = choice([u'بی‌ادب :|', u'بی‌تربیت :|', u'بی‌شخصیت :|',u'عفت کلام داشته باش یه ذره :|', u'دهنتو آب بکش :|'])
            elif m[1] == u'سلام' or m[1] == u'درود':
                r = choice([u'سلام', u'علیک سلام'])
            elif len(m) >= 3 and m[1] == u'بگو':
                r = mr[8:]
            elif m[1] == u'چطوری؟' or m[1] == u'خوبی؟':
                r = choice([u'خوبم ممنون.',u'خوبم.', u'بد نیستم.', u'خوبم. خوبی؟', u'خوبم ممنون. شما خوب هستید؟'])    
            elif m[1] == u'خداحافظ' or m[1] == u'خدافظ' or m[1] == u'بای' or m[1] == u'فعلاً' or m[1] == u'فعلا':
                r = choice([u'به سلامت', u'می‌ری درم ببند.', u'خداحافظ', u'بای'])
            elif m[1] == u'خوبی' or m[1] == u'چطوری':
                r = u'باشه :/'
            elif len(m) == 3:
                    if m[1]+u' '+m[2] == u'حالت خوبه':
                        r = u'باشه :/'
                    elif m[1]+u' '+m[2] == u'حالت خوبه؟':
                        r = choice([u'خوبم ممنون.',u'خوبم.', u'بد نیستم.', u'خوبم. خوبی؟', u'خوبم ممنون. شما خوب هستید؟'])
                    elif m[1]+u' '+m[2] == u'چه خبر؟':
                        response = urllib2.urlopen('http://www.farsnews.com/RSS')
                        rss = response.read()
                        soup = BeautifulSoup.BeautifulSoup(rss)
                        all_title = soup.findAll('title')
                        def get_link(nth):
                            item = soup.findAll('item')[nth]
                            link = re.search(r'http://www.farsnews.com/(\d+)',unicode(item)).group(0)
                            return link
                        r = unicode(all_title[2]).replace('<title>', '<a href="%s">'%get_link(0), 2).replace('</title>', '</a>') + '\n\n' + \
                            unicode(all_title[3]).replace('<title', '<a href="%s"'%get_link(1), 2).replace('</title>', '</a>') + '\n\n' + \
                         unicode(all_title[4]).replace('<title', '<a href="%s"'%get_link(2), 2).replace('</title>', '</a>')
                    else:
                        r = u'نمی‌فهمم چی می‌گی.'
            else:
                r = u'نمی‌فهمم چی می‌گی.'
        self.sender.sendMessage(r,parse_mode='HTML')


#TOKEN = sys.argv[1]  # get token from command-line
TOKEN = '198468455:AAGuz1mME3fSsf2hHrSh2zsqVlzf1_XM2rc'
bot = telepot.DelegatorBot(TOKEN, [
    (per_chat_id(), create_open(Babilo, timeout=1)),
])
#bot = telepot.async.Bot(TOKEN, )
#bot.setWebhook('https://bot-ajor.rhcloud.com')
bot.notifyOnMessage(run_forever=True)
