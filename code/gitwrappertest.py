#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 02:29:58 2021

@author: xcs
"""
import requests
import base64
import json

tokenfd = open("/home/xcs/Documents/pythonprogramming/credtok.py",'r')
TOKEN=tokenfd.readline().strip()
tokenfd.close()
print(TOKEN)
API_URL="https://api.github.com"
lsrepoprojurl="/repos/{owner}/{repo}/projects"
teamurlrepo="/users/Opifex-chathamicus/repos"
usrurlrepo="/users/alXCS/repos"
usrurl="/users/alXCS"
headers={
        "Authorization":"Basic "+TOKEN,
        "Accept":"*/*"
        }
r=requests.get(API_URL+usrurl,headers=headers)
print(r.json())
resp=r.json()
me=resp['login']
#print(me)

#####################################################################
#######################GET REPO CONTENTS #############################

r2=requests.get(API_URL+"/repos/Opifex-chathamicus/Konopzzzz/contents/modules/",headers=headers)
#print(r2.json())
counts=len(r2.json())
resp2=r2.json()
for i in range(counts):
   print(resp2[i]['name'],":")
   print(resp2[i]['sha'])
   print("=========================================================")

###########################################################################
####################### GET FILE CONTENTS #################################

headers2={
        "Authorization":"Basic "+TOKEN,
        "Accept":"application/vnd.github.v3+json"
        }
r3=requests.get(API_URL+"/repos/Opifex-chathamicus/Konopzzzz/contents/modules/dirlister.py",headers=headers2)
print(r3.json())
resp3=r3.json()
print("======================= CONTENT ======================= ")
print(resp3['content'])
contentresp3=resp3['content']
contentresp3=base64.b64decode(contentresp3)
contentresp3=contentresp3.decode("UTF-8") #the base64 decoded data has to be converted from bytes to string
print(contentresp3)

###########################################################################
####################### WRITE LOCALLY TO FILE #############################

modname=resp3['name']
modfd=open("/home/xcs/Desktop/"+modname,'w')
modfd.write(contentresp3)
modfd.close()


###########################################################################
####################### POST TO GITHUB ###################################

#Create or update file contents
#Creates a new file or replaces an existing file in a repository.
#put /repos/{owner}/{repo}/contents/{path}

# curl -i -X PUT -H "Accept: application/vnd.github.v3+json" -H "Authorization: token ghp_token"  https://api.github.com/repos/Opifex-chathamicus/Konopzzzz/contents/data/newfile -d '{"message":"message","content":"Y29udGVudA=="}' 
header={
        "Authorization":"token "+TOKEN,       ## MUST USE "Authorization":"token <token>" instead of "Authorization":"basic <token> " 
        "Accept":"application/vnd.github.v3+json
        }
print(TOKEN)
content="Nothing in there"
contentb64unm=str(base64.b64encode(content.encode("utf-8"))) 
contentb64=contentb64unm.strip('b').strip("'") 
#dprint(contentb64)
data={"message":"Created newfiletest.txt","content":contentb64}
datajson=json.dumps(data)
r4=requests.put(API_URL+"/repos/Opifex-chathamicus/Konopzzzz/contents/data/newfiletest.txt",data=datajson,headers=header)
print(r4.json())


 #y = json.dumps(x)



