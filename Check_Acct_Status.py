# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 14:33:00 2023

@author: joseph.robinson
"""

import requests
import pandas as pd
import datetime as dt

hashes=pd.read_excel('C:/Users/joseph.robinson/Desktop/NPS_Peter_v1.xlsx')

account_id=hashes['acct_num']
acct_ids=account_id.drop(labels=[276,277,278,279])
acct_ids=list(acct_ids)
#print(len(acct_ids))



acct_url = "https://gateway.stackpath.com/identity/v1/accounts/%s"
usr_url = "https://gateway.stackpath.com/identity/v1/users/%s"
stk_url = "https://gateway.stackpath.com/stack/v1/stacks"

headers = {
    "accept": "application/json",
    "authorization": "Bearer "
          }


columns={'Acct ID':[],
         'Acct Name':[],
         'Acct Created Date':[],
         'Root User ID':[],
         'Root User Email':[],     
         'Root User Name':[],
         'Stack ID':[],
         'Slug':[],
         'Status':[],
         'Updated Date':[]
         }

stk_param={'account_id':''}
stk_param2={'account_id':'',
            'page_request.first':600
            }



values={}
#print(data)
#print(acct_hash)

for acct_hash in acct_ids:
    print('Started Acct ' +  acct_hash)
    response = requests.get(acct_url %(acct_hash), headers=headers)
    data=response.json()
    r_usr_id=data['account']['rootUserId']
    a_name=data['account']['name']
    c_date=data['account']['createdAt']
    
    response2 = requests.get(usr_url %(r_usr_id), headers=headers)
    data2=response2.json()
    u_email=data2['user']['email']
    u_name=data2['user']['name']
    
    stk_param['account_id']=acct_hash
    response3 = requests.get(stk_url, params=stk_param, headers=headers)
    data3=response3.json()
    t_count=int(data3['pageInfo']['totalCount'])
    if t_count == 0:
        stk_id='DELETED'
        slug='DELETED'
        stat='DELETED'
        up_date='Not Applicable'
        
        values[acct_hash]=[]
        values[acct_hash].extend([acct_hash, a_name, c_date,
                                  r_usr_id, u_email, u_name,
                                  stk_id, slug, stat,up_date ])
        print('Completed Acct ' + acct_hash + " : There were no stacks ")
    elif t_count == 1:
        stk_param2['account_id']=acct_hash
        response4 = requests.get(stk_url, params=stk_param2, headers=headers)
        data4=response4.json()
        result_len=len(data4['results'])
        stk_id=data4['results'][0]['id']
        slug=data4['results'][0]['slug']
        stat=data4['results'][0]['status']
        up_date=data4['results'][0]['updatedAt']
        
        values[acct_hash]=[]
        values[acct_hash].extend([acct_hash, a_name, c_date,
                                  r_usr_id, u_email, u_name,
                                  stk_id, slug, stat, up_date])
        print('Completed Acct ' + acct_hash)        



print('COMPLETED ALL HASHES')
len(values)
values.keys()
#print(t_count)
#acct_hash


df_list=[]
df_dict={}

for k in values.keys():
    for col, v in zip(columns.keys(),values[k]):
        df_dict[col]= v                               
    df=pd.DataFrame([df_dict])
    df_list.append(df)
    print('%s Done' %(k))

export=pd.concat(df_list,axis=0) 

today=dt.date.today()
path=r'C:\Users\joseph.robinson\Desktop\Projects_Desktop\Ad_Hoc\NPS_v1 %s.xlsx' %(today)
export.to_excel(path,index= False, header= True)

print('File has been exported with %s rows & %s columns' % (export.shape[0],export.shape[1])) 
export




#response = requests.get(stk_url, params={'account_id':'3186357b-5a51-42d8-a927-fc4ab899a7c7'}, headers=headers)

#print(len(response.json()['results']))
#print(response.json()['results'][0])
#response.json()['user']['name']


#stk_url2 = "https://gateway.stackpath.com/stack/v1/stacks?page_request.after=9?account_id=3186357b-5a51-42d8-a927-fc4ab899a7c7"
#response2 = requests.get(stk_url2, headers=headers,)

#print(response2.json())
