#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 02:29:58 2021

@author: xcs
"""
import requests
import base64

tokenfd = open("/credtok.py",'r')
TOKEN=tokenfd.readline().strip()
tokenfd.close()
print(TOKEN)
API_URL="https://api.github.com"
#lsrepoprojurl="/repos/{owner}/{repo}/projects"
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






