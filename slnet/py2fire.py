import mss
import mss.tools
import time
import keyboard
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import threading
import random
from datetime import datetime
import numpy as np

def send_str(res_lis, prev_message):
    
    cred = credentials.Certificate('')
    db = firestore.client()
    now = datetime.utcnow()
    dic = [] # Insert your sign language
    res_str = ""

    lis_sz = len(res_lis)
    dic_sz = len(dic)

    print(lis_sz)

    for i in range(0,lis_sz):
        check_str = res_lis[i]
        
        for j in range(0,dic_sz):
            check_str_2 = str(dic[j][0])
            print(check_str_2)
            if check_str==check_str_2:
                res_str += dic[j][1]
                res_str += " "
                break


    data = {
    u'message': str(res_str),
    u'timestamp': now,
    u'user': u'target'
    }


    db.collection(u'messages').document(str(random.random())).set(data)