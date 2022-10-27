import random
import mysql.connector


a=mysql.connector.connect(host='localhost',user='root',password=' ', database='shayali')   
b=a.cursor()

print("================================================================================")
x="Project: Random Password Generator".upper()
print(x.center(70))
print("================================================================================")

Option=(
input("\n\t\t\Select Following Option\n\n 1:GENERATE PASSWORD\n 2:SHOW GENERATED PASSWORD:\n 3:UPDATE PASSWORD\t").upper())

try:

    if (Option=='1' or Option=='GENERATE PASSWORD'):


        def passgen():

            a=mysql.connector.connect(host='localhost',user='root',password='', database='shayali')   
            b=a.cursor()
            #print(a)
            
            #b.execute("create table Password(ID INTEGER PRIMARY KEY AUTO_INCREMENT, Name varchar(20),Password_Type varchar(20), App varchar(10),Password varchar(32)) ")
            #a.commit()


            if (Choice=='Poor' or Choice=='1'):
                for x in range(0,2):
                    password=random.choicepoor+random.choice(small)
            
           
                for y in range(pass_len-2):
                    password=password+random.choice(poor+small)
                
            
                print("\nPassword Has Been Generated Successfully:  ", password)
                

            
            elif (Choice=='Medium' or Choice=='2'):
                for x in range(0,3):
                    password=random.choice(poor)+random.choice(small)+random.choice(cap)
            
           
                for y in range(pass_len-3):
                    password=password+random.choice(poor+small+cap)
                
            
                print("\nPassword Has Been Generated Successfully:  ",password)


            elif (Choice=='Strong' or Choice=='3'):
                for x in range(0,4):
                    password=random.choice(poor)+random.choice(small)+random.choice(cap)+random.choice(sym)
            
           
                for y in range(pass_len-4):
                    password=password+random.choice(poor+small+cap+sym)
                
            
                print("\nPassword Has Been Generated Successfully:  ",password)

            else:
                print("Please Enter Correct Choice")
                
                
            

            
            mySql_insert_query = """INSERT INTO password(Name,Password_Type,App,Password) 
                                        VALUES (%s, %s, %s,%s) """
            record = (Name1,Choice,App,password)
            b.execute(mySql_insert_query, record)

            d=b.execute("update password set Password_Type=replace(Password_Type,'1','Poor')")
            d=b.execute("update password set Password_Type=replace(Password_Type,'2','Avarage')")
            d=b.execute("update password set Password_Type=replace(Password_Type,'3','Strong')")
                        
            a.commit()
            

            
        

        Name1=input("\nEnter Your name: ")
        App=input("Enter Your Application Name For Password: ")

        Choice=(input("\n\t\t\tSelect Password Type:\n 1.Poor\n 2.Avarage\n 3.Strong \t").capitalize())
        #Choice.capitalize()


        pass_len=int(input("\enter length of password: "))
        


        poor=['1','2','3','4','5','6','7','8','9','0']

        small=['a','b','c','d','e','f','g','h','i','j','k','l',
             'm','n','o','p','q','r','s','t','u','v','w','y','z']   

        cap=['A','B','C','D','E','F','G','H','I','J','K','L',
                   'M','N','O','P','Q','R','S','T','U','V','W','Y','Z']


        sym = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|',
                   '~', '>', '*', '<']

        passgen()

        x=input("\nDo you want add one more password: (Y/N): ")
        if (x=='y' or x=='Y'):
            passgen()

        
    elif (Option=='2' or Option=='SHOW GENRATED PASSWORD'):

        
        def SHOW_GENRATED_PASSWORD():
            d=b.execute("select * from password where Name=%s AND App=%s",(name,app))
            for i in b:
                print(i)




        name=input("\nEnter Your Name: ")
        app=input("\nEnter Password Generate App Name: ")

        SHOW_GENRATED_PASSWORD()

    elif (Option=='3' or Option=='UPDATE PASSWORD'):
        def UPDATE_PASSWORD():
            d=b.execute("update password set Password=%s where ID=%s",(new_pass,user))
            a.commit()

        user=int(input("Enter Your ID: "))
        new_pass=input("Enter New Password: ")
        UPDATE_PASSWORD()

    else:
        print("\nPlease Enter Correct Option")


finally:
    print("\n\t\t\tThank You For Visiting Please Come Again")

