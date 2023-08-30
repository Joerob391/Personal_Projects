# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 10:41:20 2023

@author: joseph.robinson
"""
import requests
import json
import pandas as pd
import datetime as dt


hashes=pd.read_excel('C:/Users/joseph.robinson/Desktop/GEN5 to 7 customer workload migration (workloads).xlsx')

account_id=hashes['acct_num']
#acct_ids=account_id.drop(labels=[276,277,278,279])



columns={'Acct ID':[],
         'Acct Name':[],
         'Acct Created Date':[],
         'Root User ID':[],
         'Root User Email':[],     
         'Root User Name':[],
         'Billing Account Status':[],
         'Billing Type':[],
         'Updated Date':[]
         }


header1 = {
    "accept": "application/json",
    "authorization": "Bearer "
          }



header2 = {
    "accept": "*/*",
    "authorization": "Bearer ",
    'authority': 'gateway.stackpath.com',
    'origin': 'https://internal.stackpath.net',
    'referer': 'https://internal.stackpath.net',
    "content-type": "application/json",
    "accept-language": "en-US,en;q=0.9"
          }


url3="https://gateway.stackpath.com/graphql"
acct_url = "https://gateway.stackpath.com/identity/v1/accounts/%s"
usr_url = "https://gateway.stackpath.com/identity/v1/users/%s"


payload={"operationName":"GetBillingAccount","variables":{"accountId":""},
       "query":"query GetBillingAccount($accountId: String!) {\n  billingAccount(accountId: $accountId) {\n    ...BillingAccountFields\n    __typename\n  }\n}\n\nfragment BillingAccountFields on BillingAccount {\n  id\n  billingType\n  status\n  createdAt\n  updatedAt\n  remoteId\n  __typename\n}\n"}


#print(data)

values={}
for acct_hash in account_id:
    print('Started Acct ' +  acct_hash)
    response = requests.get(acct_url %(acct_hash), headers=header1)
    data=response.json()
    r_usr_id=data['account']['rootUserId']
    a_name=data['account']['name']
    c_date=data['account']['createdAt']
    
    response2 = requests.get(usr_url %(r_usr_id), headers=header1)
    data2=response2.json()
    u_email=data2['user']['email']
    u_name=data2['user']['name']
    
    payload['variables']["accountId"]=acct_hash
    response3 = requests.post(url=url3, headers=header2, data=json.dumps(payload))
    data3=response3.json()
    b_type=data3['data']['billingAccount']['billingType']
    stat=data3['data']['billingAccount']['status']
    u_date=data3['data']['billingAccount']['updatedAt']
    values[acct_hash]=[]
    values[acct_hash].extend([acct_hash, a_name, c_date,
                              r_usr_id, u_email, u_name,
                              stat, b_type, u_date])
    print('Completed Acct ' + acct_hash) 

print('COMPLETED ALL HASHES')


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
path=r'C:\Users\joseph.robinson\Desktop\Projects_Desktop\Ad_Hoc\GEN5 to 7 customer workload migration (workloads) %s.xlsx' %(today)
export.to_excel(path,index= False, header= True)

print('File has been exported with %s rows & %s columns' % (export.shape[0],export.shape[1])) 






