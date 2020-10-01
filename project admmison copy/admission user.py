from funtion import *
from random import choice
import datetime

mode=take("INPUT",["1","2"],"Enter the mode","","Enter from 1 or 2 or 0 only",1)
print("===>  You are using",[0,"User","Admin"][int(mode)]," mode")
while(1==1):
    if(mode=="1"):
        ch1=take("INT",[1,0],"    ","Enter your choice from MAIN MENU\t:\t","        Enter from the MAIN MENU only",2,mode)
    if(mode=="2"):
        ch1=take("INT",[1,2,0],"    ","Enter your choice from MAIN MENU\t:\t","        Enter from the MAIN MENU only",2,mode)
    #                                                 Exiting option
    if(ch1==0):
        exit()
    #                                                admission option
    elif(ch1==1):
        l=[]
        ######################################information list
        #           taking date of admission
        l+=[datetime.datetime(int(datetime.datetime.now().strftime("%Y")),int(datetime.datetime.now().strftime("%m")),int(datetime.datetime.now().strftime("%d")))]
        doa=(int(datetime.datetime.now().strftime("%d")),int(datetime.datetime.now().strftime("%m")),int(datetime.datetime.now().strftime("%Y")))
        #           Taking admission type
        ch2=take("INT",[1,2],"        ","Enter your admission type\t:\t","            Enter only 1 or 2\n",3)
        if(ch2==1):
            l+=[["FRESH_ADMISSION",None,None]]
        elif(ch2==2):
            tc_no=take("INT",None,"            ","enter your T.C number\t:\t","                T.C number must be integer",0,0)
            kv=input("            Enter your kv name\t:\t")
            l+=[["KV_TC_ADMISSION",tc_no,kv]]
            del tc_no
            del kv
        #                   get tc date
        if(l[1][1]!=None):
            while(1==1):
                try :
                    tcd=input("            enter the tc in formate dd/mm/yyyy\t:\t").split("/")
                    p=datetime.datetime(int(tcd[2]),int(tcd[1]),int(tcd[0]))
                    if(tcd[0].isdigit() and tcd[1].isdigit()  and tcd[2].isdigit()):
                        break
                except:
                    print("                Invalid date")
        #           cheking any special admission 
        ch2=take("INPUT",["Y","N"],"            ","Do you want admission under special dispension if yes enter y/Y if no enter n/N\t:\t","            Enter y/n only",0,0)
        if(ch2.upper()=="Y"):
            l+=[["Y",take("INPUT",["HRM","MP","KM"],"                ","Enter which special condition  hrm/mp/km \t:\t","                    Enter only from hmr/mp/km",0,0)]]
        elif(ch2.upper()=="N"):
            l+=[["N",None]]
        #           taking class
        cla=take("INT",[1,2,3,4,5,6,7,8,9,10,11,12],"        ","Enter the class\t:","            Enter from 1 to 12 integer only",0,0)
        l+=[cla]
        #          application number
        admin=("INT",None,"        ","Enter the application number:\t","            it must be integer",0,0)
        #           giving section
        if(cla!=12 and cla!=11):
            sec=section(l[3])
            l+=[sec]
            print("        Your section is\t\t",sec)
        else:
                sec=take("INPUT",["SCIENCE","COMMERCE"],"        "," Enter your stream science/commerce","            Enter stream science,commerce only",0,0)
                l+=[sec]
                data=collecting_data("COUNT_SECTION.DAT")
                data[str(cla)+"th"][sec.lower()]+=1
                exchanging_data("COUNT_SECTION.DAT",data)
        #count_check()
        del sec
        #           taking student name
        name=spaces(input("        Enter full name\t:\t"))
        l+=[name]
        del name
        #           taking father name
        l+=[spaces(input("        Father name without Mr.\t:\t"))]
        l+=[take("INPUT",["SC","ST","OBC","GEN"],"        ","Enter your from SC/ST/OBC/GEN","            ENTER FROM SC/ST/OBC/GEN",0,0)]
        #           taking service catagary
        l+=[take("INT",[1,2,3,4,5],"        ","Enter your service catagary 1/2/3/4/5\t:\t","            Enter from 1-5 only",0,0)]
        #           taking gender
        l+=[take("INPUT",["M","F"],"        ","Enter m for male or f for female\t:\t","            'm' or 'f' only",0,0)]
        #           taking DOB
        while(1==1):
            try :
                dob=input("        Enter your dob in formate dd/mm/yyyy")
                dob=dob.split("/")
                dob=datetime.datetime(int(dob[2]),int(dob[1]),int(dob[0]))
                if(dob<l[0]):
                    l+=[dob]
                    break
                else:
                    print("            dob must be before today")
            except:
                print("                Invalid date")

        #           taking salary
        l+=[take("INT",None,"        ","Enter father salary\t:\t","            Salary must be integer,",0,0)]
        #           giving remarks
        if(l[3]!=1):
            if(l[1][1]!=None ):
                remar=[str(l[1][1])+"/"+tcd[0]+"-"+tcd[1]+"-"+tcd[2]+"/"+l[1][2]]
            else:
                remar=[None]
        elif(l[3]==1):
            remar=[admin]
        #                   giving admition number
        admission_no1=admission_no()
        l+=[admission_no1]
        print("        Your Admission number is",admission_no1)
        #             inserting info to all
        dat=dict()
        if(l[1]=="FRESH_ADMISSION"):
            dat["admission"]="Fresh admission"
        elif(l[1]=="KV_TC_ADMISSION"):
            dat["admission"]={"KV name":l[1][2],"TC number":l[1][1],"TC date":tcd}
        elif(l[1][1]!=None):
            dat["special admission"]=l[2][1]
        elif(l[1][1]==None):
            dat["special admission"]=None
        
        dat["class"]=l[3]
        dat["section"]=l[4]
        dat["student name"]=l[5]
        dat["father name"]=l[6]
        dat["caste"]=l[7]
        dat["Service catagery"]=l[8]
        dat["gen"]=l[9]
        dat["date of birth"]=l[10]
        dat["salary"]=l[11]
        dat["remarks"]=remar
        dat["admission_no"]=admission_no1
        data=collecting_data("MASTER_FILES.dat")
        data["kvp3/"+datetime.datetime.now().strftime("%Y")+"-"+str(int(datetime.datetime.now().strftime("%y"))+1)+"/"+str(len(collecting_data("MASTER_FILES.dat").keys())+1)]=dat
        exchanging_data("MASTER_FILES.dat",data)
        del dat
        #             inserting info to fresh admission
        if(l[1]=="FRESH_ADMISSION"):
            dat=dict()
            dat["remarks"]=remar
            dat["admission_no"]=admission_no1
            dat["date of birth"]=l[10]
            dat["gen"]=l[9]
            dat["Service catagery"]=l[8]
            dat["caste"]=l[7]
            dat["section"]=l[4]
            dat["class"]=l[3]
            dat["student name"]=l[5]
            dat["father name"]=l[6]
            data=collecting_data("FRESH_ADMISSION.dat")
            data["kvp3/"+datetime.datetime.now().strftime("%Y")+"-"+str(int(datetime.datetime.now().strftime("%y"))+1)+"/"+str(len(collecting_data("FRESH_ADMISSION.dat").keys())+1)]=dat
            exchanging_data("FRESH_ADMISSION.dat",data)
            del dat
        #                   store data  admission under special condition
        if(l[2][1]!=None):
           dat=dict()
           dat["student name"]=l[5]
           dat["gen"]=l[9]
           dat["date of birth"]=l[10]
           dat["father name"]=l[6]
           dat["caste"]=l[7]
           dat["date of admission"]=l[0]
           dat["Service catagery"]=l[8]
           dat["salary"]=l[11]
           dat["class"]=l[3]
           dat["remarks"]=remar
           data=collecting_data("ADMISSION_UNDER_SPECIAL_DISPERSATION.dat")
           data["kvp3/"+datetime.datetime.now().strftime("%Y")+"-"+str(int(datetime.datetime.now().strftime("%y"))+1)+"/"+str(len(collecting_data("ADMISSION_UNDER_SPECIAL_DISPERSATION.dat").keys())+1)]=dat
           exchanging_data("ADMISSION_UNDER_SPECIAL_DISPERSATION.dat",data)
           del dat
        #                   store data kv tc
        if(l[1][2]!=None):
           dat=dict()
           dat["student name"]=l[5]
           dat["tc number"]=l[1][1]
           dat["kv name"]=l[1][2]
           dat["gen"]=l[9]
           dat["date of birth"]=l[10]
           dat["father name"]=l[6]
           dat["caste"]=l[7]
           dat["date of admission"]=l[0]
           dat["Service catagery"]=l[8]
           dat["class"]=l[3]
           dat["salary"]=l[11]
           data=collecting_data("KV_TC_ADMISSION.dat")
           data["kvp3/"+datetime.datetime.now().strftime("%Y")+"-"+str(int(datetime.datetime.now().strftime("%y"))+1)+"/"+str(len(collecting_data("KV_TC_ADMISSION.dat").keys())+1)]=dat
           exchanging_data("KV_TC_ADMISSION.dat",data)
        #                   store data xi addmisioon
        if(l[3]==11):
            dat=dict()
            dat["salary"]=l[11]
            dat["date of admission"]=l[0]
            dat["date of birth"]=l[10]
            dat["father name"]=l[6]
            dat["caste"]=l[7]
            dat["gen"]=l[9]
            dat["student name"]=l[5]
            data=collecting_data("CLASS_XI_ADMISSION.dat")
            data["kvp3/"+datetime.datetime.now().strftime("%Y")+"-"+str(int(datetime.datetime.now().strftime("%y"))+1)+"/"+str(len(collecting_data("CLASS_XI_ADMISSION.dat").keys())+1)]=dat
            exchanging_data("CLASS_XI_ADMISSION.dat",data)
"""    elif(ch1==2 and mode=="2"):
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
"""                               
