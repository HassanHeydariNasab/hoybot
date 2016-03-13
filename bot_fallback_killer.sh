#!/bin/bash
pi=`ps -ef | grep "/usr/bin/python2.7 ./bot_fallback.py" | awk '{print $2}'`
pii=`echo $pi | cut -d " " -f1`
kill -9 $pii
#echo $pii $1 > ppp
#sleep 1
#/usr/bin/python2.7 ./bot.py
