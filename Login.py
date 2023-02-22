
#from tkinter import *
#from tkinter import Tk
#from View import * 
#from Main import * 
#from tkinter import messagebox
#from PIL import Image, ImageTk

#def Login():
   # user = Entry_User.get()
   #  passw = Entry_Passw.get()
   #  cursor = conexao.cursor()
   #  query = "Select * from Login Where Username =%s and Password =%s" 
   #  val = (user,passw)
   #  cursor.execute(query,val)
   # result = cursor.fetchone()
   # if result:
   #     messagebox.showinfo("Status","Login sucessful")
   # else:
   #      messagebox.showinfo("Status","Login failed")
    






#Janela_Login = Tk()
#Janela_Login.title("Login")
#Janela_Login.geometry("660x440")



#img = Image.open('back.jpg')
#img = img.resize((6000,3375))
#img = ImageTk.PhotoImage(img)

#label1 = Label(Janela_Login, image=img)
#label1.pack()

#Frame_Login = Frame(Janela_Login,width=320, height=360,bg="#e9edf5")
#Frame_Login.place(relx=0.5, rely=0.5, anchor=CENTER)

#Label_Frase = Label(Frame_Login, text="Faça Login na sua conta",font=("Verdana",16),fg="#000000",bg="#e9edf5",anchor=CENTER)
#Label_Frase.place(x=50, y=20)

#Label_User = Label(Frame_Login,text="Username:", font=("Verdana",12),fg="#000000",bg="#e9edf5")
#Label_User.place(x=50,y=70)

#Entry_User = Entry(Frame_Login,font=("Verdana",12))
#Entry_User.place(x=50,y=100)

#Label_Passw = Label(Frame_Login,text="Password:", font=("Verdana",12),fg="#000000",bg="#e9edf5")
#Label_Passw.place(x=50,y=130)

#Entry_Passw = Entry(Frame_Login,font=("Verdana",12),show="*")
#Entry_Passw.place(x=50,y=160)

#Button_Login = Button(Frame_Login,text="  Entrar",width=20,height=1,font=("Verdana",12),anchor=CENTER,fg="#000000",bg="#e9edf5",overrelief=RIDGE,command=Login)
#Button_Login.place(x=50,y=200)

#Janela_Login.mainloop()

