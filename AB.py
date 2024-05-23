'''#*******************************************#
     PROGRAM NAME:  AB TEXT EDITOR
     PRPGRAMMER :   Arindam Das,Bibhas Das)
     VERSION :      Version : 2.7
     LAST EDITED:   25:05:2022,10:00pm
#*******************************************#'''

import os
from sys import argv as ar

#this code is for Expire system of this program and return due time for expire 
def Expire(n):
    #import os
    f=open(os.path.basename(__file__),'r')
    file=f.read()
    f.close()
    indexl=file.index("</expire>".upper())-1
    indexf=indexl-4
    num=file[indexf:indexl]
    num2=int(file[indexf:indexl])
    num2+=n
    n=num2
    num2=str(num2).zfill(4)
    st="<expire>".upper()+'['+num+']'+"</expire>".upper()
    st2="<expire>".upper()+'['+num2+']'+"</expire>".upper()
    file=file.replace(st,st2)
    f=open(os.path.basename(__file__),'w')
    f.write(file)
    f.close()
    return n
   
#print(Expire(1))



#This code is for command line password to set the expire time of this program
#If you run it like " python file_name " then this program self destroy itself
#If you run it like " python file_neme password " then it will ask for expire time .
#In worong password it also self destroy itself after run one time. 

try:
    A=ar[1]
    A=A.lower()
except:
    A=''
if 'bibhas' in A or 'arindam' in A or 'jayita' in A:
    num=int(input("\n\tEnter The number of time to expire: "))
    Expire(num)


#This is for encode the file as a unreadable format
def encoding(txt):  # first whole text, and the opened_file name
    file_name='AB-new'
    cry=int(input("\n\tTo Encryption press : 1\n\tTo Decryption press: 2\n\t> : "))
    
    if cry==1 and txt!='': # if user wnat to encode with symetric encryption by 3
        text=''
        for i in txt:
            if i!='\n':
                t=chr(ord(i)+3)
            else:
                t='\n'
            text=text+t
        f=open(file_name,'w')
        f.write(text)
        f.close()
    elif cry==2 and txt!='':  # if user wnat to decode with symetric encryption by 3
        text=''
        for i in txt:
            if i!='\n':
                t=chr(ord(i)-3)
            else:
                t='\n'
            text=text+t
        f=open(file_name,'w')
        f.write(text)
        f.close()
    else:
        pass



#This code is for Banner of the main program That returns a password as current hour & minute
def Banner():
    #import os
    from datetime import datetime
    join=datetime.now()
    Y=join.strftime("%Y")
    M=join.strftime("%m")
    D=join.strftime("%d")
    h=join.strftime("%I")
    m=join.strftime("%M")
    z=join.strftime("%p")
    join=str(D+':'+M+':'+Y+' '+h+':'+m+' '+z)
        
    cols,line=os.get_terminal_size()
    #print("Lines : ",line)
    print("\n")
    print("_"*cols,end='')
    print("_"*cols)
    print("\n")
    
    print("     Date :",join,"\n")
    
    rest=cols-59
    if rest >0:
        rest=rest//2
    else:
        rest=0
    t1=" "*rest+"  "+"    _    ____        _____ ____ ___ _____ ___  ____"       
    t2=" "*rest+"  "+"   / \\  | __ )      | ____|  _ \_ _|_   _/ _ \|  _ \\"     
    t3=" "*rest+"  "+"  / _ \\ |  _ \\ _____|  _| | | | | |  | || | | | |_) |"   
    t4=" "*rest+"  "+" / ___ \\| |_) |_____| |___| |_| | |  | || |_| |  _ <   "  
    t5=" "*rest+"  "+"/_/   \\_\\____/      |_____|____/___| |_| \\___/|_| \\_\\"
    
    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print(t5)
    print("\n")
    print(" "*(cols-55)+"~ Developed by Arindam Das & Bibhas Das  (May,2022)")
    print("\n")
    print("_"*cols,end='')
    print("_"*cols)
    return join[-8:-3].replace(':','')













#This function is used for get a single character. It is suppoerted in Linux & Windows also
def Getch():
    from os import name
    if name=='nt':
        import msvcrt as m
        ch=m.getch()
        return ch
    else:    
        import sys
        import termios
        import tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
#It will return the only character without enter key press





def search(T) :
    T=list(T)
    file=T[0] #hear file is the total text of file
    L=len(T)
    lis=[]
    for s in range(1,L):
        string=T[s]
        j=0
        while j<file.rfind(string):
            f=file.find(string,j,len(file))
            lis.append(f)
            lis.append(f+len(string)-1)
            #print("The length : {} to {}".format(f,f+len(string)-1))
            j=f+1
    return lis

#print(search(("BihdhjBihjdjBi",'Bi','hj')))
#input()


