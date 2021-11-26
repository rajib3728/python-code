while(1):
    print("  enter 1 for area ")
    print(" enter 2 for swap")
    print(" enter 3 for kilometer to mile ")
    print(" enter  4 for  c to f conversion")
    print("enter 5 for sq ")
    print("enter other digit for exit this loop")
    x=int(input("enter your choice="))
    if x==1:
        print(" finding area:")
        a=float(input("enter base value="))
        b=float(input("enter hight value="))
        c=0.5*a*b
        print("area=",c)
    elif x==2:
        print("  swap with out third variable:")    
        a=float(input("enter no 1="))
        b=float(input("enter no 2="))
        b=a+b
        a=b-a
        b=b-a
        print("no 1=",a)
        print("no 2=",b)
    elif x==3:
        print("kilometer to mile conversion:")
        d=float(input("enter kilometer value="))
        e=0.621371*d
        print("mile=",e)
    elif x==4:
        print("celsius to fahrenheit:")
        d=float(input("enter c value=")) 
        e=(d*9/5)+ 32
        print(" f=",e)  
    elif x==5:
        print(" for square:") 
        f=float(input("enter a no="))
        f=f*f
        print("square=",f)
    else:
        break     


