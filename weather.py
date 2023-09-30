from tkinter import *

from tkinter import ttk
import requests

# just for Cheking Purpose
# city_name = 'Gujrat'
# data = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=bc13fc55115399e3348592d177a906de').json()
# print(data)


def get_data():
    city = city_name.get()
    data = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=bc13fc55115399e3348592d177a906de').json()
    
    d_label_1.config(text=data['weather'][0]['main'])
    climate_label_1.config(text=data['weather'][0]['description'])
    t_label_1.config(text=int((data['main']['temp']-273.15)))








root = Tk()

root.title('Weather app by Dipesh')
# use color
root.config(bg='blue')

# height and width
root.geometry('500x500')
 # This code for box
name_label = Label(root,text='Code soft Weather App',
                font=('Time New Roman',20,'bold') )
name_label.place(x=25,y=50,height=50,width=450)
# name_label.pack()

# make a combo box..  First import from tkinter import ttk
city_name = StringVar()

list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
combo_box = ttk.Combobox(root,text='Code soft Weather App', values=list_name ,
                font=('Time New Roman',20,'bold'),textvariable=city_name )

combo_box.place(x=50,y=120,height=60,width=400)


# 4 label

# climate
d_label = Label(root,text='Weather Climate ',
                font=('Time New Roman',15) )
d_label.place(x=25,y=260,height=50,width=210)

# this code for blank.
d_label_1 = Label(root,text='',
                font=('Time New Roman',15) )
d_label_1.place(x=250,y=260,height=50,width=210)




# temp
t_label = Label(root,text='Weather Temprature ',
                font=('Time New Roman',15) )
t_label.place(x=25,y=330,height=50,width=210)

t_label_1 = Label(root,text='',
                font=('Time New Roman',15) )
t_label_1.place(x=250,y=330,height=50,width=210)


# # Description
climate_label = Label(root,text='Weather Description ',
                font=('Time New Roman',15) )
climate_label.place(x=25,y=400,height=50,width=210)

climate_label_1 = Label(root,text=' ',
                font=('Time New Roman',15) )
climate_label_1.place(x=250,y=400,height=50,width=210)









# make button..
button_1 = Button(root,text='Select and  Then Click ...',
                font=('Time New Roman',12,'bold'),command=get_data )
button_1.config(bg='red')
button_1.place(x=100,y=190,height=50,width=200)





root.mainloop()