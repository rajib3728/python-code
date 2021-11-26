import os
import shutil
import filecmp
while(1):
    x=int(input("enter between 1 to 10"))
    if x==1:
        f=open("poems.txt","r")
        for line in f:
            for word in line.split():
                if(word=='twinkle'):
                    print(word)
        f.close()
    elif x==2:
        f=open('Hiscore.txt','w')
        e=int(input("enter new score"))
        f.write(e)
        f.close()
    elif x==3:
        a=int(input("enter a number between 2 to 20 "))
        f=open('mul.txt','w')
        for i in range(1,11):
            c=a*i
            f.write("\n")
            f.write("%d"%c)
        f.close() 
    elif x==4:
        print("donkey word replacing with ####")
        f=open('p.txt','r')
        for line in f:
            for word in line.split():
                f.write(word.replace('donkey','####'))
                print(word)
        f.close()
    elif x==5:
        f=open("poems.txt","r")
        for line in f:
            for word in line.split():
                if(word=='python'):
                    print(word)
        f.close()
    elif x==6:
        f=open("poems.txt","r")
        for line in f:
            for word in line.split():
                if(word=='python'):
                    print(line.index)
    elif x==7:
        print("it will copy a txt file")
        shutil.copy('mul.txt','abc.txt')
    elif x==8:
        f1=open('mul.txt','r')
        f2=open('abc.txt','r')
        c=filecmp.cmp(f1,f2)
        print(c)
    elif x==9:
        print("it will help to erase")
        f=open("mul.txt","r+")
        f.truncate(0)
        f.close()
    elif x==10:
        print("it will remane a file")
        os.rename()          
