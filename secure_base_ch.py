from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
#from firebase import firebase
from selenium import webdriver
import webbrowser as web
from tkinter.ttk import Notebook
from PIL import Image, ImageTk
from ecapture import ecapture as ecap
import time
import ftplib
from songline import Sendline
import requests
import os
import sys
print(sys.path)
'''url = 'https://ch-n-ex.firebaseio.com/'
messenger = firebase.FirebaseApplication(url)'''

def open_c():
	myCmd = 'start chrome "google.com"'
	#myCmd = 'start microsoft-edge: google.com'
	os.system(myCmd)
	close_program()


URL_LINE = "https://notify-api.line.me/api/notify" 
token = 'aKe3ZlD1AU9IlG2Gs8qUtnyWEOpx5Bfp1we0MS4hwSa' 
def line_pic():
    file_img = {'imageFile': open('myPic.png', 'rb')}
    msg = ({'message': 'รีบไปที่คอมด่วน!!!'})
    LINE_HEADERS = {"Authorization":"Bearer "+token}
    session = requests.Session()
    session_post = session.post(URL_LINE, headers=LINE_HEADERS, files=file_img, data=msg)
    print(session_post.text)

def run_line():
	
	messenger1 = Sendline(token)
	messenger1.sendtext('คนๆนี้ แอบเข้า google chrome,explorer')
	time.sleep(.1)
	line_pic()
	#http://uncle-pydatabase.com/Bank/myPic.png
	messenger1.sticker(6,1)
	
#'se-pho.appspot.com'
def detect():

	ecap.capture(1,False,'myPic.png')
	time.sleep(.1)
	upload('myPic.png')
	run_line()
def upload(filename):
	IP='119.59.104.31'
	PORT=2002
	ftp=ftplib.FTP()
	ftp.connect(IP,PORT)#connect เข้า sever
	ftp.login('unclepyd','Uncle1234')
	mypath='/domains/uncle-pydatabase.com/public_html/Bank'
	checkpath=ftp.cwd(mypath)#เข้าถึง path
	#print(checkpath)#250->เวลา CWD command successful<-เข้าถึงได้

	files=ftp.nlst()#มีไฟล์อะไรบ้าง ก่อน upload
	#print(files)

	#upload
	file_upload=open(filename,'rb')#rb=read binary->เอาไฟล์มา
	result=ftp.storbinary('STOR '+filename,file_upload)

	files=ftp.nlst()#มีไฟล์อะไรบ้าง หลัง upload
	file_upload.close()

def login(event=None):
	password=E1.get()


	if password=='Bank52345':
		return open_c()
	else:
		l1=Label(text='ERROR',font='Ansananew 40',fg='red',bg='black')
		l1.place(x=670,y=600)
		return detect()

GUI = Tk()
GUI.title('Bank Secure')
GUI.geometry('1920x800+-11+-2')
GUI.configure(background='black')


im=Image.open("C:\\Python-work\\chrome_con\\v5s22QiP_400x400.jpg")
im = im.resize((450, 450), Image.ANTIALIAS)
im1 = ImageTk.PhotoImage(im)
im11 = Label(GUI , image=im1,borderwidth=0)         
im11.image=im1
im11.pack()

pas=Label(text='Enter password :',font='A.I.Rebellion 25',fg='green',bg='black')
pas.place(x=350,y=525)
E1=Entry(GUI,width=20,font='* 20',fg='green',bg='#869394',show='*')
E1.bind('<Return>',login)
E1.place(x=620,y=530)
E1.focus()

def close_program():
    GUI.destroy()

def disable_event():
    pass

logon = Button(GUI, text = "Login",font='Ansananew 25', command = login,fg='black',bg='blue')


logon.place(x=960,y=515)
'''
btn = Button(GUI, text = "Click me to close",bg='blue',fg='black',font='Ansananew 20',command = close_program)
btn.place(x=699,y=699)'''



GUI.protocol("WM_DELETE_WINDOW", disable_event)



GUI.mainloop()