This version is as same as oToToT's. It's to be adapted.

The reason for making this fork is just to let this python script,
apply directly in pttbbs or even other TelnetBBS-system (such as Maple-itoc, SOB, or other BBS version)

And it's function going to be made more simply, 
and just focus on how to simplify the core python script to analyze the info requested from Central Weather Bureau in Taiwan.

And just for test and fun.

# AutoWeatherPtt

Post daily weather information on ptt or any other bbs.

##HOWTO

Download python3 an use pip to install requests.

Apply an Authorization key of http://opendata.cwb.gov.tw/ and edit the authKey variable in weather.py

edit user , password and board variables in weather.py

Also you can edit host variable if needed

After doing all these preparation, you can just run it or use crontab and the --check=false paramter to post it timely

p.s if you don't want it bottom your post you can add --buttom=false paramter

