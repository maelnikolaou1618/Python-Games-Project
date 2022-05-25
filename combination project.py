from tkinter import *
import random
import time
#from tkinter.ttk import *
from tkinter import messagebox

window =Tk()
window.title("Python Games")
window.geometry('600x600')
window.config(bg='#161032')
timeleft=30
score = 0

questlist = ['f(x)=1/(x+1) is defined:\n1.R\n2.Z\n3.R-{-1}\n4.R-{1}', '3'] \
        , ['f(x)=19/(23x-1) is defined:\n1.R\n2.R-{1/23}\n3.R-{23}\n4.R-{-1/23}', '2'] \
        , ['If a<b and c<0 then:\n1.ac>bc\n2.ac<bc\n3.all of the above\n4.none of the above', '1'] \
        , ['If n=0(mod2) and a<b then:\n1.a^n<b^n\n2.a^n>b^n\n3.the first one if a,b>0\n4.the second one if a,b>0', '3']

def colorgame():
    for widget in window.winfo_children():
        widget.destroy()
    global timeleft
    colours = ["Red", "Blue", "Green", "Pink", "Yellow", "Orange", "Brown", "White", "Purple"]
    score = 0
    timeleft = 30
    window.geometry("650x350")
    def startgame(event):
        global timeleft
        if timeleft == 30:
            countdown()
        nextColour()

    def countdown():
        global timeleft
        if timeleft > 0:
            timeleft -= 1
            timeLabel.config(text="Time left: " + str(timeleft) +' s')
            timeLabel.after(1000, countdown)

    def nextColour():
        global score, timeleft, txt
        if timeleft > 0:
            if e.get().lower() == colours[1].lower():
                score += 1
            e.delete(0, END)
            random.shuffle(colours)
            label.config(fg=str(colours[1]), text=str(colours[0]))
            scoreLabel.config(text="Score: " + str(score))
        else:
            popup = Tk()
            popup.geometry("200x100")
            popup.title("SCORE")
            txt = Label(popup, text="Your score was: " + str(score), font=('Helvetica', 12))
            txt.pack()

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        window.geometry('600x600')
        lbldown = Label(window, text="Python Games", font=('Helvetica', 35), bg='#161032', fg='light blue')
        lbldown.place(x=150, y=500)
        lblchoice = Label(window, text="SELECT THE GAME YOU LIKE", font=('Helvetica', 15), bg='#161032', fg='light blue')
        lblchoice.place(x=160, y=20)
        btn1 = Button(window, text='Color Game', font=('Helvetica', 15), bg='#FAFF81', fg='#E06D06', command=colorgame)
        btn1.place(x=245, y=100)
        btn2 = Button(window, text='Math Game', font=('Helvetica', 15), bg='#FAFF81', fg='#E06D06', command=mathgame)
        btn2.place(x=245, y=180)
        btn3 = Button(window, text='Speed Game', font=('Helvetica', 15), bg='#FAFF81', fg='#E06D06', command=speedgame)
        btn3.place(x=238, y=260)


    instructions = Label(window, text="Type in the colour of the words, not the word text!", fg='#FAFF81', font=('Helvetica', 20), bg='#161032')
    instructions.pack()
    scoreLabel = Label(window, text="Press enter to start.", font=('Helvetica', 21), bg='#161032', fg='#FAFF81')
    scoreLabel.pack()
    timeLabel = Label(window, text="Time left: " + str(timeleft) + " s", font=('Helvetica', 21), bg='#161032', fg='#E06D06')
    timeLabel.pack()
    label = Label(window, font=('Helvetica', 60), bg='#161032')
    label.pack()
    e = Entry(window, justify='center', fg='#E06D06')
    window.bind('<Return>', startgame)
    e.pack()
    e.focus_set()
    btn_back1 = Button(window, text='BACK', font=('Helvetica', 15), bg='#FAFF81', fg='blue', command=back)
    btn_back1.place(x=53, y=300)

