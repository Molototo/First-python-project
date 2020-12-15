from tabulate import tabulate
from data import *

########### invoice number generator ########
invoice_number = []
for i in range(1,999):
        invoice_number.append(i)

invoice_number.reverse()


def initial_stock(n):
    initialize_stock = {}
    for n in range(n):
        x = input('Please enter inventory ID: ')
        y = int(input('Please enter inventory unit price: '))
        z = int(input('Please enter inventory q-ty: '))
        initialize_stock[x] = [y,z]
    
    for key,value in initialize_stock.items():
        qq = key
        x = [value[0],value[1]]
            
        stoc_initial[qq]=x
        achizitie[qq]=[0,0]
        vanzare[qq]=[0]
        
        if qq not in id_s:
            id_s.append(qq)

def purch_invoice(n):
    purchasing_invoice = {}
    for n in range(n):
        x = input('Please enter new purchase ID: ')
        y = int(input('Please enter new purchase unit price: '))
        z = int(input('Please enter new purchase q-ty: '))
        purchasing_invoice[x] = [y,z]
   
    
    for key,value in purchasing_invoice.items():
        qq = key
        x = [value[0],value[1]]
        if qq in id_s:
            achizitie[qq].extend(x)
        else:
            achizitie[qq]=x
        
        if qq not in id_s:
            id_s.append(qq)
            stoc_initial[qq]=[0,0]
            vanzare[qq]=[0]



def sales_invoice(n):
    from tabulate import tabulate
    from datetime import date
    global invoice_number

    salesinvoice = {}
    printedinvoice = []
    
    for n in range(n):
        x = input('Please enter ID: ')
        while x not in id_s:
            print('Article not found, please check!')
            x = input('Please enter ID: ')
            if x in id_s:
                break
        z = int(input('Please enter q-ty: '))
        y = achizitie[x]
        w = stoc_initial[x]
        q = vanzare[x]
        if x in stoc_initial.keys():
            while z > sum(y[1::2])+sum(w[1::2])- sum(q):
                print(f'Q-ty exeedes actual stock level! Your curent stoc is {sum(y[1::2])+sum(w[1::2])- sum(q)}')
                z = int(input('Please enter q-ty: '))
                if z <= sum(y[1::2])+sum(w[1::2])- sum(q):
                    break
        else:
            while z > sum(y[1::2])- sum(q):
                print(f'Q-ty exeedes actual stock level! Your curent stoc is {sum(y[1::2])-sum(q)}')
                z = int(input('Please enter q-ty: '))
                if z <= sum(y[1::2])- sum(q):
                    break
        m = float(input('Commercial excess __%: '))
        if m < 0 or m > 100:
            while m < 0 or m > 200:
                print('Please insert a resonable procentage...')
                m = float(input('Commercial excess __%: '))
                if m > 0 and m < 200:
                    break
        
        #cogs
        a = y[0::2]
        b = y[1::2]
        c = w[0::2]
        d = w[1::2]
        
        purchstockvalue = [a[i] * b[i] for i in range(len(a))]
        initialstockvalue = [c[i] * d[i] for i in range(len(c))]
        
        u = (sum(purchstockvalue)+sum(initialstockvalue))/(sum(b)+sum(d))*(1+(m/100))
        v = (u*z)
        salesinvoice[x] = [z]
        printedinvoice.append([x,z,u,v])
    
    totalq = []
    totalv = [] 


    for i in range(len(printedinvoice)):
        totalq.append(printedinvoice[i][1])
        totalv.append(printedinvoice[i][3])

    totalqty = sum(totalq)
    totalval = sum(totalv)
    
    printedinvoice.append(['TOTAL',totalqty,'======= ',totalval])
    
    
    today = date.today()
    pop = invoice_number.pop()
    
    print('\n' * 10)
    print('{:^24s}'.format("INVOICE"))
    print("Date:", today)
    print("Invoice no:", pop)
    print('\n' * 5)
    t = tabulate(printedinvoice, headers=['ID', 'Q-ty','Unit price','Value'], tablefmt='orgtbl')
    print(t)
    print('\n' * 10)
     
    
    for key,value in salesinvoice.items():
        qq = key
        x = [value[0]]
        vanzare[qq].extend(x)

    file = open(f"Invoice_no_{pop}.txt","w+") 


    line1 = ("\n")
    line2 = ('{:^15s}'.format("INVOICE"))
    line3 = ("\n")
    line4 = ('Date:'+str(today))
    line5 = ("\n")
    line6 = ('Invoice no:'+str(pop))
    line7 = ("\n")
    line8 = (t)

    file.writelines([line1,line2,line3,line4,line5,line6,line7,line8])

