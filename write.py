'''
Module name: write
Function name: over_write
Overview of the function:
1) Opens the products.csv file
2) Shows the remaining stock with product name in terminal
3) Over writes the csv file after purchase
'''
def over_write(List,Dictionary): #an over_write function 
    L=List #assign list with variable name 'L'
    d=Dictionary #assign Dictionary with variable name 'd'
    '''
    Update quantity of product after customer purchased some quantity of any product.
    And print remaining stock products.
    '''
    for keys in d.keys():
        if keys=="CROCIN":
            L[0][2]=str(int(L[0][2])-d['CROCIN']) 
        elif keys=="RABIPUR":
            L[1][2]=str(int(L[1][2])-d['RABIPUR'])
        else:
            L[2][2]=str(int(L[2][2])-d['PARACETAMOL']) 
    print("\nRemaining Stock Products:\n",L)
        
    files=open("products.csv","w")  #opens stock file (products.csv) file in write mode.     
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")         
    files.close()
    return