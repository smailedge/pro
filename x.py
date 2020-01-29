# -*-coding: utf-8 -*-
from Linephu.linepy import *
from Linephu.akad.ttypes import *
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse, timeit, traceback
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()
cl = LINE()
cl.log("Auth Token : " + str(cl.authToken))
cl.log("Timeline Token : " + str(cl.tl.channelAccessToken))
print ("====Admin登入成功====")
k1 = LINE()
k1.log("Auth Token : " + str(k1.authToken))
k1.log("Timeline Token : " + str(k1.tl.channelAccessToken))
print ("====Bot1登入成功====")
k2 = LINE()
k2.log("Auth Token : " + str(k2.authToken))
k2.log("Timeline Token : " + str(k2.tl.channelAccessToken))
print ("====Bot2登入成功====")
k3 = LINE()
k3.log("Auth Token : " + str(k3.authToken))
k3.log("Timeline Token : " + str(k3.tl.channelAccessToken))
print ("====Bot3登入成功====")
#k4 = LINE()
#k4.log("Auth Token : " + str(k4.authToken))
#k4.log("Timeline Token : " + str(k4.tl.channelAccessToken))
#print ("====Bot4登入成功====")

KAC = [cl,k1,k2,k3]
clMID = cl.profile.mid
AMID = k1.profile.mid
BMID = k2.profile.mid
CMID = k3.profile.mid
#DMID = k4.profile.mid
Bots = [clMID,AMID,BMID,CMID]

clProfile = cl.getProfile()
k1Profile = k1.getProfile()
k2Profile = k2.getProfile()
k3Profile = k3.getProfile()
#k4Profile = k4.getProfile()

lineSettings = cl.getSettings()
k1Settings = k1.getSettings()
k2Settings = k2.getSettings()
k3Settings = k3.getSettings()
#k4Settings = k4.getSettings()

oepoll = OEPoll(cl)
oepoll1 = OEPoll(k1)
oepoll2 = OEPoll(k2)
oepoll3 = OEPoll(k3)
#oepoll4 = OEPoll(k4)

#==============================================================================#

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
banOpen = codecs.open("ban.json","r","utf-8")
adminOpen = codecs.open("admin.json","r","utf-8")

read = json.load(readOpen)
settings = json.load(settingsOpen)
ban = json.load(banOpen)
admin = json.load(adminOpen)

