#Imports
from tkinter import *
import os, csv
from tkinter import ttk
from geopandas import *
#=================================================================================================================
#Creating window
window = Tk()
window.geometry('1920x1080')
window.resizable(width=False, height=False)
window.config(bg = "#556ee6")
window.title("Data Uploader to Website")
value = 1
#=================================================================================================================
def selectedDate():
    global value
    value -= 1
    if value == 0:
        array1 = []

        gdf = gpd.read_file("C:/TSE_datasets/CoL_LWS_21-22.tab")
        toCSV = gpd.GeoDataFrame(gdf).to_file(driver="csv",filename=gdf)
        gdf2 = gpd.read_file("C:/TSE_datasets/CoL_LWS_21-22.csv")
        array1.append(gdf2)


        for row in gdf2:
            array1.append(row)

                
        height = 46
        width = 16
        cells = {}
        counter = 0
        counter1 = 0
        for i in range(height): #Rows
            for j in range(width): #Columns        
                b = Entry(window, width=15,bg = '#778beb', fg='black', highlightbackground="Black", font=('Arial',10,'bold'))
                b.grid(row=i, column=j)
                b.insert(0, array1[i][j])
                cells[(i,j)] = b
    else:
        pass
#=================================================================================================================            



        
#=================================================================================================================
#Change table year    
selecttext = StringVar(window)
selecttext.set("Please Select the date")
optionData = ["2023"]
z = OptionMenu(window, selecttext, *optionData)
z.place(x=1660, y=50)
z.config(width=30)
z.config(bg="#778beb", fg="black", highlightthickness=2, highlightbackground="Black")
if selecttext == "2023":
    selectedDate()
#=================================================================================================================
#Date of data Text 
lbl = Label(window, text="Date of data", bg = '#778beb', fg = "black", highlightbackground="Black")
lblFont = ("Agency FB", 20, "bold")
lbl.config(font = lblFont)
lbl.grid(column=0, row=0)
lbl.place(x=1470, y=45)
#=================================================================================================================
#Update Date button
btn = Button(window, text="Update Date", bg = '#778beb', highlightbackground="Black", command=selectedDate)
btnFont = ("Agency FB", 20, "bold")
btn.config(width=40)
btn.config(font = btnFont)
btn.grid(column=0, row=0)
btn.place(x=1470, y=100)
#=================================================================================================================
#Save button
btn = Button(window, text="Save", bg = '#778beb', highlightbackground="Black")
btnFont = ("Agency FB", 20, "bold")
btn.config(width=40)
btn.config(font = btnFont)
btn.grid(column=0, row=0)
btn.place(x=1470, y=440)
#=================================================================================================================
#Close Button
def closecommand():
    window.destroy()
btn = Button(window, text="Close", bg = '#778beb', highlightbackground="Black", command=closecommand)
btnFont = ("Agency FB", 20, "bold")
btn.config(width=40)
btn.config(font = btnFont)
btn.grid(column=0, row=0)
btn.place(x=1470, y=800)
#=================================================================================================================

window.mainloop()

