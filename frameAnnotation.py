'''
Created on 9 de jan de 2019

@author: aoliveir
'''
from Tools.scripts.make_ctype import values

import pandas
import PySimpleGUI as sg


def getAnno():
        
    layout = [ 
        [sg.Frame(layout=[      
        [sg.Radio('none', "RADIO1", default=True), 
         sg.Radio('very_low', "RADIO1",),
         sg.Radio('low', "RADIO1",),
         sg.Radio('medium', "RADIO1",),
         sg.Radio('high', "RADIO1",)]],
        title='Options',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
        [ sg.OK() ]] 
             
        
    window = sg.Window('Do the frame annotation', 
                default_element_size=(40, 1), grab_anywhere=False).Layout(layout) 
          
    event, values = window.Read()
    print(values,type(values))
        
    return event, values

def writeAnno(values):
    
    file = open("humanAnnotation.txt","a")
    
    
    i = 0
    newAnno = ["","","","",""]
    for value in values:
        
        if i == 0 and value is True:
            newAnno[0] = "none"
            file.write(newAnno[0]+",0\n") 
        if i == 1 and value is True:
            newAnno[1] = "very_low"
            file.write(newAnno[1]+",1\n")     
        if i == 2 and value is True:
            newAnno[2] = "low"
            file.write(newAnno[2]+",2\n")    
        if i == 3 and value is True:
            newAnno[3] = "medium" 
            file.write(newAnno[3]+",3\n")   
        if i == 4 and value is True:
            newAnno[4] = "high"
            file.write(newAnno[4]+",4\n")       
        i=i+1
        
    file.close()
    print(newAnno)        
    
if __name__ == '__main__':
      
        
    event, values = getAnno()
    writeAnno(values)
        
        