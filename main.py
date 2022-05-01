from Database import *
from Qr_code import *

mycursor.execute("CREATE DATABASE IF NOT EXISTS BusFair")
mycursor.execute("USE BusFair")


def tnx():
    print("\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t#########  Thanks For Using Our Service"
          " !!!  #########\t\t\t\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


def busdata():
    mycursor.execute("CREATE TABLE IF NOT EXISTS `207` (Place VARCHAR(50) PRIMARY KEY, Distance double);")
    mycursor.execute("SELECT COUNT(Place) FROM `207`;")
    result = mycursor.fetchall()
    if result[0][0] == 0:
        sql_stmnt = "INSERT INTO `207`(place , distance) VALUES(%s, %s)"
        values = (
            ("Tongi", 0.0),
            ("Azampur", 7.4),
            ("Mohakhali", 19.0),
            ("Farmgate", 21.5),
            ("Manik Mia Ave", 23.3),
            ("City College", 25.4),
            ("Nilkhet", 26.5),
            ("Dhakeshwari Mandir", 28.0))

        mycursor.executemany(sql_stmnt, values)
        dbcnct.commit()

    mycursor.execute("CREATE TABLE IF NOT EXISTS `176` (Place VARCHAR(50) PRIMARY KEY, Distance double);")
    mycursor.execute("SELECT COUNT(Place) FROM `176`;")
    result = mycursor.fetchall()
    if result[0][0] == 0:
        sql_stmnt = "INSERT INTO `176`(place , distance) VALUES(%s, %s)"
        values = (
            ("Pallabi Duaripara", 0.0),
            ("Mirpur 11", 2.4),
            ("Mirpur 10", 3.3),
            ("Mirpur 1", 5.2),
            ("Ansar Camp", 6.1),
            ("New Market", 14.8),
            ("Atimkhana", 15.1),
            ("Dhakeshshori Mondir", 15.5))

        mycursor.executemany(sql_stmnt, values)
        dbcnct.commit()

    mycursor.execute("CREATE TABLE IF NOT EXISTS `120` (Place VARCHAR(50) PRIMARY KEY, Distance double);")
    mycursor.execute("SELECT COUNT(Place) FROM `120`;")
    result = mycursor.fetchall()
    if result[0][0] == 0:
        sql_stmnt = "INSERT INTO `120`(place , distance) VALUES(%s, %s)"
        values = (
            ("Kalshi Mirpur", 0.0),
            ("Mirpur-10", 3.0),
            ("Mirpur-1", 4.9),
            ("Darussalam", 6.9),
            ("Collage Gate", 9.5),
            ("Asad Gate", 10.2),
            ("Mohammadpur Town Hall", 10.8),
            ("Sat Mosque", 11.5),
            ("Shankar", 12.4),
            ("Dhanmondi-15", 13.4),
            ("Zigatola", 14.0),
            ("Science Lab", 15.1),
            ("Shahbag", 16.3),
            ("Press Club", 17.9),
            ("Gulistan", 19.0),
            ("Notre Dame College", 20.8))

        mycursor.executemany(sql_stmnt, values)
        dbcnct.commit()

    mycursor.execute("CREATE TABLE IF NOT EXISTS `104` (Place VARCHAR(50) PRIMARY KEY, Distance double);")
    mycursor.execute("SELECT COUNT(Place) FROM `104`;")
    result = mycursor.fetchall()
    if result[0][0] == 0:
        sql_stmnt = "INSERT INTO `104`(place , distance) VALUES(%s, %s)"
        values = (
            ("Pallabi", 0.0),
            ("Mirpur 11", 1.4),
            ("Mirpur 10", 2.3),
            ("Mirpur 2", 2.9),
            ("Mirpur 1", 4.2),
            ("Ansar Camp", 5.1),
            ("Technical", 6.3),
            ("Shishu Mela", 7.6),
            ("Asad Gate", 9.6),
            ("Sukrabad", 10.3),
            ("Kalabagan", 11.2),
            ("Science Lab", 12.3),
            ("New Market", 13.1),
            ("Katabon", 15.7),
            ("Shahbag", 16.7),
            ("High-Court", 17.9),
            ("Puraton Railway Hospital", 18.1),
            ("Bongobondhu Ave", 18.7))

        mycursor.executemany(sql_stmnt, values)
        dbcnct.commit()

    mycursor.execute("CREATE TABLE IF NOT EXISTS `436` (Place VARCHAR(50) PRIMARY KEY, Distance double);")
    mycursor.execute("SELECT COUNT(Place) FROM `436`;")
    result = mycursor.fetchall()
    if result[0][0] == 0:
        sql_stmnt = "INSERT INTO `436`(place , distance) VALUES(%s, %s)"
        values = (
            ("Sadarghat Victoria", 0.0),
            ("Bongobondhu Ave", 2.6),
            ("Kakrail", 4.0),
            ("Malibagh", 4.7),
            ("Mouchak", 5.1),
            ("Rampura", 7.9),
            ("Kuril Bissoroad", 14.0),
            ("Airport", 18.6),
            ("Abdullahpur", 22.1),
            ("Dhour", 27.7),
            ("Zirabo", 33.0),
            ("Asulia (Fantasy Kingdom)", 37.3),
            ("Baipail", 39.8))

        mycursor.executemany(sql_stmnt, values)
        dbcnct.commit()

    mycursor.execute("CREATE TABLE IF NOT EXISTS `229` (Place VARCHAR(50) PRIMARY KEY, Distance double);")
    mycursor.execute("SELECT COUNT(Place) FROM `229`;")
    result = mycursor.fetchall()
    if result[0][0] == 0:
        sql_stmnt = "INSERT INTO `229`(place , distance) VALUES(%s, %s)"
        values = (
            ("Saydabad", 0.0),
            ("Jatrabari", 0.8),
            ("Postogola", 3.1),
            ("Shyampur", 3.8),
            ("Pagla", 6.8),
            ("Ponchoboti", 10.4),
            ("Narayanganj", 15.0))

        mycursor.executemany(sql_stmnt, values)
        dbcnct.commit()

    mycursor.execute("CREATE TABLE IF NOT EXISTS `225` (Place VARCHAR(50) PRIMARY KEY, Distance double);")
    mycursor.execute("SELECT COUNT(Place) FROM `225`;")
    result = mycursor.fetchall()
    if result[0][0] == 0:
        sql_stmnt = "INSERT INTO `225`(place , distance) VALUES(%s, %s)"
        values = (
            ("Saydabad", 0.0),
            ("Malibagh", 4.0),
            ("Satrasta", 8.0),
            ("Mohakhali", 12.0),
            ("Airport", 20.0),
            ("Tongi Bazar", 24.0),
            ("Cheragh Ali", 27.0),
            ("Board Bazar", 31.0),
            ("Chowrasta", 37.0),
            ("Gazipur", 42.0))

        mycursor.executemany(sql_stmnt, values)
        dbcnct.commit()

    mycursor.execute("CREATE TABLE IF NOT EXISTS `273` (Place VARCHAR(50) PRIMARY KEY, Distance double);")
    mycursor.execute("SELECT COUNT(Place) FROM `273`;")
    result = mycursor.fetchall()
    if result[0][0] == 0:
        sql_stmnt = "INSERT INTO `273`(place , distance) VALUES(%s, %s)"
        values = (
            ("Gabtoli Bridge", 0.0),
            ("Tecnical", 1.8),
            ("Mirpur 1", 3.6),
            ("Mirpur 2", 4.9),
            ("Mirpur 10", 5.4),
            ("Mirpur 11", 6.8),
            ("Purobi", 6.9),
            ("Kalshi", 9.9),
            ("E.C.B.", 11.7),
            ("Kakoli", 15.6),
            ("Mohakhali Amtoli", 17.1),
            ("Gulshan 1", 18.9),
            ("Badda Link Road", 21.4),
            ("Meradia Bazar", 26.5))

        mycursor.executemany(sql_stmnt, values)
        dbcnct.commit()

    mycursor.execute("CREATE TABLE IF NOT EXISTS `131` (Place VARCHAR(50) PRIMARY KEY, Distance double);")
    mycursor.execute("SELECT COUNT(Place) FROM `131`;")
    result = mycursor.fetchall()
    if result[0][0] == 0:
        sql_stmnt = "INSERT INTO `131`(place , distance) VALUES(%s, %s)"
        values = (
            ("Chiriyakhana", 0.0),
            ("Mirpur 1", 1.8),
            ("Darussalam", 3.8),
            ("Shyamoli", 5.8),
            ("Asad Gate", 7.2),
            ("Farmgate", 9.0),
            ("Press Club", 12.6),
            ("Gulistan", 13.7),
            ("Victoria Park", 16.0))

        mycursor.executemany(sql_stmnt, values)
        dbcnct.commit()

    mycursor.execute("CREATE TABLE IF NOT EXISTS `301` (Place VARCHAR(50) PRIMARY KEY, Distance double);")
    mycursor.execute("SELECT COUNT(Place) FROM `301`;")
    result = mycursor.fetchall()
    if result[0][0] == 0:
        sql_stmnt = "INSERT INTO `301`(place , distance) VALUES(%s, %s)"
        values = (
            ("Japan Garden City", 0.0),
            ("Shyamoli Ring Road", 1.5),
            ("Agargaon", 3.5),
            ("ShewraPara", 5.2),
            ("Mirpur 10", 7.1),
            ("Kalshi", 11.8),
            ("E.C.B.", 13.6),
            ("Airport", 20.3),
            ("Abdullahpur", 24.0),
            ("Dhour", 29.5))

        mycursor.executemany(sql_stmnt, values)
        dbcnct.commit()


busdata()


def FairCalculetor():

    mydata = scanner()
    busname = mydata[0]
    busID = mydata[1]
    time.sleep(2)


    mycursor.execute("SELECT * FROM `%s` ORDER BY place;" % busID)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t **** %s **** \t\n\n" % busname)
    rest = mycursor.fetchall()
    j = 1
    for i in rest:
        print(j, ". ", i[0])
        j += 1

    print("\n\n\t\t\t\t** Input your journey start and end place code. **\t\t")
    departure = input("\n\t\t\tDeparture:  ")
    destination = input("\n\t\t\tDestination: ")

    j = 1
    for i in rest:
        if j == int(departure):
            global start, end
            start = i[0]
        if j == int(destination):
            end = i[0]
        j += 1

    mycursor.execute(" SELECT ABS(Distance - (SELECT Distance FROM `%s` WHERE Place = '%s')) AS Distances, "
                     "ABS(round((SELECT Distance - (SELECT Distance FROM `%s` WHERE place = '%s') "
                     "FROM `%s` WHERE place = '%s')*2.15)) AS TK FROM `%s` "
                     "WHERE place = '%s'; " % (busID, start, busID, start, busID, end, busID, end))

    for i in mycursor:
        return i


def islogin():
    f = 3
    while f != 0:
        uname = input("\n\n\t\tUsername: ")
        password = input("\n\t\tpassword: ")

        mycursor.execute("USE BusFair")

        mycursor.execute("select * from user where username = '%s' and pass = '%s';" % (uname, password))

        result = mycursor.fetchone()

        if (result is None):
            f -= 1
            print("\n\t\tUsername or Password doesn't Match...!!!\n\t\t\"\"  Remaining %i times try  \"\"" % f)
            print(
                "\n\t\t\t\t\t\t\t\t\t\t\t\tForget Password...?\n\n\t\t\t\t\t\t\t\t\t\t\t Press '1' for help "
                "\n\t\t\t\t\t\t\t\t\t\t\t\t\tOR \t\n\t\t\t\t\t\t\t\t\t\t\t Press '0' for Try Again.")
            fpass = int(input("\n\t\t\t=>> "))
            if fpass == 0 and f == 0:
                print("\n\t\t\t\t\t\t\t\t\tYou have no remaining to TRY !!! ")
            elif fpass == 1:
                uname = input("\n\n\t\tUsername: ")
                mycursor.execute("select * from user where username = '%s';" % uname)
                forget = mycursor.fetchone()
                if forget[0] == uname:
                    dob = input("\n\t\tDate Of Birth(y-m-d): ")
                    phn = input("\t\tPhone: ")
                    mycursor.execute("select DOB, Phone from passenger where username = '%s' and DOB = '%s' "
                                     "and Phone = '%s' ;" % (uname, dob, phn))
                    newfetch = mycursor.fetchone()
                    if newfetch is None:
                        print("\n\t\t\tWrong DOB or Phone.")

                    else:
                        print("\n\t\t\tAn OTP sent to your mobile Number")
                        otp = int(input("\n\t\tInput your OTP: "))
                        if otp == 123456:
                            print("Your password is: ", forget[1])
                        else:
                            print("OTP doesn't match")

        else:
            print("\n\n\n\n\t\t\t\t\t\t\t***Login Successfully.***\t\t\n")
            f = 0
            return True, uname

    return False, uname


def addmoney(username):
    mycursor.execute("SELECT * FROM `payment` WHERE username = '%s';" % username)
    result = mycursor.fetchone()

    balance = result[1]

    taka = int(input("\n\n\n\t\tAmount: "))
    taka = taka + result[1]
    bkash = input("\n\t\tYour Bkash account number: ")
    print("\n\n\n\t\t\t\t\tAn OTP send to your phone: ")
    otp = int(input("\n\n\t\tOTP: "))
    if otp == 123456:
        passw = input("\n\n\t\tInput your Bkash account Password: ")
        mycursor.execute("UPDATE `payment` SET balance = %s WHERE username = '%s'" % (taka, username))
        print("\n\n\t\t\t\t\t**** Balance Added Successfully ****\t\t\n\n")
        dbcnct.commit()
    dbcnct.commit()
    time.sleep(3)


def payment(username, pay):
    mycursor.execute("SELECT * FROM `payment` WHERE username = '%s';" % username)
    result = mycursor.fetchone()

    balance = result[1]

    mycursor.execute("SELECT profession FROM `passenger` WHERE username = '%s';" % username)

    ans = mycursor.fetchone()
    if ans[0].lower() == "student":
        pay = round(pay / 2)
        print("\n\n\t\t\t\t For Student you pay ", pay, " TK")


    print("\n\n\t\tYour Current Balance is : ", balance)
    if balance >= pay:
        new = balance-pay
        mycursor.execute("UPDATE `payment` SET balance = %s WHERE username = '%s'" % (new, username))
        print("\n\n\n\t\t\t\t\t\t\t\t\t\t****  Payment Complete **** \t\t\t\n\n")
        print("\n\t\tYour new balance is : ", new)
        dbcnct.commit()

        if new < 10:
            print("\n\n\t\t\t\t\t\tYour Balance is less then 10 TK. Please recharge before your next travel.\n\t\t"
                  "\t\t\t\t\t\t\t\t\t\tHappy Travel")

    else:
        print("\n\n\t\tYour balance is insufficient. Please recharge from your nearest point or through Mobile Banking")

        c = int(input("\n\n\n\t\t\t\tFor add money press '1' ELSE press 0\t\t\n\n\t\t\t\t => "))
        if c == 1:
            addmoney(username)
            payment(username, pay)

    print("\n\n\t\t\t\t\t\t\t\t\t\t \"\"\" RETURNING MAIN MENU \"\"\"\t\n\n")
    time.sleep(4)
    dbcnct.commit()


def profile(username):
    mycursor.execute("SELECT name FROM passenger WHERE username = '%s'" % username)
    result = mycursor.fetchone()
    print("\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", result[0])
    mycursor.execute("SELECT balance FROM payment WHERE username = '%s'" % username)
    result = mycursor.fetchone()
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Balance: ", result[0], " TK")

    print("\n\t\t\t\t\t\t\t****** JATRIK ******\t\t\n\n\n")
    print("\t\t\t1. View Profile \n\n")
    print("\t\t\t2. Change Password \n\n")
    print("\t\t\t3. Change Mobile Number \n\n")
    print("\t\t\t4. Change Address \n\n")
    print("\t\t\t5. Menu \n\n")

    choice = int(input("\n\t\t\t\t ==> "))

    if choice == 1:
        mycursor.execute("SELECT * FROM passenger WHERE username = '%s'" % username)
        result = mycursor.fetchone()
        print("\n\n\n\n\n\t\t\t\t\t\t\t****** JATRIK ******\t\t")
        print("\n\t\t\t\t\t\t\t****** Profile ******\t\t")
        print("\n\n\n\t\t Name : ", result[1])
        print("\n\t\t Address : ", result[3])
        print("\n\t\t Phone : ", result[2])
        print("\n\t\t Blood Group : ", result[4])
        print("\n\t\t Date of Birth : ", result[5])
        print("\n\t\t Profession : ", result[6])
        print("\n\t\t NID : ", result[7])
        print("\n\t")

    elif choice == 2:
        old = input("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t Your old Password: ")
        mycursor.execute("SELECT pass FROM user WHERE username = '%s'" % username)
        result = mycursor.fetchone()
        if old == result[0]:
            new = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t Your new Password: ")
            confirm = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t Confirm Your new Password: ")
            if new == confirm:
                mycursor.execute("UPDATE `user` SET pass = '%s' WHERE username = '%s'" % (confirm, username))
                print("\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tYour Password has been changed successfully. ")
                dbcnct.commit()
                time.sleep(2)
            else:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t *** Your password doesn't match !!! ***")
        else:
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t *** Your current password is incorrect !!! ***")

    elif choice == 3:
        old = input("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t Your old Mobile Number: ")
        mycursor.execute("SELECT Phone FROM passenger WHERE username = '%s'" % username)
        result = mycursor.fetchone()
        print(result[0])
        if old == result[0]:
            new = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t Your new Mobile Number: ")
            confirm = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t Confirm Your New Mobile Number: ")
            if new == confirm:
                mycursor.execute("UPDATE `passenger` SET phone = '%s' WHERE username = '%s'" % (confirm, username))
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tYour Mobile Number has been changed successfully. \n\n\n\n\n\n\n\n\n\n\n")
                dbcnct.commit()
                time.sleep(2)
            else:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t *** Your Mobile Number doesn't match !!! ***")
        else:
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t *** Your Old Mobile Number is incorrect !!! ***")

    elif choice == 4:
        print("Construct this")

    elif choice == 5:
        menu()

    print("\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t Press '0' for BACK and '1' for MAIN MENU")
    choice = int(input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ==> "))
    if choice == 0:
        profile(username)
    dbcnct.commit()


def menu():
    mycursor.execute("SELECT name FROM passenger WHERE username = '%s'" % login[1])
    result = mycursor.fetchone()
    print("\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", result[0])
    mycursor.execute("SELECT balance FROM payment WHERE username = '%s'" % login[1])
    result = mycursor.fetchone()
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Balance: ", result[0], " TK")

    print("\n\t\t\t\t\t\t\t****** JATRIK ******\t\t\n\n\n")
    print("\t\t\t1. PAYMENT \n\n")
    print("\t\t\t2. PROFILE \n\n")
    print("\t\t\t3. ADD MONEY \n\n")
    print("\t\t\t4. Bus Schedule \n\n")
    print("\t\t\t5. LOGOUT \n\n")

    choice = int(input("\n\t\t\t\t ==> "))

    if choice == 1:
        bfair = FairCalculetor()
        distant = bfair[0]
        fair = bfair[1]
        print("Total Distance is = ", distant)
        if fair < 10:
            print("Fair is = ", 10)
            fair = 10
        else:
            print("Fair is = ", fair)

        c = int(input("\n\n\t\t\t\t\t *****  Press '1' To Confirm Payment **** \t\t\t\n\n\t\t\t\t\t=>  "))
        if c == 1:
            payment(login[1], fair)
        else:
            print("You cancel your payment !!! ")
            menu()

    if choice == 2:
        profile(login[1])

    if choice == 3:
        addmoney(login[1])
        menu()

    if choice == 4:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t This section is under Maintenance. "
              "We are extremely Sorry !!! \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n ")
        time.sleep(2)

    if choice == 5:
        tnx()
        exit()
    else:
        menu()


# Main Function write here

print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ****** JATRIK ******\t\t\n\n\n")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t 1. Login\t\n")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t 2. Registration\n\n")

