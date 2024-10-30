from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FF6969"
RED = "#C80036"
GREEN = "#219C90"
YELLOW = "#FEFBD8"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps
    window.after_cancel(timer)
    reps = 0
    timer_label.config(text="Timer",font=(FONT_NAME,50),fg=GREEN,bg=YELLOW)
    canvas.itemconfig(timer_text,text=f"00:00")
    check_marks.config(text="")
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    #print(reps)
    text=""
    color=GREEN
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps==8:
        sec=long_break_sec
        text="Break"
        color=RED
        
    elif reps%2==0:
        sec=short_break_sec
        text="Break"
        color=PINK
        
    else:
        sec=work_sec
        text="Work"
        color=GREEN
    
    timer_label.config(text=f"{text}",fg=color)
    count_down(sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count): 
    global timer
    count_min = math.floor(count/60)
    count_sec =count%60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
      
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_sessions= math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)
        
# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="day28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text=canvas.create_text(100,130, text="00.00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


timer_label = Label(text="Timer",font=(FONT_NAME,50),fg=GREEN,bg=YELLOW)
timer_label.grid(column=1,row=0)


start_button=Button(text="Start",highlightthickness=0,command=start_timer,height=2,width=10,bg=GREEN,fg="white",font=(FONT_NAME,15,"bold"))
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",highlightthickness=0,command=timer_reset,height=2,width=10,bg=RED,fg="white",font=(FONT_NAME,15,"bold"))
reset_button.grid(column=2,row=2)

check_marks = Label(fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)






window.mainloop()