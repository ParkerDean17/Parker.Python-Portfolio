# Parker Dean
# 3/13/19

from tkinter import *


class Application(Frame):
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.displayarea=""
        self.opperator=""
        self.position1=""
        self.position2=""
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.display = Entry(width=25)
        self.bttn1 = Button(text="\t1\t", command=self.bttn1_press)
        self.bttn2 = Button(text="\t2\t", command=self.bttn2_press)
        self.bttn3 = Button(text="\t3\t", command=self.bttn3_press)
        self.bttn4 = Button(text="\t4\t", command=self.bttn4_press)
        self.bttn5 = Button(text="\t5\t", command=self.bttn5_press)
        self.bttn6 = Button(text="\t6\t", command=self.bttn6_press)
        self.bttn7 = Button(text="\t7\t", command=self.bttn7_press)
        self.bttn8 = Button(text="\t8\t", command=self.bttn8_press)
        self.bttn9 = Button(text="\t9\t", command=self.bttn9_press)
        self.bttn0 = Button(text="\t0\t", command=self.bttn0_press)
        self.bttnadd = Button(text="\t+\t", command=self.bttnadd_press)
        self.bttnsub = Button(text="\t-\t", command=self.bttnsub_press)
        self.bttnmul = Button(text="\t*\t", command=self.bttnmul_press)
        self.bttndiv = Button(text="\t/\t", command=self.bttndiv_press)
        self.bttnequ = Button(text="\t=\t", command=self.bttnequ_press)
        self.bttnclr = Button(text="\tC\t", command=self.bttnclr_press)

        self.display.grid(row=0, column=1, columnspan=4, sticky=NSEW)
        self.bttn1.grid(row=1, column=0, sticky=NSEW)
        self.bttn2.grid(row=1, column=1, sticky=NSEW)
        self.bttn3.grid(row=1, column=2, sticky=NSEW)
        self.bttn4.grid(row=2, column=0, sticky=NSEW)
        self.bttn5.grid(row=2, column=1, sticky=NSEW)
        self.bttn6.grid(row=2, column=2, sticky=NSEW)
        self.bttn7.grid(row=3, column=0, sticky=NSEW)
        self.bttn8.grid(row=3, column=1, sticky=NSEW)
        self.bttn9.grid(row=3, column=2, sticky=NSEW)
        self.bttn0.grid(row=4, column=0, sticky=NSEW)
        self.bttnadd.grid(row=1, column=3, sticky=NSEW)
        self.bttnsub.grid(row=2, column=3, sticky=NSEW)
        self.bttnmul.grid(row=3, column=3, sticky=NSEW)
        self.bttndiv.grid(row=4, column=3, sticky=NSEW)
        self.bttnclr.grid(row=4, column=2, sticky=NSEW)
        self.bttnequ.grid(row=4, column=1, sticky=NSEW)

    def bttn1_press(self):
        self.displayarea += "1"
        self.display.delete(0,END)
        self.display.insert(0,self.displayarea)
    def bttn2_press(self):
        self.displayarea += "2"
        self.display.delete(0,END)
        self.display.insert(0,self.displayarea)
    def bttn3_press(self):
        self.displayarea += "3"
        self.display.delete(0, END)
        self.display.insert(0, self.displayarea)
    def bttn4_press(self):
        self.displayarea += "4"
        self.display.delete(0,END)
        self.display.insert(0,self.displayarea)
    def bttn5_press(self):
        self.displayarea += "5"
        self.display.delete(0,END)
        self.display.insert(0,self.displayarea)
    def bttn6_press(self):
        self.displayarea += "6"
        self.display.delete(0,END)
        self.display.insert(0,self.displayarea)
    def bttn7_press(self):
        self.displayarea += "7"
        self.display.delete(0,END)
        self.display.insert(0,self.displayarea)
    def bttn8_press(self):
        self.displayarea += "8"
        self.display.delete(0,END)
        self.display.insert(0,self.displayarea)
    def bttn9_press(self):
        self.displayarea += "9"
        self.display.delete(0,END)
        self.display.insert(0,self.displayarea)
    def bttn0_press(self):
        self.displayarea += "0"
        self.display.delete(0,END)
        self.display.insert(0,self.displayarea)

    def bttnadd_press(self):
        self.position1 = self.displayarea
        self.displayarea = ""
        self.opperator = "+"
        self.display.delete(0, END)
    def bttnsub_press(self):
        self.position1 = self.displayarea
        self.displayarea = ""
        self.opperator = "-"
        self.display.delete(0, END)
    def bttnmul_press(self):
        self.position1 = self.displayarea
        self.displayarea = ""
        self.opperator = "*"
        self.display.delete(0, END)
    def bttndiv_press(self):
        self.position1 = self.displayarea
        self.displayarea = ""
        self.opperator = "/"
        self.display.delete(0, END)
    def bttnclr_press(self):
        self.displayarea = ""
        self.opperator = ""
        self.position1 = ""
        self.position2 = ""
        self.total = ""
        self.display.delete(0, END)
    def bttnequ_press(self):
        self.position2 = self.display.get()
        self.sidplayare = ""
        if self.opperator == "+":
            self.total = int(self.position1)+int(self.position2)
        elif self.opperator == "-":
            self.total = int(self.position1)-int(self.position2)
        elif self.opperator == "*":
            self.total = int(self.position1)*int(self.position2)
        elif self.opperator == "/":
            self.total = int(self.position1)/int(self.position2)
        self.displayarea=self.total
        self.display.delete(0, END)
        self.display.insert(0, self.displayarea)

# main
root = Tk()
root.title("Calculator")
app = Application(root)
root.mainloop()