choose = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   =>  "))

if choose == 1:
    login = islogin()
    if login[0]:
        menu()

    dbcnct.commit()

elif choose == 2:
    f = 1
    while f == 1:
        uname = input("\n\n\t\tEnter a Unique Username: ")
        password = input("\n\t\tEnter a password: ")

        mycursor.execute("CREATE DATABASE IF NOT EXISTS BusFair")

        mycursor.execute("USE BusFair")
        mycursor.execute("CREATE TABLE IF NOT EXISTS user(username varchar(100) UNIQUE , PRIMARY KEY(username),"
                         "pass varchar(100) NOT NULL );")

        mycursor.execute("SELECT username FROM user WHERE username = '%s'" % uname)
        result = mycursor.fetchone()

        if result is None :
            sql_stmnt = "Insert into user(username, pass) values(%s, %s)"
            values = (uname, password)
            mycursor.execute(sql_stmnt, values)
            f = 0
            break
        else:
            print("\n\t\t\"\"\"Username Already Use ! Try Another One \"\"\" ")
    dbcnct.commit()
    mycursor.execute("CREATE TABLE IF NOT EXISTS passenger(username varchar(100) UNIQUE, Name varchar(100) NOT NULL, "
                     "Phone varchar(15) NOT NULL UNIQUE, Address varchar(200), Blood varchar(5) NOT NULL, DOB date NOT NULL, "
                     "Profession varchar(100) NOT NULL, NID varchar(100) NOT NULL , PRIMARY KEY(NID), "
                     "KEY `FK_username`(username), CONSTRAINT `FK_username` FOREIGN KEY(username) "
                     "REFERENCES `user`(username) ON DELETE CASCADE ON UPDATE CASCADE);")
    Name = input("\n\n\t\tYour Name:\t")
    Phone = input("\t\tMobile Number:\t")
    Address = input("\t\tAddress:\t")
    DOB = input("\t\tDate of Birth(y-m-d):\t")
    Blood = input("\t\tBlood Group: ")
    Profession = input("\t\tProfession:\t")
    NID = input("\t\tNID/Birth Certificate:\t")

    sql_stmnt = "Insert into passenger(username, Name, Phone, Address, Blood, Profession, NID, DOB) " \
                "values(%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (uname, Name, Phone, Address, Blood, Profession, NID, DOB)
    mycursor.execute(sql_stmnt, values)

    # mycursor.execute("select * from passenger;")
    # for i in mycursor:
    #     print(i)

    dbcnct.commit()

    mycursor.execute("CREATE TABLE IF NOT EXISTS payment(username varchar(100) UNIQUE NOT NULL, Balance double "
                     "NOT NULL DEFAULT 0.0, KEY `FK_payment`(username), CONSTRAINT `FK_payment` FOREIGN KEY(username) "
                     "REFERENCES `user`(username) ON DELETE CASCADE ON UPDATE CASCADE) ")

    sql_stmnt = "INSERT INTO `payment`(username, balance) values( %s, %s)"
    values = (uname, 0.00)
    mycursor.execute(sql_stmnt, values)

    print("Registration Complete")
    dbcnct.commit()


dbcnct.commit()