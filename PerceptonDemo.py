# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:56:08 2020

@author: Qi Yue
"""

import numpy as np
import random
import matplotlib.pyplot as plt
import warnings 

warnings.filterwarnings('ignore')

class PerceptronDemo:
    #初始化实例数、学习率、权重
    def __init__(self,sample_size, l_rate):
        self.sample_size = sample_size
        self.half_sample = (int) (self.sample_size/2)
        self.l_rate = l_rate
        self.w = np.random.rand(1,2)
        self.b = np.random.rand()
        self.iter_number = 0        
        
    #随机生成线性可分的数据集
    def generate_data(self):
        X_f = np.random.rand(self.half_sample,2)*50
        X_b = np.random.rand(self.half_sample,2)*50+50
        X = np.concatenate((X_f,X_b),axis=0)
        y = [-1]*self.half_sample+[1]*self.half_sample
        return X, y
        
    #画散点图并标明类别
    def scatter(self,X,y):
        plt.scatter(X[:self.half_sample,0],X[:self.half_sample,1],c='red',label='Class=-1')
        plt.scatter(X[self.half_sample:self.sample_size,0],X[self.half_sample:self.sample_size,1],c='green',label='Class=1')
        plt.xlabel('$X_1$')
        plt.ylabel('$X_2$')
       
    #在散点图上加上目标函数f
    def target_plot(self,X,y):
        plt.subplot(1,2,1)
        self.scatter(X,y)
        plt.legend(['Class=-1','Class=1'],loc=2)
        plt.title('Scatterplot with f')
        xvalues = np.linspace(0,100,500)
        plt.plot(xvalues,(100-xvalues))
       # plt.show()
    
    #在散点图上加上目标函数f和最终假设g
    def g_plot(self,X,y,w,b):
        plt.subplot(1,2,2)
        self.scatter(X,y)
        plt.title('Scatterplot with f and g')
        xvalues = np.linspace(0,100,500)
        plt.plot(xvalues,(100-xvalues),label='f=$-100+X_1+X_2$')
        plt.plot(xvalues,(-b/w[0,1]-w[0,0]/w[0,1]*xvalues),label='g=$%d+%dX_1+%dX_2$'%((int)(b),(int)(w[0,0]),(int)(w[0,1])))
        plt.legend(loc=2)
        plt.show()
        
        
    #训练感知机模型
    def train(self,X, y):
        isWrong = True
        while(isWrong):
            wrong_cnt = 0
            random_s = random.sample(range(len(X)),len(X))
            for i in random_s:
                if y[i]*(np.dot(self.w,X[i,])+self.b)<=0:
                    wrong_cnt += 1
                    self.w += np.dot(y[i],X[i,])
                    self.b += y[i]
                    self.iter_number+=1
            if wrong_cnt==0: isWrong = False
        print("Final hypothesis g is %.2f+%.2fX1+%.2fX2. Perceptron has updated the weights for %d times."%(self.b,self.w[0,0],self.w[0,1],self.iter_number))
                     
    #生成数据集、画图1、训练模型、画图2
    def main(self):
        X, y = self.generate_data()
        plt.figure(figsize=(13, 6))
        self.target_plot(X, y)
        self.train(X, y)
        self.g_plot(X,y,self.w,self.b)

#主程序入口，遍历训练三种学习率，四种实例数下的感知机模型并作图        
if __name__=="__main__":
    print("We run 12 percepton demo with sample size = 20, 20, 100, 1000 and learning rate = 1, 0.01, 0.0001.")
    i = 1;
    results = []
    for l_rate in (1,0.01,0.0001):
        for sample_size in (20,20,100,1000):
            print("\nScenario %d, we do a perceptron demo with sample size = %d and learning rate = %s."%(i,sample_size,(str)(l_rate)))
            p = PerceptronDemo(sample_size, l_rate)
            p.main()
            results.append([sample_size, l_rate, p.iter_number])
            i+=1
    print(results)
    plt.plot(results)
            
