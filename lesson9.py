from tkinter import *

ALL = N+S+W+E

class Application(Frame):
    
 
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        self.master.title("Grid Manager")

        self.rowconfigure(0, weight=1) 
        self.rowconfigure(1, weight=1) 
        self.rowconfigure(2, weight=0) 
                     
        frame1 = Frame(self, bg="blue")
        frame1.grid(row = 0, column = 0, columnspan = 2, sticky = W+E+N+S) 
        frame1.bind("<Button-1>", self.handler1)
        
        frame2 = Frame(self, bg="yellow")
        frame2.grid(row = 1, column = 0, columnspan = 2, sticky = W+E+N+S)
        frame2.bind("<Button-1>", self.handler2)
        
        self.frame3 = Frame(self, bg="white")
        self.frame3.grid(row = 0, column = 2, rowspan = 2, columnspan = 3, sticky = W+E+N+S)
        
        self.entryfield = Entry(self.frame3)
        self.textdisplay = Text(self.frame3, state=DISABLED, wrap=WORD)
        self.entryfield.pack(fill=X, expand=False)
        self.textdisplay.pack(fill=BOTH, expand=True)
        self.textdisplay.configure(state=NORMAL)
        self.textdisplay.insert(INSERT, "NO FILE LOADED")
        
        for c in range(5):
            self.columnconfigure(c, weight=1)
        Button(self, width=25, text="Red", command = self.bredhandler).grid(row=2,column=0,sticky=E+W) 
        Button(self, width=25, text="Blue", command = self.bbluehandler).grid(row=2,column=1,sticky=E+W)
        Button(self, width=25, text="Green", command = self.bgreenhandler).grid(row=2,column=2,sticky=E+W)
        Button(self, width=25, text="Black", command = self.bblackhandler).grid(row=2,column=3,sticky=E+W)   
        Button(self, width=25, text="Open", command = self.bopenhandler).grid(row=2,column=4,sticky=E+W)          
    

    def bredhandler(self):
        self.textdisplay.configure(fg="red")

    def bbluehandler(self):
        self.textdisplay.configure(fg="blue")

    def bgreenhandler(self):
        self.textdisplay.configure(fg="green")

    def bblackhandler(self):
        self.textdisplay.configure(fg="black")       
    
    def bopenhandler(self):    
        self.textdisplay.configure(state=NORMAL)
        self.textdisplay.delete(1.0, END)
        self.textdisplay.insert(INSERT, "LOADING FILE")
        self.textdisplay.configure(state=DISABLED)
        filename = self.entryfield.get()

    # tries to read file from current directory
        try:
            fi = open(filename, 'r')
            textToShow = fi.read()
            self.textdisplay.configure(state=NORMAL)
            self.textdisplay.delete(1.0, END)
            self.textdisplay.insert(INSERT, textToShow)
            self.textdisplay.configure(state=DISABLED)
        except FileNotFoundError:
            self.textdisplay.configure(state=NORMAL)
            self.textdisplay.delete(1.0, END)
            self.textdisplay.insert(INSERT, "*** File Not Found ***")
            self.textdisplay.configure(state=DISABLED)

      
    def handler1(self, event):
        print("clicked at Frame 1", event.x, event.y) 

    def handler2(self, event):
        print("clicked at Frame 2", event.x, event.y) 

root = Tk()
root.geometry("600x400")
app = Application(master=root)
app.mainloop()
