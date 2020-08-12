from tkinter import *
import  tkinter as tk
import math
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


###Defining The List that we are going to use#################

tempratureList = []
humidityList = []
yearsList = []


####################################### initialising the window

window = Tk()
window.title("Weather App")
window.geometry("550x650")
window.iconbitmap("icon.ico")

################################################################Frame 1

frame01 = Frame(window)
frame01.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

backroundimg = PhotoImage(file="backround.png")
backroundobject = Label(frame01, image=backroundimg)
backroundobject.place(relheight=1, relwidth=1)

################################################################Frame 2


def inpuButtonProcess():
    yearalreadyexist = False
    if(int(yearinput.get()) in yearsList):
       x = yearsList.index(yearinput.get())
       yearsList[x] = yearinput.get()
       yearalreadyexist = True




    else:

        yearsList.append(yearinput.get())

        yearalreadyexist = False







    if (checkervar.get() == 0):####temp
        if(yearalreadyexist == True):
            x = yearsList.index(yearinput.get())
            tempratureList.append(input.get())
            tempratureList.pop(x+1)
            print("year already exist")

        if(yearalreadyexist == False):
            tempratureList.append(input.get())
            print("new year entered")





    if(checkervar.get() == 1):###hum
        if(yearalreadyexist == True):
            x = yearsList.index(yearinput.get())
            humidityList.append(input.get())
            humidityList.pop(x+1)


        if(yearalreadyexist == False):
            humidityList.append(input.get())






frame02 = Frame(window)
frame02.place(relx=0.1, rely=0.15, relheight=0.15, relwidth=0.8)

generallbl = Label(frame02, text = "Enter a: ")
generallbl.place(relx=-0.05, rely=0.05, relheight=0.3, relwidth=0.2)


yearlbl = Label(frame02, text = "Year")
yearlbl.place(relx=0.1, rely=0.05, relheight=0.3, relwidth=0.1)

templbl = Label(frame02, text = "Temprature //")
templbl.place(relx=0.3, rely=0.05, relheight=0.3, relwidth=0.2)

humLbl = Label(frame02, text = "Humidity")
humLbl.place(relx=0.5, rely=0.05, relheight=0.3, relwidth=0.15)

yearinput = IntVar()
InputYearsEntry = Entry(frame02, textvariable = yearinput, bd =5)
InputYearsEntry.place(relx=0.05, rely=0.4, relheight=0.3, relwidth=0.2)

input = IntVar()
InputEntry = Entry(frame02, textvariable = input, bd =5)
InputEntry.place(relx=0.3, rely=0.4, relheight=0.3, relwidth=0.45)


InputButton = Button(frame02, text = "Input", bd = 5 , bg = "red", command = inpuButtonProcess)
InputButton.place(relx=0.8, rely=0.4, relheight=0.3, relwidth=0.2)

#########################################################Frame 3


def modifyButtonProcess():

    if(int(yearmodify.get()) in yearsList):
        x = yearsList.index(yearmodify.get())
        if(checkervar.get() == 0):####temp
            if(x == None):
                x = 0
            tempratureList[x] = modify.get()



        if(checkervar.get() == 1):####hum
            if (x == None):
                x = 0
            humidityList[x] = modify.get()




    else:
        return


frame03 = Frame(window)
frame03.place(relx=0.1, rely=0.32, relheight=0.15, relwidth=0.8)


generallbl = Label(frame03, text = "Enter a: ")
generallbl.place(relx=-0.05, rely=0.05, relheight=0.3, relwidth=0.2)

yearlbl = Label(frame03, text = "Year")
yearlbl.place(relx=0.1, rely=0.05, relheight=0.3, relwidth=0.1)

templbl = Label(frame03, text = "Temprature //")
templbl.place(relx=0.32, rely=0.05, relheight=0.3, relwidth=0.2)


humLbl = Label(frame03, text = "Humidity")
humLbl.place(relx=0.51, rely=0.05, relheight=0.3, relwidth=0.15)


