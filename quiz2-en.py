# -*- coding: cp1253 -*-
from tkinter import *
from time import sleep

var = 0


def create(w, x1, y1):
    w.place(x=x1, y=y1)


def erase(w):
    w.destroy()


def reset(w):
    w.destroy()
    start()


def exit(w):
    w.destroy()


def callback(event):
    print("clicked at", event.x, event.y)


def clicked(event):
    global var
    var = 1


def nextquestion(TL, root, counter, step):
    step += 1
    if step <= 10:
        e_q1(root, counter, step)
        TL.destroy()
    else:
        TL.destroy()
        endscreen(root, counter)


def endscreen(root, counter):
    TL = Toplevel()
    w, h = TL.winfo_screenwidth(), TL.winfo_screenheight()
    TL.overrideredirect(1)
    TL.geometry("%dx%d+0+0" % (w, h))
    photo = PhotoImage(file="final.gif")
    wback = Label(TL, image=photo)
    wback.photo = photo
    wback.place(x=-5, y=-5)

    ex = Button(TL, text="Exit", bd=1, width=6, font="Verdana 10 bold", bg="red", fg="White",
                command=lambda: restart(TL, root))
    ex.pack()
    ex.place(x=1200, y=725)
    l = Label(TL, text=str(counter)+" out of 10", font="Verdana 80", bg="white", pady=10)
    l.pack(side=TOP)
    if counter >= 9:
        photo = PhotoImage(file="excellent.gif")
    elif counter >= 7:
        photo = PhotoImage(file="welldone.gif")
    elif counter >= 5:
        photo = PhotoImage(file="nicetry.gif")
    else:
        photo = PhotoImage(file="nexttime.gif")
    wlogo = Label(TL, image=photo)
    wlogo.photo = photo
    wlogo.place(x=230, y=200)
    TL.update()


def restart(TL,root):
    counter = 0
    step = 1
    TL.destroy()

    # backfile = 'final.gif'
    #    photo = PhotoImage(file=backfile)
    #    w = Label(TL, image=photo)
    #    w.photo = photo
    #    w.place(x=-5, y=-5)
    #    ex = Button(TL, text="EXIT", bd=1, width=6, font="Verdana 10 bold", bg="red", fg="White",
    #                command=lambda: root.destroy())
    #    ex.pack()
    #    ex.place(x=1168, y=725)
    #    if counter >= 7:
    #        l = Label(TL, text="You got more than 7 questions right, well done!", font="Verdana 20", bg="Plum", pady=10)
    #        l.pack(side=TOP)