class Product:
    def __init__(self,id_,price,onhandq):
        self.id_ = id_
        self.price = price
        self.onhandq = onhandq
        self.value = self.price * self.onhandq
        if self.value == 0:
            self.cogs = 0
        else:
            self.cogs = self.value / self.onhandq
        
    def __str__(self):
        return f'ID:   {self.id_}\nPrice: ${self.cogs}\nStock: {self.onhandq}\nStock Value: {self.value}'
        
    def purchase(self,pprice,add_q):
        self.onhandq += add_q
        self.pprice = pprice
        self.value += add_q*pprice
        self.cogs = self.value / self.onhandq
        
    def sale(self,remove_q):
        if self.onhandq >= remove_q:
            self.onhandq -= remove_q
            if self.onhandq == 0:
                self.value -= 0
                self.cogs = 0
            else:
                self.value -= self.cogs*remove_q 
                self.cogs = self.value / self.onhandq
    
        else:
            print(f'Error! Stock for this item is {self.onhandq}, please check')


def stock_atrib(element):
    for key,value in stoc_initial.items():
        if key == id_s[id_s.index(element)]:
            x = (value[0],value[1])
            return x

def purchases(element):
    for key,value in achizitie.items():
        if key == id_s[id_s.index(element)]:
            a = achizitie[element][1::2]
            b = achizitie[element][0::2]
            try:
                res_list = [a[i] * b[i] for i in range(len(a))] 
                cogss = sum(res_list)/sum(a)
            except:
                cogss = 0
                x = (cogss,sum(value[1::2]))
            else:
                res_list = [a[i] * b[i] for i in range(len(a))] 
                cogss = sum(res_list)/sum(a)
                x = (cogss,sum(value[1::2]))
            return x

def sales(element):
    for key,value in vanzare.items():
        if key == id_s[id_s.index(element)]:
            x = sum(value)
            return [x]

def show_stock():
    
    x = input('Please enter ID: ')
    element = x
    while element not in id_s:
        print('Article not found, please check!')
        x = input('Please enter ID: ')
        if element in id_s:
            break
            
    variabila = Product(id_s[id_s.index(element)],*stock_atrib(element))  
    
    variabila.purchase(*purchases(element))
    
    variabila.sale(*sales(element))
    
    print(variabila)

def show_total_stock():
    
    total_stock = []
    
    for id_ in id_s:
        element = id_
        variabila = Product(id_s[id_s.index(element)],*stock_atrib(element))
        variabila.purchase(*purchases(element))
        variabila.sale(*sales(element))
        
        total_stock.append([variabila.id_,variabila.onhandq,variabila.cogs,variabila.value])
    
    totalq = []
    totalv = [] 


    for i in range(len(total_stock)):
        totalq.append(total_stock[i][1])
        totalv.append(total_stock[i][3])

    totalqty = sum(totalq)
    totalval = sum(totalv)
    
    total_stock.append(['TOTAL',totalqty,'======= ',totalval])
    
    t = tabulate(total_stock, headers=['ID', 'Q-ty','Unit price','Value'], tablefmt='orgtbl')
    print('\n'*2)
    print(t)
    print('\n'*4)

def total_purchases_ids():
    

    total_purchases = []
    
    for key,value in achizitie.items():
        x = key
        y = achizitie[key]
        a = y[0::2]
        b = y[1::2]
        purchstockvalue = [a[i] * b[i] for i in range(len(a))]
        if sum(purchstockvalue) == 0:
            u = 0
            v = sum(purchstockvalue)
        else:
            u = ((sum(purchstockvalue)/sum(b)))
            v = sum(purchstockvalue)
        
        total_purchases.append([x,sum(b),u,v])
        
    
    totalq = []
    totalv = [] 

    for i in range(len(total_purchases)):
        totalq.append(total_purchases[i][1])
        totalv.append(total_purchases[i][3])

    totalqty = sum(totalq)
    totalval = sum(totalv)
    
    total_purchases.append(['TOTAL',totalqty,'======= ',totalval])
    
    t = tabulate(total_purchases, headers=['ID', 'Q-ty','Unit price','Value'], tablefmt='orgtbl')
    print('\n'*2)
    print(t)
    print('\n'*4)


def total_sold_ids():
    

    total_solditems = []
    
    for key,value in vanzare.items():
        x = key
        y = sum(vanzare[key])
       
        
        total_solditems.append([x,y])
        
    
    totalq = [] 

    for i in range(len(total_solditems)):
        totalq.append(total_solditems[i][1])

    totalqty = sum(totalq)
    
    total_solditems.append(['TOTAL',totalqty])
    
    t = tabulate(total_solditems, headers=['ID', 'Q-ty'], tablefmt='orgtbl')
    print('\n'*2)
    print(t)
    print('\n'*4)

def savedata():
    with open('data.py', 'w') as f:
        print(str('stoc_initial = ') + str(stoc_initial), file=f)
        print(str('achizitie = ') + str(achizitie), file=f)
        print(str('vanzare = ') + str(vanzare), file=f)
        print(str('id_s = ') + str(id_s), file=f)


