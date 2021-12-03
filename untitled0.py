# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 20:19:22 2021

@author: xtf
"""
#需要的包
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets,linear_model


#读取数据函数
def get_data(file_name):
    data=pd.read_csv(file_name,encoding='gbk')
    X_parameter=[]
    Y_parameter=[]
    for single_square_feet,single_price_value in zip(data['square_feet'],data['price']):
        #遍历数据
        X_parameter.append([float(single_square_feet)])
        Y_parameter.append(float(single_price_value))
    
    return X_parameter,Y_parameter

    
#将数据拟合到线性模型
def linear_model_main(X_parameter,Y_parameter,predict_value):
    #创建线性回归对象
    regr=linear_model.LinearRegression()
    regr.fit(X_parameter,Y_parameter)
    predict_outcome=regr.predict(predict_value)
    predictions={}
    predictions['intercept']=regr.intercept_
    predictions['coefficient']=regr.coef_
    predictions['predict_value']=predict_outcome
    return predictions

X,Y=get_data('input_data.csv')
predictvalue=[[700]]
#predictvalue=np.array(predictvalue).reshape(-1,1)#将700转换为二维数组
result=linear_model_main(X, Y, predictvalue) 
print("Intercept value",result['intercept']) 
print("coefficient",result['coefficient'])
print("Predicted Value:",result['predict_value'])
  