def e_q1(root, counter, step):
    global var
    TL = Toplevel()
    w, h = TL.winfo_screenwidth(), TL.winfo_screenheight()
    TL.overrideredirect(1)
    TL.geometry("%dx%d+0+0" % (w, h))
    a01 = 0
    a02 = 0
    a03 = 0
    if step == 1:
        question = "1: What percentage of the total water is not suitable for consumption?"
        a1 = "37%"
        a2 = "97%"
        a3 = "67%"
        backfile = "1.gif"  # effinet
        solution = "1ans.gif"
        a02 = 1
    elif step == 2:
        question = "2: How much water do Europeans consume on average every day?"
        a1 = "60 Liters"
        a2 = "130 Liters"
        a3 = "10 Liters"
        solution = "2ans.gif"
        backfile = "2.gif"  # William Newman
        a02 = 1
    elif step == 3:
        question = "3: What substance is typically used for disinfecting water?"
        a1 = "Soap"
        a2 = "Acid"
        a3 = "Chlorine"
        solution = "3ans.gif"
        backfile = "3.gif"  # Jacob Vanderheyden
        a03 = 1
    elif step == 4:
        question = "4: How much water is typically lost in the EU due to leakages?"
        a1 = "20%"
        a2 = "50%"
        a3 = "12%"
        solution = "4ans.gif"
        backfile = "4.gif"  # Pete
        a01 = 1
    elif step == 5:
        question = "5: What is the percentage of energy used in the US for producing and distributing water?"
        a1 = "7%"
        a2 = "13%"
        a3 = "3%"
        solution = "5ans.gif"
        backfile = "5.gif"  #
        a02 = 1
    elif step == 6:
        question = "6: How water utilities detect hidden leaks?"
        a1 = "With robots"
        a2 = "With water demand increase during the night"
        a3 = "With consumer complaints"
        solution = "6ans.gif"
        backfile = "6.gif"  #
        a02 = 1
    elif step == 7:
        question = "7: A water pump..."
        a1 = "increases pressure"
        a2 = "reduces energy and pressure"
        a3 = "improves water quality"
        backfile = "7.gif"  #
        solution = "7ans.gif"
        a01 = 1
    elif step == 8:
        question = "8: Energy is used by water utilties to: "
        a1 = "disinfect water"
        a2 = "operate computer servers"
        a3 = "operate pumps"
        solution = "8ans.gif"
        backfile = "8.gif"  #
        a03 = 1
    elif step == 9:
        question = "9: How can we reduce energy costs in water utilities?"
        a1 = "Use pumps in off-peak hours "
        a2 = "Increase water price"
        a3 = "Use pumps in peak hours"
        solution = "9ans.gif"
        backfile = "9.gif"  #
        a01 = 1
    elif step == 10:
        question = "10: In the future, water utilities will:"
        a1 = "Send information to consumers"
        a2 = "Receive information from consumers"
        a3 = "All the above"
        solution = "10ans.gif"
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
                command=lambda: e_correct1(root, TL, a01, counter, step, solution))
    b2.pack()
    b2.place(x=500, y=250)
    b3 = Button(TL, text=a2, bd=10, width=35, font="Verdana 11 bold", bg="Darkred", fg="White",
                command=lambda: e_correct1(root, TL, a02, counter, step, solution))
    b3.pack()
    b3.place(x=500, y=340)
    b2 = Button(TL, text=a3, bd=10, width=35, font="Verdana 11 bold", bg="Darkred", fg="White",
                command=lambda: e_correct1(root, TL, a03, counter, step, solution))
    b2.pack()
    b2.place(x=500, y=430)
    # ex = Button(window2, text="EXIT", bd=1, width=6, font="Verdana 10 bold", bg="red", fg="White",
    # command=lambda: exit2(window1))
    # ex.pack()
    # ex.place(x=1168, y=725)
    ex1 = Button(TL, text="Return", bd=1, width=8, font="Verdana 10 bold", bg="red", fg="White",
                 command=lambda: TL.destroy())
    ex1.pack()
    ex1.place(x=1200, y=725)


def e_correct1(root, TL, a, counter, step, solution):
    # t = Text(TL, text=solution, font="Verdana 20", bg="Plum")
    # t.place(100,20)
    # l = Label(TL, text=solution, font="Verdana 20", bg="Plum", pady=10)
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
    if step <= 10:
        #sleep(4)
        if step == 10:
            print("step10")
        TL.update()
        ex1 = Button(TL, text="Next", bd=1, width=10, font="Verdana 12 bold", bg="blue", fg="White",
                     command=lambda: nextquestion(TL, root, counter, step))
        ex1.pack()
        ex1.place(x=180, y=625)


def start():
    global var
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
    b2 = Button(root, text='The Smart Water Challenge!', bd=10, height=1, font="Verdana 14 bold", bg="Black",
                fg="White", command=lambda: e_q1(root, counter, step), compound=CENTER)
    b2.pack()
    b2.place(x=500, y=350)
    ex = Button(root, text="Exit", bd=1, width=6, font="Verdana 10 bold", bg="red", fg="White",
                command=lambda: root.destroy())
    ex.pack()
    ex.place(x=1200, y=725)
    root.mainloop()


start()