def mathgame():
    global i, cor, wr
    i = 0
    cor = 0
    wr = 0
    window.geometry('500x500')
    for widget in window.winfo_children():
        widget.destroy()

    questlist = ['f(x)=1/(x+1) is defined:\n1.R\n2.Z\n3.R-{-1}\n4.R-{1}', '3'] \
        , ['f(x)=19/(23x-1) is defined:\n1.R\n2.R-{1/23}\n3.R-{23}\n4.R-{-1/23}', '2'] \
        , ['If a<b and c<0 then:\n1.ac>bc\n2.ac<bc\n3.all of the above\n4.none of the above', '1'] \
        , ['If n=0(mod2) and a<b then:\n1.a^n<b^n\n2.a^n>b^n\n3.the first one if a,b>0\n4.the second one if a,b>0', '3']

    def check(*args):
        global i, cor, wr, questlist, lblscore, txtname, y
        if txt.get() == str(questlist[i][1]):
            cor += 1
            lblscore.configure(text="Score:" + str(cor) + "/4")
            messagebox.showinfo('Answer', 'Correct!')
        else:
            messagebox.showinfo('Answer', 'Wrong...')
            wr += 1
        if i < 3:
            i += 1
            lbll.configure(text=questlist[i][0])
            lbll.update()
        else:
            if cor == 0:
                messagebox.showinfo('Results', 'Correct:' + str(cor) + '\nWrong:' + str(wr) + "\nNext time..." + y)
            elif cor < 3:
                messagebox.showinfo('Results', 'Correct:' + str(cor) + '\nWrong:' + str(wr) + "\nNice try " + y + "!")
            elif cor < 4:
                messagebox.showinfo('Results', 'Correct:' + str(cor) + '\nWrong:' + str(wr) + "\nGood job " + y + "!")
            else:
                messagebox.showinfo('Results', 'Correct:' + str(cor) + '\nWrong:' + str(wr) + "\nGongrats " + y + "!")
        txt.delete(0, 'end')

    def start():
        global questlist, lbll, txt, cor, lblscore, y
        lbl.destroy()
        btn.destroy()
        y = txtname.get()
        txtname.destroy()
        lblname.destroy()
        lbll = Label(window, text=questlist[i][0], width=31, height=5, font=('Comic Sans', 20), fg='#FAFF81',
                     bg='#161032')
        lbll.pack()
        txt = Entry(window, font=('Comic Sans', 20), width=19, justify='center', fg='#E06D06')
        txt.pack()
        lblscore = Label(window, text="Score:" + str(cor) + "/4", width=31, height=5, font=('Comic Sans', 20),
                         fg='light blue', bg='#161032')
        lblscore.pack()
        window.bind('<Return>', check)

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        window.geometry('600x600')
        lbldown = Label(window, text="Python Games", font=('Helvetica', 35), bg='#161032', fg='light blue')
        lbldown.place(x=150, y=500)
        lblchoice = Label(window, text="SELECT THE GAME YOU LIKE", font=('Helvetica', 15), bg='#161032', fg='light blue')
        lblchoice.place(x=160, y=20)
        btn1 = Button(window, text='Color Game', font=('Helvetica', 15), bg='#FAFF81', fg='#E06D06', command=colorgame)
        btn1.place(x=245, y=100)
        btn2 = Button(window, text='Math Game', font=('Helvetica', 15), bg='#FAFF81', fg='#E06D06', command=mathgame)
        btn2.place(x=245, y=180)
        btn3 = Button(window, text='Speed Game', font=('Helvetica', 15), bg='#FAFF81', fg='#E06D06', command=speedgame)
        btn3.place(x=238, y=260)

    lbl = Label(window, text='Welcome to Math Quiz!', width=25, height=3, font=('Comic Sans', 20), fg='#FAFF81',
                bg='#161032')
    lbl.pack()
    lblname = Label(window, text='Your name is:', width=21, height=2, font=('Comic Sans', 20), fg='light blue',
                    bg='#161032')
    lblname.pack()
    txtname = Entry(window, text="Your name is:", font=('Comic Sans', 20), width=15, justify='center', fg='#E06D06')
    txtname.pack()
    btn = Button(window, text="START", width=11, height=2, font=('Comic Sans', 20), fg='#FAFF81', bg='#161032',
                 command=start, relief="sunken")
    btn.pack()
    btn_back2 = Button(window, text='BACK', font=('Helvetica', 15), bg='#FAFF81', fg='blue', command=back)
    btn_back2.place(x=53, y=420)


