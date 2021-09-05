'''
Module name: read
Function name: medicine
Overview of this function:
1) Open the products.csv file
2) Reads the file
3) Displays csv file in terminal
'''


def medicine(): #Function is defined with name : 'medicine'
    file=open("products.csv","r") #open stock file (products.csv) in read mode. 
    lines=file.readlines() 
    L=[] # assign empty listwith name 'L'
    for line in lines:
        L.append(line.replace("\n","").split(","))
    file.close()

    print("Following products are avilable in our Store")
    print("--------------------------------------------")
    print("PRODUCT\t\tPRICE\t\tQUANTITY")
    print("--------------------------------------------")
    for i in range(len(L)):
        print(L[i][0],"\t\t",L[i][1],"\t\t",L[i][2]) # prints the availabile product, price and quantity
    print("--------------------------------------------")
    return L