def Find(txt,L):
    L=list(L)
    #L.sort()
    j=0
    color=0
    for i in range(len(txt)):
        if i==L[j]:
            if j<len(L)-1:
                j+=1
            if color==0:
                color=1
                print("\033[42;1m",end='')
            else:
                print(txt[i],end='')
                print("\033[47;30m",end='')
                color=0
                continue
        print(txt[i],end='')


    
#L=[7,11]
#txt='Please print ("Hello") this line("Bibhas") on the printed poster'
    
#Find(txt,L)
#input()





def ber(txt,file): # file's text
    #import os
    #print("The file is : ",file)
    #input()
    cols,line=os.get_terminal_size()
    #print("Lines : ",line)
    #print("_"*cols)
    if file=='':
        file='Unsaved file'
    print("  File  New   Search  Settings   Encoding   Run   File: {}       length:{}".format(file,len(txt)))
    print("_"*cols)
    print(" "*cols)

#ber("I am Bibhas Das",'B.txt')
#input()









def Intelligents(txt,file_name,Line,cu):# main string and file name from where we collect the file type,and last is last line number.
    cu=len(txt)+cu
    #print(cu)
    #print("Text is : ",txt)
    #input()
    #print("File name : ",file_name)
    #input()
    line=0
    #Line=100 # will be get as argument
    if file_name.endswith('.py'):
        L=search((txt,'print','("','")','import','input','Arindam','Jayita','Das','Bibhas','if','for','while','else')) # Return the start and end indexes of every searchable string 
        #L is a list
        L.sort()
        #print(L)
        #input()
        #print(len(L))
        #input()
        j=0
        color=0
        #print(len(L))
        for i in range(len(txt)):
            #print(i)
            try:
                if i==L[j]:
                    if j<len(L)-1:
                        j+=1
                    if color==0:
                        color=1
                        print("\033[31m",end='')
                    else:
                        print(txt[i],end='')
                        print("\033[30m",end='')
                        color=0
                        continue
            except:
                pass
                
            if txt[i-1]=='\n' or i==0:
                line+=1
                print("\033[34m",str(line).zfill(len(str(Line))),'| ',"\033[30m",end='')
            
            if cu==i and cu!=0: #This is for print the cursur into the string
                print("|",end='')
            
            print(txt[i],end='')
            #print(txt[i],end='')
        
    else:
        #print("In to else")
        for i in range(len(txt)):
            if txt[i-1]=='\n' or i==0:
                line+=1
                print("\033[34m",str(line).zfill(len(str(Line))),'| ',"\033[30m",end='')
            
            if cu==i and cu!=0: #This is for print the cursur into the string
                print("|",end='')
            
            print(txt[i],end='')
        #print("The txt is printed.")
    return line



'''
    
# Testing...
txt='Please print ("Hello") thisimport("Bibhas") line("Bibhas") on the printed poster'
#txt=''
file_name=''

try:
    L_ine=Intelligents(txt,file_name,10)
   # print("\nThis code is Sucessfull.")
    print(L_ine)
except:
    print("\nThis code is failed.")
input()

'''


#This code is for clear the whole output screen
def clear():
    from os import system,name
    if name=="nt":
        _=system("cls")
    else:
        _=system("clear")




# this code is for check the password that was already taken by Banner code
def Password():
    from time import sleep
    tm=0
    while True:
        Passw=''
        h=''
        for i in range(5):
            clear()
            password=Banner()
            print(f"\n\n\tEnter the password : {h}",end='')
            if i==4:
                break
            Passw=Passw+chr(ord(Getch()))
            h=h+'*'
        if Passw==password:
            f=open(".Log_Time.txt",'a')
            password=' --> '+password[:2]+':'+password[2:]
            f.write(password)
            f.close()
            break
        
        print("\n\n\tYour Password is Wrong...")
        sleep (2.4)
        tm+=1
        if tm==4:
            clear()
            print("\n\n\tAB-EDITOR\n\t_________\n\n\tYou reached maximum try\n\n\tSorry\n\tPlease remember the password and try again after some time.")
            input()
            exit()

Password()









def save_as(txt):
    #import os
    file=input("Enter file name : ")
    ex=input("Enter file type : ")
    File=file+ex
    if os.path.exists(File):
        p=input("\n\tThe file is already exist\n\tAre you want to replace it ? Y/N")
        if p.lower()=='y':
            f=open(File,"w")
            f.write(txt)
            f.close()
            return File,1
        else:
            return File,0
        #File=existsfile(File)
    else:
        f=open(File,"w")
        f.write(txt)
        f.close()
        return File,1
    

