from minierp import *

while True:

    print('Welcome to mini ERP\n')

    if len(id_s)==0:
        print("This is a fresh start of mini ERP, you need to transfer some current inventory data \n If no current inevtory needs to be transfered, juts open the ID's with value 0 \n")
        m = input('Do you wish to continue? Y/N')
        if m[0].lower()  == 'y':
            n = int(input("Please insert the no of articles you want to register: "))
            if n > 0:
                try:
                    initial_stock(n)
                except:
                    print('Value needs to be greater than 0')
        else:
            if m[0].lower()  == 'n':
                savedata()
                print('Application closed')
                break
    else:

        print('What would you like to do next? \n\n-> Register a purchase       -P- \n-> Issue a sale invoice      -S- \n-> Vizualise stock inventory -I-  \n-> Reports -R-')



        x = input('Insert your choice or x to exit: ')
        if x[0].lower == 'x':
            savedata()
            print('Application closed')
            break
        


        if x[0].lower() == 'p':
            n = int(input("Please insert the no of articles you want to register: "))

            if n > 0:
                purch_invoice(n)
            else:
                m = input('Number needs to be >0! Do you wish to exit? (insert Y or N)')
                if m[0].lower()  == 'n':
                    n = int(input("Please insert the no of articles you want to register: "))
                    if n > 0:
                        purch_invoice(n)
                else:
                    if m[0].lower  == 'y':
                        break



        elif x[0].lower() == 's':
            n = int(input("Please insert the no of articles in the invoice: "))

            if n > 0:
                sales_invoice(n)
            else:
                m = input('Number needs to be >0! Do you wish to exit? (insert Y or N)')
                if m[0].lower()  == 'n':
                    n = int(input("Please insert the no of articles you invoice: "))
                    if n > 0:
                        sales_invoice(n)
                else:
                    if m[0].lower  == 'y':
                        break


        elif x[0].lower() == 'i':
            print("Do you want to interogate a single ID or the whole stock?")
            nn = input("(Q - for single interogation) (W - for whole stock)")
            if nn[0].lower() == 'q':
                show_stock()
            elif nn[0].lower() == 'w':
                show_total_stock()

            else:
                print('Please select something from the above options')
        elif x[0].lower() == 'r':
            print("Chose report:")
            nn = input("(P - for purchase report) (S - total sales report)")
            if nn[0].lower() == 'p':
                total_purchases_ids()
            elif nn[0].lower() == 's':
                total_sold_ids()

            else:
                print('Please select something from the above options')
        else:
            if x[0].lower() == 'x':
                savedata()
                print('Application closed')
                break
