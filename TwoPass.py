import numpy as np
import pandas as pd

path="C://Users//M.Barakat//Desktop//Assembly_Project_SIC//code1.txt"
code=pd.read_csv(path ,delimiter = "\t",sep=" ", header=None,dtype=object)
#x=str(code[0][0])
#x=x.strip()
#x=x.split(sep=" ")
#size=len(x)
#for i in range(1,code.shape[0]):
#    y=str(code[0][i])
#    y=y.strip()
#    y=y.split(sep=" ")
#    y=np.array(y)
#    
#    if y.size==2 and str(y[0]).lower()!="end" :
#        y=np.insert(y,0," ",axis=0)
#    y.resize(1,size)
#    x=np.vstack([x,y])
#        
x = ['p','y','t','h','o','n']
if 'p' in x:
    print(x)
#print(x.index('m'))
# if(self.arr[i,1]==self.opcode[j,0]):
#                        self.variable[index]=self.arr[i,2]



#x=x.astype(object)
#x=np.vstack([x,y])
#print(x)
#arr=np.array(code.iloc[:,:])
#print(arr)
#locator=np.ones((arr.shape[0]-1,1))
#hexa=[""]
#
#symbolTable=[[[]]for __ in range(5)]
#
#x=np.empty((3,3),dtype=str)
#
#print(x)
#symbolTable[0][0].append("hkhkjh")
#symbolTable[0].append("jkjkjkj")
#symbolTable[1][0].append("hkhkjh")
#symbolTable[1].append("jkjkjkj")
#if(arr[0,2]!=" "):
#    locator[0]=int(arr[0,2],16)
#    hexa[0]=hex(int(locator[0]))
#else:
#    locator[0]=int(0,16)
#    hexa[0]='000000'
#
##casefold() 
#i=1
#index=0
#while arr[i,1]!="End":
#    
#    if arr[i,1]!="RESW" and arr[i,1]!="RESB" and arr[i,1]!="BYTE":
#        locator[i]=locator[i-1]+3
#        
#    elif arr[i,1]=="RESW":
#        x=int(arr[i,2])*3
#        locator[i]=locator[i-1]+x
#        
#    elif arr[i,1]=="RESB":
#        locator[i]=locator[i-1]+int(arr[i,2])
#    
#    elif arr[i,1]=="BYTE":
#        x=len(arr[i,2])
#        locator[i]=locator[i-1]+x
#        
#    else:
#        print("error")
#    hexa.append(hex(int(locator[i])))
#
#    i+=1
##np.append(arr,hexa,axis=1)
#length_of_program=locator[locator.shape[0]-1]-locator[0]
#hexa_of_length=hex(int(length_of_program))
#
#
#print(hexa)
    for i in range(1,self.arr.shape[0]-1):
            for j in range(self.opcode.shape[0]):
                if(self.arr[i,1]==self.opcode[j,0] or str(self.arr[i,1]).upper()=='WORD' or str(self.arr[i,1]).upper()=="RESW" or str(self.arr[i,1]).upper()=="RESB"):
                    flag=0
                    if(self.arr[i,1]==self.opcode[j,0] and str(self.arr[i,2]) not in self.variable and "," not in str(self.arr[i,2]) ):
                        self.variable[index]=str(self.arr[i,2])
                        index=index+1
                    elif(","  in str(self.arr[i,2])):
                        temp=str(self.arr[i,2])
                        temp=temp.split(sep=",")
                        temp=str(temp[0])
                        if(temp not in self.variable):
                            self.variable[index]=temp
                            index=index+1
#                elif(str(self.arr[i,1]).upper()=='WORD' or str(self.arr[i,1]).upper()=="RESW" or str(self.arr[i,1]).upper()=="RESB"):
#                    if(self.arr[i,0] not in self.variable):
#                         flag=1

                    
                else :
                    flag=1
                    break
            if(flag==1):
                print("Syntax error in line "+str(i+1))
                return
        self.variable=np.array(self.variable)
        self.variable.resize(1,index)
        print(self.variable)