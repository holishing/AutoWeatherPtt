#!/bin/sh

case "$1" in

day)
    echo '(no information)' > /home/bbs/etc/weather.post
    /usr/bin/python3 /home/bbs/bin/weatherBIG5.py
    /home/bbs/bin/post 'Record' '全臺今日各地白天天氣' '[氣象報告]' /home/bbs/etc/weather.post
    ;;

night)
    echo '(no information)' > /home/bbs/etc/weather.post
    /usr/bin/python3 /home/bbs/bin/weatherBIG5.py
    /home/bbs/bin/post 'Record' '全臺今日各地晚上天氣' '[氣象報告]' /home/bbs/etc/weather.post
    ;;

*)
    echo "Usage ${0} {day|night}"
    ;;

esac

exit 0

## Note: usage for bin/post: /home/bbs/bin/post <board name> <title> <owner> <file>
