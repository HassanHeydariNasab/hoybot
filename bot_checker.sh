#!/bin/bash

while true
do
echo "Checking to see if bot.py is running:"
sleep 3
if  `pgrep "bot.py" >/dev/null 2>&1`
then
    echo "main bot Running"
else
    echo "main bot not Running.killing fallback and try to run main bot"
    ./bot_fallback_killer.sh
    e=`(/usr/bin/python2.7 ./bot.py); echo $?`
    if [ $e -eq 1 ]
    then
        echo "check fallback bot"
        if  `pgrep "bot_fallback.py" >/dev/null`
        then
            echo "fallback bot already run"
        else
            echo "fallback bot not running. try to run it."
            (/usr/bin/python2.7 ./bot_fallback.py)&
        fi
    else
        echo "main bot run out without error!"
    fi
fi
done