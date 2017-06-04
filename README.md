This version is as same as oToToT's. It's to be adapted.

The reason for making this fork is just to let this python script,
apply directly in pttbbs or even other TelnetBBS-system (such as Maple-itoc, SOB, or other BBS version)

And it's function going to be made more simply, 
and just focus on how to simplify the core python script to analyze the info requested from Central Weather Bureau in Taiwan.

And just for test and fun.

***

# AutoWeatherBBS

Post daily weather information on ptt or any other bbs.
This version can be post directly by [CurrrentPtt BBS System](https://github.com/ptt/pttbbs).

## HOWTO

Download python3 and use pip to install requests.

Clone this repository and install into your BBS binary directory (`/home/bbs/bin`)
Apply an Authorization key of [CWB OpenData](http://opendata.cwb.gov.tw/) and edit the authKey variable in weatherBIG5.py

use `crontab -e` to add your regularly work into it, to make it run automaticly.
(If you want to know how to set up, use `man crontab` to get help)

That's it!
