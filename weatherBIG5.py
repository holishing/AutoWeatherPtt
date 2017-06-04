import requests, telnetlib, sys, time
import xml.etree.ElementTree as ET

# no need to connect to another host anymore
"""
host = 'ptt2.cc'
user = '***'
password = '***'

#board="*****"

"""

# Apply an Authorization key of http://opendata.cwb.gov.tw/ and edit the authKey variable
authKey = " "

# no need to connect to another host anymore
"""
#btm=True
"""

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
    Small[chr(0xff11) ] = '1'
    Small[chr(0xff12) ] = '2'
    Small[chr(0xff13) ] = '3'
    Small[chr(0xff14) ] = '4'
    Small[chr(0xff15) ] = '5'
    Small[chr(0xff16) ] = '6'
    Small[chr(0xff17) ] = '7'
    Small[chr(0xff18) ] = '8'
    Small[chr(0xff19) ] = '9'
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

# no need to connect to another host anymore
"""

##def WriteIntoLog():
    
#def login(host, user ,password) :
#    global telnet
#    telnet = telnetlib.Telnet(host)
#    time.sleep(1)
#    content = telnet.read_very_eager().decode('big5','ignore')
#    if "系統過載" in content :
#        print("系統過載, 請稍後再來")
#        sys.exit(0)
#        
#
#    if "請輸入代號" in content:
#        print("輸入帳號中...")
#        telnet.write((user + "\r\n").encode('big5') )
#        time.sleep(1)
#        print("輸入密碼中...")
#        telnet.write((password + "\r\n").encode('big5'))
#        time.sleep(5)
#        content = telnet.read_very_eager().decode('big5','ignore')
#        #print content
#        if "密碼不對" in content:
#           print("密碼不對或無此帳號。程式結束")
#           sys.exit()
#           content = telnet.read_very_eager().decode('big5','ignore')
#        if "您想刪除其他重複登入" in content:
#           print('刪除其他重複登入的連線....')
#           telnet.write(("n\r\n").encode('big5'))
#           time.sleep(10)
#           content = telnet.read_very_eager().decode('big5','ignore')
#        if "請按任意鍵繼續" in content:
#           print("資訊頁面，按任意鍵繼續...")
#           telnet.write(("\r\n").encode('big5') )
#           time.sleep(2)
#           content = telnet.read_very_eager().decode('big5','ignore')
#        if "您要刪除以上錯誤嘗試" in content:
#           print("刪除以上錯誤嘗試...")
#           telnet.write("n\r\n".encode('big5'))
#           time.sleep(5)
#           content = telnet.read_very_eager().decode('big5','ignore')
#        if "您有一篇文章尚未完成" in content:
#           print('刪除尚未完成的文章....')
#           # 放棄尚未編輯完的文章
#           telnet.write("q\r\na".encode('big5'))   
#           time.sleep(5)   
#           content = telnet.read_very_eager().decode('big5','ignore')
#        print("----------------------------------------------")
#        print("------------------ 登入完成 ------------------")
#        print("----------------------------------------------")
        
#    else:
#        print("沒有可輸入帳號的欄位，網站可能掛了")

#def disconnect() :
#     print("登出中...")
#     # q = 上一頁，直到回到首頁為止，g = 離開，再見
#     telnet.write("qqqqqqqqqg\r\ny\r\n".encode('big5') )
#     time.sleep(3)
#     #content = telnet.read_very_eager().decode('big5','ignore')
#     #print content
#     print("----------------------------------------------")
#     print("------------------ 登出完成 ------------------")
#     print("----------------------------------------------")
#     telnet.close()

#def post(title, content) :
#        print('發文中...')
#        # s 進入要發文的看板
#        telnet.write('s'.encode('big5'))
#        telnet.write((board + '\r\n').encode('big5'))
#        time.sleep(1)
#        c = telnet.read_very_eager().decode('big5','ignore')
#        #telnet.write("\r\n".encode('big5'))                            
#        time.sleep(2)
#        #請參考 http://donsnotes.com/tech/charsets/ascii.html#cntrl
#        # Ctrl+P
#        if btm:
#            buttom(False)
#        telnet.write('\x10'.encode('big5')) 
#        # 發文類別
#        telnet.write('\r\n'.encode('big5'))
#        telnet.write(('''[預報] '''+title + '\r\n').encode('big5'))
#        time.sleep(1)
#        # Ctrl+X
#        for xd in range(0,len(content)):
#            telnet.write(content[xd].encode('big5'))
#            print(content[xd], end="")
#            time.sleep(0.1)
#        telnet.write('\x18'.encode('big5'))
#        #telnet.write((content +'\x18').encode('big5') )
#        time.sleep(1)
#        # 儲存文章
#        telnet.write('s\r\na'.encode('big5') )
#        if btm:
#            buttom(True)
#        print("\n----------------------------------------------")
#        print("------------------ 發文成功 ------------------")
#        print("----------------------------------------------")

#def SendToPtt(b,t,c):
#    login(host, user ,password) 
#    post(b,t,c)
#    disconnect()

#def buttom(tf):
#    if tf:
#        telnet.write(("_y\r\nm".encode("big5")))
#    else:
#        telnet.write(("$_y\r\n").encode("big5"))

"""

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
    content += ('\n預 報 分 區 天       氣           雨率   氣溫(攝氏)\n')
    for index in range(1,23):
        content += ('＊' + root[8][index][0].text + '    ' + addN(root[8][index][1][1][2][0].text) + addNinFront( addWColor( turnFull( root[8][index][5][1][2][0].text ) ) ) + "％ " + addTColor(turnFull(root[8][index][3][1][2][0].text)) + " － " +addTColor(turnFull(root[8][index][2][1][2][0].text))+'\n')	
    content += ( '\n＊備註：各縣市預報係以各縣市政府所在地附近為預報參考位置。\n')
    content += ('\n----資料來源:中央氣象局---\n--- Coded By oToToT@ptt2 / Adapted by r2@CTB ---\n\n')
#    SendToPtt(board,tle,content) ccontent = content.encode('cp950').decode('cp950') print(ccontent) print(content)
    file = open('/home/bbs/etc/weather.post', 'w', encoding = 'Big5')
    file.write(content)
    file.close()

main()

# no need to connect to another host anymore
"""
#if len(sys.argv) > 1:
#    if sys.argv[1].lower() == '--check=false' or sys.argv[2].lower() == '--check=false':
#        if sys.argv[1].lower() == '--buttom=false' or sys.argv[2].lower() == '--check=false':
#            btm=False
#        else:    
#            main()
#else:
#    while True:
#        if(time.localtime(time.time()).tm_hour == 17 or time.localtime(time.time()).tm_hour == 5):
#            main()
#        print("Waiting...")
#        time.sleep(3600)
"""
