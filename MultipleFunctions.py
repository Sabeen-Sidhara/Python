class MultipleFunctions():
    def Subfields():
        lists=["Sub-fields in AI are:" ,"Machine Learning" ,"Neural Networks" ,"Vision" ,"Robotics" ,"Speech Processing" ,"Natural Language Processing"]
        for items in lists:
            print(items)

    def OddEven():
        num=int(input("Enter a number:"))
        if((num%2)==0):
            print(num,"is Even Number")
        else:
            print(num,"is Odd Number")

    def Eligible():
        gend=(input("Your Gender:"))
        age=int(input("Your Age:")) 
        if(gend=="Male" and age>=21):
            print("ELIGIBLE")
        elif(gend=="Female" and age>=18):
            print("ELIGIBLE") 
        else:
            print("NOT ELIGIBLE")

    def percentage():
        num1=int(input("Subject1="))
        num2=int(input("Subject2="))
        num3=int(input("Subject3="))
        num4=int(input("Subject4="))
        num5=int(input("Subject5="))
        Total=num1+num2+num3+num4+num5
        print("Total:",Total)
        percen=(Total/5)
        print("Percentage :",percen)
    
    def triangle():
        Height=int(input("Height:")) 
        Breadth=int(input("Breadth:")) 
        Area=(Height*Breadth)/2 
        print("Area formula:(Height*Breadth)/2")
        print("Area of Triangle:",Area)
        Height1=int(input("Height1:")) 
        Height2=int(input("Height2:")) 
        breadth=int(input("Breadth:"))
        Perimeter=Height1+Height2+breadth 
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",Perimeter)


    