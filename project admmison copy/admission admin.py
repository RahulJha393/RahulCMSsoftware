from funtion import *
from random import choice
import datetime
print("===>  You are using",[0,"User","Admin"][2]," mode")
while(1==1):
    ch1=take("INT",[1,2,0],"    ","Enter your choice from MAIN MENU\t:\t","        Enter from the MAIN MENU only",0,2)
    if(1==1):
        choi=take("INT",[1,2,3,4,5,6,7,8,9,10,11,12,0],"            ","Enter your choice from search option\t:\t","                Enter only from search option",4,0)
        if(choi==1):
            admintion=take("INT",None,"            ","Enter the admission number\t:\t","            Enter only admition number",0,0)
            search("admission_no",admintion)
        elif(choi==2):
            cla=take("INT",[1,2,3,4,5,6,7,8,9,10,11,12],"            ","Enter the class\t:\t","            Enter only class only",0,0)
            search("class",cla)
        elif(choi==3):
            cat=take("INT",[1,2,3,4,5],"            ","Enter the sevice catagery\t:\t","            Enter only sevice catagery only",0,0)
            search("Service catagery",cat)
        elif(choi==4):
            nam=spaces(take("INPUT",None,"            ","Enter the student name\t:\t","            Enter  name only",0,0))
            search("student name",nam)
        elif(choi==5):
            cas=take("INPUT",["SC","ST","OBC","GEN"],"        ","Enter the caste\t:\t","            Enter caste only",0,0)
            search("caste",cas)
        elif(choi==6):
            search("special admission","HRM")
        elif(choi==7):
            search("special admission","KM")
        elif(choi==8):
            search("special admission","MP")
        elif(choi==9):
            SUM=0
            print("                ################################################")
            for x in collecting_data("KV_TC_ADMISSION.dat"):
                SUM+=1
                print("                ################################################")
                for y in collecting_data(file)[x].keys():
                    if(str(type(collecting_data(file)[x][y]))!="<class 'datetime.datetime'>"):
                       print("                ",y,"\t:",collecting_data(file)[x][y])
                    else:
                        print("                ",y,"\t",collecting_data(file)[x][y].day,"/",collecting_data(file)[x][y].month,"/",collecting_data(file)[x][y].year)
            print("                ----------------------------------------------------------------------------------------") 
            print("                ==>",SUM,"  found")
            print("                ################################################")
        elif(choi==10):
            file="FRESH_ADMISSION.dat"
            SUM=0
            print("                ################################################")
            for x in collecting_data("FRESH_ADMISSION.dat"):
                SUM+=1
                print("                ################################################")
                for y in collecting_data(file)[x].keys():
                    if(str(type(collecting_data(file)[x][y]))!="<class 'datetime.datetime'>"):
                       print("                ",y,"\t:",collecting_data(file)[x][y])
                    else:
                        print("                ",y,"\t",collecting_data(file)[x][y].day,"/",collecting_data(file)[x][y].month,"/",collecting_data(file)[x][y].year)
            print("                ----------------------------------------------------------------------------------------") 
            print("                ==>",SUM,"  found")
            print("                ################################################")     
        elif(choi==11):
            ra=input("            Enter the range ex 100-200")
            file="MASTER_FILES.dat"
            SUM=0
            print("                ################################################")
            for x in collecting_data(file):
                SUM+=1
                if(collecting_data(file)[x]["salary"] in range(int(ra.split("-")[0]),int(ra.split("-")[1]))):
                    print("                ################################################")
                    for y in collecting_data(file)[x].keys():
                        if(str(type(collecting_data(file)[x][y]))!="<class 'datetime.datetime'>"):
                            print("                ",y,"\t:",collecting_data(file)[x][y])
                        else:
                            print("                ",y,"\t",collecting_data(file)[x][y].day,"/",collecting_data(file)[x][y].month,"/",collecting_data(file)[x][y].year)
            print("                ----------------------------------------------------------------------------------------") 
            print("                ==>",SUM,"  found")
            print("                ################################################")
        elif(choi==12):
            SUM=0
            file="MASTER_FILES.dat"
            print("                ################################################")
            for x in collecting_data("MASTER_FILES.dat"):
                SUM+=1
                print("                ################################################")
                for y in collecting_data(file)[x].keys():
                    if(str(type(collecting_data(file)[x][y]))!="<class 'datetime.datetime'>"):
                       print("                ",y,"\t:",collecting_data(file)[x][y])
                    else:
                        print("                ",y,"\t",collecting_data(file)[x][y].day,"/",collecting_data(file)[x][y].month,"/",collecting_data(file)[x][y].year)
            print("                ----------------------------------------------------------------------------------------")     
            print("                ==>",SUM,"  found")
            print("                ################################################")                                             
