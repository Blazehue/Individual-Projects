import mysql.connector
print("Welcome to Sales Database Management System")
mydb=mysql.connector.connect(host="localhost",user="root",password="1234")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists salesdatabase_management")
mycursor.execute("use salesdatabase_management")
mycursor.execute("create table if not exists login(User varchar(25) not null,Password varchar(25) not null)")
mycursor.execute("create table if not exists purchase(Date date not null,name varchar(20) not null,pcode int not null,amount int not null)")
mycursor.execute("create table if not exists stock(pcode int not null,pname varchar(20) not null,quantity int not null,Price int not null)")
mydb.commit()
c=0
mycursor.execute("select * from login")
for i in mycursor:
    c+=1
if(c==0):
    mycursor.execute("insert into login values('User','rp')")
    mydb.commit()
while True:
    print("""1.Admin
2.Customer
3.Exit
""")
    ch=int(input("Enter your choice from above:"))
    if(ch==1):
        passs=input("Enter password:")
        mycursor.execute("select * from login")
        for i in mycursor:
            User,Password=i
        if(passs==Password):
            print("Welcome!")
            loop2='y'
            while(loop2=='y' or loop2=='Y'):
                print("""
            1.Add New Item
            2.Update Price
            3.Delete Product
            4.Display every Item
            5.Change Password
            6.Logout
""")
                ch=int(input("Enter your choice:"))
                if(ch==1):
                    loop='y'
                    while(loop=='y' or loop=='Y'):
                        pcode=int(input("Enter the product code:"))
                        pname=input("Enter the product name:")
                        quantity=int(input("Enter the product quantity"))
                        price=int(input("Enter product price:"))
                        mycursor.execute("insert into stock values('"+str(pcode)+"','"+pname+"','"+str(quantity)+"','"+str(price)+"')")
                        mydb.commit
                        print("Record Success")
                        loop=input("Do you want to enter more products(y/n)?")
                    loop2=input("Do you want to continue editing stocks(y/n)?")
                elif(ch==2):
                    loop2='y'
                    while(loop2=='y' or loop2=='Y'):
                        pcode=int(input("Enter product code:"))
                        new_price=int(input("Enter new price:"))
                        mycursor.execute("update stock set price='"+str(new_price)+"'where pcode='"+str(pcode)+"'")
                        mydb.commit()
                        loop2=input("Do you want to change price of any other item(y/n):")
                elif(ch==3):
                    loop='y'
                    while(loop=='y' or loop=='Y'):
                        pcode=int(input("Enter product code:"))
                        mycursor.execute("delete from stock where pcode='"+str(pcode)+"'")
                        mydb.commit()
                        loop=input("Do you want to delete any other data(y/n):")
                        loop2=input("Do you want to continue editing stock(y/n):")
                elif(ch==4):
                    mycursor.execute("select * from stock")
                    print("pcode || pname || quantity || price")
                    for i in mycursor:
                        t_code,t_name,t_quan,t_price=i
                        print(f"{t_code} || {t_name} || {t_quan} || {t_price}")
                elif(ch==5):
                    old_passs=input("Enter old password")
                    mycursor.execute("select * from login")
                    for i in mycursor:
                        User,Password=i
                    if(old_passs==Password):
                        new_passs=input("Enter the new password:")
                        mycursor.execute("update login set password='"+new_passs+"'")
                        mydb.commit()
                elif(ch==6):
                    break
                else:
                    print("wrong password entered")
#Customer Area
    elif(ch==2):
        print("""
1.Product Bucket
2.Payment of Product
3.Show available products
4.Go Back
""")
        ch2=int(input("Enter your choice:"))
        if(ch2==1):
            name=input("Enter your name:")
            pcode=int(input("Enter product code:"))
            quantity=int(input("Enter product quantity:"))
            mycursor.execute("select * from stock where pcode='"+str(pcode)+"'")
            for i in mycursor:
                t_code,t_name,t_quan,t_price=i
                amount=t_price*quantity
                net_quan=t_quan-quantity
                mycursor.execute("update stock set quantity='"+str(net_quan)+"' where pcode='"+str(pcode)+"'")
                mycursor.execute("insert into purchase values(now(),'"+name+"','"+str(pcode)+"','"+str(amount)+"'")
                mydb.commit()
        elif(ch2==2):
            quantity=int(input("Enter product quantity:"))
            price=int(input("Enter the price:"))
            amount=price*quantity
            print(f"amount to be paid is given as :{amount}")
        elif(ch2==3):
            print("CODE || NAME || PRICE")
            mycursor.execute("select * from stock")
            for i in mycursor:
                t_code,t_name,t_quan,t_price=i
                print(f"{t_code} || {t_name} || {t_price}")
        elif(ch==4):
            break
    elif(ch==3):
        break
                
                
        
           
                
                    
                    
                    
                
                        
               
                
            
                    
    
                
            