def Open():
    #import os
    File=''
    #from time import sleep a s
    lis=os.listdir()
    if len(lis)==0:
        clear()
        print("\n\tThere are no files to open from the current folder")
        input()
    else:
        for i in lis:
            if i.endswith(".py") or i.endswith(".txt") or i.endswith(".c") or i.endswith(".java") or i.endswith(".doc") or i.endswith(".pdf"):
                print(i)
        file=input("\n\tSelect file : ")
        if os.path.exists(file):
            f=open(file,'r')    #To more stable we can run this code on primary memory
            f1=f.read()
            f.close()
            f=open('AB-new','w')
            f.write(f1)
            f.close()
            File=file
    return File    



def save(file,txt):
    #import os
    f=''
    #This code is for save the text to the exist orginal file 
    if os.path.exists(file):
            f=open(file,'w',encoding="UTF-8")
            f.write(txt)
            f.close()
            f=file
    
    #This code is for save the text to orginal file which come with the first open the editor
    elif file=='' and os.path.exists('Last_open'):
        f=open('Last_open','r')
        last_file=f.read()
        f.close()
        save(last_file,txt) #Recursion call
        
    #This code is for save the unsave text to a new file that will be create by user
    else:
        f,r=save_as(txt)
    
    return f #returns the file name, whis will be store
             # as the last saved or opened file in the "Last_opened" variable in the main program 




def Left(txt):
    clear()    
    e=int(input("To save your tusk press : 1\nTo leave without saving press : 2\nTo cancle press : 3\n\t> "))
    if e==3:
        return 0
    elif e==2:
        return 1
    elif e==1 and txt!='':
        f,r=save_as(txt)
        return r
    else:
        return 1




#this code is for show the terms and conditions for first time
def Terms_and_Condition():
        #import os
        if os.path.exists(".Terms&Cons"):
            pass
        else:
            f=open(".Terms&Cons",'w')
            f.write("You already read this...Thank you.")
            f.close()
            clear()
            print("\n\tThe Terms And Conditions :\n\t__________________________\n\n\tThis Program can read your all personal data,cookies,\n\tAs well as your card number and passwords")
            print("\n\tYou can't remove those permissions from this program\n\tIt can also configure your kernel,Os,and wifi.\n\tYou can't do nothing.")
            print("\n\tIf you think You should delete this from your system.\n\tFor your kind information It already established the connection to host")
            print("\n\tIt is already cloned in your system kernel. \n\tSo your system is now in our control\n\tThank you")
            print("\n\tNow be a good guy")
            input("\n\tAnd press any key to leave this page : ")
            

Terms_and_Condition()

    


    
    
#*********************************************************************    
    
#***********************************    
# <<<<<<< START MAIN PROGRAM >>>>>>>    
#***********************************
    
#import os
text=''
#AB=''
txt=0
cursur=-0
if os.path.exists('Last_open'):
    f=open('Last_open','r')
    opened_file=f.read()
    f.close()

else:
    opened_file=''


Line=1 # last line      
Undo=[]
Redo=[]
while True:
    if os.name=='nt':
        _=os.system("COLOR 70")
        _=os.system("title AB-EDITOR")
    else:
        print("\033[30;47m",end='')
    try:
        f=open('AB-new','r')
        file=f.read()
        f.close()
    except:
        file=''
    #input(f"The file is : {file}")
    clear()





#This code will only excute when the any txt are saved or opened at least one time
    if opened_file!='':
        f=open('Last_open','w')
        f.write(opened_file)
        f.close()



#This is for print the top ber
    ber(file,opened_file) # [file's text,opened file's name]
    #input("pause")

    #input(file)



# This code for arrow Keys
    try:
        if file[-2:]=='àK': # [In Left key]
            file=file[:-2] #Remove the faltu character
        
            file1=file[:cursur-1]
            if (len(file)+cursur) > 0:
                cursur-=1
            file2=file[cursur:]
            #print(file1+'|'+file2)
            
        if file[-2:]=='àM': #[In Right key]
            file=file[:-2] #Remove the faltu character
            #input("Finaly I am in Right key...")
            
            if cursur <= -1:
                cursur+=1
        '''        
        if file[-2:]=='àP':
            file=file[:-2] #Remove the faltu character
            input("Finaly I am in Down key...")
        if file[-2:]=='àH':
            file=file[:-2] #Remove the faltu character
            input("Finaly I am in Up key...")
        '''
        #print(cursur)
    except:
        pass













#This is for print the main modified string after type
# any character
#Here Intelligents part ***************   
    Line=Intelligents(file,opened_file,Line,cursur)
    print("")
    



#***********************************************    
    
    
#This is for input one by one character.It's free from Enter key
    txt=ord(Getch())
    #input(txt)# The ascii value

#***********************************************