yearmodify = IntVar()
ModifyYearsEntry = Entry(frame03, textvariable = yearmodify, bd =5)
ModifyYearsEntry.place(relx=0.05, rely=0.4, relheight=0.3, relwidth=0.2)

modify= IntVar()
modifyEntry = Entry(frame03, textvariable = modify, bd =5)
modifyEntry.place(relx=0.3, rely=0.4,relheight=0.3, relwidth=0.45)


modifyButton = Button(frame03, text = "Modify", bd = 5 , bg = "red", command = modifyButtonProcess)
modifyButton.place(relx=0.8, rely=0.4, relheight=0.3, relwidth=0.2)

################################################################Frame 4


def deletButtonProcess():

    if (yeardelete.get() in yearsList):
        y = yearsList.index(yeardelete.get())
        if(len(tempratureList) > 0):
            tempratureList.pop(y)
        else:
            print("Temprature List Is Empty")

        if (len(humidityList) > 0):
            humidityList.pop(y)
        else:
            print("Humidity List Is Empty")
        if (len(yearsList) > 0):
            yearsList.pop(y)
        else:
            print("Years List Is Empty")

    else:
        print("Year Not Found Please Try to Input A year First")


def tutorialButtonProcess():
    tutWindow = Toplevel(window)
    tutWindow.title("Tutorial Window")
    tutWindow.geometry("500x500")

    tutoriallabel = Label(tutWindow, text = "HELLO DEAR USER\nThis tutorial will teach u how to use my program\n1- First, to input a year with its average Temprature // Humidity\n you should check the RadioButton that says (tempratue)// (humidity)\nYou can NOT neither MODIFY a year that does NOT exist nor delete it\n2-Feel free to use the Charts Button to display a chart of a specific list\nFIRST print Button will print the Data of the temprature/years/humidity lists\nand the second Print button will show u the average of the tempratue/humidity lists\nMake sure to have values in temprature/humidty lists \nBEFOR CHECKING FOR THERE AVERAGES!!\n\n\n\n\n Credits :\nCharbel Fayad", bg= "black", fg = "green")
    tutoriallabel.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)






frame04 = Frame(window)
frame04.place(relx=0.1, rely=0.49, relheight=0.15, relwidth=0.8)

generallbl = Label(frame04, text = "Enter a: ")
generallbl.place(relx=0, rely=0.05, relheight=0.3, relwidth=0.2)


yearlbl = Label(frame04, text = "Year")
yearlbl.place(relx=0.175, rely=0.05, relheight=0.3, relwidth=0.1)




yeardelete = IntVar()
deleteYearsEntry = Entry(frame04, textvariable = yeardelete, bd =5)
deleteYearsEntry.place(relx=0.175, rely=0.4, relheight=0.3, relwidth=0.2)




deleteButton = Button(frame04, text = "Delete", bd = 5 , bg = "red", command = deletButtonProcess)
deleteButton.place(relx=0.4, rely=0.4, relheight=0.3, relwidth=0.2)


TutorialButton = Button(frame04, text = "Tutorial", bd = 5, bg = "blue", command = tutorialButtonProcess)
TutorialButton.place(relx=0.75, rely=0.4, relheight=0.3, relwidth=0.2)



##################################################################Frame 5

def printBt1Process():



    yearprinter = Message(frame07, text = "year list==>\n"+ str(yearsList), bg = "red")
    yearprinter.place(relx=0.05, rely=0.05, relheight=0.7, relwidth=0.3)
    tempprinter01 = Message(frame07, text = "temp list ==>\n" + str(tempratureList), bg = "green")
    tempprinter01.place(relx=0.37, rely=0.05, relheight=0.7, relwidth=0.3)
    humprinter01 = Message(frame07, text="humidity list ==>\n" + str(humidityList), bg = "blue")
    humprinter01.place(relx=0.7, rely=0.05, relheight=0.7, relwidth=0.3)


