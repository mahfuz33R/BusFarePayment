from tkinter import *


def getvariable(event):
    print("Submitting form....")
    print(f"{ namevalue.get(),phonevalue.get(),Gendervalue.get(),emailvalue.get(),checkvalue.get()}")

    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get(),phonevalue.get(),Gendervalue.get(),emailvalue.get(),checkvalue.get()}\n")



root = Tk()


width = 400
hight = 600

root.geometry(f"{width}x{hight}")
root.minsize(width, hight)
root.maxsize(width, hight)

root.title("Registration Form")

Label(root, text="Welcome to JATRIK", font="comicsansms 20 bold",fg="black", bg="light pink", pady=15).grid(row=0, column=3)

name = Label(root, text="Name:", fg="blue")
phone = Label(root, text="Phone:",fg="blue")
date_of_birth = Label(root, text="Date Of Birth",fg="blue")
Address = Label(root, text="Address:", fg="blue")
Pro = Label(root, text="Profession:", fg="blue")

name.grid(row=1, column=2)
phone.grid(row=2,column=2)
date_of_birth.grid(row=3, column=2)
Address.grid(row=4, column=2)
Pro.grid(row=5, column=2)

namevalue =StringVar()
phonevalue =StringVar()
birthvalue = StringVar()
Gendervalue = StringVar()
emailvalue = StringVar()
checkvalue = IntVar()

nameentry = Entry(root, textvariable=namevalue, fg="blue", bg="light green")
phoneentry = Entry(root, textvariable=phonevalue,fg="blue",bg="light green")
birthentry = Entry(root, textvariable=birthvalue,fg="blue",bg="light green")
Genderentry = Entry(root, textvariable=Gendervalue,fg="blue",bg="light green")
emailentry = Entry(root, textvariable=emailvalue,fg="blue",bg="light green")

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
birthentry.grid(row=3, column=3)
Genderentry.grid(row=4, column=3)
emailentry.grid(row=5,column=3)

check = Checkbutton(text="above information is true!",fg="blue", variable=checkvalue)
check.grid(row=6, column= 3)

widget = Button(root, text="Click Here", bg="light blue")
widget.grid(row=7,column=3)
widget.bind('<Button-1>', getvariable)
#widget.bind('<Double-1>', quit)





root.mainloop()