from pickle import dump,load
from random import choice
def search(WS,E,file="MASTER_FILES.dat"):
    SUM=0
    print("                ################################################")
    for x in collecting_data(file):
        if(collecting_data(file)[x][WS]==E):
            print("                ################################################")
            SUM+=1
            for y in collecting_data(file)[x].keys():
                if(str(type(collecting_data(file)[x][y]))!="<class 'datetime.datetime'>"):
                   print("                ",y,"\t:",collecting_data(file)[x][y])
                else:
                   print("                ",y,"\t",collecting_data(file)[x][y].day,"/",collecting_data(file)[x][y].month,"/",collecting_data(file)[x][y].year)
    print("                -----------------------------------------------------------------------------------------")
    print("                ==>",SUM,"  found")
    print("                ################################################")
def menu(n,mode=0):
    if(n==0):
        print("Admin menu")
        print("1)Admission under special dispersation")
        print("2)Fresh admission")
        print("3)K.V tc admission")
        print("0)")
        
    if(n==1):
        print("1)User mode")
        print("2)Admin mode")
    elif(n==2):
        print("    MAIN MENU")
        print("    1)Admission")
        print("    0)Exit")
    elif(n==3):
        print("        Admission Type")
        print("        1)Fresh admission")
        print("        2)TC from another kendriya vidyalya")
    elif(n==4):
        print("            Search option")
        print("            1)by admition number.")
        print("            2)by class.")
        print("            3)by service catagary.")
        print("            4)by name.")
        print("            5)by caste")
        print("            6)HRM student")
        print("            7)KM student")
        print("            8)MP student")
        print("            9)kv tc student")
        print("            10)fresh student")
        print("            11)salary.")
        print("            12)All student")
    elif(n==5):
        print("1st class")
        print("other than first class")
def take(Type,choice,gap,output,not_output,menu_choice,mode=0):
    s=0
    if(Type.upper()=="INT"):
        while(s==0):
            menu(menu_choice,mode)
            ABC=input(gap+output)
            if(ABC.isdigit()):
                ABC=int(ABC)
                if(choice==None):
                    s=1
                elif(ABC in choice):
                    s=1
            else:
                print(not_output)
    elif(Type.upper()=="INPUT"):
        while(s==0):
            menu(menu_choice,mode)
            ABC=input(gap+output).upper()
            if(choice==None):
                s=1
            elif(ABC in choice):
                s=1
            else:
                print(not_output)
    return ABC

def spaces(S):                  # no more than 1 space in bundle
    L=S.split()
    S1=""
    for x in L:
        S1+=x+" "
    return (S1.capitalize())[0:-1]
def admission_no():
    f=open("ADMISSION_NUMBER.dat","rb")
    I=load(f)
    ma=max(I)
    f.close()
    f=open("ADMISSION_NUMBER.dat","wb")
    dump(I+[ma+1],f)
    f.close()
    return ma+1
def collecting_data(file):
    f=open(file,"rb")
    data=load(f)
    f.close()
    return data
def exchanging_data(file,data):
    f=open(file,"wb")
    dump(data,f)
    f.close()
def section(cla,stram=0):
    
    if(cla==1):
        cl="1st"
    if(cla==2):
        cl="2nd"
    if(cla==3):
        cl="3rd"
    if(cla>=4 and cla<=13):
        cl=str(cla)+"th"
    
    a=collecting_data("COUNT_SECTION.dat")[cl]["a"]
    b=collecting_data("COUNT_SECTION.dat")[cl]["b"]
    c=collecting_data("COUNT_SECTION.dat")[cl]["c"]
    if([a,b,c].count(0)==3):
        sec=choice(("a","b","c"))
    else:
        sec=choice((["a"]*(b+c))+(["b"]*(c+a))+(["c"]*(a+b)))
    d=collecting_data("COUNT_SECTION.dat")
    d[cl][sec]+=1
    exchanging_data("COUNT_SECTION.dat",d)
    return sec
def count_check():
    for x in collecting_data("COUNT_SECTION.dat"):
        print(x,"\t\t",collecting_data("COUNT_SECTION.dat")[x])