msg_dict = {}
bl = [""]
#==============================================================================#
def restartBot():
    print ("[ 訊息 ] 機器重啟")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = ban
        f = codecs.open('ban.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = admin
        f = codecs.open('admin.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def helpmessage():
    helpMessage = """╔══════════════
╠♥  𝐹𝒶𝓃𝓉𝒶𝓈𝓎𝒮𝓉𝓊𝒹𝒾𝑜 Bot  ♥
║
╠══✪〘 指令一覽表 〙✪═══
║
╠✪〘 Help 〙✪══════════
╠➥ Help 查看指令
╠➥ help 查看指令
║
╠✪〘 Status 〙✪════════
╠➥ restart 重新啟動
╠➥ save 儲存設定
╠➥ runtime 運作時間
╠➥ Speed 速度
╠➥ speed 速度
╠➥ Sp 速度
╠➥ sp 速度
╠➥ set 設定
╠➥ about   關於本帳
╠➥ "集合" 機器進群
╠➥ "解散" 機器退群
╠➥ "報數" 報數測試
║
╠✪〘 Settings 〙✪═══════
╠➥ autoAdd on/off 自動加入
╠➥ autoJoin on/off 自動進群
╠➥ autoLeave on/off 離開副本
╠➥ autoRead on/off 自動已讀
╠➥ share on/off 公開/私人
╠➥ reRead on/off 查詢收回
╠➥ pro on/off 所有保護
╠➥ protect on/off 踢人保護
╠➥ qrProtect on/off 網址保護
╠➥ invprotect on/off 邀請保護
╠➥ getmid on/off 取得mid
╠➥ detect on/off 標註偵測
╠➥ timeline on/off 文章網址預覽
╠➥ welcome on/off 進群留言開關
╠➥ leave on/off 退群留言開關
╠➥ ck on/off查看貼圖資料 開/關
║
╠✪〘 Self 〙✪═════════
╠➥ me 我的連結
╠➥ myMid 我的mid
╠➥ myName 我的名字
╠➥ myBio 個簽
╠➥ myPicture 我的頭貼
╠➥ myCover 我的封面
╠➥ contact @ 標註取得連結
╠➥ mid @ 標註查mid
╠➥ name @ 查看名字
║
╠✪〘 Blacklist 〙✪═══════
╠➥ ban @ 加入黑單
╠➥ unban @ 取消黑單
╠➥ banlist 查看黑單
╠➥ cleanBan 清空黑單
╠➥ kickban 踢除黑單
║
╠✪〘 Group 〙✪════════
╠➥ groupCreator創群者
╠➥ groupId 群組ID
╠➥ groupName 群組名稱
╠➥ groupPicture 群組圖片
╠➥ groupLink 群組網址
╠➥ link「on/off」網址開啟/關閉
╠➥ groupList所有群組列表
╠➥ groupMemberList 成員名單
╠➥ groupInfo 群組資料
╠➥ Gn (文字) 更改群名
╠➥ nk @ 單、多踢
╠➥ Zk 踢出0字元
╠➥ byeall翻群
╠➥ lnv (mid) 透過mid邀請
╠➥ lnv @ 標註多邀
╠➥ ri @ 來回機票
║
╠✪〘 Special 〙✪═══════
╠➥ mimic「on/off」模仿說話
╠➥ mimicList 模仿名單
╠➥ mimicAdd @ 新增模仿名單
╠➥ mimicDel @ 模仿名單刪除
╠➥ tagall 標註全體
╠➥ zc 發送0字元友資
╠➥ setread 已讀點設置
╠➥ cancelread 取消偵測
╠➥ Checkread 已讀偵測
╠➥ Gbc: 群組廣播
╠➥ Fbc: 好友廣播
║
╠✪〘 Admin 〙✪═════════
╠➥ adminadd @ 新增權限
╠➥ admindel @ 刪除權限
╠➥ adminlist 查看權限表
║
╠✪〘 Invite 〙✪════════
╠➥ botsadd @ 加入自動邀請
╠➥ botsdel @ 取消自動邀請
╠➥ botslist 自動邀請表
╠➥ join 自動邀請
║
╚═ 作者By:𝐹𝒶𝓃𝓉𝒶𝓈𝓎𝒮𝓉𝓊𝒹𝒾𝑜-Yuan"""
    return helpMessage
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile() 
contact = k1.getProfile() 
contact = k2.getProfile() 
contact = k3.getProfile() 
#contact = k4.getProfile() 
backup = cl.getProfile() 
backup = k1.getProfile() 
backup = k2.getProfile() 
backup = k3.getProfile() 
#backup = k4.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

creator =['ub6f9d53713c5869f0d78e71febe13837']
admin =['ub6f9d53713c5869f0d78e71febe13837']
owners =['ub6f9d53713c5869f0d78e71febe13837']
#if clMID not in owners:
#    python = sys.executable
#    os.execl(python, python, *sys.argv)
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            contact = cl.getContact(op.param1)
            print ("[ 5 ] 通知添加好友 名字: " + contact.displayName)
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                cl.sendMessage(op.param1, "感謝您加入我為好友！".format(str(contact.displayName)))
        if op.type == 1:
            print ("[1]更新配置文件")

        if op.type == 11:
            group = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            if settings["qrprotect"] == True:
                if op.param2 in admin or op.param2 in ban["bots"]:
                    pass
                else:
                    gs = cl.getGroup(op.param1)
                    gs.preventJoinByTicket = True
                    cl.updateGroup(gs)
                    invsend = 0
                    cl.sendMessage(op.param1,cl.getContact(op.param2).displayName + "你沒有權限觸碰網址!")
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        k2.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            GS = group.creator.mid
            print ("[ 13 ] 通知邀請群組: " + str(group.name) + "\n邀請者: " + contact1.displayName + "\n被邀請者" + contact2.displayName)
            if clMID in op.param3:
                if settings["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1, "歡迎邀請我加入群組")
                    if group.preventedJoinByTicket == True:
                        group.preventedJoinByTicket = False
                        cl.updateGroup(group)
                    else:
                        pass
                    ticket = cl.reissueGroupTicket(op.param1)
                    k1.acceptGroupInvitationByTicket(op.param1, ticket)
                    k2.acceptGroupInvitationByTicket(op.param1, ticket)
                    k3.acceptGroupInvitationByTicket(op.param1, ticket)
                    #k4.acceptGroupInvitationByTicket(op.param1, ticket)
                    group.preventedJoinByTicket = True
                    cl.updateGroup(group)
            elif settings["invprotect"] == True:
                if op.param2 in admin or op.param2 in ban["bots"]:
                    cl.sendMessage(op.param1, "群組邀請保護開啟中")
                    try:
                        k1.cancelGroupInvitation(op.param1, [op.param3])
                    except:
                        k2.cancelGroupInvitation(op.param1, [op.param3])
                    try:
                        ban['blacklist'][op.param2] = True
                        with open('ban.json', 'w') as fp:
                            json.dump(settings, fp, sort_keys=True, indent=4)
                        cl.sendMessage(op.param1, "成功新增黑單")
                        cl.sendContact(op.param1, op.param2)
                    except:
                        cl.sendMessage(op.param1, "[警告]\n新增黑單失敗")
            else:
                if op.param3 in ban['blacklist']:
                    sa.cancelGroupInvitation(op.param1, [op.param3])
                    k3.sendMessage(op.param1, "[警告]\n邀請者位於黑單中")
                    cl.sendContact(op.param1, op.param3)
                elif op.param2 in ban['blacklist']:
                    k2.cancelGroupInvitation(op.param1, [op.param3])
                    cl.sendMessage(op.param1, "[警告]\n你於黑名單中不能邀請")
                    cl.sendContact(op.param1, op.param3)
# ----------------- 有人退出群組時
        if op.type == 15:
            if settings["Lv"] == True:
              if op.param2 in admin or op.param2 in ban["bots"]:
                return
            ginfo = str(cl.getGroup(op.param1).name)		
            try:
                strt = int(3)
                akh = int(3)
                akh = akh + 8
                aa = """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(op.param2)+"},"""
                aa = (aa[:int(len(aa)-1)])
                cl.sendMessage(op.param1, "我們的@wanping 同胞退出了"+ginfo , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                contact = cl.getContact(op.param2)
                image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
                cl.sendImageWithURL(op.param1,image)	
            except Exception as e:
                print(str(e))
				
# ----------------- 有人加入群組時				
        if op.type == 17:
            if settings["Wc"] == True:
              if op.param2 in admin or op.param2 in ban["bots"]:
                return
            ginfo = str(cl.getGroup(op.param1).name)  		
            try:
                strt = int(3)
                akh = int(3)
                akh = akh + 8
                aa = """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(op.param2)+"},"""
                aa = (aa[:int(len(aa)-1)])
                cl.sendMessage(op.param1, "歡迎 @wanping 同胞加入了"+ginfo , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                contact = cl.getContact(op.param2)
                image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
                cl.sendImageWithURL(op.param1,image)	
            except Exception as e:
                print(str(e))
# ----------------- 在群組內有人踢人時				
        if op.type == 19:
            msg = op.message
            chiya = []
            chiya.append(op.param2)
            chiya.append(op.param3)
            cmem = cl.getContacts(chiya)
            zx = ""
            zxc = ""
            zx2 = []
            xpesan ='警告!'
            for x in range(len(cmem)):
                xname = str(cmem[x].displayName)
                pesan = ''
                pesan2 = pesan+"@x 請"
                xlen = str(len(zxc)+len(xpesan))
                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                zx2.append(zx)
                zxc += pesan2
            text = xpesan+ zxc + "出群組"
            try:
                cl.sendMessage(op.param1, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus								
                cl.sendImageWithURL(op.param1,image)	
            except:
                cl.sendMessage(op.param1,"通知從群組中踢出")
            print ("[19]有人把人踢出群組 群組名稱: " + str(group.name) +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n被踢者" + contact2.displayName + "\nMid:" + contact2.mid )
            if op.param2 not in admin:
                if op.param2 in ban["bots"]:
                    pass
                elif settings["protect"] == True:
                    ban["blacklist"][op.param2] = True
                    k2.kickoutFromGroup(op.param1,[op.param2])
                    k3.inviteIntoGroup(op.param1,[op.param3])
                else:
                    cl.sendMessage(op.param1,"")
            else:
                cl.sendMessage(op.param1,"")				

        if op.type == 24:
            print ("[ 24 ] 通知離開副本")
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)

        if op.type == 25 or op.type == 26:
            K0 = admin
            msg = op.message
            if settings["share"] == True:
                K0 = msg._from
            else:
                K0 = admin
#        if op.type == 25 :
#            if msg.toType ==2:
#                g = cl.getGroup(op.message.to)
#                print ("sended:".format(str(g.name)) + str(msg.text))
#            else:
#                print ("sended:" + str(msg.text))
#        if op.type == 26:
#            msg =op.message
#            pop = cl.getContact(msg._from)
#            print ("replay:"+pop.displayName + ":" + str(msg.text))
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return		
#==============================================================================#
            if sender in K0 or sender in owners:
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                    cl.sendContact(to,"ub6f9d53713c5869f0d78e71febe13837")
                if text.lower() == 'Help':
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                    cl.sendContact(to,"ub6f9d53713c5869f0d78e71febe13837")
                elif text.lower() == 'bye':
                    cl.sendMessage(to,"此功能已失效♥")
#==============================================================================#					
                elif text.lower() == '報數':
                    cl.sendMessage(msg.to,"➲ test 1")
                    k1.sendMessage(msg.to,"➲ test 2")
                    k2.sendMessage(msg.to,"➲ test 3")
                    k3.sendMessage(msg.to,"➲ test 4")
                    #k4.sendMessage(msg.to,"➲ test 5")
                    cl.sendMessage(msg.to,"➲ 報數完成")
						
                if text.lower() in ["解散"]:    
                    k1.sendMessage(to,"下次再見 如果只是測試和玩此功能 記得邀我回來 愛你/妳歐♥")
                   # cl.leaveGroup(msg.to)
                    k1.leaveGroup(msg.to)
                    k2.leaveGroup(msg.to)
                    k3.leaveGroup(msg.to)
                    #k4.leaveGroup(msg.to)      
                if text.lower() in ["集合"]:    
                    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    cl.sendMessage(to,"正在邀請機器人中請稍後……")
                    G.preventedJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                    k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    #k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = cl.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    cl.updateGroup(G)
#==============================================================================#
                elif text.lower() == 'speed':
                    start = time.time()
                    cl.sendMessage(to, "正在檢查中….請您耐心稍等一會兒…")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,format(str(elapsed_time)) + "秒")				

                elif text.lower() == 'sp':
                    start = time.time()
                    cl.sendMessage(to, "正在檢查中….請您耐心稍等一會兒…")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,format(str(elapsed_time)) + "秒")								
					
                elif text.lower() == 'Speed':
                    start = time.time()
                    cl.sendMessage(to, "正在檢查中….請您耐心稍等一會兒…")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,format(str(elapsed_time)) + "秒")								
				
                elif text.lower() == 'Sp':
                    start = time.time()
                    cl.sendMessage(to, "正在檢查中….請您耐心稍等一會兒…")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,format(str(elapsed_time)) + "秒")								
				
										
                elif text.lower() == 'save':
                    backupData()
                    cl.sendMessage(to,"儲存設定成功!")
                elif text.lower() == 'restart':
                    cl.sendMessage(to, "正在重新啟動中...請您耐心稍等一會兒…")
                    time.sleep(5)
                    cl.sendMessage(to, "重啟成功，請重新登入")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "本機器已運作 {}".format(str(runtime)) + "秒")
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner ="ua10c2ad470b4b6e972954e1140ad1891"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        ret_ = "╔══[ 關於使用者 ]"
                        ret_ += "\n╠ 使用者名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組數 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友數 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 已封鎖 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於本bot ]"
                        ret_ += "\n╠ 版本 : V1"
                        ret_ += "\n╠ 作者 : {}".format(creator.displayName)
                        ret_ += "\n╚══[ 感謝您的使用 ]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))	
							
				
#==============================================================================#
                elif text.lower() == 'set':
                    try:
                        ret_ = "╔══[ 狀態清單如下： ]"
                        if settings["autoAdd"] == True: ret_ += "\n╠ 自動加入 ✅"
                        else: ret_ += "\n╠ 自動加入 ❌"
                        if settings["autoJoin"] == True: ret_ += "\n╠ 自動進群 ✅"
                        else: ret_ += "\n╠ 自動進群 ❌"
                        if settings["autoLeave"] == True: ret_ += "\n╠ 離開副本 ✅"
                        else: ret_ += "\n╠ 離開副本 ❌"
                        if settings["autoRead"] == True: ret_ += "\n╠ 自動已讀 ✅"
                        else: ret_ += "\n╠ 自動已讀 ❌"
                        if settings["protect"] ==True: ret_+="\n╠ 踢人保護 ✅"
                        else: ret_ += "\n╠ 踢人保護 ❌"
                        if settings["qrprotect"] ==True: ret_+="\n╠ 網址保護 ✅"
                        else: ret_ += "\n╠ 網址保護 ❌"
                        if settings["invprotect"] ==True: ret_+="\n╠ 邀請保護 ✅"
                        else: ret_ += "\n╠ 邀請保護 ❌"
                        if settings["detectMention"] ==True: ret_+="\n╠ 標註偵測 ✅"
                        else: ret_ += "\n╠ 標註偵測 ❌"
                        if settings["reread"] ==True: ret_+="\n╠ 查詢收回 ✅"
                        else: ret_ += "\n╠ 查詢收回 ❌"
                        if settings["share"] ==True: ret_+="\n╠ 公開/私人 ✅"
                        else: ret_ += "\n╠ 公開/私人 ❌"
                        ret_ += "\n╚══[ 結束 ]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'autoadd on':
                    settings["autoAdd"] = True
                    cl.sendMessage(to, "自動加入開啟")
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    cl.sendMessage(to, "自動加入關閉")
                elif text.lower() == 'autojoin on':
                    settings["autoJoin"] = True
                    cl.sendMessage(to, "自動進群開啟")
                elif text.lower() == 'autojoin off':
                    settings["autoJoin"] = False
                    cl.sendMessage(to, "自動進群關閉")
                elif text.lower() == 'autoleave on':
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "離開副本開啟")
                elif text.lower() == 'autojoin off':
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "離開副本關閉")
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    cl.sendMessage(to, "自動已讀開啟")
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    cl.sendMessage(to, "自動已讀關閉")
                elif text.lower() == 'reread on':
                    settings["reread"] = True
                    cl.sendMessage(to,"查詢收回開啟")
                elif text.lower() == 'reread off':
                    settings["reread"] = False
                    cl.sendMessage(to,"查詢收回關閉")
                elif text.lower() == 'protect on':
                    settings["protect"] = True
                    cl.sendMessage(to, "踢人保護開啟")
                elif text.lower() == 'protect off':
                    settings["protect"] = False
                    cl.sendMessage(to, "踢人保護關閉")
                elif text.lower() == 'share on':
                    settings["share"] = True
                    cl.sendMessage(to, "已開啟分享")
                elif text.lower() == 'share off':
                    settings["share"] = False
                    cl.sendMessage(to, "已關閉分享")
                elif text.lower() == 'detect on':
                    settings["detectMention"] = True
                    cl.sendMessage(to, "已開啟標註偵測")
                elif text.lower() == 'detect off':
                    settings["detectMention"] = False
                    cl.sendMessage(to, "已關閉標註偵測")
                elif text.lower() == 'qrprotect on':
                    settings["qrprotect"] = True
                    cl.sendMessage(to, "網址保護開啟")
                elif text.lower() == 'qrprotect off':
                    settings["qrprotect"] = False
                    cl.sendMessage(to, "網址保護關閉")
                elif text.lower() == 'invprotect on':
                    settings["invprotect"] = True
                    cl.sendMessage(to, "邀請保護開啟")
                elif text.lower() == 'invprotect off':
                    settings["invprotect"] = False
                    cl.sendMessage(to, "邀請保護關閉")
                elif text.lower() == 'getmid on':
                    settings["getmid"] = True
                    cl.sendMessage(to, "mid獲取開啟")
                elif text.lower() == 'getmid off':
                    settings["getmid"] = False
                    cl.sendMessage(to, "mid獲取關閉")
                elif text.lower() == 'timeline on':
                    settings["timeline"] = True
                    cl.sendMessage(to, "文章預覽開啟")
                elif text.lower() == 'timeline off':
                    settings["timeline"] = False
                    cl.sendMessage(to, "文章預覽關閉")
                elif text.lower() == 'pro on':
                    settings["protect"] = True
                    settings["qrprotect"] = True
                    settings["invprotect"] = True
                    cl.sendMessage(to, "踢人保護開啟")
                    cl.sendMessage(to, "網址保護開啟")
                    cl.sendMessage(to, "邀請保護開啟")
                elif text.lower() == 'pro off':
                    settings["protect"] = False
                    settings["qrprotect"] = False
                    settings["invprotect"] = False
                    cl.sendMessage(to, "踢人保護關閉")
                    cl.sendMessage(to, "網址保護關閉")
                    cl.sendMessage(to, "邀請保護關閉")