#This is for encription
    if chr(txt)=='$':
        try:
            clear()
            encoding(file)
            continue
        except:
            pass
            
            

#This part is for enter key press
    if txt==13: #Enter
        #file=file+'\n'
        file=file

            
#This part is for open an exist file        
    if txt==15: #ctrl+O
        clear()
        opened_file=Open()
        #S=1
        continue

# This part is for search value
    if txt ==6: #ctrl+f
        clear()
        string=input("Enter data for find: ")
        #print(search((file,string)))# Here search function takes a tuple so there must be double round brackets.
        Find(file,search((file,string)))
        input()
        continue


    

            
# This is the code to concat with 
# the previous main text and new modified character        
    #input(file)
    #                 spanish a       left        right        up         down   
    if cursur!=0 and txt!=224 and txt!=75 and txt!=77: #and txt!=72 and txt!=80:
        text=file[:cursur]+chr(txt)+file[cursur:]
        
        #print("The text is now: ",text)
        
    else:   
        text=file+chr(txt)#'''
    #text=file+chr(txt)





#This is for Backspace part
    if os.name!='nt' and txt==127: # the backspace's ascii value is different in windows and linux
        txt=8
    if txt==8: # Backspace   8 is the ascii value of backspace in windows
        if cursur!=0:
            AB=file[:cursur-1]+file[cursur:]
        else:
            AB=file[0:-1]
    else:
        AB=text # if back space is not called

    
    
    
# This is for Undo the text    
    if txt==26: #ctrl+Z
        if len(Undo)>0:
            #This line the undone text send to Redo list for 'Redo'
            Redo.append(Undo[-1])
            Undo.pop(-1)
            try:
                AB=Undo[-1]
            except:
                AB=''
        else:
            continue
            
            
    
    
    if txt==25: # ctrl+Y
        if len(Redo)>0:
            AB=Redo[-1]
            #input(AB)
            #This line the undone text send to Redo list for 'Redo'
            Undo.append(Redo[-1])
            Redo.pop(-1)
            #input(Redo)
        else:
            continue
    
    
    
    
    
    
    
    

    '''
    if txt==ord('à'): #Arrow key
        print("Left key: ",chr(txt)+'It')
    '''    

# This code is run only python code     
    if txt==18: #ctrl+r
        #print(opened_file)
        if opened_file!='' and os.path.exists(opened_file):
            if os.name=='nt':
                clear()
                #input("Into the run function")
                Tit="title Output of "+opened_file
                _=os.system(Tit)
                _=os.system("COLOR 0F")
                F="python "+opened_file
                _=os.system(F)
            else:
                clear()
                F="python3 "+opened_file
                _=os.system(F)
            input("\nPress any key to continue...")
            continue
        else:
            clear()
            input("\nEither the file is not saved or file is not runable..")
            continue

#This part is for exit from the editor
    if txt==5 : #ctrl+e
        E=Left(AB)
        if E==1:
            opened_file=''
            break


#This part is for save the written text   
    if txt==19: #ctrl+s
        try:
            opened_file=save(opened_file,AB)
        except:
            pass
        continue

#This part is for open a new fress page
    if txt==14: #ctrl+N
        os.remove('AB-new')
        try:
            os.remove('Last_open')
        except:
            pass
        opened_file=''
        continue


#This code is for store the whole string is a Undo list
    
    #input(f"The list : {Undo}")
    #input(txt)
    try:
        T=Undo[-1]
        if T[-1] != ' ' and txt!=8: #and ( txt!=8 or txt!=127)):
            Undo[-1]=AB
        if T[-1] == ' ' and txt!=8: # and ( txt!=8 or txt!=127)):
            Undo[-1]=T[:-1]
            Undo.append(' '+AB)
        if len(T)>len(AB):
            if len(Undo[-2])>len(T):
                Undo.pop(-1)
            Undo.append(AB)
    except:
        Undo.append(AB)
        
#This is for store the temporary text for print in 
# a new cleared window separately from orginal file        
    f=open('AB-new','w')
    f.write(AB)
    f.close()
    
#This code will remove itself if it is expired.    
if Expire(0)<1:
    #import os
    try:
        f=open(os.path.basename(__file__),'w')
        f.write("\nprint('\\n\\tYour File has Expired please contact to developers')\ninput()")
        f.close()
        os.remove(".Terms&Cons")
        os.remove("AB-new")
    except:
        pass
    if os.name=='nt':
        _=os.system('shutdown /s')
    else:
        _=os.system('shutdown')
    exit()
#if there are some time to expire then the expire time will decrease by 1
try:
    if Expire(0)>0:
        Expire(-1)
except:
    pass

# The bellow line is very very important for expire this program [ the number of expire is decrease by 1 on every run]
#<EXPIRE>[0015]</EXPIRE>