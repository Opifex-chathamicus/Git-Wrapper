#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 00:19:10 2021

@author: xcs
"""

import requests
import base64


API_URL="https://api.github.com"


def login():
    tokenfd = open("/home/xcs/Documents/pythonprogramming/credtok.py",'r')
    token=tokenfd.readline().strip()
    tokenfd.close()
    headers={
        "Authorization":"Basic "+token,
        "Accept":"*/*"
        }
    return token,headers
    
#####################################################################
#######################GET REPO CONTENTS #############################

def get_repo_contents(token,headers):
    r=requests.get(API_URL+"/repos/Opifex-chathamicus/Konopzzzz/contents/modules/",headers=headers)
    #print(r2.json())
    counts=len(r.json())
    resp=r.json()
    files=[]
    for i in range(counts):
        files.append(resp[i]['name'])
        print(resp[i]['name'],":")
        print(resp[i]['sha'])
        print("=========================================================")
    
###########################################################################
####################### GET FILE CONTENTS #################################

def get_file_contents(token,filename):
    headers={
            "Authorization":"Basic "+token,
            "Accept":"application/vnd.github.v3+json"
            }
    r=requests.get(API_URL+"/repos/Opifex-chathamicus/Konopzzzz/contents/modules/"+filename,headers=headers)
    resp=r.json()
    contentresp=resp['content']
    contentresp=base64.b64decode(contentresp)
    contentresp=contentresp.decode("UTF-8") #the base64 decoded data has to be converted from bytes to string
    return contentresp

###########################################################################
####################### POST TO GITHUB ###################################

#Create or update file contents
#Creates a new file or replaces an existing file in a repository.
#put /repos/{owner}/{repo}/contents/{path}

def store_to_file(token,filename,content):
    headers={
        "Authorization":"token "+token,
        "Accept":"application/vnd.github.v3+json"
    }
<<<<<<< HEAD
    contentb64unm=str(base64.b64encode(content.encode("utf-8"))) 
    contentb64=contentb64unm.strip('b').strip("'") 
    data={"message":"Created newfiletest.txt","content":contentb64}
    datajson=json.dumps(data)
    r=requests.put(API_URL+"/repos/Opifex-chathamicus/Konopzzzz/contents/data/"+filename,data=datajson,headers=headers)
=======
    contentb64=base64.b64encode(content.encode("utf-8"))
    data={"message":"Created or edited "+filename,"content":contentb64}
    r4=requests.put(API_URL+"/repos/Opifex-chathamicus/Konopzzzz/contents/data/newfiletest.txt",data=data,headers=headers)
>>>>>>> 6884b1976357df2cd56c42dd12df37c64131f190
    


