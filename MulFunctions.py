class mulpFunction():
    def oddoreven():
        a=int(input("Enter a number: "))
        if(a%2==0):
            print(a,"is even number")
        else:
            print(a,"is odd number")
            
    def elegible():
        gender=input("Your gender:")
        age=int(input("Your age:"))
        if(gender== "Male" and age>=21):
            print("Elegible")
            a="Elegible"
        elif(gender=="Male" and age<=20):
            print("Not Elegible")
            a="Not Elegible"
        elif(gender=="Female" and age>=18):
            print("Elegible")
            a="Elegible"
        elif(gender=="Female" and age<=17):
            print("Not Elegible")
            a="Elegible"
        else:
            print("Entered items are not valid")
            a="Entered items are not valid"
        return a
    
    def percentage():
        s1=int(input("Subject1= "))
        s2=int(input("Subject2= "))
        s3=int(input("Subject3= "))
        s4=int(input("Subject4= "))
        s5=int(input("Subject5= "))
        total=s1+s2+s3+s4+s5
        print("Total: ",total)
        print("Percentage:",total/5)

    def triangle():
        h=int(input("Height: "))
        b=int(input("Breadth: "))
        print("Area of formula: (Height*Breadth)/2")
        print("Area of Triangle: ",(h*b)/2)
        h1=int(input("Height1: "))
        h2=int(input("Height2: "))
        b1=int(input("Breadth: "))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",h1+h2+b1)

 
    def Subfields(*a):
        for i in a:
            print(i)
subfieldsinAI=mulpFunction          
subfieldsinAI.Subfields('Sub-fields in AI are:', 'Machine Learning', 'Neural Networks', 'Vision', 'Robotics','Speech Processing','Natural Language Processing')



   
     
        
        