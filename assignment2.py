while(1):
    x=int(input("enter any between 1 to 6 other to exit loop"))
    if x==1:
        ch=input(" enter a for sq b for rect c for tri")
        if ch=="a":
            A=float(input("enter side of sq"))
            B=A*A
            print("area of sq",B)
        elif ch=="b":
            B=float(input("enter length"))
            C=float(input("enter breadth"))
            A=B*C
            print(" area=",A)
        elif ch=="c" :
            A=float(input(" enter hight"))  
            B=float(input("enter base")) 
            c=0.5*A*B
            print("area=",c)
    elif x==2:
        print(" interest based problem")    
        p=float(input("enter money"))  
        t=float(input(" enter time in year"))  
        if t>12:
            s=p*t*0.1
            print("interest=",s)
        else:
            s=p*t*15/100
            print("interest=",s) 
    elif x==3:
        print("discount problem")  
        a=float(input("item 1"))  
        b=float(input("item 2")) 
        c=float(input("item 3"))    
        d=float(input("item 4"))  
        e=float(input("item 5"))
        s=a+b+c+d+e
        if s<5000:
            print("10 percent discount")
            g=0.9*s
            print("you have to pay=",g)
        else:
            print("5 percent discount")  
            g=(1-5/100)*s
            print("you have to pay=",s) 
    elif x==4:
        print("bonus problem")  
        t=float(input("enter year of service"))  
        s=float(input("salary"))  
        if t> 5:
            a=(1+5/100)*s
            print("with 5 percent bonus salary",a)
        else: 
            print("salary=",s)  
    elif x==5:
        print("report card")  
        x=float(input("enter marks"))
        if x<25:
            print("F")
        elif x>=25 and x<45:
            print(" E")           
        elif x>=45 and x<50:
            print("D")
        elif x>=50 and x<60:
            print("C")
        elif x>=60 and x<80:
            print("B")
        elif x>=80:
            print("A")   
    elif x==6:
        print("palindrome")     
        a=input("enter")
        b=a[::-1]
        if a==b:
            print("palindrome")
        else:
            print("no")    
        print(b)
    else:
        break   