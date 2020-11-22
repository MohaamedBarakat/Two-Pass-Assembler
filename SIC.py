import numpy as np
import pandas as pd

class SIC:
    """
check all sytntax error in the programe produced
"""
    def __init__(self,path):
        self.path=path
        self.code=pd.read_csv(self.path ,delimiter = "\t",sep=" ", header=None,dtype=object)
        self.arr=str(self.code[0][0])
#        self.arr=self.arr.strip()
        self.arr=self.arr.split(sep=" ")
        """ length of first row """
        self.size=len(self.arr)
        self.variable=["","","","","",""]
        for i in range(1,self.code.shape[0]):
            y=str(self.code[0][i])
            y=y.strip()
            y=y.split(sep=" ")
            y=np.array(y)
    
            if y.size==2 and str(y[0]).lower()!="end" :
                y=np.insert(y,0," ",axis=0)
            y.resize(1,self.size)
            self.arr=np.vstack([self.arr,y])

            """ name of the program """
#        if self.arr[0,0]==' ':
#            print("You must enter the program name")
#            nameProgram=input()
#            self.arr[0,0]=nameProgram

        for i in range(3,self.arr.shape[1]):
            temp=str(self.arr[0,i])
            if temp[0]!=';':
                print("Syntax error in line 1")
                return
        
        if(len(str(self.arr[0,2]))>6):
             print("Syntax error in line 1, may the start address more than six digit")
             return
        if("START" in self.arr[1:,:]):
            print("Sytnatx error there are another START")
            return
             
    
        self.path1="C://Users//M.Barakat//Desktop//Assembly_Project_SIC//SIC_instructions.txt"
        self.opcode=pd.read_csv(self.path1,header=None)
        self.opcode=np.array(self.opcode.iloc[:,:])
#        print(self.arr)
#        print(self.opcode)
        flag=0
        index=0
        """ taking variables of program"""
        for i in range(1,self.arr.shape[0]-1):
            if(self.arr[i,1] in self.opcode):
                flag=0
                if(str(self.arr[i,2]) not in self.variable and "," not in str(self.arr[i,2]) ):
                    self.variable[index]=str(self.arr[i,2])
                    index=index+1
                elif(","  in str(self.arr[i,2])):
                    temp=str(self.arr[i,2])
                    temp=temp.split(sep=",")
                    if(str(temp[1]).lower()!='x'):
                        flag=1
                    temp=str(temp[0])
                    if(temp not in self.variable):
                        self.variable[index]=temp
                        index=index+1
            elif(str(self.arr[i,1]).upper()=='WORD' or str(self.arr[i,1]).upper()=="RESW" or str(self.arr[i,1]).upper()=="RESB"):
                if(str(self.arr[i,0]) in self.variable):
                    flag=0
                    
                else:
                    flag=1
                    
            else :
                flag=1
                
            if(flag==1):
                print("Syntax error in line "+str(i+1))
                return
            
        self.variable=np.array(self.variable)
        self.variable.resize(1,index)
        
        """
        end of constractor
        """
    def Locations(self):
            
        locator=np.ones((self.arr.shape[0]-1,1))
        hexa=[""]
        if(self.arr[0,2]!=" "):
            locator[0]=int(self.arr[0,2],16)
            hexa[0]=hex(int(locator[0]))
        else:
            locator[0]=int(0,16)
            hexa[0]='000000'
        i=1
        while str(self.arr[i,0]).lower()!="end":
    
            if self.arr[i,1]!="RESW" and self.arr[i,1]!="RESB" and self.arr[i,1]!="BYTE":
                locator[i]=locator[i-1]+3
        
            elif self.arr[i,1]=="RESW":
                x=int(self.arr[i,2])*3
                locator[i]=locator[i-1]+x
        
            elif self.arr[i,1]=="RESB":
                locator[i]=locator[i-1]+int(self.arr[i,2])
    
            elif self.arr[i,1]=="BYTE":
                x=len(self.arr[i,2])
                locator[i]=locator[i-1]+x
        
            else:
                print("error")
            hexa.append(hex(int(locator[i])))

            i+=1
        self.length_of_program=locator[locator.shape[0]-1]-locator[0]
        self.length_of_program=hex(int(self.length_of_program))
        return hexa
            
    def Length(self):
        return self.length_of_program
            
           

path="C://Users//M.Barakat//Desktop//Assembly_Project_SIC//code1.txt"
test=SIC(path)
y=test.Locations()
x=test.Length()
print(y)