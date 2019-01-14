'''
Created on 9 de jan de 2019

@author: aoliveir
'''
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score




#import accuracy_score
class pXr:
    
    def readAnno(self):
        
        file_human = open("humanAnnotation.txt","r")
        file_machine = open("machineAnno.txt","r")
        
        humanAnno =[]
        machineAnno = []
        lines_h = file_human.readlines()
        lines_m = file_machine.readlines()
            
        for line in lines_h:
            line = line.split(",")
            humanAnno.append(line)
        print(humanAnno)    
        file_human.close() 
        
        for line in lines_m:
            line = line.split(",")
            machineAnno.append(line)
        print(machineAnno,"machine")    
        file_machine.close()
        
        sumAnnoData = pXr()
        sum,tp,fp,fn = sumAnnoData.sumAnno(humanAnno, machineAnno)
        
        print(sum,tp,fp,fn)
        
        
    def sumAnno(self,humanAnno,machineAnno):
        
        sum = len(humanAnno) #whole population
        tp = 0 #true positive
        fp = 0 #false positive  
        fn = 0 #false negative
        if len(humanAnno) == len(machineAnno):
            print("go!")
                         
        else:
            print("Error: file lenght is different") 
            return 0   
        
        for data in range(len(humanAnno)):
            
            if humanAnno[data][0] == machineAnno[data][0]:
                tp = tp+1
            
            elif humanAnno[data][1] > machineAnno[data][1]:  
                fp = fp+1
                
            elif humanAnno[data][1] < machineAnno[data][1]: 
                fn = fn+1  
                       
        if sum != (tp+fp+fn):
            print("Error: file lenght is different") 
            return 0
                   
        return sum,tp,fp,fn    


    def calc_plot_PxR_curve(self):
        
        df = pd.read_csv('data.csv')
        df.head()
        thresh = 0.5
        df['predicted_RF'] = (df.label_rf >= 0.60).astype('int')
        print(df.predicted_RF.values)
        accuracy_sc = accuracy_score(df.actual_label.values, df.predicted_RF.values)
        recall_sc = recall_score(df.actual_label.values, df.predicted_RF.values)
        precision_sc = precision_score(df.actual_label.values, df.predicted_RF.values)

        print("accuracy score:" +str(accuracy_sc)+"\n recall score:" + str(recall_sc) 
              + "\n precision score:"+ str(precision_sc))
        return 1
        
       
if __name__ == '__main__':
    
    newCall = pXr()
    #newCall.readAnno()   
    newCall.calc_plot_PxR_curve()
    