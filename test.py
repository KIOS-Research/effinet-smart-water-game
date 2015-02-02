# -*- coding: cp1253 -*-
from tkinter import *
from time import sleep

def create(w, x1, y1):
    w.place(x=x1, y=y1)


def erase(w):
    w.destroy()


def reset(w):
    w.destroy()
    start()


def exit(w):
    w.destroy()


def e_q1(root, counter, step):
    TL = Toplevel()
    w, h = TL.winfo_screenwidth(), TL.winfo_screenheight()
    TL.overrideredirect(1)
    TL.geometry("%dx%d+0+0" % (w, h))
    a01 = 0
    a02 = 0
    a03 = 0
    if step == 1:
        question = "Question 1: How much of Earth's water is salty and undrinkable?"
        a1 = "37%"
        a2 = "97%"
        a3 = "67%"
        backfile = "1.gif"  # effinet
        solution = "1a.gif"
        a02 = 1
    elif step == 2:
        question = "Question 2: How much water do Europeans use per day on average?"
        a1 = "50 Liters"
        a2 = "150 Liters"
        a3 = "10 Liters"
        solution = ""
        backfile = "2.gif"  # William Newman
        a02 = 1
    elif step == 3:
        question = "Question 3: Which substance do water companies use to kill bacteria in water?"
        a1 = "Soap"
        a2 = "Citric Acid"
        a3 = "Chlorine"
        solution = ""
        backfile = "3.gif"  # Jacob Vanderheyden
        a03 = 1
    elif step == 4:
        question = "Question 4: How much water is lost due to leakages in Cyprus?"
        a1 = "Around 20%"
        a2 = "Around 50%"
        a3 = "Around 12%"
        solution = ""
        backfile = "4.gif"  # Pete
        a01 = 1
    elif step == 5:
        question = "Question 5: What is the energy cost to deliver water to consumers in Barcelona, Spain?"
        a1 = "7 Million Euros"
        a2 = "700,000 Euros"
        a3 = "70 Million Euros"
        solution = ""
        backfile = "5.gif"  #
        a01 = 1
    elif step == 6:
        question = "Question 6: How water utilities detect leakages?"
        a1 = "Using many sensors"
        a2 = "Monitoring night flow increase"
        a3 = "Consumer complaints"
        solution = ""
        backfile = "6.gif"  #
        a02 = 1
    elif step == 7:
        question = "Question 7: A water tank is equivalent to:"
        a1 = "A battery"
        a2 = "A lamp"
        a3 = "A switch"
        backfile = "7.gif"  #
        solution = ""
        a01 = 1
    elif step == 8:
        question = "Question 8: The most energy consumption in a water network goes for"
        a1 = "Disinfection System"
        a2 = "ICT Functions"
        a3 = "Pump operations"
        solution = ""
        backfile = "8.gif"  #
        a03 = 1
    elif step == 9:
        question = "Question 9: How can we reduce energy usage in water networks?"
        a1 = "Use pumps during off-peak hours"
        a2 = "Use ground water"
        a3 = "Increase water prices"
        solution = ""
        backfile = "9.gif"  #
        a01 = 1
    elif step == 10:
        question = "Question 10: In the future, water utilities will"
        a1 = "Communicate information to the consumers"
        a2 = "Get information directly from the consumers"
        a3 = "Both of the above"
        solution = ""
        backfile = "10.gif"  #
        a03 = 1

    photo = PhotoImage(file=backfile)
    wback = Label(TL, image=photo)
    wback.photo = photo
    wback.place(x=-5, y=-5)

    photo = PhotoImage(file="logo2.gif")
    wlogo = Label(TL, image=photo)
    wlogo.photo = photo
    wlogo.place(x=1050, y=100)

    l = Label(TL, text=question, font="Verdana 20", bg="Plum", pady=10)
    l.pack(side=TOP)

    b2 = Button(TL, text=a1, bd=10, width=35, font="Verdana 11 bold", bg="Darkred", fg="White",
                command=lambda: e_correct1(root, TL, a01, counter, step,solution))
    b2.pack()
    b2.place(x=500, y=250)
    b3 = Button(TL, text=a2, bd=10, width=35, font="Verdana 11 bold", bg="Darkred", fg="White",
                command=lambda: e_correct1(root, TL, a02, counter, step,solution))
    b3.pack()
    b3.place(x=500, y=340)
    b2 = Button(TL, text=a3, bd=10, width=35, font="Verdana 11 bold", bg="Darkred", fg="White",
                command=lambda: e_correct1(root, TL, a03, counter, step, solution))
    b2.pack()
    b2.place(x=500, y=430)
    # ex = Button(window2, text="EXIT", bd=1, width=6, font="Verdana 10 bold", bg="red", fg="White",
    #            command=lambda: exit2(window1))
    #ex.pack()
    #ex.place(x=1168, y=725)
    ex1 = Button(TL, text="RESET", bd=1, width=8, font="Verdana 10 bold", bg="red", fg="White",
                 command=lambda: TL.destroy())
    ex1.pack()
    ex1.place(x=1048, y=725)


def e_correct1(root, TL, a, counter, step, solution):
    #t = Text(TL, text=solution, font="Verdana 20", bg="Plum")
    #t.place(100,20)
    #l = Label(TL, text=solution, font="Verdana 20", bg="Plum", pady=10)
    #l.pack(side=BOTTOM)

    photo = PhotoImage(file=solution)
    wsol = Label(TL, image=photo)
    wsol.photo = photo
    wsol.place(x=100, y=100)

    if a == 1:
        counter += 1
        photo = PhotoImage(file="cr.gif")
        w = Label(TL, image=photo)
        w.photo = photo
        w.place(x=570, y=60)
    else:
        photo = PhotoImage(file="wr.gif")
        w = Label(TL, image=photo)
        w.photo = photo
        w.place(x=570, y=60)
    if step < 10:
        TL.update()
        sleep(3)
        e_q1(root, counter, step + 1)
        TL.destroy()
    else:
        sleep(0.5)
        backfile = '0.gif'
        photo = PhotoImage(file=backfile)
        w = Label(TL, image=photo)
        w.photo = photo
        w.place(x=-5, y=-5)
        ex = Button(TL, text="EXIT", bd=1, width=6, font="Verdana 10 bold", bg="red", fg="White",
                    command=lambda: root.destroy())
        ex.pack()
        ex.place(x=1168, y=725)
        # t= lambda: reset(w)
        #window2.after(1500, t)


def start():
    root = Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    photo = PhotoImage(file="0.gif")
    w = Label(root, image=photo)
    w.photo = photo
    w.place(x=-5, y=-5)
    photo = PhotoImage(file="logo2.gif")
    w = Label(root, image=photo)
    w.photo = photo
    w.place(x=1050, y=100)
    counter = 0
    step = 1
    b2 = Button(root, text='Begin Smart Water Challenge!', bd=10, height=1, font="Verdana 14 bold", bg="Black",
                fg="White", command=lambda: e_q1(root, counter, step), compound=CENTER)
    b2.pack()
    b2.place(x=500, y=350)
    ex = Button(root, text="EXIT", bd=1, width=6, font="Verdana 10 bold", bg="red", fg="White",
                command=lambda: root.destroy())
    ex.pack()
    ex.place(x=1168, y=725)
    root.mainloop()


start()