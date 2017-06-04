This version is adapted from oToToT's version.

The reason for making this fork is just to let this python script,
apply directly in pttbbs or even other TelnetBBS-system (such as Maple-itoc, SOB, or other BBS version)

And it's function going to be made more simply, 
and just focus on how to simplify the core python script to analyze the info requested from Central Weather Bureau in Taiwan.

And just for test and fun.

***

# AutoWeatherBBS

Post daily weather information on ptt or any other bbs.
This version can be post directly by [CurrentPtt BBS System](https://github.com/ptt/pttbbs).

## HOWTO

### Install Python3 & "request" module
Download `python3` and use `pip` to install `requests`.

### Get this source and Install it!

First, you must `su bbsadm` to get into BBS system account.

Clone this repository and install into your BBS binary directory (`/home/bbs/bin`):
`git clone --branch clam-test https://github.com/holishing/AutoWeatherBBS`
`cp AutoWeatherBBS/weatherBBS.sh /home/bbs/bin/`
`cp AutoWeatherBBS/weatherBIG5.py /home/bbs/bin/`

Apply an Authorization key of [CWB OpenData](http://opendata.cwb.gov.tw/),
<br>and edit the `authKey` variable in `/home/bbs/bin/weatherBIG5.py` file

### Setting crontab file for BBS

And use `crontab -e` to add your regularly work into it, to make it run automaticly.
(If you want to know how to set up, use `man crontab` to get help)

or you can try:
`crontab -l > ~/crontab.now`
`cat AutoWeatherBBS/crontab.reference >> ~/crontab.now`
`crontab ~/crontab.now`
to add this crontab to run regularly.

***

That's it!
