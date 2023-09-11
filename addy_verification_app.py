#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 21:58:32 2023

@author: joe91
"""
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

xlxs=pd.read_excel('/home/joe91/Desktop/version1.xlsx')


columns={}
columns['address']={'Mailing Address':[], 'Real Address (Y|N)':[], 'Owner':[], 'Addt Notes': []} 
                    
                    
id_1='cphMainContentArea_ucSearchType_wzrdRealPropertySearch_ucSearchType_ddlCounty'                   
id_2="cphMainContentArea_ucSearchType_wzrdRealPropertySearch_ucSearchType_ddlSearchType"
id_3='cphMainContentArea_ucSearchType_wzrdRealPropertySearch_StartNavigationTemplateContainerID_btnContinue'
id_4="cphMainContentArea_ucSearchType_wzrdRealPropertySearch_ucEnterData_txtStreenNumber"
name_4="ctl00$cphMainContentArea$ucSearchType$wzrdRealPropertySearch$ucEnterData$txtStreenNumber"
id_5='cphMainContentArea_ucSearchType_wzrdRealPropertySearch_ucEnterData_txtStreetName'
id_6='cphMainContentArea_ucSearchType_wzrdRealPropertySearch_ucEnterData_txtStreenNumber'
id_7='cphMainContentArea_ucSearchType_wzrdRealPropertySearch_ucEnterData_txtStreetName'
id_8='cphMainContentArea_ucSearchType_wzrdRealPropertySearch_StepNavigationTemplateContainerID_btnStepNextButton'
id_9='cphMainContentArea_ucSearchType_wzrdRealPropertySearch_ucDetailsSearch_dlstDetaisSearch_lblOwnerName_0'
id_10='cphMainContentArea_ucSearchType_wzrdRealPropertySearch_StepNavigationTemplateContainerID_btnNewSearch'
id_11="cphMainContentArea_ucSearchType_wzrdRealPropertySearch_ucSearchResult_gv_SearchResult" # checking to see if multiple results pull up on search
class_1="lnkdetails"  #the collective class of the results from the multi result search. You can then cycle/iterate through this to check each result/record against the owner name from the excel
id_12= "cphMainContentArea_ucSearchType_wzrdRealPropertySearch_ucSearchResult_gv_SearchResult_txtOwnerName_{}" #if once result found
id_13="cphMainContentArea_ucSearchType_wzrdRealPropertySearch_ucDetailsSearch_dlstDetaisSearch_lblMailingAddress_0"#grabbing mailing address from result page instead of using excels as source of truth
class_2='btnNewSearc'
id_14='cphMainContentArea_ucSearchType_wzrdRealPropertySearch_btnNewSearchTop1'

#<input type="submit" name="ctl00$cphMainContentArea$ucSearchType$wzrdRealPropertySearch$StepNavigationTemplateContainerID$btnNewSearch" value="New Search" onclick="return ReDirect();" id="cphMainContentArea_ucSearchType_wzrdRealPropertySearch_StepNavigationTemplateContainerID_btnNewSearch" class="btnNewSearch">


url='https://sdat.dat.maryland.gov/RealProperty/Pages/default.aspx'
# =============================================================================

# options.add_argument('headless')
# options.add_argument('--no-sandbox')
# options.add_argument("--disable-gpu")
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('----enable-features=NetworkService,NetworkServiceInProcess')
# options.add_experimental_option(    "excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# =============================================================================

# =============================================================================
# USER_AGENT = {
#     # usual user agent string
#     "userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
#     "platform": "Linux",
#     "acceptLanguage": "en-US, en",
#     "userAgentMetadata": {
#         # ensure the order of this array matches real browser!
#         "brands": [
#             # at the time of writing this is always == 99
#             {"brand": " Not A;Brand", "version": "99"},
#             # ensure that the versions here match ones from User-Agent string
#             {"brand": "Chromium", "version": "116"},
#             {"brand": "Google Chrome", "version": "116"},
#         ],
#         "fullVersion": "116.0.5845.140",
#         "platform": "Linux",
#         "platformVersion": "10.0",
#         "architecture": "x86",
#         "model": "",
#         "mobile": False,
#     },
# }
# =============================================================================
#browser.delete_all_cookies()
#browser.close()
#browser.execute_cdp_cmd("Network.setUserAgentOverride", USER_AGENT)
#browser.execute_cdp_cmd("Network.setUserAgentOverride", USER_AGENT)# 






# =============================================================================
# street=xlxs['ADDRESS'][57]
# 
# f_name=xlxs['FIRSTNAME'][57]
# l_name=xlxs['LASTNAME'][57]
# county=xlxs['FIPS_COUNTY_NAME'][57]
# =============================================================================


options=webdriver.ChromeOptions()
options.add_argument('headless')
browser=webdriver.Chrome(executable_path='/home/joe91/Desktop/chromedriver', options=options)

browser.get(url)

#print(browser.session_id)




for street, county, f_name, l_name in zip(xlxs['ADDRESS'][13025:20000], xlxs['FIPS_COUNTY_NAME'][13025:20000], xlxs['FIRSTNAME'][13025:20000], xlxs['LASTNAME'][13025:20000]):
    f_name=f_name.strip().upper()
    l_name=l_name.strip().upper()
    
    if county.strip() == 'Anne Arundel':
        county = "ANNE ARUNDEL COUNTY"
        button=browser.find_element(By.ID, id_1)
        button.send_keys(county)
    elif county.strip()  == 'Baltimore':
        county = 'BALTIMORE COUNTY'
        button=browser.find_element(By.ID, id_1)
        button.send_keys(county)
    elif county.strip()  == 'Baltimore City':
        county = 'BALTIMORE CITY'  
        button=browser.find_element(By.ID, id_1)
        button.send_keys(county)
    elif county.strip()  == 'Carroll':
        county = 'CARROLL COUNTY'
        button=browser.find_element(By.ID, id_1)
        button.send_keys(county)
    elif county.strip()  == 'Howard':
        county = 'HOWARD COUNTY'          
        button=browser.find_element(By.ID, id_1)
        button.send_keys(county) 
    elif county.strip()  == 'Montgomery':
        county = 'MONTGOMERY COUNTY'           
        button=browser.find_element(By.ID, id_1)
        button.send_keys(county) 
    elif county.strip()  == 'Prince Georges':
        county = "PRINCE GEORGE'S"          
        button=browser.find_element(By.ID, id_1)
        button.send_keys(county)
    
    button2=browser.find_element(By.ID, id_2)
    method_1='STREET ADDRESS'
    button2.send_keys(method_1)
    time.sleep(1.5)
    button3=browser.find_element(By.ID, id_3)
    button3.click()  
    
    street_breakup = street.split()
    street_num = street_breakup[0]
    street_breakup_2 = street_breakup[1:-1]
    if len(street_breakup_2) == 0:
        street_breakup_2 =street_breakup[-1] 

    if  len(street_breakup_2)>1:
        street_name = ' '.join(street_breakup_2)
        time.sleep(1.5)
        button4=browser.find_element(By.NAME, name_4)
        button4.send_keys(street_num)
        time.sleep(1.5)
        button5=browser.find_element(By.ID, id_5)
        button5.send_keys(street_name)
        time.sleep(1.5)
        button8=browser.find_element(By.ID, id_8)
        button8.click()
        try:
         time.sleep(1.5)   
         button9=browser.find_element(By.ID,id_9)
         owner=button9.text
         button12=browser.find_element(By.ID, id_13)
         mailing_addy=button12.text
         columns['address']['Mailing Address'].append(mailing_addy)
         columns['address']['Real Address (Y|N)'].append('Y')
         columns['address']['Owner'].append(owner)
         columns['address']['Addt Notes'].append('N/A')
         time.sleep(1.5)
         button10=browser.find_element(By.ID,id_10)
         button10.click()
        except NoSuchElementException:
         try:   
             time.sleep(1.5)
             result_check=browser.find_element(By.ID, id_11)
             elements=browser.find_elements(By.CLASS_NAME, class_1)
             rslts=[x.text for x in elements]
             counter=0
             rslts_count=len(rslts)
             for name in rslts:
                 counter+=1
                 if (f_name in name) == True:
                     button11=browser.find_element(By.ID, id_12.format(counter-1))
                     time.sleep(1.5)
                     button11.click()
                     time.sleep(1.5)
                     button12=browser.find_element(By.ID, id_13)
                     mailing_addy=button12.text
                     button9=browser.find_element(By.ID,id_9)
                     owner=button9.text
                     columns['address']['Mailing Address'].append(mailing_addy)
                     columns['address']['Real Address (Y|N)'].append('Y')
                     columns['address']['Owner'].append(owner)
                     columns['address']['Addt Notes'].append('N/A')
                     time.sleep(1.5)
                     button10=browser.find_element(By.ID,id_10)
                     button10.click()
                     break
                 elif (l_name in name) == True:
                     button11=browser.find_element(By.ID, id_12.format(counter-1))
                     time.sleep(1.5)
                     button11.click()
                     time.sleep(1.5)
                     button12=browser.find_element(By.ID, id_13)
                     mailing_addy=button12.text
                     button9=browser.find_element(By.ID,id_9)
                     owner=button9.text
                     columns['address']['Mailing Address'].append(mailing_addy)
                     columns['address']['Real Address (Y|N)'].append('Y')
                     columns['address']['Owner'].append(owner) 
                     columns['address']['Addt Notes'].append('N/A')
                     time.sleep(1.5)
                     button10=browser.find_element(By.ID,id_10)
                     button10.click()
                     break

                 elif (counter == rslts_count) == True:
                     full_name=str(f_name + ' ' + l_name).capitalize()
                     columns['address']['Mailing Address'].append(street)
                     columns['address']['Real Address (Y|N)'].append('N')
                     columns['address']['Owner'].append(full_name)
                     columns['address']['Addt Notes'].append("Address Verified but owners didn't match original doc")
                     time.sleep(1.5)
                     button10=browser.find_element(By.ID,id_10)
                     button10.click()
                     break
                 
         except NoSuchElementException:
             print("it's failing here")
             columns['address']['Mailing Address'].append(street)
             columns['address']['Real Address (Y|N)'].append('N')
             columns['address']['Owner'].append('NA')
             columns['address']['Addt Notes'].append('Unable to verify address w/ given information')
             button10=browser.find_element(By.ID,id_10)
             button10.click()         
    else:
        street_name = str(street_breakup_2[0])
        time.sleep(1.5)
        button6=browser.find_element(By.ID, id_6)
        button6.send_keys(street_num)
        time.sleep(1.5)
        button7=browser.find_element(By.ID, id_7)
        button7.send_keys(street_name)
        time.sleep(1.5)
        button8=browser.find_element(By.ID, id_8)
        button8.click()
        try:
            time.sleep(1.5)   
            button9=browser.find_element(By.ID,id_9)
            owner=button9.text
            button12=browser.find_element(By.ID, id_13)
            mailing_addy=button12.text
            columns['address']['Mailing Address'].append(mailing_addy)
            columns['address']['Real Address (Y|N)'].append('Y')
            columns['address']['Owner'].append(owner)
            columns['address']['Addt Notes'].append('N/A')
            time.sleep(1.5)
            button10=browser.find_element(By.ID,id_10)
            button10.click()

        except NoSuchElementException:
            print('exception1')
            try:   
                time.sleep(1.5)
                result_check=browser.find_element(By.ID, id_11)
                elements=browser.find_elements(By.CLASS_NAME, class_1)
                rslts=[x.text for x in elements]
                counter=0
                rslts_count=len(rslts)
                for name in rslts:
                    counter+=1
                    print('round 1  counter=' + str(counter))
                    print('rslts_count & counter equal yet?: '+ str(counter == rslts_count))
                    
                    if  (f_name in name) == True:
                        button11=browser.find_element(By.ID, id_12.format(counter-1))
                        time.sleep(1.5)
                        button11.click()
                        time.sleep(1.5)
                        button12=browser.find_element(By.ID, id_13)
                        mailing_addy=button12.text
                        button9=browser.find_element(By.ID,id_9)
                        owner=button9.text
                        columns['address']['Mailing Address'].append(mailing_addy)
                        columns['address']['Real Address (Y|N)'].append('Y')
                        columns['address']['Owner'].append(owner)
                        columns['address']['Addt Notes'].append('N/A')
                        button10=browser.find_element(By.ID,id_10)
                        button10.click()
                        break
                    elif (l_name in name) == True:
                         button11=browser.find_element(By.ID, id_12.format(counter-1))
                         time.sleep(1.5)
                         button11.click()
                         time.sleep(1.5)
                         button12=browser.find_element(By.ID, id_13)
                         mailing_addy=button12.text
                         button9=browser.find_element(By.ID,id_9)
                         owner=button9.text
                         columns['address']['Mailing Address'].append(mailing_addy)
                         columns['address']['Real Address (Y|N)'].append('Y')
                         columns['address']['Owner'].append(owner)
                         columns['address']['Addt Notes'].append('N/A')
                         time.sleep(1.5)
                         button10=browser.find_element(By.ID,id_10)
                         button10.click()

                         break
                 
                    elif (counter == rslts_count) == True:
                        print("'it's working")
                        full_name=str(f_name + ' ' + l_name).capitalize()
                        columns['address']['Mailing Address'].append(street)
                        columns['address']['Real Address (Y|N)'].append('Y')
                        columns['address']['Owner'].append(full_name)
                        columns['address']['Addt Notes'].append("Address Verified but owners didn't match original doc")
                        time.sleep(1.5)
                        button10=browser.find_element(By.ID, id_14)
                        button10.click()
                        break
                 
            except NoSuchElementException:
             print('exception2')   
             columns['address']['Mailing Address'].append(street)
             columns['address']['Real Address (Y|N)'].append('N')
             columns['address']['Owner'].append('NA')
             columns['address']['Addt Notes'].append('Unable to verify address w/ given information')
             time.sleep(1.5)
             button10=browser.find_element(By.ID,id_10)
             button10.click()
         

    print(len(columns['address']['Mailing Address']))

    print(columns['address']['Mailing Address'][-1])
    
    print(columns['address']['Real Address (Y|N)'][-1])
    
    print(columns['address']['Addt Notes'][-1])
    
    


browser.close()









xlxs['ADDRESS'][32714]#Console7/A left off here. Tasked with 0-10K
xlxs.head(3462)

st=pd.Series(columns['address']['Mailing Address'])
yn=pd.Series(columns['address']['Real Address (Y|N)'])
own=pd.Series(columns['address']['Owner'])
ad_in=pd.Series(columns['address']['Addt Notes'])

pt_1=pd.concat([st,yn,own, ad_in], axis=1)
pt_1_1=pt_1.rename(columns={0:'Mailing Address filed with Taxes', 1:'Real Address (Y|N)', 2:'Owner Name', 3:'Additional Notes'})

first_10k_excel=xlxs.head(3462)

final=pd.concat([first_10k_excel, pt_1_1], axis=1)
path=r'C:\home\joe91\Desktop\address_confirmation_1.xlsx'
final.to_excel(path,index= False, header= True)



xlxs['ADDRESS'][12780]#Console8/A left off here. Tasked with 10K-20K
xlxs.iloc[10000:12781]

st2=pd.Series(columns['address']['Mailing Address'])
yn2=pd.Series(columns['address']['Real Address (Y|N)'])
own2=pd.Series(columns['address']['Owner'])
ad_in2=pd.Series(columns['address']['Addt Notes'])

pt_2=pd.concat([st2,yn2,own2, ad_in2], axis=1)
pt_2_2=pt_2.rename(columns={0:'Mailing Address filed with Taxes', 1:'Real Address (Y|N)', 2:'Owner Name', 3:'Additional Notes'})

second_10k_excel=xlxs.iloc[10000:12781]

final2=pd.concat([second_10k_excel, pt_2_2], axis=1)
path2=r'C:\home\joe91\Desktop\address_confirmation_2.xlsx'
final2.to_excel(path2,index= False, header= True)



xlxs['ADDRESS'][22723]#Console9/A left off here. Tasked with 20K-30K
xlxs.iloc[20000:22724]

st3=pd.Series(columns['address']['Mailing Address'])
yn3=pd.Series(columns['address']['Real Address (Y|N)'])
own3=pd.Series(columns['address']['Owner'])
ad_in3=pd.Series(columns['address']['Addt Notes'])

pt_3=pd.concat([st3,yn3,own3, ad_in3], axis=1)
pt_3_3=pt_3.rename(columns={0:'Mailing Address filed with Taxes', 1:'Real Address (Y|N)', 2:'Owner Name', 3:'Additional Notes'})

third_10k_excel=xlxs.iloc[20000:22724]

final3=pd.concat([third_10k_excel, pt_3_3], axis=1)
path3=r'C:\home\joe91\Desktop\address_confirmation_3.xlsx'
final3.to_excel(path3,index= False, header= True)



xlxs['ADDRESS'][32714]#Console10/A left off here. Tasked with 30K-
xlxs.iloc[30000:32715]
    
st4=pd.Series(columns['address']['Mailing Address'])
yn4=pd.Series(columns['address']['Real Address (Y|N)'])
own4=pd.Series(columns['address']['Owner'])
ad_in4=pd.Series(columns['address']['Addt Notes'])

pt_4=pd.concat([st4,yn4,own4, ad_in4], axis=1)
pt_4_4=pt_4.rename(columns={0:'Mailing Address filed with Taxes', 1:'Real Address (Y|N)', 2:'Owner Name', 3:'Additional Notes'})

fourth_10k_excel=xlxs.iloc[30000:32715]

final4=pd.concat([fourth_10k_excel, pt_4_4], axis=1)
path4=r'C:\home\joe91\Desktop\address_confirmation_4.xlsx'
final4.to_excel(path4,index= False, header= True)





#This is to merge all the excels
import pandas as pd
xlxs1=pd.read_excel('address_confirmation_1.xlsx')
xlxs2=pd.read_excel('address_confirmation_2.xlsx')
xlxs3=pd.read_excel('address_confirmation_3.xlsx')
xlxs4=pd.read_excel('address_confirmation_4.xlsx')


output=pd.concat([xlxs1, xlxs2, xlxs3, xlxs4], axis=1)
output.head()

    #print(columns['address']['Real Address (Y|N)'])
    
    #print(columns['address']['Owner'][-1])

#print(columns['address']['Street'])
# =============================================================================
# 
# print(rslts)
# print(owner)
# print(f_name)
# print(name)
# print(street)
# print(street_breakup_2)
# print(street_name)
# f_name in name
# print(counter)
# for name in rslts:
#     print(name)
# =============================================================================







### THIS FIRST DATAFRAME IS FROM 451 - 7176 OF ORIGINAL EXCEL (em did the first 450 manually) ###
st=pd.Series(columns['address']['Mailing Address'])
yn=pd.Series(columns['address']['Real Address (Y|N)'])
own=pd.Series(columns['address']['Owner'])
ad_in=pd.Series(columns['address']['Addt Notes'])
pt_1=pd.concat([st,yn,own, ad_in], axis=1)

pt_1
pt_1_1=pt_1.rename(columns={0:'Mailing Address filed with Taxes', 1:'Real Address (Y|N)', 2:'Owner Name', 3:'Additional Notes'})
pt_1_1



### THIS SECOND DATAFRAME IS FROM 7177 - 11246 OF ORIGINAL EXCEL  ###
#st_2=pd.Series(columns['address']['Street'])
#yn_2=pd.Series(columns['address']['Real Address (Y|N)'])
#own_2=pd.Series(columns['address']['Owner'])
#pt_2=pd.concat([st_2,yn_2,own_2], axis=1)

pt_2
pt_2_2=pt_2.rename(columns={0:'Street', 1:'Real Address (Y|N)', 2:'Owner Name'})
pt_2_2


xlxs.head(3462)
first_10k_excel=xlxs.head(3462)
first_10k_excel


merge_1=[pt_1_1, pt_2_2]
merge_1_1=pd.concat(merge_1).reset_index(drop=True)
merge_1_1

final=pd.concat([first_10k_excel, merge_1_1], axis=1)
path=r'C:\home\joe91\Desktop\Updated_address_confirmation.xlsx'
final.to_excel(path,index= False, header= True)
