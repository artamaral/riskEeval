'''
Created on 9 de jan de 2019

@author: aoliveir
'''
class pXr:
    
    def readAnno(self):
        
        file_human = open("humanAnnotation.txt","r")
        file_machine = open("machineAnnotation.txt","r")
        humanAnno = []
        machineAnno = []
        lines_h = file_human.readlines()
        lines_m = file_machine.readlines()
            
        for line in lines_h:
            humanAnno.append(line)
        print(humanAnno)    
        file_human.close() 
        
        for line in lines_m:
            machineAnno.append(line)
        print(machineAnno)    
        file_machine.close()
        
        sumAnnoData = pXr()
        sum,tp,fp = sumAnnoData.sumAnno(humanAnno, machineAnno)
        
        print(sum,tp,fp)
        
        
    def sumAnno(self,humanAnno,machineAnno):
        
        sum = len(humanAnno)
        tp = 0 
        fp = 0   
        if len(humanAnno) == len(machineAnno):
            print("go!")
                         
        else:
            print("Error: file lenght is different") 
            return 0   
        
        for data in range(len(humanAnno)):
            
            if humanAnno[data] == machineAnno[data]:
                tp = tp+1
                
            if humanAnno[data] != machineAnno[data]:
                fp = fp+1
                       
        if sum != (tp+fp):
            print("Error: file lenght is different") 
            return 0
                   
        return sum,tp,fp    

       
if __name__ == '__main__':
    
    newCall = pXr()
    newCall.readAnno()   
    