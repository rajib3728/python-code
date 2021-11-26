import calendar
def add():
    n=int(input(" total number you want to add"))
    c=[]
    s=0
    for i in range(n):
        e=int(input("enter"))
        c.append(e)
    print(c) 
    for j in range(n):
        s=s+c[j] 
    print("sum=",s)
def mul():
    a=int(input(" total number you want to multiply"))
    c=[]
    b=1
    for i in range(a):
        e=int(input("enter"))
        c.append(e)
    print(b) 
    for j in range(a):
        b=b*c[j] 
    print("multiply=",b) 
def fibb():
    a=0
    b=1
    n=int(input("enter range"))
    for i in range(n):
        print("fibb=",a)
        c=a+b
        a=b
        b=c
def lcm(x, y):  
   if x > y:  
       greater = x  
   else:  
       greater = y  
   while(True):  
       if((greater % x == 0) and (greater % y == 0)):  
           lcm = greater  
           break  
       greater += 1  
   return lcm  
def hcf(x, y): 
   if x > y:  
       smaller = y  
   else:  
       smaller = x  
   for i in range(1,smaller + 1):  
       if((x % i == 0) and (y % i == 0)):  
           hcf = i  
   return hcf          
while True:
    x=int(input(" enter any choice with in 1 to 7 and other for exit "))
    if x==1:
        print("lcm")
        num1 = int(input("Enter first number: "))  
        num2 = int(input("Enter second number: "))  
        print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))
    elif x==2:
        print("hcf")  
        num1 = int(input("Enter first number: "))  
        num2 = int(input("Enter second number: "))  
        print("The H.C.F. of", num1,"and", num2,"is", hcf(num1, num2))  

    elif x==3:
        e=int(input(" enter number")) 
        print("binary=",bin(e)) 
        print("octal=",oct(e))
        print("hex=",hex(e))
    elif x==4:
        s=input("enter a char")
        print("ascii value=",ascii(s))
    elif x==5:
        print("calculator") 
        a=int(input("enter 1 for add 2 for sub 3 for multiply 4 for divide "))
        if a==1:
             add()
        elif a==2:
             c=float(input("enter no 1:"))  
             d=float(input("enter no 2:"))   
             f=c-d
             print("sub=",f)
        elif a==3:
            mul()
        elif a==4:
            c=float(input("enter no 1:"))  
            d=float(input("enter no 2:")) 
            e=c/d
            print("div=",e)
    elif x==6:
        m=int(input("enter month"))  
        y=int(input("enter year"))  
        print(calendar.monthcalendar(y,m))
    elif x==7:
        print("fibonnaci series")
        fibb()




