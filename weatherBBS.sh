#!/bin/sh

case "$1" in

day)
    echo '(no information)' > /home/bbs/etc/weather.post
    /usr/bin/python3 /home/bbs/bin/weatherBIG5.py
    /home/bbs/bin/addpost 'SYSTEM' 'SYSOP' '夢之精靈' "[記錄] [ `date +%-0m` 月 `date +%-0d` 日] 全臺今日各地白天天氣" etc/weather.post
    ;;

night)
    echo '(no information)' > /home/bbs/etc/weather.post
    /usr/bin/python3 /home/bbs/bin/weatherBIG5.py
    /home/bbs/bin/addpost 'SYSTEM' 'SYSOP' '夢之精靈' "[記錄] [ `date +%-0m` 月 `date +%-0d` 日] 全臺今日各地晚上天氣" etc/weather.post
    ;;

*)
    echo "Usage ${0} {day|night}"
    ;;

esac

exit 0