def speedgame():
    for widget in window.winfo_children():
        widget.destroy()
    global txt, lbltime,lblsent,lblpoints,sentap, tleft,points,list
    window.geometry("720x450")
    tleft = 50
    points = 0
    list = ["Did Jerry win a lottery?", "The subtle art of mathematics", "I never dreamed that I would win.",
            "She refused his proposal.", "Clean up the room.", "Once bitten twice shy",
            "The early bird catches the worm", "Too many cooks spoil the broth.", "Better safe than sorry",
            "Acts speak louder than words.", "Come in, the door's open.", "Look up at the stars...", "Study for exams",
            "Do your homework now!"]
    sentap = random.choice(list)
    lblinstr = Label(window,
                     text="Type what you see. \nPress '0' to start and 'Enter' to submit your text. \nTime: 50 seconds",
                     width=45, height=5, font=('New York Times', 20), fg='dark blue', bg='light blue')
    lblinstr.grid(row=0, column=0, columnspan=2)
    lblsent = Label(window, text="", width=30, height=3, font=('Comic Sans', 20), fg="#E06D06", bg='#161032')
    lblsent.grid(row=3, column=0, columnspan=2)
    txt = Entry(window, font=('Comic Sans', 15), width=40, fg="#E06D06", justify='center')
    txt.grid(row=4, column=0, columnspan=3)
    lbltime = Label(window, text="Time left: " + str(tleft), width=15, height=1, font=('Comic Sans', 15),
                    fg='#E06D06', bg='#FAFF81')
    lbltime.place(x=170, y=350)
    lblpoints = Label(window, text="Score: " + str(points), width=15, height=1, font=('Comic Sans', 15), fg='#E06D06',
                      bg='#FAFF81')
    lblpoints.place(x=370, y=350)


    def time(*args):
        global tleft, points, lbltime
        tleft = int(tleft) - 1
        lbltime.configure(text="Time left: " + str(tleft))
        start()
        if tleft <= 10:
            lbltime.configure(fg="red", font=('Comic Sans', 15))
        if tleft <= 0:
            lbltime.configure(text="Time's up!", fg="dark blue")
            lblsent.configure(text="")
            txt.destroy()
            lblinstr.configure(text="GAME OVER... \nWere you fast enough?")

    def start(*args):
        lbltime.after(1000, time)
        window.bind("<Return>", shuffle)

    def shuffle(*args):
        global txt, answer, sentap, lblsent, list, points
        answer = txt.get()
        if answer == sentap:
            points = points + 1
            lblpoints.configure(text="Score: " + str(points))
        list.remove(sentap)
        sentap = random.choice(list)
        txt.delete(0, 'end')
        lblsent.configure(text=str(sentap))

    def back():
        for widget in window.winfo_children():
            widget.destroy()
        window.geometry('600x600')
        lbldown = Label(window, text="Python Games", font=('Helvetica', 35), bg='#161032', fg='light blue')
        lbldown.place(x=150, y=500)
        lblchoice = Label(window, text="SELECT THE GAME YOU LIKE", font=('Helvetica', 15), bg='#161032', fg='light blue')
        lblchoice.place(x=160, y=20)
        btn1 = Button(window, text='Color Game', font=('Helvetica', 15), bg='#FAFF81', fg='#E06D06', command=colorgame)
        btn1.place(x=245, y=100)
        btn2 = Button(window, text='Math Game', font=('Helvetica', 15), bg='#FAFF81', fg='#E06D06', command=mathgame)
        btn2.place(x=245, y=180)
        btn3 = Button(window, text='Speed Game', font=('Helvetica', 15), bg='#FAFF81', fg='#E06D06', command=speedgame)
        btn3.place(x=238, y=260)

    btn_back3 = Button(window, text='BACK', font=('Helvetica', 15), bg='#FAFF81', fg='blue', command=back)
    btn_back3.place(x=53, y=400)

    window.bind("<0>", start)


lbldown = Label(window, text="Python Games", font=('Helvetica', 35), bg='#161032', fg='light blue')
lbldown.place(x=150, y=500)
lblchoice = Label(window, text="SELECT THE GAME YOU LIKE", font=('Helvetica', 15), bg='#161032', fg='light blue')
lblchoice.place(x=160, y=20)
btn1 = Button(window, text='Color Game', font=('Helvetica', 15), bg='#FAFF81', fg='#E06D06', command=colorgame)
btn1.place(x=245, y=100)
btn2 = Button(window, text='Math Game', font=('Helvetica', 15), bg='#FAFF81', fg='#E06D06', command=mathgame)
btn2.place(x=245, y=180)
btn3 = Button(window, text='Speed Game', font=('Helvetica', 15), bg='#FAFF81', fg='#E06D06', command=speedgame)
btn3.place(x=238, y=260)



window.mainloop()