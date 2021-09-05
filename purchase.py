'''
Module name: purchase
Function name: purchase
Overview of this function:
1) Customer interaction for what and how much quantity they want to buy.
2) Check the user interaction valid or not with exception handelling.
3) Calculating the customer purchase product with discount(if discountable)
4) Show the last update of the product
5) Write the invoice for customer with unique naming
'''
def purchase(List):
    L=List #assign list with variable name 'L'.
    a_name=input("Please enter patient name: ")
    phone_number=input("Please enter patient's phone number: +91 ")
    employee_name=input("Please enter your code: ")
    print("\nHello "+employee_name+"! Welcome to your Hospital Billing System.\nLook at above and select product as customer wants to buy.")
    q={}  #assign empty dictionary with variable name 'q'.
    flag="Y"
    while flag.upper()=="Y":  #check and go if flag is 'Y' or 'y'.
        product=input("\nWhat product does customer want to buy? ")  
        product_name=product.upper()    #change the string value in the upper case.
        
        if product_name==L[0][0].upper() or product_name==L[1][0].upper() or product_name==L[2][0].upper(): #check the user entered product name with stock of store 
            p=True
            while p==True:
                try:
                    p_quantity=int(input("How many "+product+" does customer want to buy: "))
                    p=False
                except:                             #executes, if customer entered unexpected value.
                    print("\t\tError!!!\nPlease enter integer value!! ") 
            if product_name==L[0][0].upper() and p_quantity<=int(L[0][2]):       
                q[product_name]=p_quantity    
            elif product_name==L[1][0].upper() and p_quantity<=int(L[1][2]):
                    q[product_name]=p_quantity
            elif product_name==L[2][0].upper() and p_quantity<=int(L[2][2]):
                    q[product_name]=p_quantity
            else:
                print("\nSorry!! "+a_name+"!, "+product+" is out of stock.\nWe will add stock of "+product+" later. \nLets hope, you will get this product after next shopping.\n")
                
            flag=(input(a_name+" do the customer want to buy more products?(Y/N)"))
        else:
            print("sorry!! "+product+" is not available in our store.")
            print("\nChoose from following products please!")
            print("--------------------------------------------")
            print("PRODUCT\t\tPRICE\t\tQUANTITY")
            print("--------------------------------------------")
            for i in range(len(L)):
                print(L[i][0],"\t\t",L[i][1],"\t\t",L[i][2]) # print, last updated product name, quantity and price.
            print("--------------------------------------------")
                
    print ("\nYou Choosed Items and it's Quantity respectively:\n",q,"\n")

    '''
        In the following operation:
        1) Change every string value in the upper case letter.
        2) Check what is the product entered by customer.
        3) Executes respective condition if product is crocine or rabipur or paracetamol entered by user.
    '''
    
    f_amount=0  #final amount
    for keys in q.keys():
        if keys==L[0][0].upper(): #executes this operation if product is phone entered by customer.
            p_price=int(L[0][1])
            p_num=int(q[keys])
            p_amount=(p_price*p_num)
            f_amount+=(p_price*p_num)
            print("\nTotal cost for crocin: ",p_amount) 
        elif keys==L[1][0].upper():  #executes this operation if product is laptop entered by customer.
            l_price=int(L[1][1])
            l_num=int(q[keys])
            l_amount=(l_price*l_num)
            f_amount+=(l_price*l_num)
            print("Total cost for rabipur: ",l_amount)
        else:                        #executes this operation if product is hdd entered by customer.
            h_price=int(L[2][1])
            h_num=int(q[keys])
            h_amount=(h_price*h_num)
            f_amount+=(h_price*h_num)
            print("Total cost for paracetamol: ",h_amount)
    print("\nYour subtotal amount is: ", f_amount)

    '''
        In the following operation:
        1) Ask to customer for expected discount % in total purchase amount.
        2) Check the total purchase amount which is dcustomer expected discountable or not.
        3) Check the total purchase amount which is basic discountable or not.
    '''
    
    disc=float(input("Please enter your expected discount (%): "))
    dis=0.0
    if ((f_amount>=5000) and (f_amount<10000)):
        discount=disc
        if(discount<=5.0):
            dis=(discount*f_amount)/100
            total=float(f_amount-dis)
            print("You got your expected "+str(disc)+"% discount and amount is: ",dis)
        else:
            discount=5.0
            dis=(discount*f_amount)/100
            total=float(f_amount-dis)
            print("You did not got your expected "+str(disc)+"% discount\nBecause, your total purchase is not meet the minimum criteria for "+str(disc)+"% discount.")
            print("You got basic 5% discount and discounted amount is:",dis)
    elif (f_amount>=10000):
        discount=disc
        if(discount<=10.0):
            dis=(discount*f_amount)/100
            total=float(f_amount-dis)
            print("You got your expected "+str(disc)+"% discount and amount is: ",dis)
        else:
            discount=10.0
            dis=(discount*f_amount)/100
            total=float(f_amount-dis)
            print("You did not got your expected "+str(disc)+"% discount\nBecause, your totel purchase is not meet the minimum criteria for "+str(disc)+"% discount.")
            print("You got basic 10% discount and discounted amount is:",dis)
    else:
        discount=0.0
        total=float(f_amount)
        print("You did not got your expected "+str(disc)+"% discount\nBecause, your total purchase is not meet the minimum criteria for "+str(disc)+"% discount.")
    print("Your payable amount is: ",total)

    '''
        In the following operation:
        1) Write a each unique invoive name which includes current date and time with patient name and patient phone number as well.
        2) Write a purchase product name and details in file (invoice).
        3) Write a discounted amount and final payable amount in file (invoice).
    '''
    
    import datetime  #import system date and time for create a unique invoive name.
    dt=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().hour)+"-"+str(datetime.datetime.now().minute)+"-"+str(datetime.datetime.now().second)
    invoice=str(dt)    #unique invoice
    t=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day) #date
    d=str(t)    #date
    u=str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+":"+str(datetime.datetime.now().second) #time
    e=str(u)    #time
    
    file=open(invoice+" ("+a_name+").txt","w")      #generate a unique invoive name and open it in write mode.
    file.write("=============================================================")
    file.write("\nHospital Store\t\t\t\tINVOICE")
    file.write("\n\nInvoice: "+invoice+"\t\tDate: "+d+"\n\t\t\t\t\tTime: "+e+"")
    file.write("\nName of Patient: "+str(a_name)+"")
    file.write("\nPhone Number: "+str(phone_number)+"")
    file.write("\n=============================================================")
    file.write("\nPARTICULAR\tQUANTITY\tUNIT PRICE\tTOTAL")                     
    file.write("\n-------------------------------------------------------------")
          
    for keys in q.keys():           #In this loop, write in a file only those product which is purchase by user.
        if keys=="CROCIN":
            file.write(str("\n"+str(keys)+" \t\t "+str(q['CROCIN'])+" \t\t "+str(L[0][1])+" \t\t "+str(p_amount)))
        elif keys=="RABIPUR":
            file.write(str("\n"+str(keys)+" \t\t "+str(q['RABIPUR'])+" \t\t "+str(L[1][1])+" \t\t "+str(l_amount)))
        else: 
            file.write(str("\n"+str(keys)+" \t\t "+str(q['PARACETAMOL'])+" \t\t "+str(L[2][1])+" \t\t "+str(h_amount)))
       
    file.write("\n\n-------------------------------------------------------------")
    file.write("\n\t\t\tYour total product amount: "+str(f_amount))
    file.write("\n-------------------------------------------------------------")
    file.write("\n\t\t   Your "+str(discount)+"% discounted amount is: "+str(dis))
    file.write("\n-------------------------------------------------------------")
    file.write("\n\t\t\t Your payable amount is: "+str(total))
    file.write("\n-------------------------------------------------------------")
    file.write("\n\n\tThank You "+a_name+" for your shopping.\n\t\tSee you again!")
    file.write("\n=============================================================")
    file.close()
    return q