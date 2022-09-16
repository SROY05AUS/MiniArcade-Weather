from tkinter import *
import urllib.request
import json
import tkinter.messagebox
class WeatherAPP:
    mainweb = "http://api.openweathermap.org/data/2.5/weather?appid=de8851a6beaed43a1cdaee8d555afc26&q="
    def __init__(self,master):
        self.master = master
        self.master.title("Weather app **SIMPLE**")
        self.mainFrame = Frame(self.master, width = 300, height = 700)
        self.mainFrame.pack()
        self.TempLab = Label(self.mainFrame, text = "Temperature: ", fg = "purple")
        self.HumLab = Label(self.mainFrame, text = "Humidity levels:", fg = "purple")
        self.condLab = Label(self.mainFrame, text = "Conditions:", fg = "purple")
        self.searchLab = Label(self.mainFrame, text = "Search for City:", fg = "purple")
        self.TempLab.grid(row = 0, column = 0, sticky = W)
        self.HumLab.grid(row = 2, column = 0, sticky = W)
        self.condLab.grid(row = 4, column = 0, sticky = W)
        self.searchLab.grid(row = 8, column = 0, sticky = W)
        self.searchBUTT = Button(self.mainFrame, text = "Search City", command = self.SearchCITY)
        self.searchBUTT.grid(row = 10, column = 0, sticky = W)
        self.searchEntry = Entry(self.mainFrame)
        self.searchEntry.grid(row = 8, column = 1)
        self.menu = Menu(self.mainFrame)
        self.master.config(menu = self.menu)
        self.Settings = Menu(self.menu)
        self.menu.add_cascade(label = "Settings", menu = self.Settings)
        self.unitChoice = "metric"
        self.Settings.add_command(label = "Change units", command = self.changeUnit)
        self.minTempLab = Label(self.mainFrame, text = "Min-Temp:", fg = "purple")
        self.minTempLab.grid(row = 5, column = 0, sticky = W)
        self.maxTempLab = Label(self.mainFrame, text = "Max-Temp:", fg = "purple")
        self.maxTempLab.grid(row = 7, column = 0, sticky = W)
    def accessCOND(self):
        self.enteredCity = self.searchEntry.get()
        self.finalUrl = self.mainweb+self.enteredCity+"&units="+self.unitChoice
        self.webMAIN = urllib.request.urlopen(self.finalUrl).read()
        self.jsondat = str(self.webMAIN ,"utf-8")
        self.finaljsondat = json.loads(self.jsondat)
        self.unitChoice = "metric"
        
        for item in self.finaljsondat["weather"]:
        #print(item)
            for xs in item:
                if xs == "description":
                    #print("conditions:"+item[xs])
                    self.CONDLAB = Label(self.mainFrame, text = item[xs]+"                  ")
                    self.CONDLAB.grid(row = 4, column = 1, sticky = W)
                    break
        #print(self.finaljsondat)
    def SearchCITY(self):
        try:
            try:
                self.accessCOND()
                self.accessTEMP()
                self.accessHUMandMinTemp()
                self.accessMaxTemp()
            except urllib.error.URLError:
                tkinter.messagebox.showinfo("ERROR", "Are you connected to Wi-fi?")
        except urllib.error.HTTPError:
            tkinter.messagebox.showinfo("ERROR", "Invalid City, Enter Again")
    def accessTEMP(self):
        
        
        self.enteredCity = self.searchEntry.get()
        self.finalUrl = self.mainweb+self.enteredCity+"&units="+self.unitChoice
        self.webMAIN = urllib.request.urlopen(self.finalUrl).read()
        self.jsondat = str(self.webMAIN ,"utf-8")
        self.finaljsondat = json.loads(self.jsondat)
        self.TEMPCLAB = Label(self.mainFrame, text=str(self.finaljsondat["main"]["temp"])+" degree C         ")
        self.TEMPCLAB.grid(row = 0, column = 1, sticky = W)
        #print(str(self.finaljsondat["main"]["temp"])+" degree C      ")
    def accessHUMandMinTemp(self):
        self.enteredCity = self.searchEntry.get()
        self.finalUrl = self.mainweb+self.enteredCity+"&units="+self.unitChoice
        self.webMAIN = urllib.request.urlopen(self.finalUrl).read()
        self.jsondat = str(self.webMAIN ,"utf-8")
        self.finaljsondat = json.loads(self.jsondat)
        self.HUMLAB = Label(self.mainFrame, text = str(self.finaljsondat["main"]["humidity"])+"    ")
        self.HUMLAB.grid(row = 2, column = 1, sticky = W)
        self.minTempCLAB = Label(self.mainFrame, text = str(self.finaljsondat["main"]["temp_min"])+"   ")
        self.minTempCLAB.grid(row = 5, column = 1, sticky = W)
    def changeUnit(self):
        if self.unitChoice == "metric":
            self.unitChoice = "imperial"
        elif self.unitChoice == "imperial":
            self.unitChoice = "metric"
    def accessMaxTemp(self):
        self.enteredCity = self.searchEntry.get()
        self.finalUrl = self.mainweb+self.enteredCity+"&units="+self.unitChoice
        self.webMAIN = urllib.request.urlopen(self.finalUrl).read()
        self.jsondat = str(self.webMAIN ,"utf-8")
        self.finaljsondat = json.loads(self.jsondat)
        self.maxCLAB = Label(self.mainFrame, text = str(self.finaljsondat["main"]["temp_max"])+"   ")
        self.maxCLAB.grid(row = 7, column = 1, sticky = W)
        
        
        
root = Tk()
NEWWEATHERAPP = WeatherAPP(root)
root.mainloop()
        
