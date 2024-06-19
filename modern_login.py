from tkinter import *

root=Tk()
root.configure(bg='#e3f2fd')

#=====Fuctions to browse the links=====
def open_google():
    import webbrowser
    webbrowser.open("https://accounts.google.com/signin")
    
def open_facebook():
    import webbrowser
    webbrowser.open("https://www.facebook.com/login/")

def open_github():
    import webbrowser
    webbrowser.open("https://github.com/login")
    
def open_linkedin():
    import webbrowser
    webbrowser.open("https://www.linkedin.com/login")
#=====Frame1=====
frame1=Frame(root,bg='#fafafa')
frame1.place(x=100,y=350,width=1000,height=800)

lblsign=Label(frame1,text='SIGN IN',bg='#fafafa',fg='black',font=('Celibri',15,'bold')).place(x=180,y=100)

#=====Buttons=====
photo1=PhotoImage(file='google.png')
photo2=PhotoImage(file='facebook.png')
photo3=PhotoImage(file='github.png')
photo4=PhotoImage(file='linkedin.png')

btngoogle=Button(frame1,image=photo1,bg='#fafafa',width=60,height=50,bd=3,command=lambda:open_google()).place(x=80,y=200)

btnfacebook=Button(frame1,image=photo2,bg='#fafafa',width=60,height=50,bd=3,command=lambda:open_facebook()).place(x=180,y=200)

btngithub=Button(frame1,image=photo3,bg='#fafafa',width=60,height=50,bd=3,command=lambda:open_github()).place(x=280,y=200)

btnlinkedin=Button(frame1,image=photo4,bg='#fafafa',width=60,height=50,bd=3,command=lambda:open_linkedin()).place(x=380,y=200)
#==========
lblmessage2=Label(frame1,text='or use your email password',bg='#fafafa').place(x=130,y=300)
#=====Entrys=====
#lblemail=Label(frame1,text='Email : ',bg='#fafafa').place(x=10,y=350)
entryemail=Entry(frame1,placeholder='  Email',width=30,bg='whitesmoke').place(x=50,y=350,height=50)

#lblpass=Label(frame1,text='Password : ',bg='#fafafa').place(x=10,y=400)
entrypass=Entry(frame1,placeholder='  Password',show='*',width=30,bg='whitesmoke').place(x=50,y=420,height=50)
#==========
lblmessage3=Label(frame1,text='Forget Your Password ?',bg='#fafafa').place(x=130,y=490)
#=====Button Sign in=====
btnsignin=Button(frame1,text='SIGN IN',bg='#512da8',fg='white').place(x=200,y=540)


#=====Frame2=====
frame2=Frame(frame1,bg='#512da8')
frame2.place(x=510,y=1,width=490,height=800)

lblhello=Label(frame2,text='Hello, Friend!',bg='#512da8',fg='#fafafa',font=('Celibri',16,'bold')).pack(pady=200)


lblmessage=Label(frame2,text='Register with your personal details to use all \n of application feuture',bg='#512da8',fg='#fafafa',font=('Celibri',7)).pack()

btnsignup=Button(frame2,text='SIGN UP',bg='#512da8',fg='#fafafa').pack(pady=50)

#=====My Name=====
lblmyname=Label(frame1,text='By : Haitham.N.Sharlie',bg='#fafafa').place(x=150,y=750)


root.mainloop()