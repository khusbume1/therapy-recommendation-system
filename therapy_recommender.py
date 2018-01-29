# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 00:04:24 2018

@author: KHUSHBU
"""

import pandas as pd
from scipy.spatial.distance import pdist
therapies = pd.read_csv('therapies.csv')
patient_detail = pd.read_csv('patients.csv')
therapy_rating = pd.read_csv('therapy_rating.csv')

data = pd.pivot_table(data=therapy_rating,index='patientId', values='therapy_effectiveness',columns='therapyId')
#user = input('Please input your ID: ')
user =1
#df.loc[df['decision_Nephritis_of_renal_pelvis_origin'] == "yes"]

selected_patient = patient_detail.loc[patient_detail['id'] == user, ['id','age', 'gender','family_history','years_of_first_diagnosis','current_stage']]
#like_patient = patient_detail.loc[patient_detail['age'] == selected_patient['age']+10, ['age', 'gender','family_history','years_of_first_diagnosis','current_stage']]
age = selected_patient.loc[selected_patient['id'] == user, 'age'].item()
gender = selected_patient.loc[selected_patient['id'] == user, 'gender'].item()
family_history = selected_patient.loc[selected_patient['id'] == user, 'family_history'].item()
current_stage = selected_patient.loc[selected_patient['id'] == user, 'current_stage'].item()
#like_patient = patient_detail.loc[((((patient_detail['age'] == age+10) & (patient_detail['gender'] == gender)) & (patient_detail['family_history'] == family_history) & (patient_detail['current_stage'] == current_stage))), ['id','age', 'gender','family_history','current_stage']]
like_patient = patient_detail.loc[((((patient_detail['age'] == age+10) & (patient_detail['gender'] == gender)) & (patient_detail['family_history'] == family_history))), ['id','age', 'gender','family_history','current_stage']]
#df1 = df[['a','b']]
ids_of_like_patient = like_patient.loc[:,['id']]

therapy_used_by_like_patient = therapy_rating.loc[therapy_rating['patientId']== ids_of_like_patient,['therapyId','patientId','therapy_effectiveness']]
used = data.loc[user,:][data.loc[user,:].notnull()].index.tolist()
chk = ~pd.isnull(data.loc[:,used])
others = chk.index.tolist()
others.remove(user)
user_rating = data.loc[user,used]
other_rating = data.loc[others,used]

#sim =[]
#for another in other_rating.index:
#    pairwise = user_rating.to_frame().join(other_rating.loc[another,:]).transpose()
#    pairwise = pairwise.dropna(axis=1, how='any')
#    sim.append(pdist(pairwise,'cosine')[0])
#chk['#'] = chk.sum(axis=1)
#chk = chk[chk['#']>overlap*len(seen)] -I don't do this because I dont have to match less than some percentage
