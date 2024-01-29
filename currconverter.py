#A Python Program for Currency Conversion

'''This program is made with the most basic concepts of python for converting a particular country's currency into another.''' 


import sys

#created an empty dictionary for storing currency name and exchange rates into key-value format.
data = {}

#selected a file to fetch data about currency conversion.
with open('currexchangedata.txt','r') as f: 

    
    def converter1():
        
        '''creating a function to convert INR currency into foreign currency'''

         #created a loop to access every line.
        for lines in f:
            #created a list of the above imported text file using .split() method.
            a = lines.split(' \t')          
            #print(a)

            #added the currency name as key and the value of 1INR in that currency as value in a dictionary.
            data[a[0]] = a[1]
        amount = int(input('Enter INR Amount to be converted into desired foreign currency : '))
        print('Available options for the name of foreign currencies you want to convert INR into :\n')
        [print(i) for i in data]
        currency  = input('Please enter name of Currency : ')
        print('{} INR in {} ='.format(amount,currency),amount*float(data[currency]))


    def converter2():
        
        '''creating a function to convert foreign currency into INR'''
        
        for lines in f:                     
            a = lines.split(' \t')
            
            #added the currency name as key and the value of 1 unit currency in INR as value in a dictionary.
            data[a[0]] = a[2]               
        amount = int(input('Enter Amount to be converted into INR : '))
        print('Available options for the name of Currency you want convert into INR :\n')
        [print(i ) for i in data]           
        currency  = input('Please enter name of Currency : ')
        print('{} {} in INR ='.format(amount,currency),amount*float(data[currency]))

    def converter3():
        
        '''function for converting two foreign currencies as per user's choice'''
        
        for lines in f:
            a = lines.split(' \t')          
            data[a[0]] = a[1]
            data[a[0]] = a[2]
        print('Available options for the name of Currency you want convert :')
        [print(i ) for i in data]   
        curr1 = input('Enter the input currency : ')
        amount = int(input('Enter the Amount to be converted : '))
        halfcon = amount * float(data[curr1])
        #print(halfcon)
        curr2 = input('Enter name of the currency to be converted into : ')
        print(float(halfcon)/float(data[curr2]))
        
                   
        
    choice =input("""Choose Conversion Option
1)INR-Foreign
2)Foreign-INR
3)Foreign-Foreign
4)Exit.
Enter your choice : """)

    if choice == '1':
        converter1()
    elif choice == '2':
        converter2()
    elif choice == '3':
        converter3()
    else:
        sys.exit()
        
    
        
        
        
    

        
        


