import requests
import xml.etree.ElementTree as ET


# Apply an Authorization key of http://opendata.cwb.gov.tw/ and edit the authKey variable
authKey = "**********"

def add0(s):
    if len(s) == 1:
        return "0"+s
    else:
        return s

def addTColor(s):
    #print(s)
    cp = int(turnSmall(s))
## \x15(^U) > \x1b(ESC)
    if cp <= 10:
        return "\x1b[1;34m"+s+"\x1b[m"
    elif cp<= 15:
        return "\x1b[36m"+s+"\x1b[m"
    elif cp<= 20:
        return "\x1b[1;36m"+s+"\x1b[m"
    elif cp<= 25:
        return "\x1b[1;33m"+s+"\x1b[m"
    elif cp<= 30:
        return "\x1b[34m"+s+"\x1b[m"
    elif cp<= 35:
        return "\x1b[31m"+s+"\x1b[m"
    else:
        return "\x1b[1;31m"+s+"\x1b[m"
    
def addWColor(s):
    cp = int(turnSmall(s))
    if cp == 0:
        return s
    elif cp<= 20:
        return "\x1b[1m"+s+"\x1b[m"
    elif cp<= 40:
        return "\x1b[1;36m"+s+"\x1b[m"
    elif cp<= 60:
        return "\x1b[36m"+s+"\x1b[m"
    elif cp<= 80:
        return "\x1b[1;34m"+s+"\x1b[m"
    else:
        return "\x1b[34m"+s+"\x1b[m"
def addN(s):
    if(len(s)<11):
        return(s+"  "*(11-len(s)))
    return s
def turnSmall(s):
    Small = {}
    Small[chr(0xff10) ] = '0'
    Small['１'] = '1'
    Small['２'] = '2'
    Small['３'] = '3'
    Small['４'] = '4'
    Small['５'] = '5'
    Small['６'] = '6'
    Small['７'] = '7'
    Small['８'] = '8'
    Small['９'] = '9'
    opt = ''
    for k in range(0,len(s)):
        opt = opt + Small[(s[k])]
    return(opt)
def turnFull(s):
    Full = "０１２３４５６７８９"
    opt = ''
    for k in range(0,len(s)):
        opt = opt + Full[int(s[k])]
    return(opt)
def addNinFront(s):
    if(len(s)<2):
        return("　"+s)
    return s

def main():
    content = ''
#    print("Downloading Data...")
    r = requests.get('http://opendata.cwb.gov.tw/opendataapi?dataid=F-C0032-001&authorizationkey='+authKey)
#    print("Parsing Data...")
    root = ET.fromstring(r.text)
#    print("Analysising Data")
    d = root[8][0][1].text.split("T")[0].split("-")

    tle="test"
    if root[8][1][1][1][0].text.split("T")[1].split(':')[0] == '18':
        tle = root[8][1][1][1][0].text.split("T")[0].split('-')[0]+"/"+add0(root[8][1][1][1][0].text.split("T")[0].split('-')[1])+"/"+add0(root[8][1][1][1][0].text.split("T")[0].split('-')[2])+' 晚上'
    elif root[8][1][1][1][0].text.split("T")[1].split(':')[0] == '12':
        tle = root[8][1][1][1][0].text.split("T")[0].split('-')[0]+"/"+add0(root[8][1][1][1][0].text.split("T")[0].split('-')[1])+"/"+add0(root[8][1][1][1][0].text.split("T")[0].split('-')[2])+' 中午'
    else:
        tle = root[8][1][1][1][0].text.split("T")[0].split('-')[0]+"/"+add0(root[8][1][1][1][0].text.split("T")[0].split('-')[1])+"/"+add0(root[8][1][1][1][0].text.split("T")[0].split('-')[2])+' 白天'
    content += ("\n發布時間："+ turnFull(str( int(d[0])-1911 )) + '年' + turnFull(d[1]) + '月' +  turnFull(d[2]) + '日' + turnFull( root[8][0][1].text.split("T")[1].split(":")[0] ) + "時 ０分\n")
    content += ("有效時間："+turnFull(root[8][1][1][1][0].text.split("T")[0].split('-')[2]) + '日' + turnFull(root[8][1][1][1][0].text.split("T")[1].split(':')[0]) + '時起至' + turnFull(root[8][1][1][1][1].text.split("T")[0].split('-')[2]) + '日' + turnFull(root[8][1][1][1][1].text.split("T")[1].split(':')[0])+'時\n')
    content += ('\n預 報 分 區 天       氣           雨率   氣溫(攝氏)\n\n')
    for index in range(1,23):
        content += ('＊' + root[8][index][0].text + '    ' + addN(root[8][index][1][1][2][0].text) + addNinFront( addWColor( turnFull( root[8][index][5][1][2][0].text ) ) ) + "％ " + addTColor(turnFull(root[8][index][3][1][2][0].text)) + " － " +addTColor(turnFull(root[8][index][2][1][2][0].text))+'\n')

    content += ('\n＊備註：各縣市預報係以各縣市政府所在地附近為預報參考位置。\n')
    content += ('\n----資料來源:中央氣象局---\n--- Coded By oToToT@ptt2 / Adapted by r2@CTB ---\n\n')

# Writing information to "weather.post" text files in Big5 (for BBS system in Taiwan)
    file = open('/home/bbs/etc/weather.post', 'w', encoding = 'Big5')
    file.write(content)
    file.close()    

main()
