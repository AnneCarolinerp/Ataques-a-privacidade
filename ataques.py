# -*- coding: utf-8 -*-
# Importar bibliotecas
import numpy as np
import pandas as pd

#Importar e ler dataframe
data = pd.read_csv('diabetes_v1.csv')
print(data.to_string())

#Filter dataframe
#Tentar identificar João
display(data.loc[(data['Glucose']==115) & (data['SkinThickness']==30)])

#Tentar identificar Maria
display(data.loc[(data['Pregnancies']==1) & (data['BloodPressure']==66)])

#Tentar identificar Antônio
display(data.loc[(data['Pregnancies']==0) & (data['BloodPressure']==100)])