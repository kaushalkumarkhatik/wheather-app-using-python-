from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import requests

root=Tk()
app=Frame(root,bg="#0072A0")
app.config(width=1000, height=1300)
app.place(relx=.5, rely=.53, anchor="c")
app.pack_propagate(0)

root.title("wheather app")
root.geometry("700x350")
root.config(bg="skyblue")

#img
#logo image
log= (Image.open(r"logo.png"))

resized_image= log.resize((250,250), Image.ANTIALIAS)
logo= ImageTk.PhotoImage(resized_image)

img_logo=Label(root,image=logo,bg="skyblue")
img_logo.place(x=80,y=100)

#title
ti=Label(root,text="Wheather live")
ti.config(font=("Times New Roman", 15),fg="#fff",bg="skyblue")
ti.place(x=380,y=200)

#images
street= (Image.open(r"street-view.png"))

resized_image=street.resize((220,220), Image.ANTIALIAS)
img1= ImageTk.PhotoImage(resized_image)

#data fill
#city name
city_name=Label(app,bg="#0072A0")
city_name.config(font=("Arial", 20),fg="#fff")
city_name.place(x=300,y=380)

#type
cur_type=Label(app,bg="#0072A0",fg="#fff")
cur_type.place(x=500,y=700)

#temp
t=Label(app,bg="#0072A0")
t.config(font=("Times New Roman", 25),fg="#fff")
t.place(x=180,y=850)

#min and max temp
min_max=Label(app,bg="#0072A0",fg="#D3D3D3")
min_max.place(x=180,y=1100)

def srch():
	city=entry.get()
	url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=b9697c694afd4b0d728c01899afd9194"
	
	data=requests.get(url).json()
	
	if data['cod'] == 200:
		y=data["main"]
		current_temp=y["temp"]
		current_min=y["temp_min"]
		current_max=y["temp_max"]
		z = data["weather"]
		cur_desc = z[0]["main"]
		
		#cal
		degree_sign = u"\N{DEGREE SIGN}"
		cal=f"{current_temp}{degree_sign}Cel"
		#min
		min_max_temp=f"min : {current_min}{degree_sign}Cel | max : {current_max}{degree_sign}Cel"
		
		#city name
		city_name.configure(text=city.upper())
		#type
		cur_type.configure(text=cur_desc)
		#img
		img=Label(app,image=img1,bg="#0072A0")
		img.place(x=280,y=580)
		#temp
		t.configure(text=cal)
	    #min max temp
		min_max.configure(text=min_max_temp)
		
	elif city=="":
		messagebox.showwarning("warning","Please provide a city.")
	
	else:
		messagebox.showwarning("warning","City Not Found")
	
#search city
label=Label(app,text="Search City")
label.config(font=("Times New Roman", 12, "italic"),bg="#0072A0",fg="#fff")
label.place(x=180,y=100)
#entry box
entry=Entry(app,text="search",width=13,font=('Arial 13'))
entry.place(x=90,y=200)

#search button
btn=Button(app,text="Search",command=srch)
btn.config(font=("Times New Roman",8, "italic"),)
btn.place(x=680,y=200)
root.mainloop()


