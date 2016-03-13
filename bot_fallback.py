#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import telepot
from telepot.delegate import per_chat_id, create_open
import re
import subprocess

class Babilo(telepot.helper.ChatHandler):
    def __init__(self, seed_tuple, timeout):
        super(Babilo, self).__init__(seed_tuple, timeout)
        
    def on_message(self, msg):
        m = msg['text'].split(' ')
        mr = msg['text']
        if m[0] == u'mojose':
            r = 'fallback'
        elif m[0] == u'dimodo' and m[1] == u'k':
            r = u"Main bot killed. I\'m fallabck bot! I\'ll running while main bot is sick!"
        elif m[0] == u'dimodo':
            process = subprocess.Popen(['/bin/bash'], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            process.stdin.write(mr[6:]+'\n')
            r = process.stdout.readline()
        self.sender.sendMessage(r)


#TOKEN = sys.argv[1]  # get token from command-line
TOKEN = '198468455:AAGuz1mME3fSsf2hHrSh2zsqVlzf1_XM2rc'
bot = telepot.DelegatorBot(TOKEN, [
    (per_chat_id(), create_open(Babilo, timeout=10)),
])
#bot.setWebhook('https://bot-ajor.rhcloud.com')
bot.notifyOnMessage(run_forever=True)
