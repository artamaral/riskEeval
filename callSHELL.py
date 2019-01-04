'''
Created on 4 de jan de 2019

@author: aoliveir
'''

import subprocess
from timeit import default_timer as timer

class shellCall():
    
    def call(self):
        
        start = timer()
        #where the file to be call is located
        folderLocation = ("C:/Users/aoliveir/")
               
        #call the problog and check errors       
        pr = subprocess.Popen(['problog','teste.pl'], cwd = folderLocation,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout, stderr = pr.communicate()
        
        #handling errors on problog
        stdout_err = str(stdout)
        stdout_err= stdout_err.capitalize()
        print(stdout, stderr)
        
        err = "error"
        
        if err in stdout_err:
            
            print("Error:",str(stdout_err))
            return 0
        #getting the output from probability from problog
        else:
            p =stdout[7:12] #clean up string and get only the probability
            p = float(p)
            print(type(p),p)
            print("Probability :",p)
        
        #getting the output from probability from problog
        end = timer()
        print("Inference elapsed time ",(end-start)*1000,"ms")

if __name__ == '__main__':
    
    newCall = shellCall()    
    newCall.call()