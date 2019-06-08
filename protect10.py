# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,ast,requests

cl = LINETCR.LINE() #LULY 4
#cl.login(token='EqNQbHEC2On79FPw9I98.T7wQ6Fh12YlZQUcbuycIIa.LscxpP7GVAtUGbCypt6IYamMuIBwtlc8bUyTkk7Txdg=')
cl.login(token='EFitAQlaqdMz659xrog4.v1HrXTya8vs3Kmp/GY36La.YK0lAHUSB+3cZrROYJicXyV6BW28n59IPL3+6so7DgU=')
cl.loginResult()

ki = LINETCR.LINE()#LULY 2
ki.login(token='EF5yaohc7GcnExGpPtAb.iEKLQqr+KXdSVGWpsvd/QW.hGk1ZTM44oa6VUxNGz9DSQmqEAlkbeBcpE0cUwnLdzs=')
ki.loginResult()

kk = LINETCR.LINE()#LULY 3
kk.login(token='EF49wrk3oIrh1lWyRnF0.nvD/uRjfRoBETK4ZOWhZSa.3GJMLgxnJ6CoFaOaNBjmkNGhjDOjPDsCIdJVBtpnCng=')
kk.loginResult()

kc = LINETCR.LINE()#LULY 1
#kc.login(token='EqicsCjcHpVC4XlNP8O2.ZWXwD1cn0eMz0FrM4e6YGG.vKDlz0NSxJ6s62UBLEmGsad9QyxkYyi42qN5KehZDiU=')
kc.login(token='EFgS2ZfQ1QJRlkCY4SM4./Coef04cSd1Ymaih+V2ADa.+gZ7mkM8pohBkL97g7IjWacuqwgaM6RDyLCetjtxA7k=')
kc.loginResult()

ks = LINETCR.LINE()#LULY 5 REVOKE
ks.login(token='EFkWxBjUivxkoZBoO6p1.f04Z5tIwN8oo0wvkaqNsqq.ylJ4f7++HXMP5mmeuL4MTtDSzmI39jzk3UwXDnWSxVE=')
ks.loginResult()

ka = LINETCR.LINE()#LULY 6
ka.login(token='EFLokmnYGRNtWG2v2SU5.hY1gor5CBWozmN09XaJ2nq.a7UI3Vjw2oOv2s8BIlDF6DkmSYm5/iCi/zJe4p3nRIg=')
ka.loginResult()

kb = LINETCR.LINE()#LULY 7
kb.login(token='EFdTKWhbbSiroRo6amQd.JZJ/1Jhb9oyNKqIA+uiyFq.l1e6VJ4eo4xFAJDJBWl6bPAAIqcg8uCwS+Kv/8If92E=')
kb.loginResult()

ko = LINETCR.LINE()#LULY 9
ko.login(token='EFZUic52lOXfXyBhy277.t/IdFcgcW7pVEtQdsL6WzW.0KPQzxVupBE8zJimSx8UsuQzIMmLmx8TfCWbSUKPig8=')
ko.loginResult()

ke = LINETCR.LINE()#LULY 10
ke.login(token='EFW9269im8b5ymsZW6k9.sq7xakrN1v28/yW8CSq42q.uiVktMG5AzV5lrn2tVrv66w7AnO7+6L0Y8wIoWSBAC8=')
ke.loginResult()

ku = LINETCR.LINE()#LULY 11
ku.login(token='EFEtOrP4OI3T3bUVXjub.bAXEGo6vXQI0VRhomlb3MW.hhjT+wYlx4jsr8E5SwQaGTLWVH5qKAKZnN8DY4oWLsM=')
ku.loginResult()

k1 = LINETCR.LINE()#LULY 12 (GHOST)
k1.login(token='EFmZI7AyEF4yUVOlgvAa.uA70OmZ6xGXhLjifkBHlgG.u8JwLoZU4VbHclyyBzddWznslvCwBoO+lfw+5/gsCaI=')
k1.loginResult()

satpam = LINETCR.LINE() #Akun utama
satpam.login(token='EFKCgbHKYsPDRcEV0Ek2.XhCwJBakhq3WIw4uZqu08G.9gahigg8sbRSeqesJ7oj2ScjUWh8o/JtokZIaiASLRY=')
satpam.loginResult()

print("=================[டΰட௶ ᴮᴼᵀ]=================")
print("        ᵀʰᵃⁿᵏˢ ᶠᵒʳ ᵀᶜᴿ ᵃⁿᵈ ᴹʸ ᶠᵃᵐᶦˡʸ      ")
print("================[© By_т.ȥ.κ]================")

reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" 
╔════════════════════
║ ŔÀÑg0 ᴮᴼᵀ
╠════════════════════
║  COMMAND HELP
╠════════════════════
║╔═══════════════
║╠❂➣Menu owner
║╠❂➣Menu admin
║╠❂➣Menu staff
║╠❂➣Menu member
║╚═══════════════
╚══════════════════════
"""

helpmenumember =""" 
╔════════════════════
║ ŔÀÑg0 ᴮᴼᵀ
╠════════════════════
║  MENU MEMBER
╠════════════════════
║╔═══════════════
║╠❂➣Me
║╠❂➣Mid @
║╠❂➣Creator
║╠❂➣Bot
║╠❂➣Pp @
║╠❂➣Cover @
║╠❂➣Detail @
║╠❂➣Ppgroup
║╠❂➣Respon chat
║╚═══════════════
╚══════════════════════
"""

helpmenustaff =""" 
╔════════════════════
║ ŔÀÑg0 ᴮᴼᵀ
╠════════════════════
║  MENU STAFF
╠════════════════════
║╔═══════════════
║╠➣Adminlist
║╠➣Stafflist
║╠➣Crewlist
║╠➣Banlist
║╠➣Cek ban
║╠➣Gift
║╠➣3gift
║╠➣Cancel invite
║╠➣Luly cancel
║╠➣Cancel on/off
║╠➣Qr on/off
║╠➣Contact on/off
║╠➣Gcancel on/off
║╠➣Share on/off
║╠➣Comment on/off
║╠➣Notif on/off
║╠➣Autosider on/off
║╠➣Cancelall
║╠➣Gurl
║╠➣Cctv → Ciduk
║╠➣Tagall
║╠➣Luly say hi
║╠➣Speed
║╠➣Clear invite
║╚═══════════════
╚══════════════════════
"""

helpmenuadmin =""" 
╔════════════════════
║ ŔÀÑg0 ᴮᴼᵀ
╠════════════════════
║  COMMAND ADMIN
╠════════════════════
║╔═══════════════
║╠➣Gn [text]
║╠➣2gn [text]
║╠➣3gn [text]
║╠➣4gn [text]
║╠➣Kick [mid]
║╠➣2kick [mid]
║╠➣3kick [mid]
║╠➣4kick [mid]
║╠➣Invite [mid]
║╠➣2invite [mid]
║╠➣3invite [mid]
║╠➣4invite [mid]
║╠➣Spam: [text] [jml]
║╠➣Luly contact
║╠➣L1-L10
║╠➣1mid-10mid
║╠➣Satpam
║╠➣Mc [mid]
║╠➣Respons1
║╠➣Respons2
║╠➣Respons3
║╠➣Autojoin on/off
║╠➣Autoleave on/off
║╠➣Autoadd on/off
║╠➣Ghost on/off
║╠➣Message Change: [text]
║╠➣Message
║╠➣Comment: [text]
║╠➣Add comment: [text]
║╠➣Comment bl [text]
║╠➣Jam on/off
║╠➣Ubah jam
║╠➣Jam update
║╠➣Kill [mid]
║╠➣NK @
║╠➣Blacklist @
║╠➣Banned @
║╠➣Mid @
║╠➣Unban @
║╠➣Up (spam)
║╠➣Ping
║╠➣Kill ban
║╠➣Update welcome: [text]
║╠➣Update goodnye: [text]
║╚═══════════════
╚══════════════════════
"""

helpchat = """
╔════════════════════
║ ŔÀÑg0 ᴮᴼᵀ
╠════════════════════
║ COMMAND RESPON CHAT
╠════════════════════
║╔═══════════════
║╠❂➣Bot
║╠❂➣Wkwkwk
║╠❂➣Hehehe
║╠❂➣Galau
║╠❂➣You
║╠❂➣Hadeuh
║╠❂➣Please
║╠❂➣Haaa
║╠❂➣Lol
║╠❂➣Hmmm
║╠❂➣Welcome
║╚═══════════════
╚══════════════════════
"""
helpown = """
╔════════════════════
║ ŔÀÑg0 ᴮᴼᵀ
╠════════════════════
║  COMMAND OWNER
╠════════════════════
║╔═══════════════
║╠❂➣Admin add @
║╠❂➣Admin remove @
║╠❂➣Staff add @
║╠❂➣Staff remove @
║╠❂➣Luly add @
║╠❂➣Allbio: [text]
║╠❂➣1rn-10rn [text]
║╠❂➣Jgid
║╠❂➣/invitemeto: [gid]
║╠❂➣Masuk sayang (CL in)
║╠❂➣/join (no CL)
║╠❂➣Bubar say(ALL)
║╠❂➣/out (no CL)
║╠❂➣Luly like
║╠❂➣Luly like teman
║╠❂➣Sikaat (Clearse)
║╠❂➣Bcg [text]
║╠❂➣LG
║╠❂➣LG2
║╠❂➣Bubar all group
║╠❂➣Ban [mid]
║╠❂➣Unban [mid]
║╠❂➣Respon1 on/off
║╠❂➣Respon2 on/off
║╠❂➣Respon3 on/off
║╚═══════════════
╚══════════════════════
"""

KAC=[cl,ki,kk,kc,ks,ka,kb,ko,ke,ku]
DEF1=[ki,kk,kc,ks,ka,kb,ko,ke,ku] #Udah Ga Kepake(Boleh di apus)
DEF2=[cl,kk,kc,ks,ka,kb,ko,ke,ku] #Udah Ga Kepake(Boleh di apus)
DEF3=[cl,ki,kc,ks,ka,kb,ko,ke,ku] #Udah Ga Kepake(Boleh di apus)
DEF4=[cl,ki,kk,ks,ka,kb,ko,ke,ku] #Udah Ga Kepake(Boleh di apus)
DEF5=[cl,ki,kk,kc,ka,kb,ko,ke,ku] #Udah Ga Kepake(Boleh di apus)
DEF6=[cl,ki,kk,kc,ks,kb,ko,ke,ku] #Udah Ga Kepake(Boleh di apus)
DEF7=[cl,ki,kk,kc,ks,ka,ko,ke,ku] #Udah Ga Kepake(Boleh di apus)
DEF8=[cl,ki,kk,kc,ks,ka,kb,ke,ku] #Udah Ga Kepake(Boleh di apus)
DEF9=[cl,ki,kk,kc,ks,ka,kb,ko,ku] #Udah Ga Kepake(Boleh di apus)
DEF10=[cl,ki,kk,kc,ks,ka,kb,ko,ke] #Udah Ga Kepake(Boleh di apus)
mid = cl.getProfile().mid #Luffy
Amid = ki.getProfile().mid #Zorro
Bmid = kk.getProfile().mid #Sanji
Cmid = kc.getProfile().mid #Ussop
Dmid = ks.getProfile().mid #Chooper
Emid = ka.getProfile().mid #Franky
Fmid = kb.getProfile().mid #Brook
Gmid = ko.getProfile().mid #Nami
Hmid = ke.getProfile().mid #Robin
Imid = ku.getProfile().mid #Jinbei
Smid = satpam.getProfile().mid #Akun Utama
mid1 = k1.getProfile().mid #Backup

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Smid,mid1,"ubbf5fbe22865fcd64a4c4937d5b547c6"]
#there MID ud02674bbd4671d852c02883f8a4ee73d
#abay MID ucc81edac143bab9dd6e8109b50fc4a0e
admin=["u575851c6d600f154b790c3fe832dfa94",mid] 
owner=["u575851c6d600f154b790c3fe832dfa94"]
staff=[]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"""тerima Kasih Sudah Menambahkan Aku Jadi Teman
≫ Aku Ga Jawab PM Karna aq Cuma Bot Protect ≪
""",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"™Luffy™ ",
    "cName2":"™Zorro™ ",
    "cName3":"™Sanji™ ",
    "cName4":"™Ussop™ ",
    "cName5":"™Chooper™ ",
    "cName6":"™Franky™ ",
    "cName7":"™Brook™ ",
    "cName8":"™Nami™ ",
    "cName9":"™Robin™ ",
    "cName10":"™Jinbei™ ",
    "cName11":"",
    "cName12":"™ONE PIECE BOT™ ",
    "blacklist":{},
    "detectMention":False,
    "detectMention2":False,
    "detectMention3":False,
    "detectMention4":False,
    "detectMention5":False,
    "detectMention6":False,
    "sticker":False,
    "Ghost":False,
    "wblacklist":False,
    "dblacklist":False,
    "welmsg":" Selamat Datang di ",
    "welmsg2":" Semoga tidak ada baper diantara kita yah",
    "Sambutan":True,
    "Protectgr":True,
    #"Protectjoin":True, # Ga Kepake(Yang Gabung langsung di kick :D) Udah  Udah ada Protect Cancell
    "Protectcancl":True,
    "protectionOn":True,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
	
cctv = {
    "cyduk":{},
    "point":{},
    "MENTION":{},
    "sidermem":{}
}	

setTime = {}
setTime = wait2['setTime']

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "Mention"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

#def NOTIFIED_READ_MESSAGE(op):
    #try:
        #if op.param1 in wait2['readPoint']:
            #Name = cl.getContact(op.param2).displayName
            #if Name in wait2['readMember'][op.param1]:
                #pass
            #else:
                #wait2['readMember'][op.param1] += "\n・" + Name
                #wait2['ROM'][op.param1][op.param2] = "・" + Name
        #else:
            #pass
    #except:
        #pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #------Protect Group Kick start------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if op.param2 not in Bots:
              G = random.choice(KAC).getGroup(op.param1)
              G.preventJoinByTicket = True
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).updateGroup(G)
              random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Jangan Buka Kode QR Njiiir")
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            if op.param2 not in Bots:
              group = cl.getGroup(op.param1)
              gMembMids = [contact.mid for contact in group.invitee]
              random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
        #------Cancel Invite User Finish------#
            
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = Amid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in Bmid:
                if op.param2 in Amid:
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in Cmid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                
            if op.param3 in Dmid:
                if op.param2 in Cmid:
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                
            if op.param3 in Emid:
                if op.param2 in Dmid:
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                
            if op.param3 in Fmid:
                if op.param2 in Emid:
                    X = ka.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                
            if op.param3 in Gmid:
                if op.param2 in Fmid:
                    X = kb.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                
            if op.param3 in Hmid:
                if op.param2 in Gmid:
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    
            if op.param3 in Imid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)        

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
        #------Joined User Kick start------#
        #if op.type == 17: #awal 17 ubah 13
           #if wait["Protectjoin"] == True:
               #if op.param2 not in admin and Bots : # Awalnya admin doang
                   #random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Joined User Kick start------#
        if op.type == 19: #Member Ke Kick
          if op.param2 not in Bots:
            if op.param2 not in admin:
                if op.param2 not in staff:
                   random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                   cl.inviteIntoGroup(op.param1,[op.param3])
        
        if op.type == 19: 
          if op.param3 in admin: #Kalo Admin ke Kick
            if op.param2 in Bots:
              pass
            if op.param2 in owner:
              pass
            else:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                cl.inviteIntoGroup(op.param1,[op.param3])
				
        if op.type == 19: 
          if op.param3 in staff: #Kalo Staff ke Kick
            if op.param2 in Bots:
              pass
            if op.param2 in owner:
              pass
            if op.param2 in admin:
              pass
            else:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                cl.inviteIntoGroup(op.param1,[op.param3])
              
        if op.type == 19:
          try:
            if op.param3 in Smid: #Akun Utama Ke Kick
              G = random.choice(KAC).getGroup(op.param1)
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              G.preventJoinByTicket = False
              random.choice(KAC).updateGroup(G)
              Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
              satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.001)
              G.preventJoinByTicket = True
              random.choice(KAC).updateGroup(G)
              satpam.updateGroup(G)
              wait["blacklist"][op.param2] = True
                                
            if op.param3 in mid:
              if op.param2 in Amid:
                G = ki.getGroup(op.param1)
                G.preventJoinByTicket = False
                ki.updateGroup(G)
                Ticket = ki.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                G.preventJoinByTicket = True
                ki.updateGroup(G)
              else:
                G = ki.getGroup(op.param1)
                ki.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ki.updateGroup(G)
                Ticket = ki.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
                ki.updateGroup(G)
                wait["blacklist"][op.param2] = True
                
            if op.param3 in Amid:
              if op.param2 in Bmid:
                G = kk.getGroup(op.param1)
                G.preventJoinByTicket = False
                kk.updateGroup(G)
                Ticket = kk.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                G.preventJoinByTicket = True
                kk.updateGroup(G)
              else:
                G = kk.getGroup(op.param1)
                kk.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                kk.updateGroup(G)
                Ticket = kk.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                G.preventJoinByTicket = True
                #cl.updateGroup(G)
                kk.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Bmid:
              if op.param2 in Cmid:
                G = kc.getGroup(op.param1)
                G.preventJoinByTicket = False
                kc.updateGroup(G)
                Ticket = kc.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                G.preventJoinByTicket = True
                kc.updateGroup(G)
              else:
                G = kc.getGroup(op.param1)
                kc.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                kc.updateGroup(G)
                Ticket = kc.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                G.preventJoinByTicket = True
                #cl.updateGroup(G)
                kc.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Cmid:
              if op.param2 in Dmid:
                G = ks.getGroup(op.param1)
                G.preventJoinByTicket = False
                ks.updateGroup(G)
                Ticket = ks.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                G.preventJoinByTicket = True
                ks.updateGroup(G)
              else:
                G = ks.getGroup(op.param1)
                ks.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ks.updateGroup(G)
                Ticket = ks.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                G.preventJoinByTicket = True
                #cl.updateGroup(G)
                ks.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Dmid:
              if op.param2 in Emid:
                G = ka.getGroup(op.param1)
                G.preventJoinByTicket = False
                ka.updateGroup(G)
                Ticket = ka.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                G.preventJoinByTicket = True
                ka.updateGroup(G)
              else:
                G = ka.getGroup(op.param1)
                ka.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ka.updateGroup(G)
                Ticket = ka.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                G.preventJoinByTicket = True
                #cl.updateGroup(G)
                ka.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Emid:
              if op.param2 in Fmid:
                G = kb.getGroup(op.param1)
                G.preventJoinByTicket = False
                kb.updateGroup(G)
                Ticket = kb.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                G.preventJoinByTicket = True
                kb.updateGroup(G)
              else:
                G = kb.getGroup(op.param1)
                kb.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                kb.updateGroup(G)
                Ticket = kb.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                G.preventJoinByTicket = True
                #cl.updateGroup(G)
                kb.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Gmid:
              if op.param2 in Hmid:
                G = ku.getGroup(op.param1)
                G.preventJoinByTicket = False
                ku.updateGroup(G)
                Ticket = ku.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                G.preventJoinByTicket = True
                ku.updateGroup(G)
              else:
                G = ku.getGroup(op.param1)
                ku.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ku.updateGroup(G)
                Ticket = ku.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                G.preventJoinByTicket = True
                #cl.updateGroup(G)
                ku.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Hmid:
              if op.param2 in Imid:
                G = ko.getGroup(op.param1)
                G.preventJoinByTicket = False
                ko.updateGroup(G)
                Ticket = ko.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                G.preventJoinByTicket = True
                ko.updateGroup(G)
              else:
                G = ko.getGroup(op.param1)
                ko.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ko.updateGroup(G)
                Ticket = ko.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                #cl.updateGroup(G)
                ko.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                
            if op.param3 in Imid:
              if op.param2 in mid:
                G = cl.getGroup(op.param1)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                Ticket = cl.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
              else:
                G = cl.getGroup(op.param1)
                cl.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ka.updateGroup(G)
                Ticket = cl.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.001)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
                #ke.updateGroup(G)
                #wait["blacklist"][op.param2] = True
          except:
            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            cl.inviteIntoGroup(op.param1,[op.param3])
#--------------------------------
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                              
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message


            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Menu admin"]:
                if msg.from_ in admin + owner:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,helpmenuadmin)
					else:
						cl.sendText(msg.to,Sett)
                else:
                    cl.sendText(msg.to,"Perintah ditolak")
                    cl.sendText(msg.to,"Perintah ini hanya untuk Admin")
            elif msg.text in ["Menu staff"]:
                if msg.from_ in admin + staff + owner:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,helpmenustaff)
					else:
						cl.sendText(msg.to,Sett)
                else:
                    cl.sendText(msg.to,"Perintah ditolak")
                    cl.sendText(msg.to,"Perintah ini untuk Staff dan Admin")
            elif msg.text in ["Menu owner"]:
                if msg.from_ in owner:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,helpown)
					else:
						cl.sendText(msg.to,helpt)
                else:
					cl.sendText(msg.to,"Perintah ditolak")
					cl.sendText(msg.to,"Perintah ini hanya untuk Owner kami")
            elif msg.text in ["Respon chat"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpchat)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Menu member"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpmenumember)
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
              if msg.from_ in admin + owner:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("2gn " in msg.text):
              if msg.from_ in admin + owner:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("2gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("3gn " in msg.text):
              if msg.from_ in admin + owner:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("3gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("4gn " in msg.text):
              if msg.from_ in admin + owner:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("4gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
#------------------------KICK------------------------------------					
            elif "Kick " in msg.text:
              if msg.from_ in admin + owner:
                midd = msg.text.replace("Kick ","")
                random.choice(KAC).kickoutFromGroup(msg.to,[midd])
            elif "2kick " in msg.text:
              if msg.from_ in admin + owner:
                midd = msg.text.replace("2kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "3kick " in msg.text:
              if msg.from_ in admin + owner:
                midd = msg.text.replace("3kick ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "4kick " in msg.text:
              if msg.from_ in admin + owner:
                midd = msg.text.replace("4kick ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "2invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("2invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "3invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("3invite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "4invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("4invite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
    #--------------- SC Add Admin ---------
            elif "Admin add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = ka.getGroup(msg.to)
                gs = kb.getGroup(msg.to)
                gs = ku.getGroup(msg.to)
                gs = ke.getGroup(msg.to)
                gs = ko.getGroup(msg.to)
                gs = satpam.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            cl.sendText(msg.to,"Admin Ditambahkan")
                        except:
                            pass
                print "[Command]Staff add executed"
              else:
                cl.sendText(msg.to,"Command denied.")
                cl.sendText(msg.to,"Admin permission required.")
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = ka.getGroup(msg.to)
                gs = kb.getGroup(msg.to)
                gs = ku.getGroup(msg.to)
                gs = ke.getGroup(msg.to)
                gs = ko.getGroup(msg.to)
                gs = satpam.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"Admin Dihapus")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                cl.sendText(msg.to,"Command denied.")
                cl.sendText(msg.to,"Admin permission required.")
				
    #--------------- SC Add Staff ---------
            elif "Staff add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Staff add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = ka.getGroup(msg.to)
                gs = kb.getGroup(msg.to)
                gs = ku.getGroup(msg.to)
                gs = ke.getGroup(msg.to)
                gs = ko.getGroup(msg.to)
                gs = satpam.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            staff.append(target)
                            cl.sendText(msg.to,"Staff Ditambahkan")
                        except:
                            pass
                print "[Command]Staff add executed"
              else:
                cl.sendText(msg.to,"Command denied.")
                cl.sendText(msg.to,"Owner permission required.")
                
            elif "Staff remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Staff remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = ka.getGroup(msg.to)
                gs = kb.getGroup(msg.to)
                gs = ku.getGroup(msg.to)
                gs = ke.getGroup(msg.to)
                gs = ko.getGroup(msg.to)
                gs = satpam.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            staff.remove(target)
                            cl.sendText(msg.to,"Staff Dihapus")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                cl.sendText(msg.to,"Command denied.")
                cl.sendText(msg.to,"Owner permission required.")
				
            elif msg.text in ["Stafflist","stafflist"]:
             if msg.from_ in admin + staff + owner:
              if staff == []:
                  cl.sendText(msg.to,"The stafflist is empty")
              else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "||Staff ||\n=====================\n"
                  for mi_d in staff:
                      mc += "••>" +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
                
            elif msg.text in ["Adminlist","adminlist"]:
             if msg.from_ in admin + staff + owner:
              if admin == []:
                  cl.sendText(msg.to,"The Adminlist is empty")
              else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "||Admin ||\n=====================\n"
                  for mi_d in admin:
                      mc += "••>" +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
				  
            elif msg.text in ["Crewlist","crewlist"]:
             if msg.from_ in admin + staff + owner:
              if admin == []:
                  cl.sendText(msg.to,"The Crewlist is empty")
              else:
                  cl.sendText(msg.to,"Tunggu...")
                  mo = ""
                  ma = ""
                  ms = ""
                  for mi_d in owner:
                      mo += "••>" +cl.getContact(mi_d).displayName + "\n"
                  for mi_d in admin:
                      ma += "••>" +cl.getContact(mi_d).displayName + "\n"
                  for mi_d in staff:
                      ms += "••>" +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,"==========OWNER==========\n" + mo + "\n==========ADMIN==========\n" + ma + "\n==========STAFF==========\n" + ms)
                  print "[Command]Stafflist executed"
    #--------------------------------------
    #-------------- Add Friends ------------
            elif "Luly add @" in msg.text:
              if msg.toType == 2:
                if msg.from_ in owner:
                  print "[Command]Add executing"
                  _name = msg.text.replace("Luly add @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  gs = ki.getGroup(msg.to)
                  gs = kk.getGroup(msg.to)
                  gs = kc.getGroup(msg.to)
                  gs = ks.getGroup(msg.to)
                  gs = ka.getGroup(msg.to)
                  gs = kb.getGroup(msg.to)
                  gs = ke.getGroup(msg.to)
                  gs = ko.getGroup(msg.to)
                  gs = ku.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    random.choice(KAC).sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        ki.findAndAddContactsByMid(target)
                        kk.findAndAddContactsByMid(target)
                        kc.findAndAddContactsByMid(target)
                        ks.findAndAddContactsByMid(target)
                        ka.findAndAddContactsByMid(target)
                        kb.findAndAddContactsByMid(target)
                        ko.findAndAddContactsByMid(target)
                        ke.findAndAddContactsByMid(target)
                        ku.findAndAddContactsByMid(target)
                      except:
                        cl.sendText(msg.to,"Error")
              else:
                cl.sendText(msg.to,"Perintah Ditolak")
                cl.sendText(msg.to,"Perintah ini Hana Untuk Owner Kami")
                  
    #-------------=SC AllBio=---------------- Ganti Bio Semua Bot Format => Allbio: SUKA SUKA KALIAN :D
            elif "Allbio: " in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Allbio: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ks.getProfile()
                    profile.statusMessage = string
                    ks.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ka.getProfile()
                    profile.statusMessage = string
                    ka.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kb.getProfile()
                    profile.statusMessage = string
                    kb.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ku.getProfile()
                    profile.statusMessage = string
                    ku.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ke.getProfile()
                    profile.statusMessage = string
                    ke.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ko.getProfile()
                    profile.statusMessage = string
                    ko.updateProfile(profile)
                    cl.sendText(msg.to,"Bio berubah menjadi " + string + "")
    #--------------=Finish=----------------
    #--------------= SC Ganti nama Owner=--------------
            elif "Rename: " in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Rename: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    Satpam.updateProfile(profile)
                    cl.sendText(msg.to,"Yang punya ganti nama jadi : " + string + "")
    #-------------- copy profile----------
            elif "Spam: " in msg.text:
              if msg.from_ in admin + owner:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam: ")+str(txt[1])+" "+str(jmlh + " ","")
                tulisan = jmlh * (teks+"\n")
                 #@reno.a.w
                if txt[1] == "on":
                    if jmlh <= 300:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 300:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
    #-----------------=Selesai=------------------
            elif msg.text in ["Luly contact"]: #Ngirim Semua Kontak Bot
              if msg.from_ in admin + owner:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ks.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ka.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                kb.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                ko.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                ke.sendMessage(msg)
				
                msg.contentType = 13
                msg.contentMetadata = {'mid': Imid}
                ku.sendMessage(msg)
				
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                random.choice(KAC).sendMessage(msg)

            elif msg.text in ["L1"]:
              if msg.from_ in admin + owner:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                kk.sendMessage(msg)
				
            elif msg.text in ["L2"]:
              if msg.from_ in admin + owner:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                kk.sendMessage(msg)
				
            elif msg.text in ["L3"]:
              if msg.from_ in admin + owner:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
				
            elif msg.text in ["L4"]:
              if msg.from_ in admin + owner:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kk.sendMessage(msg)
				
            elif msg.text in ["L5"]:
              if msg.from_ in admin + owner:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                kk.sendMessage(msg)
				
            elif msg.text in ["L6"]:
              if msg.from_ in admin + owner:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                kk.sendMessage(msg)
				
            elif msg.text in ["L7"]:
              if msg.from_ in admin + owner:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                kk.sendMessage(msg)
				
            elif msg.text in ["L8"]:
              if msg.from_ in admin + owner:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                kk.sendMessage(msg)
				
            elif msg.text in ["L9"]:
              if msg.from_ in admin + owner:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                kk.sendMessage(msg)
				
            elif msg.text in ["L9"]:
              if msg.from_ in admin + owner:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
				
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
              if msg.from_ in admin + staff + owner:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","3gift"]:
             if msg.from_ in admin + staff + owner:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
            elif msg.text in ["Cancel invite"]:
             if msg.from_ in admin + staff + owner:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Luly cancel","luly cancel"]:
             if msg.from_ in admin + staff + owner:
                if msg.toType == 2:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"No one is inviting")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Buka qr","Open qr","Oqr","Bqr"]:
              if msg.from_ in admin + staff + owner:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"QR Sudah Dibuka")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Terbuka Plak")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")

            elif msg.text in ["Tutup qr","Close qr","Tqr","Cqr","tutup qr","close qr","cqr","tqr"]:
              if msg.from_ in admin + staff + owner:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Kode QR Sudah Di Tutup")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Tertutup Plak")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")

            elif msg.text in ["Jointicket "]:
                 if msg.from_ in admin + staff + owner:
					rplace=msg.text.lower().replace("jointicket ")
					if rplace == "on":
						wait["atjointicket"]=True
					elif rplace == "off":
						wait["atjointicket"]=False
						cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
				   
            elif "/ti/g/" in msg.text.lower():
                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                links = link_re.findall(msg.text)
                n_links=[]
                for l in links:
                   if l not in n_links:
                      n_links.append(l)
                      for ticket_id in n_links:
                         if wait["atjointicket"] == True:
                            group=cl.findGroupByTicket(ticket_id)
                            cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
                            cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
                     
            elif "Info Group" == msg.text:
              if msg.toType == 2:
                if msg.from_ in admin + staff + owner:
                  ginfo = cl.getGroup(msg.to)
                  try:
                    gCreator = ginfo.creator.displayName
                  except:
                    gCreator = "Error"
                  if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                      sinvitee = "0"
                    else:
                      sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventJoinByTicket == True:
                      QR = "Close"
                    else:
                      QR = "Open"
                    random.choice(KAC).sendText(msg.to,"╔════════════════════\n║ Nama Group\n╚════════════════════\n" + str(ginfo.name) + "\n\n╔════════════════════\n║ Group ID\n╚════════════════════\n" +  msg.to + "\n\n╔════════════════════\n║ Group Creator\n╚════════════════════\n" +  gCreator + "\n\n╔════════════════════\n║ Group Status\n╚════════════════════\n" + "Status QR ❂➣ " + QR + "\n\n╔════════════════════\n║ Group Picture\n╚════════════════════\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n═════════════════════"+"\n\n"+"Members: " + str(len(ginfo.members)) +"\nPending: " + sinvitee)
                  else:
                    random.choice(KAC).sendText(msg.to,"╔════════════════════\n║ Nama Group\n╚════════════════════\n" + str(ginfo.name) + "\n\n╔════════════════════\n║ Group ID\n╚════════════════════\n" + msg.to + "\n\n╔════════════════════\n║ Group Creator\n╚════════════════════\n" + gCreator + "\n\n╔════════════════════\n║ Group Status\n╚════════════════════\n" + "\n╔════════════════════\n║ Group Picture\n╚════════════════════\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Can not be used outside the group")
                  else:
                    cl.sendText(msg.to,"Not for use less than group")
                
            elif "My mid" == msg.text:
                random.choice(KAC).sendText(msg.to, msg.from_)
				
            elif "Mid Bot" == msg.text:
              if msg.from_ in admin + owner:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
                ks.sendText(msg.to,Dmid)
                ka.sendText(msg.to,Emid)
                kb.sendText(msg.to,Fmid)
                ko.sendText(msg.to,Gmid)
                ke.sendText(msg.to,Hmid)
                ku.sendText(msg.to,Imid)
				
            elif "Satpam" == msg.text:
              if msg.from_ in admin + owner:
                cl.sendText(msg.to,Smid)
            elif "1mid" == msg.text:
              if msg.from_ in admin + owner:
                cl.sendText(msg.to,mid)
            elif "2mid" == msg.text:
              if msg.from_ in admin + owner:
                ki.sendText(msg.to,Amid)
            elif "3mid" == msg.text:
              if msg.from_ in admin + owner:
                kk.sendText(msg.to,Bmid)
            elif "4mid" == msg.text:
              if msg.from_ in admin + owner:
                kc.sendText(msg.to,Cmid)
            elif "5mid" == msg.text:
              if msg.from_ in admin + owner:
                ks.sendText(msg.to,Dmid)
            elif "6mid" == msg.text:
              if msg.from_ in admin + owner:
                ka.sendText(msg.to,Emid)
            elif "7mid" == msg.text:
              if msg.from_ in admin + owner:
                kb.sendText(msg.to,Fmid)
            elif "8mid" == msg.text:
              if msg.from_ in admin + owner:
                ko.sendText(msg.to,Gmid)
            elif "9mid" == msg.text:
              if msg.from_ in admin + owner:
                ke.sendText(msg.to,Hmid)
            elif "10mid" == msg.text:
              if msg.from_ in admin + owner:
                ku.sendText(msg.to,Imid)
				
            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Galau","Galon","galon","galau"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You","u","U","you"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh","Hadeh","hadeuh","hadeh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa","haaa","Wow","wow"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol","wew","lol","Wew"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["TL: "]:
              if msg.from_ in admin + owner:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
				
            elif msg.text in ["1rn "]:
              if msg.from_ in owner:
                string = msg.text.replace("1rn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["2rn "]:
              if msg.from_ in owner:
                string = msg.text.replace("2rn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["3rn "]:
              if msg.from_ in owner:
                string = msg.text.replace("3rn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["4rn "]:
              if msg.from_ in owner:
                string = msg.text.replace("4rn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kc.getProfile()
                    profile_B.displayName = string
                    kc.updateProfile(profile_B)
                    kc.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["5rn "]:
              if msg.from_ in owner:
                string = msg.text.replace("5rn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ks.getProfile()
                    profile_B.displayName = string
                    ks.updateProfile(profile_B)
                    ks.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["6rn "]:
              if msg.from_ in owner:
                string = msg.text.replace("6rn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ka.getProfile()
                    profile_B.displayName = string
                    ka.updateProfile(profile_B)
                    ka.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["7rn "]:
              if msg.from_ in owner:
                string = msg.text.replace("7rn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kb.getProfile()
                    profile_B.displayName = string
                    kb.updateProfile(profile_B)
                    kb.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["8rn "]:
              if msg.from_ in owner:
                string = msg.text.replace("8rn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ko.getProfile()
                    profile_B.displayName = string
                    ko.updateProfile(profile_B)
                    ko.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["9rn "]:
              if msg.from_ in owner:
                string = msg.text.replace("9rn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ke.getProfile()
                    profile_B.displayName = string
                    ke.updateProfile(profile_B)
                    ke.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["10rn "]:
              if msg.from_ in owner:
                string = msg.text.replace("10rn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ku.getProfile()
                    profile_B.displayName = string
                    ku.updateProfile(profile_B)
                    ku.sendText(msg.to,"name " + string + " done")
					
            elif msg.text in ["Mc "]:
              if msg.from_ in admin + owner:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            #elif msg.text in ["Joinn on","joinn on"]:
              #if msg.from_ in admin:
                #if wait["Protectjoin"] == True:
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"Kick Joined Group On")
                    #else:
                        #cl.sendText(msg.to,"Done")
                #else:
                    #wait["Protectjoin"] = True
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"Kick Joined Group On")
                    #else:
                        #cl.sendText(msg.to,"done")
            #elif msg.text in ["Joinn off","joinn off"]:
              #if msg.from_ in admin:
                #if wait["Protectjoin"] == False:
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"kick Joined Group Off")
                    #else:
                        #cl.sendText(msg.to,"done")
                #else:
                    #wait["Protectjoin"] = False
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"kick Joined Group Off")
                    #else:
                        #cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel on","cancel on"]:
              if msg.from_ in admin + staff + owner:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","cancel off"]:
               if msg.from_ in admin + staff + owner:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in admin + staff + owner:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in admin + staff + owner:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in admin + staff + owner:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in admin + staff + owner:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Join on","Autojoin on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
              if msg.from_ in admin + staff + owner:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Join off","Autojoin off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
              if msg.from_ in admin + owner:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
              if msg.from_ in admin + staff + owner:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Autoleave on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
              if msg.from_ in admin + owner:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Autoleave off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
              if msg.from_ in admin + owner:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
              if msg.from_ in admin + staff + owner:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
              if msg.from_ in admin + staff + owner:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Status","Set"]:
              if msg.from_ in admin + staff + owner:
                md = ""
                if wait["Protectgr"] == True: md+="Uʀʟ Pʀᴏᴛᴇᴄᴛ → ✔\n"
                else: md+="Uʀʟ Pʀᴏᴛᴇᴄᴛ → ❌ \n"
                if wait["Protectcancl"] == True: md+="Dᴇɴʏ ɪɴᴠɪᴛᴇ → ✔\n"
                else: md+="Dᴇɴʏ ɪɴᴠɪᴛᴇ → ❌\n"
                if wait["contact"] == True: md+="Cᴏɴᴛᴀᴄᴛ → ✔\n"
                else: md+=" Cᴏɴᴛᴀᴄᴛ → ❌\n"
                if wait["autoJoin"] == True: md+="Aᴜᴛᴏ Jᴏɪɴ → ✔\n"
                else: md +="Aᴜᴛᴏ Jᴏɪɴ → ❌\n"
                if wait["autoCancel"]["on"] == True:md+="Gʀᴏᴜᴘ Cᴀɴᴄᴇʟ: " + str(wait["autoCancel"]["members"]) + "→ ✔\n"
                else: md+= "Gʀᴏᴜᴘ Cᴀɴᴄᴇʟ → ❌\n"
                if wait["leaveRoom"] == True: md+="Aᴜᴛᴏ Lᴇᴀᴠᴇ → ✔\n"
                else: md+="Aᴜᴛᴏ Lᴇᴀᴠᴇ → ❌\n"
                if wait["timeline"] == True: md+="Sʜᴀʀᴇ → ✔\n"
                else:md+="Sʜᴀʀᴇ → ❌\n"
                if wait["autoAdd"] == True: md+="Aᴜᴛᴏ Aᴅᴅ → ✔\n"
                else:md+="Aᴜᴛᴏ Aᴅᴅ → ❌\n"
                if wait["commentOn"] == True: md+="Aᴜᴛᴏ Cᴏᴍᴇɴᴛ → ✔"
                else:md+="Aᴜᴛᴏ Cᴏᴍᴇɴᴛ → ❌"
                cl.sendText(msg.to,md)
				
#            elif "album merit " in msg.text:
#              if msg.from_ in admin + staff + owner:
#                gid = msg.text.replace("album merit ","")
#                album = cl.getAlbum(gid)
#                if album["result"]["items"] == []:
#                    if wait["lang"] == "JP":
#                        cl.sendText(msg.to,"There is no album")
#                    else:
#                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
#                else:
#                    if wait["lang"] == "JP":
#                        mg = "The following is the target album"
#                    else:
#                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
#                    for y in album["result"]["items"]:
#                        if "photoCount" in y:
#                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
#                        else:
#                            mg += str(y["title"]) + ":0sheet\n"
#                    cl.sendText(msg.to,mg)
#            elif "album " in msg.text:
#              if msg.from_ in admin + staff + owner:
#                gid = msg.text.replace("album ","")
#                album = cl.getAlbum(gid)
#                if album["result"]["items"] == []:
#                    if wait["lang"] == "JP":
#                        cl.sendText(msg.to,"There is no album")
#                    else:
#                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
#                else:
#                    if wait["lang"] == "JP":
#                        mg = "The following is the target album"
#                    else:
#                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
#                    for y in album["result"]["items"]:
#                        if "photoCount" in y:
#                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
#                        else:
#                            mg += str(y["title"]) + ":0sheet\n"
#            elif "album remove " in msg.text:
#              if msg.from_ in admin + staff + owner:
#                gid = msg.text.replace("album remove ","")
#                albums = cl.getAlbum(gid)["result"]["items"]
#                i = 0
#                if albums != []:
#                    for album in albums:
#                        cl.deleteAlbum(gid,album["id"])
#                        i += 1
#                if wait["lang"] == "JP":
#                    cl.sendText(msg.to,str(i) + "Deleted albums")
#                else:
#                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Jgid"]:
              if msg.from_ in owner:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
              if msg.from_ in admin + staff + owner:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
#            elif "album removeat'" in msg.text:
#              if msg.from_ in admin + staff + owner:
#                gid = msg.text.replace("album removeat’","")
#                albums = cl.getAlbum(gid)["result"]["items"]
#                i = 0
#                if albums != []:
#                    for album in albums:
#                        cl.deleteAlbum(gid,album["id"])
#                        i += 1
#                if wait["lang"] == "JP":
#                    cl.sendText(msg.to,str(i) + "Albums deleted")
#                else:
#                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Autoadd on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
              if msg.from_ in admin + owner:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Autoadd off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
              if msg.from_ in admin +owner:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
              if msg.from_ in admin + owner:
                wait["message"] = msg.text.replace("Message change: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment: " in msg.text:
              if msg.from_ in admin + staff + owner:
                c = msg.text.replace("Comment: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment: " in msg.text:
              if msg.from_ in admin + staff + owner:
                c = msg.text.replace("Add comment: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
#---------------------Sc invite owner ke group------
            elif "/invitemeto: " in msg.text:
              if msg.from_ in owner:
                gid = msg.text.replace("/invitemeto: ","")
                if gid == "":
                  cl.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    cl.findAndAddContactsByMid(msg.from_)
                    cl.inviteIntoGroup(gid,[msg.from_])
                  except:
                    cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#--------===---====--------------
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","comment on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
              if msg.from_ in admin + staff + owner:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment off","comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
              if msg.from_ in admin + staff + owner:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
              if msg.from_ in admin + staff + owner:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = random.choice(KAC).getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        random.choice(KAC).updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    random.choice(KAC).sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["Comment bl "]:
              if msg.from_ in admin + owner:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Jam on"]:
              if msg.from_ in admin + owner:
                if wait["clock"] == True:
                    kc.sendText(msg.to,"Bot 4 jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
              if msg.from_ in admin + owner:
                if wait["clock"] == False:
                    kc.sendText(msg.to,"Bot 4 jam off")
                else:
                    wait["clock"] = False
                    kc.sendText(msg.to,"Jam Sedang Off")
        #-------------Fungsi Jam on/off Finish-------------------#           
         
        #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Ubah jam "]:
                n = msg.text.replace("Ubah jam","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
        #-------------Fungsi Change Clock Finish-----------------#           
        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Jam Update"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Sukses update")
                else:
                    kc.sendText(msg.to,"Aktifkan jam terlebih dulu")
        #-------------Fungsi Jam Update Finish-------------------#

            elif msg.text == "Cctv":
              if msg.from_ in admin + staff + owner:
                cl.sendText(msg.to, "Cek CCTV")
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
                #print wait2
              
            elif msg.text == "Ciduk":
              if msg.from_ in admin + staff + owner:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                #print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "╔═══════════════%s\n╠════════════════\n%s╠═══════════════\n║Readig point creation:\n║ [%s]\n╚════════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik Cctv dulu Koplak\nBaru Ketil Ciduk\nDASAR PIKUN ♪")
#-----------------------------------------------

#-----------------------------------------------
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["Masuk sayang",".join"]:
              if msg.from_ in owner:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ki.sendText(msg.to, "Aku datang beb")
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        kk.sendText(msg.to, "Iya sayang")
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        kc.sendText(msg.to, "Ada buat kamu")
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ks.sendText(msg.to, "Cipok nih")
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ka.sendText(msg.to, "Muaaaach")
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        kb.sendText(msg.to, "Hadir beb")
                        ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        kb.sendText(msg.to, "Ada apa sayang")
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ke.sendText(msg.to, "Lope u bibeeh")
                        ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ki.sendText(msg.to, "Minggir bebeb gua")
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "Semua Sudah Lengkap Sayang"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).sendText(msg.to, "Semua sudah legkap sayang..!!")
                        random.choice(KAC).updateGroup(G)
  
            elif msg.text in ["/join"]:
              if msg.from_ in owner:
                        G = satpam.getGroup(msg.to)
                        ginfo = satpam.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        satpam.updateGroup(G)
                        invsend = 0
                        Ticket = satpam.reissueGroupTicket(msg.to)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        cl.sendText(msg.to, "Aku datang beb")
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ki.sendText(msg.to, "Aku temenin sayang")
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        kk.sendText(msg.to, "Njiiiir ke tiga gw")
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        kc.sendText(msg.to, "Assyik mojok beb")
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ks.sendText(msg.to, "Hadir sayang ku, cinta ku")
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ka.sendText(msg.to, "Gw mah cipok aja dah, muaaaach")
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        kb.sendText(msg.to, "Muaaaaaach juga")
                        ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ko.sendText(msg.to, "Muaaacccchh lagi")
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ke.sendText(msg.to, "Cintaaaaaaaaaa")
                        ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ku.sendText(msg.to, "Njiiir barisan para mantan udah pada dateng")
                        G = satpam.getGroup(msg.to)
                        ginfo = satpam.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        satpam.updateGroup(G)
                        print "Semua Sudah Lengkap"
                        G.preventJoinByTicket(G)
                        satpam.updateGroup(G)
                        random.choice(KAC).sendText(msg.to, "Semua sudah legkap sayang..!!")

            elif msg.text in ["1join"]:
              if msg.from_ in owner:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["2join"]:
              if msg.from_ in owner:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["3Join"]:
              if msg.from_ in owner:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
				  
            elif msg.text in ["4Join"]:
              if msg.from_ in owner:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ks.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["5Join"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ka.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
				  
            elif msg.text in ["6Join"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kb.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
				  
            elif msg.text in ["7Join"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ko.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
				  
            elif msg.text in ["8Join"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ke.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
				  
            elif msg.text in ["9Join"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ku.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

    #----------------------Fungsi Join Group Finish---------------#

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["Bubar say"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        ko.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        ku.leaveGroup(msg.to)
                        cl.leaveGroup(msg.to)
                    except:
                        pass
            
            elif msg.text in ["/out"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        ko.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        ku.leaveGroup(msg.to)
                        #cl.leaveGroup(msg.to)
                    except:
                        pass
                      
            elif msg.text in ["1out"]:
              if msg.from_ in admin + owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["2out"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Clout"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["3out"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["4out"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ks.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["5out"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ka.leaveGroup(msg.to)
                    except:
                        pass
    #-------------Fungsi Leave Group Finish---------------#
    
    #-------------Fungsi Tag All Start---------------#
            elif "tagall" == msg.text.lower():
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "╔════════════════════\n" + "╠➣" + str(jml) +  " Para Jones"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)       

    #-------------Fungsi Tag All Finish---------------#
            elif msg.text in ["Luly Like", "luly like"]: #Semua Bot Ngelike Status Akun Utama
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Owner")
                try:
                  likePost()
                except:
                  pass
                
            elif msg.text in ["Luly like temen", "luly like temen"]: #Semua Bot Ngelike Status Teman
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Teman Boss")
                try:
                  autolike()
                except:
                  pass
        #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill "]:
              if msg.from_ in admin + owner:
                if msg.toType == 2:
                    group = random.choice(KAC).getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Selamat tinggal")
                        random.choice(KAC).sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,kc,ks,ka,kb,ku,ke,ko]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
        #----------------Fungsi Banned Kick Target Finish----------------------#                

            elif "Sikaat" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Salam","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    random.choice(KAC).sendText(msg.to,"maaf kalo gak sopan")
                    random.choice(KAC).sendText(msg.to,"makasih semuanya..")
                    random.choice(KAC).sendText(msg.to,"hehehhehe")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    random.choice(KAC).sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        random.choice(KAC).sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in admin and Bots:
                            try:
                                klist=[cl,ki,kk,kc,ks,ka,kb,ku,ke,ko]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                random.choice(KAC).sendText(msg.to,"Sorry Brader")
                                random.choice(KAC).sendText(msg.to,"Sorry Sister")
                                random.choice(KAC).sendText(msg.to,"No Baper")

#==============================================================================#
            elif "Nk " in msg.text:
              if msg.from_ in admin + owner:
                nk0 = msg.text.replace("Nk ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("@","")
                nk3 = nk2.rstrip()
                _name = nk3
                gs = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.001)
                targets = []
                for s in gs.members:
                    if _name in s.displayName:
                       targets.append(s.mid)
                if targets == []:
                   sendMessage(msg.to,"user does not exist")
                   pass
                else:
                   for target in targets:
                      try:
                        k1.kickoutFromGroup(msg.to,[target])
                        print (msg.to,[g.mid])
                      except:
                        k1.leaveGroup(msg.to)
                        gs = cl.getGroup(msg.to)
                        gs.preventJoinByTicket = True
                        cl.updateGroup(gs)
                        gs.preventJoinByTicket(gs)
                        cl.updateGroup(gs)
#==============================================================================#  
            elif "Blacklist @ " in msg.text:
              if msg.from_ in admin + owner:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = random.choice(KAC).getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            random.choice(KAC).sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    random.choice(KAC).sendText(msg.to,"Succes Plak")
                                except:
                                    random.choice(KAC).sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Banned @" in msg.text:
              if msg.from_ in admin + owner:
                if msg.toType == 2:
                    print "[Banned] Sukses"
                    _name = msg.text.replace("Banned @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = ka.getGroup(msg.to)
                    gs = kb.getGroup(msg.to)
                    gs = ko.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    gs = ku.getGroup(msg.to)
                    gs = satpam.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Dilarang Banned Bot")
                        ki.sendText(msg.to,"Dilarang Banned Bot")
                        kk.sendText(msg.to,"Dilarang Banned Bot")
                        kc.sendText(msg.to,"Dilarang Banned Bot")
                        ks.sendText(msg.to,"Dilarang Banned Bot")
                        ka.sendText(msg.to,"Dilarang Banned Bot")
                        kb.sendText(msg.to,"Dilarang Banned Bot")
                        ko.sendText(msg.to,"Dilarang Banned Bot")
                        ke.sendText(msg.to,"Dilarang Banned Bot")
                        ku.sendText(msg.to,"Dilarang Banned Bot")
                        satpam.sendText(msg.to,"Laah yang punya ko di Banned")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                random.choice(KAC).sendText(msg.to,"Akun telah sukses di banned")
                            except:
                                random.choice(KAC).sendText(msg.to,"Error")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            #----------------Mid via Tag--------------
            elif "Mid @" in msg.text:
              if msg.from_ in admin + owner:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        random.choice(KAC).sendText(msg.to, g.mid)
                    else:
                        pass
            #-----------------------------------------
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in admin + owner:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = ka.getGroup(msg.to)
                    gs = kb.getGroup(msg.to)
                    gs = ko.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    gs = ku.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan.....")
                        ki.sendText(msg.to,"Tidak Ditemukan.....")
                        kk.sendText(msg.to,"Tidak Ditemukan.....")
                        kc.sendText(msg.to,"Tidak Ditemukan.....")
                        ks.sendText(msg.to,"Tidak Ditemukan.....")
                        ka.sendText(msg.to,"Tidak Ditemukan.....")
                        kb.sendText(msg.to,"Tidak Ditemukan.....")
                        ko.sendText(msg.to,"Tidak Ditemukan.....")
                        ke.sendText(msg.to,"Tidak Ditemukan.....")
                        ku.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                ki.sendText(msg.to,"Error")
          #----------------Fungsi Unbanned User Target Finish-----------------------#
           
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Up","up","Up Chat","Up chat","up chat","Upchat","upchat"]:
              if msg.from_ in admin + owner:
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!LAST ONE")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
        #-------------Fungsi Spam Finish---------------------#

        #-------------Fungsi Broadcast Start------------#
            elif "Bcg " in msg.text: #NgeBC Ke semua Group yang di Join :D
              if msg.from_ in owner:
                 bctxt = msg.text.replace("Bc ","")
                 a = cl.getGroupIdsJoined()
                 a = ki.getGroupIdsJoined()
                 a = kk.getGroupIdsJoined()
                 a = kc.getGroupIdsJoined()
                 a = ks.getGroupIdsJoined()
                 a = ka.getGroupIdsJoined()
                 a = ku.getGroupIdsJoined()
                 a = ke.getGroupIdsJoined()
                 a = ko.getGroupIdsJoined()
                 a = kb.getGroupIdsJoined()
                 for taf in a:
                     cl.sendText(taf, (bctxt))
                     ki.sendText(taf, (bctxt))
                     kk.sendText(taf, (bctxt))
                     kc.sendText(taf, (bctxt))
                     ks.sendText(taf, (bctxt))
                     ka.sendText(taf, (bctxt))
                     kb.sendText(taf, (bctxt))
                     ke.sendText(taf, (bctxt))
                     ku.sendText(taf, (bctxt))
                     ko.sendText(taf, (bctxt))
      #--------------Fungsi Broadcast Finish-----------#

            elif msg.text in ["LG"]: #Melihat List Group
              if msg.from_ in owner:
                 gids = cl.getGroupIdsJoined()
                 h = ""
                 for i in gids:
                  #####gn = cl.getGroup(i).name
                  h += " ➣ %s Member\n" % (cl.getGroup(i).name   +"╠➣ "+str(len(cl.getGroup(i).members)))
                 cl.sendText(msg.to,"╔════════════════════\n║  LIST GROUP\n╠════════════════════\n"+ h + "╠════════════════════\n" "Total Group :"+str(len(gids)) + "╚══════════════════════")
                
            elif msg.text in ["LG2"]: #Melihat List Group + ID Groupnya (Gunanya Untuk Perintah InviteMeTo:)
              if msg.from_ in owner:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
      #--------------List Group------------
       #------------ Keluar Dari Semua Group------
            elif msg.text in ["Bubar all group"]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
              if msg.from_ in owner:
                 gid = cl.getGroupIdsJoined()
                 gid = ki.getGroupIdsJoined()
                 gid = kk.getGroupIdsJoined()
                 gid = kc.getGroupIdsJoined()
                 gid = ks.getGroupIdsJoined()
                 gid = ka.getGroupIdsJoined()
                 gid = kb.getGroupIdsJoined()
                 gid = ko.getGroupIdsJoined()
                 gid = ke.getGroupIdsJoined()
                 gid = ku.getGroupIdsJoined()
                 for i in gid:
                   ku.leaveGroup(i)
                   ke.leaveGroup(i)
                   ko.leaveGroup(i)
                   kb.leaveGroup(i)
                   ka.leaveGroup(i)
                   ks.leaveGroup(i)
                   kc.leaveGroup(i)
                   ki.leaveGroup(i)
                   kk.leaveGroup(i)
                   cl.leaveGroup(i)
                 if wait["lang"] == "JP":
                   cl.sendText(msg.to,"Sayonara")
                 else:
                   cl.sendText(msg.to,"He declined all invitations")
 #------------------------End---------------------

 #-----------------End-----------
            elif msg.text in ["Luly say hi"]:
              if msg.from_ in admin + staff + owner:
                ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Hi bapak buddy 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Hi ibu buddy 􀜁􀅔Har Har􏿿")

#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
              if msg.from_ in admin + owner:
                cl.sendText(msg.to,"PING PONG 􀨁􀄻double thumbs up􏿿")
                ki.sendText(msg.to,"PING PONG 􀨁􀄻double thumbs up􏿿")
                kk.sendText(msg.to,"PING PONG 􀨁􀄻double thumbs up􏿿")
                kc.sendText(msg.to,"PING PONG 􀨁􀄻double thumbs up􏿿")
                ks.sendText(msg.to,"PING PONG 􀨁􀄻double thumbs up􏿿")
                ka.sendText(msg.to,"PING PING 􀜁􀅔Har Har􏿿")
                kb.sendText(msg.to,"CECAN 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ko.sendText(msg.to,"PING PING 􀜁􀅔Har Har􏿿")
                ke.sendText(msg.to,"HAYAM 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ke.sendText(msg.to,"􀜁􀅔Har Har􏿿􀜁􀅔Har Har􏿿􀜁􀅔Har Har􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Absen","Absen bot","Absen dulu","Respon"]:
              if msg.from_ in admin + owner:
                cl.sendText(msg.to,"⭐")
                ki.sendText(msg.to,"⭐⭐")
                kk.sendText(msg.to,"⭐⭐⭐")
                kc.sendText(msg.to,"⭐⭐⭐⭐")
                ks.sendText(msg.to,"⭐⭐⭐⭐⭐")
                ka.sendText(msg.to,"⭐⭐⭐⭐⭐⭐")
                kb.sendText(msg.to,"⭐⭐⭐⭐⭐⭐⭐")
                ko.sendText(msg.to,"⭐⭐⭐⭐⭐⭐⭐⭐")
                ke.sendText(msg.to,"⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                ku.sendText(msg.to,"⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                cl.sendText(msg.to,"Semua Udah Hadir Boss\nSiap Protect Group\nAman Gak Aman Yang Penting Anu Har􏿿􀜁􀅔Har Har􏿿")
      #-------------Fungsi Respon Finish---------------------#
                            

      #-------------Fungsi Balesan Respon Start---------------------#
#            elif msg.text in ["Ini Apa","ini apa","Apaan Ini","apaan ini"]:
#                ki.sendText(msg.to,"Ya gitu deh intinya mah 􀨁􀅴questioning􏿿")

      #-------------Fungsi Balesan Respon Finish---------------------#

       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Speed","Sp"]:
              if msg.from_ in admin + staff + owner:
                start = time.time()
                cl.sendText(msg.to, "Sabar mas bro...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sDetik" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban"]:
              if msg.from_ in owner:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Kirim contact")
                ki.sendText(msg.to,"Kirim contact")
                kk.sendText(msg.to,"Kirim contact")
                kc.sendText(msg.to,"Kirim contact")
                ks.sendText(msg.to,"Kirim contact")
                ka.sendText(msg.to,"Kirim contact")
                kb.sendText(msg.to,"Kirim contact")
                ko.sendText(msg.to,"Kirim contact")
                ke.sendText(msg.to,"Kirim contact")
                ku.sendText(msg.to,"Kirim contact")
            elif msg.text in ["Unban"]:
              if msg.from_ in owner:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Kirim contact")
                ki.sendText(msg.to,"Kirim contact")
                kk.sendText(msg.to,"Kirim contact")
                kc.sendText(msg.to,"Kirim contact")
                ks.sendText(msg.to,"Kirim contact")
                ka.sendText(msg.to,"Kirim contact")
                kb.sendText(msg.to,"Kirim contact")
                ko.sendText(msg.to,"Kirim contact")
                ke.sendText(msg.to,"Kirim contact")
                ku.sendText(msg.to,"Kirim contact")
      #-------------Fungsi Banned Send Contact Finish------------------#
            elif msg.text in ["Creator"]:
              msg.contentType = 13
              msg.contentMetadata = {'mid': 'ubbf5fbe22865fcd64a4c4937d5b547c6'}
              cl.sendMessage(msg)
              cl.sendText(msg.to,"Itu Creator Kami Yang ehem..ehem 😜")
                
      #-------------Fungsi Chat ----------------
            elif msg.text in ["Woy","woy","Woi","woi","bot","Bot"]:
                 quote = ['Istri yang baik itu Istri yang Mengizinkan Suaminya untuk Poligami 😂😂😂.','Kunci Untuk Bikin Suami Bahagia itu cuma satu..\nIzinkan Suamimu Untuk Selingkuh Coyyy ','Ah Kupret Lu','Muka Lu Kaya Jamban','Ada Orang kah disini?','Sange Euy','Ada Perawan Nganggur ga Coy?']
                 psn = random.choice(quote)
                 cl.sendText(msg.to,psn)
            
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin + staff + owner:
                if wait["blacklist"] == {}:
                    random.choice(KAC).sendText(msg.to,"Tidak Ada Akun Terbanned")
                else:
                    random.choice(KAC).sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
    #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["Ban cek","Cekban"]:
              if msg.from_ in admin + staff + owner:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = "ʙʟᴀᴄᴋʟɪsᴛ ᴍɪᴅ ᴜsᴇʀ ʙᴀɴᴇᴅ"
                    for mm in matched_list:
                        cocoa += "\n" + mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
              if msg.from_ in admin + owner:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear invite"]:
              if msg.from_ in admin + staff + owner:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
#            elif "Random: " in msg.text:
#              if msg.from_ in admin + owner:
#                if msg.toType == 2:
#                    strnum = msg.text.replace("random: ","")
#                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
#                    try:
#                        num = int(strnum)
#                        group = cl.getGroup(msg.to)
#                        for var in range(0,num):
#                            name = "".join([random.choice(source_str) for x in xrange(10)])
#                            time.sleep(0.001)
#                            group.name = name
#                            cl.updateGroup(group)
#                    except:
#                        cl.sendText(msg.to,"Error")
#            elif "Albumat'" in msg.text:
#              if msg.from_ in admin + staff + owner:
#                try:
#                    albumtags = msg.text.replace("Albumat'","")
#                    gid = albumtags[:6]
#                    name = albumtags.replace(albumtags[:34],"")
#                    cl.createAlbum(gid,name)
#                    cl.sendText(msg.to,name + "created an album")
#                except:
#                    cl.sendText(msg.to,"Error")
#            elif "fakecat'" in msg.text:
#              if msg.from_ in admin + owner:
#                try:
#                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
#                    name = "".join([random.choice(source_str) for x in xrange(10)])
#                    anu = msg.text.replace("fakecat'","")
#                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
#                except Exception as e:
#                    try:
#                        cl.sendText(msg.to,str(e))
#                    except:
#                        pass
						
#-------------------------------- PP BY TAG ---------------------------------
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")
								
#-----------------------------------------------------------
            elif "Detail" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass 
#-----------------------------------------------------------
            elif "Ppgroup" in msg.text:
                group = cl.getGroup(msg.to)
                path =("http://dl.profile.line-cdn.net/" + group.pictureStatus)
                cl.sendImageWithURL(msg.to, path)      
#-----------------------------------------------------------

            elif msg.text in ["Respon1 on"]:
		if msg.from_ in owner:
                    wait["detectMention"] = True
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"Aʟʀᴇᴀᴅʏ ɪɴ ᴀᴄᴛɪᴠᴇ")
		else:
		    cl.sendText(msg.to,"Khusus Owner")

            elif msg.text in ["Respon1 off"]:
		if msg.from_ in owner:
                    wait["detectMention"] = False
                    cl.sendText(msg.to,"Rᴇᴀᴅʏ Uɴᴀᴄᴛɪᴠᴇ")
		else:
		    cl.sendText(msg.to,"Khusus Owner")	
		    
		    
            elif msg.text in ["Respon2 on"]:
		if msg.from_ in owner:
                    wait["detectMention"] = False
                    wait["detectMention2"] = True
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"Aʟʀᴇᴀᴅʏ ɪɴ ᴀᴄᴛɪᴠᴇ")
		else:
		    cl.sendText(msg.to,"Khusus Owner")
            elif msg.text in ["Respon2 off"]:
		if msg.from_ in owner:
                    wait["detectMention2"] = False
                    cl.sendText(msg.to,"Rᴇᴀᴅʏ Uɴᴀᴄᴛɪᴠᴇ")
		else:
		    cl.sendText(msg.to,"Khusus Owner")	
		    

            elif msg.text in ["Respon3 on"]:
		if msg.from_ in owner:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = True
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"Aʟʀᴇᴀᴅʏ ɪɴ ᴀᴄᴛɪᴠᴇ")
		else:
		    cl.sendText(msg.to,"Khusus Owner")
            elif msg.text in ["Respon3 off"]:
		if msg.from_ in owner:
                    wait["detectMention3"] = False
                    cl.sendText(msg.to,"Rᴇᴀᴅʏ Uɴᴀᴄᴛɪᴠᴇ")
		else:
		    cl.sendText(msg.to,"Khusus Owner")	
			
            elif msg.text in ["Respons1 on"]:
		if msg.from_ in admin:
                    wait["detectMention4"] = True
                    wait["detectMention5"] = False
                    wait["detectMention6"] = False
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"Aʟʀᴇᴀᴅʏ ɪɴ ᴀᴄᴛɪᴠᴇ")
		else:
		    cl.sendText(msg.to,"Khusus admin")

            elif msg.text in ["Respons1 off"]:
		if msg.from_ in admin:
                    wait["detectMention4"] = False
                    cl.sendText(msg.to,"Rᴇᴀᴅʏ Uɴᴀᴄᴛɪᴠᴇ")
		else:
		    cl.sendText(msg.to,"Khusus Admin")	
		    
		    
            elif msg.text in ["Respons2 on"]:
		if msg.from_ in admin:
                    wait["detectMention4"] = False
                    wait["detectMention5"] = True
                    wait["detectMention6"] = False
                    cl.sendText(msg.to,"Aʟʀᴇᴀᴅʏ ɪɴ ᴀᴄᴛɪᴠᴇ")
		else:
		    cl.sendText(msg.to,"Khusus admin")
            elif msg.text in ["Respons2 off"]:
		if msg.from_ in admin:
                    wait["detectMention5"] = False
                    cl.sendText(msg.to,"Rᴇᴀᴅʏ Uɴᴀᴄᴛɪᴠᴇ")
		else:
		    cl.sendText(msg.to,"Khusus admin")	
		    

            elif msg.text in ["Respons3 on"]:
		if msg.from_ in admin:
                    wait["detectMention4"] = False
                    wait["detectMention5"] = False
                    wait["detectMention6"] = True
                    cl.sendText(msg.to,"Aʟʀᴇᴀᴅʏ ɪɴ ᴀᴄᴛɪᴠᴇ")
		else:
		    cl.sendText(msg.to,"Khusus admin")
            elif msg.text in ["Respons3 off"]:
		if msg.from_ in admin:
                    wait["detectMention6"] = False
                    cl.sendText(msg.to,"Rᴇᴀᴅʏ Uɴᴀᴄᴛɪᴠᴇ")
		else:
		    cl.sendText(msg.to,"Khusus admin")

            elif msg.text in ["Notif on"]:
              if msg.from_ in admin + staff + owner:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sᴀᴍʙᴜᴛᴀɴ Wᴇʟᴄᴏᴍᴇ Aʟʀᴇᴀᴅʏ ɪɴ ᴀᴄᴛɪᴠᴇ")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ʀᴇᴀᴅʏ ɪɴ ᴀᴄᴛɪᴠᴇ")

            elif msg.text in ["Notif off"]:
              if msg.from_ in admin + staff + owner:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sᴀᴍʙᴜᴛᴀɴ Wᴇʟᴄᴏᴍᴇ Rᴇᴀᴅʏ Uɴᴀᴄᴛɪᴠᴇ")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Rᴇᴀᴅʏ Uɴᴀᴄᴛɪᴠᴇ")
						
#-----------------------------------------------
            elif msg.text in ["Sticker on"]:
              if msg.from_ in owner:
                if wait["sticker"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aʟʀᴇᴀᴅʏ ɪɴ ᴀᴄᴛɪᴠᴇ")
                else:
                    wait["sticker"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɪɴ ᴀᴄᴛɪᴠᴇ")

            elif msg.text in ["Sticker off"]:
              if msg.from_ in owner:
                if wait["sticker"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Rᴇᴀᴅʏ Uɴᴀᴄᴛɪᴠᴇ")
                else:
                    wait["sticker"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Uɴᴀᴄᴛɪᴠᴇ") 
#-----------------------------------------------
            elif "Update welcome:" in msg.text:
              if msg.from_ in admin + owner:	
                wait["welmsg"] = msg.text.replace("Update welcome:","")
                cl.sendText(msg.to,"update welcome message succes")
            elif msg.text in ["Check welcome"]:
              if msg.from_ in admin + owner:	
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"yor bot message\n\n" + wait["welmsg"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["welmsg"])
					
            elif "Update goodbye: " in msg.text:
              if msg.from_ in admin + owner:	
                wait["welmsg2"] = msg.text.replace("Update goodbye: ","")
                cl.sendText(msg.to,"Update goodbye message succes")
            elif msg.text in ["Check goodbye"]:
              if msg.from_ in admin + owner:	
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"yor bot message\n\n" + wait["welmsg2"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["welmsg2"])
					
#--------------------------------------------------------
            elif msg.text in ["Autosider on"]:
              if msg.from_ in admin + staff + owner:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᶜᵉᵏ ᴼⁿ ˢᶦᵈᵉʳ...")
                
            elif msg.text in ["Autosider off"]:
              if msg.from_ in admin + staff + owner:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "ᶜᵉᵏ ˢᶦᵈᵉʳ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    cl.sendText(msg.to, "ᴮᵉˡᵘᵐ ᴰᶦˢᵉᵗ ᴰᵘᵈᵘˡ")   
#-------------------------------------------------------------
	    elif "Ghost on" in msg.text:
              if msg.from_ in admin + staff + owner:	        
		     wait["Ghost"] = True
		     cl.sendText(msg.to,"Ghost Sudah Aktif")
	      else:
	          cl.sendText(msg.to,"admin yg boleh")	

	    elif "Ghost off" in msg.text:
              if msg.from_ in admin + staff + owner:	 	        
		     wait["Ghost"] = False
		     cl.sendText(msg.to,"Ghost Sudah Di Nonaktifkan")
	      else:
	          cl.sendText(msg.to,"admin yg boleh")								
#--------------------------------------------------------------
        if op.type == 26:
            msg = op.message
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag!! Lagi Sibuk",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","Dia Lagi Off", cName + " Kenapa Tag Saya?","Dia Lagi Tidur\nJangan Di Tag " + cName, "Jangan Suka Tag Gua " + cName, "Kamu Siapa " + cName + "?", "Ada Perlu Apa " + cName + "?","Woii " + cName + " Jangan Ngetag, Riibut!"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in owner:
                              cl.sendText(msg.to,"Udah di PM, coba di tengok")
                              msg.contentType = 7    
                              msg.text = None
                              msg.contentMetadata = {'STKID': '17662251',
                                                            'STKPKGID': '1475424',
                                                            'STKVER': '1'}
                              cl.sendMessage(msg)  
                              gs = satpam.getGroup(msg.to)         
                              for g in gs.members:
                                  if cName == g.displayName:					  
                                     satpam.sendText(g.mid,ret_)
                                     break   
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:          
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Sekali lagi nge tag gw sumpahin jomblo seumur hidup!","Nggak Usah Tag-Tag! kesepian ya nes ","Woii " + cName + " Jangan Ngetag, Riibut!"]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in owner:
                                  cl.sendText(msg.to,ret_)
                                  cl.sendText(msg.to,cName)
                                  msg.contentType = 7    
                                  msg.text = None
                                  msg.contentMetadata = {'STKID': '12407844',
                                    'STKPKGID': '1307099',
                                    'STKVER': '1'}
                                  cl.sendMessage(msg)                                
                                  break
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention3"] == True:          
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = [cName + "\nDᴏɴᴛ Tᴀɢ Mᴇ!! Cɪᴘᴏᴋ Lᴏʜ Nᴀɴᴛɪ"]
                    balas = [cName + "\nHᴀʟᴏ Fᴀɴs Bᴇʀᴀᴛ Gᴡ!! \nAᴅᴀ Pᴇʀʟᴜ ᴀᴘᴀ Tᴀɢ Gᴡ..",cName + "\nᴬᵈᵃ ᴬᵖᵃ ᵀᵃᵍ ᴳʷ>>! \nᴹᵃᵘ ᴹⁿᵗᵃ ᵀᵃⁿᵈᵃ ᵀᵃⁿᵍᵃⁿ ᴳʷ!!!",cName + "\nHᴀᴅɪʀʀʀʀʀ Sᴇʟᴀʟᴜ \nAᴅᴀ ʏᴀɴɢ ʙɪsᴀ sᴀʏᴀ ʙᴀɴᴛᴜ",cName + "\nᴶᵃⁿᵍᵃⁿ ᵀᵃᵍ,, ᴷᵃⁿᵍᵉⁿ ᴾᶜ ˡᵃⁿᵍˢᵘⁿᵍ ᴬʲᵃ",cName + "\nDᴏɴᴛ Tᴀɢ Mᴇ....!!! \nPᴇʀɢɪ sᴀɴᴀ ᴊᴀᴜʜ ᴊᴀᴜʜ \nHᴜs Hᴜs Hᴜs"]
                    path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus                
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in owner:
                                  cl.sendText(msg.to,ret_)
                                  cl.sendImageWithURL(msg.to,path)
#                                  msg.contentType = 7    
#                                  msg.text = None
#                                  msg.contentMetadata = {'STKID': '17936151',
#                                    'STKPKGID': '1486815',
#                                    'STKVER': '1'}

#                                  cl.sendMessage(msg) 
#                                  msg.contentType = 7    
#                                  msg.text = None
#                                  msg.contentMetadata = {'STKID': '12690692',
#                                    'STKPKGID': '1314362',
#                                    'STKVER': '1'}
                                  
#                                  cl.sendMessage(msg)                                
                                  msg.contentType = 7    
                                  msg.text = None
                                  msg.contentMetadata = {'STKID': '17662251',
                                    'STKPKGID': '1475424',
                                    'STKVER':'1'}
                                  
                                  cl.sendMessage(msg)                                
                                  
                                  break
								  
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention4"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag!! Lagi Sibuk",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","Dia Lagi Off", cName + " Kenapa Tag Saya?","Dia Lagi Tidur\nJangan Di Tag " + cName, "Jangan Suka Tag Gua " + cName, "Kamu Siapa " + cName + "?", "Ada Perlu Apa " + cName + "?","Woii " + cName + " Jangan Ngetag, Riibut!"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in admin:
                                  cl.sendText(msg.to,ret_)
                                  msg.contentType = 7    
                                  msg.text = None
                                  msg.contentMetadata = {'STKID': '17662256',
                                    'STKPKGID': '1475424',
                                    'STKVER': '1'}
                                  cl.sendMessage(msg)  
                                  break   
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention5"] == True:          
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Sekali lagi nge tag gw sumpahin jomblo seumur hidup!","Nggak Usah Tag-Tag! kesepian ya nes ","Woii " + cName + " Jangan Ngetag, Riibut!"]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in admin:
                                  cl.sendText(msg.to,ret_)
                                  cl.sendText(msg.to,cName)
                                  msg.contentType = 7    
                                  msg.text = None
                                  msg.contentMetadata = {'STKID': '12407844',
                                    'STKPKGID': '1307099',
                                    'STKVER': '1'}
                                  cl.sendMessage(msg)                                
                                  break
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention6"] == True:          
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = [cName + "\nDᴏɴᴛ Tᴀɢ Mᴇ!! Cɪᴘᴏᴋ Lᴏʜ Nᴀɴᴛɪ"]
                    balas = [cName + "\nHᴀʟᴏ Fᴀɴs Bᴇʀᴀᴛ Gᴡ!! \nAᴅᴀ Pᴇʀʟᴜ ᴀᴘᴀ Tᴀɢ Gᴡ..",cName + "\nᴬᵈᵃ ᴬᵖᵃ ᵀᵃᵍ ᴳʷ>>! \nᴹᵃᵘ ᴹⁿᵗᵃ ᵀᵃⁿᵈᵃ ᵀᵃⁿᵍᵃⁿ ᴳʷ!!!",cName + "\nHᴀᴅɪʀʀʀʀʀ Sᴇʟᴀʟᴜ \nAᴅᴀ ʏᴀɴɢ ʙɪsᴀ sᴀʏᴀ ʙᴀɴᴛᴜ",cName + "\nᴶᵃⁿᵍᵃⁿ ᵀᵃᵍ,, ᴷᵃⁿᵍᵉⁿ ᴾᶜ ˡᵃⁿᵍˢᵘⁿᵍ ᴬʲᵃ",cName + "\nDᴏɴᴛ Tᴀɢ Mᴇ....!!! \nPᴇʀɢɪ sᴀɴᴀ ᴊᴀᴜʜ ᴊᴀᴜʜ \nHᴜs Hᴜs Hᴜs"]
                    path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus                
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in admin:
                                  cl.sendText(msg.to,ret_)
                                  cl.sendImageWithURL(msg.to,path)
#                                  msg.contentType = 7    
#                                  msg.text = None
#                                  msg.contentMetadata = {'STKID': '17936151',
#                                    'STKPKGID': '1486815',
#                                    'STKVER': '1'}

#                                  cl.sendMessage(msg) 
#                                  msg.contentType = 7    
#                                  msg.text = None
#                                  msg.contentMetadata = {'STKID': '12690692',
#                                    'STKPKGID': '1314362',
#                                    'STKVER': '1'}
                                  
#                                  cl.sendMessage(msg)                                
                                  msg.contentType = 7    
                                  msg.text = None
                                  msg.contentMetadata = {'STKID': '17662251',
                                    'STKPKGID': '1475424',
                                    'STKVER':'1'}
                                  
                                  cl.sendMessage(msg)                                
                                  
                                  break
#-------------------------------------------------------------
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n╠❂ " + Name
                                if " " in Name:  
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
#                                        contact = cl.getContact(op.param2)
#                                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
#                                        cl.sendText(op.param1,"╔═════════════\n" + "╠❂" +Name + "\n╚═════════════")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
#                                        cl.sendImageWithURL(op.param1,image)
                                        d = Message(to=op.param1, from_=None, text=None, contentType=7)
                                        d.contentMetadata = {"STKID": "17936157","STKPKGID": "1486815","STKVER": "1"}              
                                        cl.sendMessage(d)
                                        cl.sendText(op.param1, "Wᴏɪɪɪ!!!!! " + "☞ " + Name + " ☜" + "\nBᴇᴛᴀʜ ᴀᴍᴀᴛ ʟᴏ ᴊᴀᴅɪ sɪᴅᴇʀ \nᴀᴅᴀ ʏᴀɴɢ ɢᴀᴊɪ ʏ ᴊᴀᴅɪ sɪᴅᴇʀ   ")

                                    else:
#                                        contact = cl.getContact(op.param2)
#                                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
#                                        cl.sendText(op.param1,"╔═════════════\n" + "╠❂" + Name + "\n╚═════════════")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
#                                        cl.sendImageWithURL(op.param1,image)
                                        d = Message(to=op.param1, from_=None, text=None, contentType=7)
                                        d.contentMetadata = {"STKID": "17936157","STKPKGID": "1486815","STKVER": "1"}              
                                        cl.sendMessage(d)
                                        cl.sendText(op.param1, "Assᴀʟᴀᴍᴜᴀʟᴀɪᴋᴜᴍ " + "☞ " + Name + " ☜" + "\nNɢɪɴᴛɪᴘ ᴍᴇʟᴜʟᴜ \nᴍᴇɴᴅɪɴɢ sɪɴɪ \nᴋɪᴛᴀ ɴɢᴇʀᴜᴍᴘɪ   ")

                                else:
#                                    contact = cl.getContact(op.param2)
#                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
#                                    cl.sendText(op.param1,"╔═════════════\n" + "╠❂" + Name + "\n╚═════════════")
                                    time.sleep(0.2)
                                    summon(op.param1,[op.param2])
#                                    cl.sendImageWithURL(op.param1,image)
                                    d = Message(to=op.param1, from_=None, text=None, contentType=7)
                                    d.contentMetadata = {"STKID": "17936157","STKPKGID": "1486815","STKVER": "1"}              
                                    cl.sendMessage(d)
                                    cl.sendText(op.param1, "Nᴀʜʜʜ " + "☞ " + Name + " ☜" + "\nKᴇᴛᴀᴜᴡᴀɴ ɴɢɪɴᴛɪᴘ \nHᴀʜᴀʜᴀ   ")

                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass
#---------CCTV-----------
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              cl.sendText
          except:
             pass
#--------------------------------------
        if op.type == 25:
            msg = op.message
            if msg.contentType == 7:
                if wait['sticker'] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "☸ Sticker Check ☸\n\n☑ STKID : %s\n☑ STKPKGID : %s\n☑ STKVER : %s\n☸ Link:\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                    cl.sendText(msg.to, filler)
                else:
                    pass                    
#---------------------
        if op.type == 17:
          if wait["Sambutan"] == True:
           if op.param2 in Bots:
              return
           ginfo = cl.getGroup(op.param1)
           contact = cl.getContact(op.param2)
           image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
           cl.sendImageWithURL(op.param1,image)
           cl.sendText(op.param1,"Halo " + cl.getContact(op.param2).displayName  + "\nJones " +  wait["welmsg"] + " " + str(ginfo.name) + " ☜" + "\nBudayakan Baca Note !!! yah Ka 😊\nSemoga Betah Kk 😘")
           cl.sendText(op.param1, "Founder Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
           print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
          if wait["Sambutan"] == True:
           if op.param2 in Bots:
              return
           contact = cl.getContact(op.param2)
           image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
           cl.sendImageWithURL(op.param1,image)
           cl.sendText(op.param1,"Byee " + cl.getContact(op.param2).displayName + "\n" + wait["welmsg2"] + "\nHati - hati dijalan yah ka 😘")
           print "MEMBER HAS LEFT THE GROUP"               

#--------------------------------------------------------------------------
        if op.type == 19:
	 if wait["Ghost"] == True:
          if op.param2 in owner:
             if op.param2 in admin:
                if op.param2 in staff:
                  if op.param2 in Bots:	
                      pass
                  else:
                      try:
                          G = cl.getGroup(op.param1)
                          G.preventJoinByTicket = False
                          cl.updateGroup(G)
                          Ticket = cl.reissueGroupTicket(op.param1)
                          k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                          time.sleep(0.001)
                          k1.kickoutFromGroup(op.param1,[op.param2])
                          c = Message(to=op.param1, from_=None, text=None, contentType=13)
                          c.contentMetadata={'mid':op.param2}
                          k1.sendMessage(c)
                          k1.leaveGroup(op.param1)
                          G.preventJoinByTicket = True
                          cl.updateGroup(G)
                          wait["blacklist"][op.param2] = True
                      except:
                          G = cl.getGroup(op.param1)
                          G.preventJoinByTicket = False
                          cl.updateGroup(G)
                          Ticket = cl.reissueGroupTicket(op.param1)
                          k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                          time.sleep(0.001)
                          k1.kickoutFromGroup(op.param1,[op.param2])
                          c = Message(to=op.param1, from_=None, text=None, contentType=13)
                          c.contentMetadata={'mid':op.param2}
                          k1.sendMessage(c)
                          k1.leaveGroup(op.param1)
                          G.preventJoinByTicket = True
                          cl.updateGroup(G)
                          wait["blacklist"][op.param2] = True				
#------------------------------------------------------------------------------------
#------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
    for zx in range(0,20):
      hasil = cl.activity(limit=20)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          satpam.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          satpam.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by ⭐⭐Koplaxs⭐⭐👈\n\n™SMULE VOICE FAMILY™")
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ks.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ka.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ka.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          kb.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kb.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ku.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ku.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ke.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ke.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ko.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ko.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          print "Like"
        except:
          pass
      else:
          print "Already Liked"
time.sleep(0.60)
#thread3 = threading.Thread(target=autolike)
#thread3.daemon = True
#thread3.start()
#--------------------
def likePost():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in owner:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ka.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kb.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ku.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ke.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ko.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by ^One Piece Bot^\nStatus Boss udah Kami Like\nOwner Kami :\nHanavy Koplaxs")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Plak"
                
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

                profile5 = ks.getProfile()
                profile5.displayName = wait["cName5"]
                ks.updateProfile(profile5a)

                profile6 = ka.getProfile()
                profile6.displayName = wait["cName6"]
                ka.updateProfile(profile6)

                profile7 = kb.getProfile()
                profile7.displayName = wait["cName7"]
                kb.updateProfile(profile7)

                profile8 = ko.getProfile()
                profile8.displayName = wait["cName8"]
                ko.updateProfile(profile8)
                
                profile9 = ke.getProfile()
                profile9.displayName = wait["cName9"]
                ke.updateProfile(profile9)
                
                profile10 = ku.getProfile()
                profile10.displayName = wait["cName10"]
                ku.updateProfile(profile10)
                
                profile11 = satpam.getProfile()
                profile11.displayName = wait["cName11"]
                satpam.updateProfile(profile11)
                
                profile12 = k1.getProfile()
                profile12.displayName = wait["cName12"]
                k1.updateProfile(profile12)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