#==============進群和退群打開與關閉========================#
                elif text.lower() == 'welcome on':
                    settings["Wc"] = True
                    cl.sendMessage(to,"進群留言已打開")
                elif text.lower() == 'welcome off':
                    settings["Wc"] = False
                    cl.sendMessage(to,"進群留言已關閉")
                elif text.lower() == 'leave on':
                    settings["Lv"] = True
                    cl.sendMessage(to,"退群留言已打開")
                elif text.lower() == 'leave off':
                    settings["Lv"] = False
                    cl.sendMessage(to,"退群留言已關閉")	
#==============================================================================#
                elif msg.text.lower().startswith("adminadd "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    admin.append(str(inkey))
                    cl.sendMessage(to, "已獲得權限！")
                elif msg.text.lower().startswith("admindel "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    admin.remove(str(inkey))
                    cl.sendMessage(to, "已取消權限！")
                elif text.lower() == 'adminlist':
                    if admin == []:
                        cl.sendMessage(to,"無擁有權限者!")
                    else:
                        mc = "╔══[ Admin List ]"
                        for mi_d in admin:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n╚══[ Finish ]")
						
                elif msg.text.lower().startswith("invite "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    G = cl.getGroup
                    cl.inviteIntoGroup(to,targets)
                elif ("Say " in msg.text):
                    x = text.split(' ',2)
                    c = int(x[2])
                    for c in range(c):
                        cl.sendMessage(to,x[1])
                elif msg.text.lower().startswith("tag "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    x = text.split(' ',2)
                    c = int(x[2])
                    for c in range(c):
                        sendMessageWithMention(to, inkey)
                elif msg.text.lower().startswith("botsadd "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    ban["bots"].append(str(inkey))
                    cl.sendMessage(to, "已加入分機！")
                elif msg.text.lower().startswith("botsdel "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    ban["bots"].remove(str(inkey))
                    cl.sendMessage(to, "已取消分機！")
                elif text.lower() == 'botslist':
                    if ban["bots"] == []:
                        cl.sendMessage(to,"無分機!")
                    else:
                        mc = "╔══[ 分機清單如下： ]"
                        for mi_d in ban["bots"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n╚══[ 結束 ]")
                elif text.lower() == 'join':
                    if msg.toType == 2:
                        G = cl.getGroup
                        cl.inviteIntoGroup(to,ban["bots"])
                elif msg.text.lower().startswith("ii "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.createGroup("滾",[inkey])
                    cl.leaveGroup(op.param1)
#==============================================================================#
                elif text.lower() == 'me':
                    if msg.toType == 2 or msg.toType == 1:
                        sendMessageWithMention(to, sender)
                        cl.sendContact(to, sender)
                    else:
                        cl.sendContact(to,sender)
                elif text.lower() == 'mymid':
                    cl.sendMessage(msg.to,"[MID]\n" +  sender)
                elif text.lower() == 'myname':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"[Name]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = cl.getContact(sender)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideoprofile':
                    me = cl.getContact(sender)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = cl.getContact(sender)
                    cover = cl.getProfileCoverURL(sender)
                    cl.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("contact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            mi_d = contact.mid
                            cl.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("name "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ 名字 ]\n" + contact.displayName)
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ 個簽 ]\n" + contact.statusMessage)
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                            cl.sendImageWithURL(msg.to, str(path))
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = cl.getProfileCoverURL(ls)
                                cl.sendImageWithURL(msg.to, str(path))

#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["mimic"]["target"][target] = True
                            cl.sendMessage(msg.to,"已加入模仿名單!")
                            break
                        except:
                            cl.sendMessage(msg.to,"添加失敗 !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["模仿名單"]["target"][target]
                            cl.sendMessage(msg.to,"刪除成功 !")
                            break
                        except:
                            cl.sendMessage(msg.to,"刪除失敗 !")
                            break
                elif text.lower() == 'mimiclist':
                    if ban["mimic"]["target"] == {}:
                        cl.sendMessage(msg.to,"未設定模仿目標")
                    else:
                        mc = "╔══[ 模仿清單如下： ]"
                        for mi_d in ban["mimic"]["target"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(msg.to,mc + "\n╚══[ 結束 ]")
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if ban["mimic"]["status"] == False:
                            ban["mimic"]["status"] = True
                            cl.sendMessage(msg.to,"模仿說話開啟")
                    elif mic == "off":
                        if ban["mimic"]["status"] == True:
                            ban["mimic"]["status"] = False
                            cl.sendMessage(msg.to,"模仿說話關閉")
#==============================================================================#
                elif text.lower() == 'groupcreator':
                    group = cl.getGroup(to)
                    GS = group.creator.mid
                    cl.sendContact(to, GS)
                elif text.lower() == 'groupid':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'grouppicture':
                    group = cl.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    cl.sendImageWithURL(to, path)
                elif text.lower() == 'groupname':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[群組名稱 : ]\n" + gid.name)
                elif text.lower() == 'grouplink':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[ Group Ticket ]\nhttps://cl.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "Grouplink未開啟 {}openlink".format(str(settings["keyCommand"])))
                elif text.lower() == 'link on':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            cl.sendMessage(to, "群組網址已開")
                        else:
                            group.preventedJoinByTicket = False
                            cl.updateGroup(group)
                            cl.sendMessage(to, "開啟成功")
                elif text.lower() == 'link off':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            cl.sendMessage(to, "群組網址已關")
                        else:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.sendMessage(to, "關閉成功")
                elif text.lower() == 'groupinfo':
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "不明"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "無"
                    else:
                        gQr = "開啟"
                        gTicket = "https://cl.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ 群組狀態清單如下： ]"
                    ret_ += "\n╠ 群組名稱 : {}".format(str(group.name))
                    ret_ += "\n╠ 群組 Id : {}".format(group.id)
                    ret_ += "\n╠ 創建者 : {}".format(str(gCreator))
                    ret_ += "\n╠ 群組人數 : {}".format(str(len(group.members)))
                    ret_ += "\n╠ 邀請中 : {}".format(gPending)
                    ret_ += "\n╠ 網址狀態 : {}".format(gQr)
                    ret_ += "\n╠ 群組網址 : {}".format(gTicket)
                    ret_ += "\n╚══[ 結束 ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower() == 'groupmemberlist':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        ret_ = "╔══[ 成員名單如下： ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ 全部成員共 {} 人]".format(str(len(group.members)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'grouplist':
                        groups = cl.groups
                        ret_ = "╔══[ 群組清單如下： ]"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif msg.text.lower().startswith("nk "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.sendMessage(to,"滾")
                            ki.kickoutFromGroup(msg._from,[terget])
                        except:
                            k2.sendMessage(to,"掰掰瞜")
                
                elif "Zk" in msg.text:
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    k1.kickoutFromGroup(msg._from,[target])                 
                                    k2.kickoutFromGroup(msg._from,[target])                 
                                    k3.kickoutFromGroup(msg._from,[target])                 
                                    #k4.kickoutFromGroup(msg._from,[target])                 
                                except:
                                    pass

                elif "Ri " in msg.text:
                    Ri0 = text.replace("Ri ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.sendMessage(to,"來回機票一張")
                                    cl.kickoutFromGroup(to,[target])
                                    cl.findAndAddContactsByMid(target)
                                    cl.inviteIntoGroup(to,[target])
                                except:
                                    cl.sendMessage(to,"掰掰瞜")
                                    pass

                elif text.lower() == 'byeall':
                    if msg.toType == 2:
                        print ("[ 19 ] KICK ALL MEMBER")
                        _name = msg.text.replace("Byeall","")
                        gs = cl.getGroup(msg.to)
                        cl.sendMessage(msg.to,"Sorry guys")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendMessage(msg.to,"Not Found")
                        else:
                            for target in targets:
                                try:
                                    k1.kickoutFromGroup(msg._from,[target])
                                    k2.kickoutFromGroup(msg._from,[target])
                                    k3.kickoutFromGroup(msg._from,[target])
                                    #k4.kickoutFromGroup(msg._from,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendMessage(msg.to,"")
                elif ("Gn " in msg.text):
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        cl.updateGroup(X)
                    else:
                        cl.sendMessage(msg.to,"It can't be used besides the group.")
                elif ("Inv " in msg.text):
                    if msg.toType == 2:
                        midd = msg.text.replace("Inv ","")
                        cl.findAndAddContactsByMid(midd)
                        cl.inviteIntoGroup(to,[midd])
#==============================================================================#
                elif text.lower() == 'tagall':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        cl.sendMessage(to, "Total {} Mention".format(str(len(nama))))
                elif text.lower() == 'zt':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            sendMessageWithMention(to,target)
                elif text.lower() == 'zm':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for mi_d in targets:
                           cl.sendContect(to,mi_d)
                elif text.lower() == 'setread':
                    cl.sendMessage(msg.to, "已讀點設置成功")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                elif text.lower() == "cancelread":
                    cl.sendMessage(to, "已讀點已刪除")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                        del wait2['setTime'][msg.to]
                    except:
                        pass
                elif msg.text in ["checkread","Checkread"]:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendMessage(msg.to, "[已讀順序]%s\n\n[已讀的人]:\n%s\n查詢時間:[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendMessage(msg.to, "請輸入setread")

#==============================================================================#
                elif msg.text.lower().startswith("ban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["blacklist"][target] = True
                            cl.sendMessage(msg.to,"已加入黑單!")
                            break
                        except:
                            cl.sendMessage(msg.to,"添加失敗 !")
                            break
                elif "Ban:" in msg.text:
                    mmtxt = text.replace("Ban:","")
                    try:
                        ban["blacklist"][mmtext] = True
                        cl.sendMessage(msg.to,"已加入黑單!")
                    except:
                        cl.sendMessage(msg.to,"添加失敗 !")
                elif msg.text.lower().startswith("unban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del ban["blacklist"][target]
                            cl.sendMessage(msg.to,"刪除成功 !")
                            break
                        except:
                            cl.sendMessage(msg.to,"刪除失敗 !")
                            break
                elif text.lower() == 'banlist':
                    if ban["blacklist"] == {}:
                        cl.sendMessage(msg.to,"無黑單成員!")
                    else:
                        mc = "╔══[ 黑單清單如下： ]"
                        for mi_d in ban["blacklist"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(msg.to,mc + "\n╚══[ 結束 ]")
                elif text.lower() == 'nkban':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                    for tag in ban["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendMessage(msg.to,"此群組內無黑名單")
                        return
                    for jj in matched_list:
                        k1.kickoutFromGroup(msg._from,[jj])
                        k2.kickoutFromGroup(msg._from,[jj])
                        k3.kickoutFromGroup(msg._from,[jj])
                        #k4.kickoutFromGroup(msg._from,[jj])
                    cl.sendMessage(msg.to,"黑名單已剔除")
                elif text.lower() == 'cleanban':
                    for mi_d in ban["blacklist"]:
                        ban["blacklist"] = {}
                    cl.sendMessage(to, "已清空黑名單")
                elif text.lower() == 'banmidlist':
                    if ban["blacklist"] == {}:
                        cl.sendMessage(msg.to,"無黑單成員!")
                    else:
                        mc = "╔══[ 黑單清單如下： ]"
                        for mi_d in ban["blacklist"]:
                            mc += "\n╠ "+mi_d
                        cl.sendMessage(to,mc + "\n╚══[ 結束 ]")


#==============================================================================#
                elif "Fbc:" in msg.text:
                    cl.sendMessage(to,"此功能已失效♥")

                elif "Gbc:" in msg.text:
                    cl.sendMessage(to,"此功能已失效♥")

                elif "Copy " in msg.text:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            X = contact.displayName
                            profile = cl.getProfile()
                            profile.displayName = X
                            cl.updateProfile(profile)
                            cl.sendMessage(to, "成功...")
                            Y = contact.statusMessage
                            lol = cl.getProfile()
                            lol.statusMessage = Y
                            cl.updateProfile(lol)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            P = contact.pictureStatus
                            cl.updateProfilePicture(P)
                        except Exception as e:
                            cl.sendMessage(to, "Failed!")
            if text.lower() == '0870819':
                if sender in ['ub6f9d53713c5869f0d78e71febe13837']:
                    python = sys.executable
                    os.execl(python, python, *sys.argv)
                else:
                    pass
#==============================================================================#
            if msg.contentType == 13:
                if settings["getmid"] == True:
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"[mid]:\n" + msg.contentMetadata["mid"])
                    else:
                        cl.sendMessage(msg.to,"[mid]:\n" + msg.contentMetadata["mid"])
											
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    try:
                        msg.contentType = 0
                        f_mid = msg.contentMetadata["postEndUrl"].split("userMid=")
                        s_mid = f_mid[1].split("&")
                        mid = s_mid[0]
                        try:
                            arrData = ""
                            text = "%s " %("[文章持有者]\n")
                            arr = []
                            mention = "@x "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':mid}
                            arr.append(arrData)
                            text += mention + "\n[文章預覽]\n(僅提供100字內容)\n " + msg.contentMetadata["text"] + "\n[文章網址]\n " + msg.contentMetadata["postEndUrl"]
                            cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
                    except:
                        ret_ = "\n[文章預覽]\n(僅提供100字內容)\n " + msg.contentMetadata["text"]
                        ret_ += "\n[文章網址]\n " + msg.contentMetadata["postEndUrl"]
                        cl.sendMessage(msg.to, ret_)
#==============================================================================#
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in ban["mimic"]["target"] and ban["mimic"]["status"] == True and ban["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = cl.getContact(sender)
                                    sendMessageWithMention(to, contact.mid)
                                    cl.sendMessage(to, "為什麼要標記我呢?我正在忙線中，請私密我 謝謝您的體諒")
                                break
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.toType == 0:
                        cl.log("[%s]"%(msg._from)+msg.text)
                    else:
                        cl.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                    elif msg.contentType == 7:
                        stk_id = msg.contentMetadata['STKID']
                        msg_dict[msg.id] = {"text":"貼圖id:"+str(stk_id),"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)

#==============================================================================#              
        if op.type == 65:
            if settings["reread"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                contact = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(contact.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':contact.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, "收回訊息者 @wanping ", contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                contact = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 收回訊息 」\n"
                                ret_ += "• 收回訊息者 : {}".format(str(contact.displayName))
                                ret_ += "\n• 群組名稱 : {}".format(str(ginfo.name))
                                ret_ += "\n• 收回時間 : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• 訊息內容 : {}".format(str(msg_dict[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus								
                                cl.sendImageWithURL(op.param1,image)	
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)
#==============================================================================#
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[※]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[※]" + Name
                        print (time.time() + name)
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
#===========================================================[clMID - AMID]
        if op.type == 19:
            print ("[ 19 ] KICKOUT NADYA MESSAGE")
            try:
                if op.param3 in clMID:
                    if op.param2 in AMID:
                        G = k1.getGroup(op.param1)
#                        ginfo = k1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        k1.updateGroup(G)
                        invsend = 0
                        Ticket = k1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = k1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        k1.updateGroup(G)
                    else:
                        G = k1.getGroup(op.param1)
#                        ginfo = k1.getGroup(op.param1)
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        k1.updateGroup(G)
                        invsend = 0
                        Ticket = k1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = k1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        k1.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[clMID - BMID]
                elif op.param3 in clMID:
                    if op.param2 in BMID:
                        G = k2.getGroup(op.param1)
#                        ginfo = k2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        k2.updateGroup(G)
                        invsend = 0
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = k2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        k2.updateGroup(G)
                    else:
                        G = k2.getGroup(op.param1)
#                        ginfo = k2.getGroup(op.param1)
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        k2.updateGroup(G)
                        invsend = 0
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = k2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        k2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[clMID - CMID]
                elif op.param3 in clMID:
                    if op.param2 in CMID:
                        G = k3.getGroup(op.param1)
#                        ginfo = k3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        k3.updateGroup(G)
                        invsend = 0
                        Ticket = k3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = k3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        k3.updateGroup(G)
                    else:
                        G = k3.getGroup(op.param1)
#                        ginfo = k3.getGroup(op.param1)
                        k3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        k3.updateGroup(G)
                        invsend = 0
                        Ticket = k3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = k3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        k3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[clMID - DMID]
                #elif op.param3 in clMID:
                    #if op.param2 in DMID:
                        #G = k4.getGroup(op.param1)
#                        #ginfo = k4.getGroup(op.param1)
                        #G.preventedJoinByTicket = False
                        #k4.updateGroup(G)
                        #invsend = 0
                        #Ticket = k4.reissueGroupTicket(op.param1)
                        #cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #G = k4.getGroup(op.param1)
                        #G.preventedJoinByTicket = True
                        #k4.updateGroup(G)
                        #G.preventedJoinByTicket(G)
                        #k4.updateGroup(G)
                    #else:
                        #G = k4.getGroup(op.param1)
#                        #ginfo = k4.getGroup(op.param1)
                        #k4.kickoutFromGroup(op.param1,[op.param2])
                        #G.preventedJoinByTicket = False
                        #k4.updateGroup(G)
                        #invsend = 0
                        #Ticket = k4.reissueGroupTicket(op.param1)
                        #cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #G = k4.getGroup(op.param1)
                        #G.preventedJoinByTicket = True
                        #k4.updateGroup(G)
                        #G.preventedJoinByTicket(G)
                        #k4.updateGroup(G)
                        #settings["blacklist"][op.param2] = True
#================================================[AMID clMID]
                if op.param3 in AMID:
                    if op.param2 in clMID:
                        G = cl.getGroup(op.param1)
#                        ginfo = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        cl.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)
#                        ginfo = cl.getGroup(op.param1)
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        cl.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        cl.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[AMID BMID]
                elif op.param3 in AMID:
                    if op.param2 in BMID:
                        G = k2.getGroup(op.param1)
#                        ginfo = k2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        k2.updateGroup(G)
                        invsend = 0
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = k2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        k2.updateGroup(G)
                    else:
                        G = k2.getGroup(op.param1)
#                        ginfo = k2.getGroup(op.param1)
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        k2.updateGroup(G)
                        invsend = 0
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = k2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        k2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[AMID CMID]
                elif op.param3 in AMID:
                    if op.param2 in CMID:
                        G = k3.getGroup(op.param1)
#                        ginfo = k3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        k3.updateGroup(G)
                        invsend = 0
                        Ticket = k3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = k3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        k3.updateGroup(G)
                    else:
                        G = k3.getGroup(op.param1)
#                        ginfo = k3.getGroup(op.param1)
                        k3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        k3.updateGroup(G)
                        invsend = 0
                        Ticket = k3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = k3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        k3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[AMID DMID]
                #elif op.param3 in AMID:
                    #if op.param2 in DMID:
                        #G = k4.getGroup(op.param1)
#                        ginfo = k4.getGroup(op.param1)
                        #G.preventedJoinByTicket = False
                        #k4.updateGroup(G)
                        #invsend = 0
                        #Ticket = k4.reissueGroupTicket(op.param1)
                        #cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #G = k4.getGroup(op.param1)
                        #G.preventedJoinByTicket = True
                        #k4.updateGroup(G)
                        #G.preventedJoinByTicket(G)
                        #k4.updateGroup(G)
                    #else:
                        #G = k4.getGroup(op.param1)
#                        ginfo = k4.getGroup(op.param1)
                        #k4.kickoutFromGroup(op.param1,[op.param2])
                        #G.preventedJoinByTicket = False
                        #k4.updateGroup(G)
                        #invsend = 0
                        #Ticket = k4.reissueGroupTicket(op.param1)
                        #cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #G = k4.getGroup(op.param1)
                        #G.preventedJoinByTicket = True
                        #k4.updateGroup(G)
                        #G.preventedJoinByTicket(G)
                        #k4.updateGroup(G)
                        #settings["blacklist"][op.param2] = True
#=====================================================[BMID clMID]
                if op.param3 in BMID:
                    if op.param2 in clMID:
                        G = cl.getGroup(op.param1)
#                        ginfo = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        cl.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)
#                        ginfo = cl.getGroup(op.param1)
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        cl.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        cl.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[BMID AMID]
                elif op.param3 in BMID:
                    if op.param2 in AMID:
                        G = k1.getGroup(op.param1)
#                        ginfo = k1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        k1.updateGroup(G)
                        invsend = 0
                        Ticket = k1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = k1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        k1.updateGroup(G)
                    else:
                        G = k1.getGroup(op.param1)
#                        ginfo = k1.getGroup(op.param1)
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        k1.updateGroup(G)
                        invsend = 0
                        Ticket = k1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = k1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        k1.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[BMID CMID]
                elif op.param3 in BMID:
                    if op.param2 in CMID:
                        G = k3.getGroup(op.param1)
#                        ginfo = k3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        k3.updateGroup(G)
                        invsend = 0
                        Ticket = k3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = k3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        k3.updateGroup(G)
                    else:
                        G = k3.getGroup(op.param1)
#                        ginfo = k3.getGroup(op.param1)
                        k3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        k3.updateGroup(G)
                        invsend = 0
                        Ticket = k3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = k3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        k3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[BMID DMID]
                #elif op.param3 in BMID:
                    #if op.param2 in DMID:
                        #G = k4.getGroup(op.param1)
#                        ginfo = k4.getGroup(op.param1)
                        #G.preventedJoinByTicket = False
                        #k4.updateGroup(G)
                        #invsend = 0
                        #Ticket = k4.reissueGroupTicket(op.param1)
                        #cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #G = k4.getGroup(op.param1)
                        #G.preventedJoinByTicket = True
                        #k4.updateGroup(G)
                        #G.preventedJoinByTicket(G)
                        #k4.updateGroup(G)
                    #else:
                        #G = k4.getGroup(op.param1)
#                       # ginfo = k4.getGroup(op.param1)
                        #k4.kickoutFromGroup(op.param1,[op.param2])
                        #G.preventedJoinByTicket = False
                        #k4.updateGroup(G)
                        #invsend = 0
                        #Ticket = k4.reissueGroupTicket(op.param1)
                        #cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #G = k4.getGroup(op.param1)
                        #G.preventedJoinByTicket = True
                        #k4.updateGroup(G)
                        #G.preventedJoinByTicket(G)
                        #k4.updateGroup(G)
                        #settings["blacklist"][op.param2] = True
#================================================[CMID clMID]
                if op.param3 in CMID:
                    if op.param2 in clMID:
                        G = cl.getGroup(op.param1)
#                        ginfo = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        cl.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)
#                        ginfo = cl.getGroup(op.param1)
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        cl.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        cl.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[CMID AMID]
                elif op.param3 in CMID:
                    if op.param2 in AMID:
                        G = k1.getGroup(op.param1)
#                        ginfo = k1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        k1.updateGroup(G)
                        invsend = 0
                        Ticket = k1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = k1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        k1.updateGroup(G)
                    else:
                        G = k1.getGroup(op.param1)
#                        ginfo = k1.getGroup(op.param1)
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        k1.updateGroup(G)
                        invsend = 0
                        Ticket = k1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = k1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        k1.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[CMID BMID]
                elif op.param3 in CMID:
                    if op.param2 in BMID:
                        G = k2.getGroup(op.param1)
#                        ginfo = k2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        k2.updateGroup(G)
                        invsend = 0
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = k2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        k2.updateGroup(G)
                    else:
                        G = k2.getGroup(op.param1)
#                        ginfo = k2.getGroup(op.param1)
                        k3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        k2.updateGroup(G)
                        invsend = 0
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = k2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        k2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[CMID DMID]
                #elif op.param3 in CMID:
                    #if op.param2 in DMID:
                        #G = k4.getGroup(op.param1)
#                        ginfo = k4.getGroup(op.param1)
                        #G.preventedJoinByTicket = False
                        #k4.updateGroup(G)
                        #invsend = 0
                        #Ticket = k4.reissueGroupTicket(op.param1)
                        #cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #G = k4.getGroup(op.param1)
                        #G.preventedJoinByTicket = True
                        #k4.updateGroup(G)
                        #G.preventedJoinByTicket(G)
                        #k4.updateGroup(G)
                    #else:
                        #G = k4.getGroup(op.param1)
#                        ginfo = k4.getGroup(op.param1)
                        #k4.kickoutFromGroup(op.param1,[op.param2])
                        #G.preventedJoinByTicket = False
                        #k4.updateGroup(G)
                        #invsend = 0
                        #Ticket = k4.reissueGroupTicket(op.param1)
                        #cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #G = k4.getGroup(op.param1)
                        #G.preventedJoinByTicket = True
                        #k4.updateGroup(G)
                        #G.preventedJoinByTicket(G)
                        #k4.updateGroup(G)
                        #settings["blacklist"][op.param2] = True
#=====================================================[DMID clMID]
#                if op.param3 in DMID:
#                    if op.param2 in clMID:
#                        G = cl.getGroup(op.param1)
##                        ginfo = cl.getGroup(op.param1)
#                        G.preventedJoinByTicket = False
#                        cl.updateGroup(G)
#                        invsend = 0
#                        Ticket = cl.reissueGroupTicket(op.param1)
#                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        G = cl.getGroup(op.param1)
#                        G.preventedJoinByTicket = True
#                        cl.updateGroup(G)
#                        G.preventedJoinByTicket(G)
#                        cl.updateGroup(G)
#                    else:
#                        G = cl.getGroup(op.param1)
##                        ginfo = cl.getGroup(op.param1)
#                        k1.kickoutFromGroup(op.param1,[op.param2])
#                        G.preventedJoinByTicket = False
#                        cl.updateGroup(G)
#                        invsend = 0
#                        Ticket = cl.reissueGroupTicket(op.param1)
#                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        G = cl.getGroup(op.param1)
#                        G.preventedJoinByTicket = True
#                        cl.updateGroup(G)
#                        G.preventedJoinByTicket(G)
#                        cl.updateGroup(G)
#                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[DMID AMID]
#                elif op.param3 in DMID:
#                    if op.param2 in AMID:
#                        G = k1.getGroup(op.param1)
##                        ginfo = k1.getGroup(op.param1)
#                        G.preventedJoinByTicket = False
#                        k1.updateGroup(G)
#                        invsend = 0
#                        Ticket = k1.reissueGroupTicket(op.param1)
#                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        G = k1.getGroup(op.param1)
#                        G.preventedJoinByTicket = True
#                        k1.updateGroup(G)
#                        G.preventedJoinByTicket(G)
#                        k1.updateGroup(G)
#                    else:
#                        G = k1.getGroup(op.param1)
##                        ginfo = k1.getGroup(op.param1)
#                        k2.kickoutFromGroup(op.param1,[op.param2])
#                        G.preventedJoinByTicket = False
#                        k1.updateGroup(G)
#                        invsend = 0
#                        Ticket = k1.reissueGroupTicket(op.param1)
#                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        G = k1.getGroup(op.param1)
#                        G.preventedJoinByTicket = True
#                        k1.updateGroup(G)
#                        G.preventedJoinByTicket(G)
#                        k1.updateGroup(G)
#                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[DMID BMID]
 #               elif op.param3 in DMID:
 #                   if op.param2 in BMID:
 #                       G = k2.getGroup(op.param1)
##                        ginfo = k2.getGroup(op.param1)
 #                       G.preventedJoinByTicket = False
 #                       k2.updateGroup(G)
 #                       invsend = 0
 #                       Ticket = k2.reissueGroupTicket(op.param1)
 #                       cl.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       k1.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       k2.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       k3.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       k4.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       G = k2.getGroup(op.param1)
 #                       G.preventedJoinByTicket = True
 #                       k2.updateGroup(G)
 #                       G.preventedJoinByTicket(G)
 #                       k2.updateGroup(G)
 #                   else:
 #                       G = k2.getGroup(op.param1)
##                        ginfo = k2.getGroup(op.param1)
 #                       k3.kickoutFromGroup(op.param1,[op.param2])
 #                       G.preventedJoinByTicket = False
 #                       k2.updateGroup(G)
 #                       invsend = 0
 #                       Ticket = k2.reissueGroupTicket(op.param1)
 #                       cl.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       k1.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       k2.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       k3.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       k4.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       G = k2.getGroup(op.param1)
 #                       G.preventedJoinByTicket = True
 #                       k2.updateGroup(G)
 #                       G.preventedJoinByTicket(G)
 #                       k2.updateGroup(G)
 #                       settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[DMID CMID]
#                elif op.param3 in DMID:
#                    if op.param2 in CMID:
#                        G = k3.getGroup(op.param1)
##                        ginfo = k3.getGroup(op.param1)
#                        G.preventedJoinByTicket = False
#                        k3.updateGroup(G)
#                        invsend = 0
 #                       Ticket = k3.reissueGroupTicket(op.param1)
 #                       cl.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       k1.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       k2.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       k3.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       k4.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       G = k3.getGroup(op.param1)
 #                       G.preventedJoinByTicket = True
 #                       k3.updateGroup(G)
 #                       G.preventedJoinByTicket(G)
 #                       k3.updateGroup(G)
 #                   else:
 #                       G = k3.getGroup(op.param1)
##                        ginfo = k3.getGroup(op.param1)
 #                       k4.kickoutFromGroup(op.param1,[op.param2])
 #                       G.preventedJoinByTicket = False
#                        k3.updateGroup(G)
#                        invsend = 0
#                        Ticket = k3.reissueGroupTicket(op.param1)
#                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        G = k3.getGroup(op.param1)
#                        G.preventedJoinByTicket = True
#                        k3.updateGroup(G)
#                        G.preventedJoinByTicket(G)
#                        k3.updateGroup(G)
#                        settings["blacklist"][op.param2] = True
                        
                elif op.param2 not in Bots:
                    if op.param2 in admin:
                        pass
                    elif settings["protect"] == True:
                        settings["blacklist"][op.param2] = True
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        random.choice(KAC).sendText(op.param1,"別輕易嘗試...!")
                        
                else:
                    pass
            except:
                pass
#==============================================================================#
# Auto join if BOT invited to group
def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        cl.acceptGroupInvitation(op.param1)
        k1.acceptGroupInvitation(op.param1)
        k2.acceptGroupInvitation(op.param1)
        k3.acceptGroupInvitation(op.param1)
        k4.acceptGroupInvitation(op.param1)
    except Exception as e:
        cl.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))
# Auto kick if BOT out to group
def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        if op.param2 not in Bots:
            random.choice(KAC).kickoutFromGroup(op.param1,op.param2)
        else:
            pass
    except Exception as e:
        cl.log("[NOTIFIED_KICKOUT_FROM_GROUP] ERROR : " + str(e))		
#==============================================================================#
   					
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)