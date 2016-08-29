product=input("name of the product")
quantity=int(input("enter the number"))
if(product=="mobile"):
    print("price is 10000")
    total=10000*quantity
    print(total)
elif(product=="tv"):
    print("price is 50000")
elif(product=="computer"):
    print("price is 30000")
else:
    print("error")
        