frame05 = Frame(window)
frame05.place(relx=0.1, rely=0.66, relheight=0.08, relwidth=0.8)


PrintButton1 = Button(frame05, text = "Print All The Data Of The Temprature/Humidity/Years Lists", bd = 5 , bg = "green", command = printBt1Process)
PrintButton1.place(relx=0.05, rely=0.17, relheight=0.7, relwidth=0.9)

###################################################################frame 6


def printButton2Process():
    if(len(tempratureList) == 0):
        return

    else:
        tempprinter02 = Message(frame07, text = "temp list avg==>\n" + str(math.trunc(sum(tempratureList)/len(tempratureList))), bg = "orange")
        tempprinter02.place(relx=0.37, rely=0.05, relheight=0.7, relwidth=0.3)
    if (len(humidityList) == 0):
        return
    else:
        humprinter02 = Message(frame07,text="humidity list avg==>\n" + str(math.trunc(sum(humidityList) / len(humidityList))),bg="cyan")
        humprinter02.place(relx=0.7, rely=0.05, relheight=0.7, relwidth=0.3)




frame06 = Frame(window)
frame06.place(relx=0.1, rely=0.75, relheight=0.08, relwidth=0.8)


PrintButton2= Button(frame06, text = "Print The Average Of The Data Of The Temperature/Humidity Lists ", bd = 5 , bg = "green", command = printButton2Process)
PrintButton2.place(relx=0.05, rely=0.17, relheight=0.7, relwidth=0.9)


####################################################frame 7

frame07 = Frame(window)
frame07.place(relx=0.1, rely=0.01, relheight=0.1, relwidth=0.8)
####################################################frame 8


def openNewWindow01():
    newWindow = Toplevel(window)
    newWindow.title("TempratureChart Window")
    newWindow.geometry("500x500")

    data2 = {'Year': yearsList,
             'temprature':tempratureList
             }
    df2 = DataFrame(data2, columns=['Year', 'temprature'])


    figure2 = plt.Figure(figsize=(5, 4), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, newWindow)
    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2 = df2[['Year', 'temprature']].groupby('Year').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color='red', marker='o', fontsize=10)
    ax2.set_title('Year Vs. temprature')

def openNewWindow02():
    newWindow = Toplevel(window)
    newWindow.title("HumidityChart Window")
    newWindow.geometry("500x500")

    data2 = {'Year': yearsList,
             'Humidity': humidityList
             }
    df2 = DataFrame(data2, columns=['Year', 'Humidity'])

    figure2 = plt.Figure(figsize=(5, 4), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, newWindow)
    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2 = df2[['Year', 'Humidity']].groupby('Year').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color='red', marker='o', fontsize=10)
    ax2.set_title('Year Vs. Humidity')


frame08 = Frame(window)
frame08.place(relx=0.1, rely=0.8355, relheight=0.04, relwidth=0.8)



checkervar = IntVar()

temRadioB = Radiobutton(frame08, text = "Temprature", bg = "orange", variable = checkervar, value = 0)

humRadioB = Radiobutton(frame08, text = "Humidity", bg = "cyan", variable = checkervar, value = 1)

TempChartButton = Button(frame08, text = "Temprature Chart", bg = "orange", bd = "5", command = openNewWindow01)
HumChartButton = Button(frame08, text = "Humidity Chart", bg = "cyan", bd = "5", command = openNewWindow02)

temRadioB.place(relx=0.01, rely=0.17, relheight=0.7, relwidth=0.2)
humRadioB.place(relx=0.22, rely=0.17, relheight=0.7, relwidth=0.2)
TempChartButton.place(relx=0.44, rely=0.17, relheight=0.75, relwidth=0.25)
HumChartButton.place(relx=0.73, rely=0.17, relheight=0.75, relwidth=0.25)





####################################################main loop
window.mainloop()
####################################################




