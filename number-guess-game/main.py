from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox
import random

# 기본 설정
trial = 0
success = False


def callback(event):
    guess()


# 예측 클래스
def guess():
    global random_num, trial, success

    if success:
        tk.messagebox.showerror("check", "success!")
        return

    mynum = str(num_entry.get())
    if mynum == "":
        tk.messagebox.showerror("check", "Enter a number!")
        num_entry.focus()
        return
    if trial < 6:  # 시도횟수가 7보다 작을시
        trial += 1  # 시도횟수 1씩 증가
        if random_num == mynum:  # 만약에 랜덤숫자와 본인의 숫자가 같다면
            bottom_label['text'] = "(%d try) success" % trial
            main_label = tk.Label(frame30, image=IUimg, pady=20)
            main_label.grid(row=0, column=0)
            success = True
        elif random_num > mynum:  # 만약에 랜덤숫자가 본인의 숫자보다 크다면
            bottom_label['text'] = "(%d try) Up" % trial
            num_entry.delete('0', tk.END)
            num_entry.focus()
        elif random_num < mynum:  # 만약에 랜덤숫자보다 본인의 숫자가 크다면
            bottom_label['text'] = "(%d try) Down" % trial
            num_entry.delete('0', tk.END)
            num_entry.focus()
        print(mynum)
    elif trial == 6:  # 시도횟수가 7이랑 같을시
        trial += 1
        if random_num == mynum:
            bottom_label['text'] = "(%d try) success" % trial
            main_label = tk.Label(frame30, image=IUimg, pady=20)
            main_label.grid(row=0, column=0)
            success = True
        elif random_num > mynum:
            bottom_label['text'] = "(%d try (fail)) Up" % trial
            main_label = tk.Label(frame30, image=faimg, pady=20)
            main_label.grid(row=0, column=0)
            num_entry.focus()
        elif random_num < mynum:
            bottom_label['text'] = "(%d try (fail)) Down" % trial
            main_label = tk.Label(frame30, image=faimg, pady=20)
            main_label.grid(row=0, column=0)
            num_entry.focus()
        print(mynum)
    else:  # 그 외에
        trial += 1
        if random_num == mynum:
            bottom_label['text'] = "(%d try (fail)) success" % trial
            main_label = tk.Label(frame30, image=faimg, pady=20)
            main_label.grid(row=0, column=0)
            success = True
        elif random_num > mynum:
            bottom_label['text'] = "(%d try (fail)) Up" % trial
            main_label = tk.Label(frame30, image=faimg, pady=20)
            main_label.grid(row=0, column=0)
            num_entry.delete('0', tk.END)
            num_entry.focus()
        elif random_num < mynum:
            bottom_label['text'] = "(%d try (fail)) Down" % trial
            main_label = tk.Label(frame30, image=faimg, pady=20)
            main_label.grid(row=0, column=0)
            num_entry.delete('0', tk.END)
            num_entry.focus()
        print(mynum)


#초기화 클래스
def reset():
    global random_num, trial, success
    random_num = str(random.randrange(1, 100))
    trial = 0
    success = False
    print(random_num)
    bottom_label["text"] = ""
    num_entry.delete('0', tk.END)
    main_label = tk.Label(frame30, image=grimg, pady=20)
    main_label.grid(row=0, column=0)


window = tk.Tk()
window.title("Number guessing game")
window.geometry("900x900")  # 550x400

frame1 = tk.Frame(window, pady="10")
frame1.pack()

frame2 = tk.Frame(window, pady=10)
frame2.pack()

frame3 = tk.Frame(window)
frame3.pack()

frame4 = tk.Frame(window)
frame4.pack()

# 칸 채우기 용
frame5 = tk.Frame(window)
frame5.pack()
frame6 = tk.Frame(window)
frame6.pack()
frame7 = tk.Frame(window)
frame7.pack()
frame8 = tk.Frame(window)
frame8.pack()
frame9 = tk.Frame(window)
frame9.pack()
frame10 = tk.Frame(window)
frame10.pack()
frame11 = tk.Frame(window)
frame11.pack()
frame12 = tk.Frame(window)
frame12.pack()
frame13 = tk.Frame(window)
frame13.pack()
frame14 = tk.Frame(window)
frame14.pack()
frame15 = tk.Frame(window)
frame15.pack()
frame16 = tk.Frame(window)
frame16.pack()
frame17 = tk.Frame(window)
frame17.pack()
frame18 = tk.Frame(window)
frame18.pack()
frame19 = tk.Frame(window)
frame19.pack()
frame20 = tk.Frame(window)
frame20.pack()
frame21 = tk.Frame(window)
frame21.pack()
frame22 = tk.Frame(window)
frame22.pack()
frame23 = tk.Frame(window)
frame23.pack()
frame24 = tk.Frame(window)
frame24.pack()
frame25 = tk.Frame(window)
frame25.pack()
frame26 = tk.Frame(window)
frame26.pack()
frame27 = tk.Frame(window)
frame27.pack()
frame28 = tk.Frame(window)
frame28.pack()
frame29 = tk.Frame(window)
frame29.pack()
frame30 = tk.Frame(window)
frame30.pack()
frame31 = tk.Frame(window)
frame31.pack()
frame32 = tk.Frame(window)
frame32.pack()
frame33 = tk.Frame(window)
frame33.pack()
frame34 = tk.Frame(window)
frame34.pack()
frame35 = tk.Frame(window)
frame35.pack()
frame36 = tk.Frame(window)
frame36.pack()
frame37 = tk.Frame(window)
frame37.pack()
frame38 = tk.Frame(window)
frame38.pack()
frame39 = tk.Frame(window)
frame39.pack()
frame40 = tk.Frame(window)
frame40.pack()
frame41 = tk.Frame(window)
frame41.pack()
frame42 = tk.Frame(window)
frame42.pack()
frame43 = tk.Frame(window)
frame43.pack()
frame44 = tk.Frame(window)
frame44.pack()
frame45 = tk.Frame(window)
frame45.pack()
frame46 = tk.Frame(window)
frame46.pack()
frame47 = tk.Frame(window)
frame47.pack()
frame48 = tk.Frame(window)
frame48.pack()
frame49 = tk.Frame(window)
frame49.pack()

resetButton = tk.Button(frame2,
                        text='Reset',
                        fg='red',
                        bg='white',
                        font="Times 14 bold",
                        command=reset)
resetButton.grid(row=0, column=3)

top_label = tk.Label(
    frame1,
    text="Enter a number 1 to 100 \n You have to get it in 7 times.",
    fg='white',
    bg="skyblue",
    font="Times 18 bold")
top_label.grid(row=0, column=0)

num_label = tk.Label(frame2,
                     text="number : ",
                     fg='blue',
                     font="Times 16 bold",
                     padx=10,
                     pady=10)
num_label.grid(row=0, column=0)
num_entry = tk.Entry(frame2, width="10")
num_entry.grid(row=0, column=1)
num_btn = tk.Button(frame2,
                    text="Enter",
                    fg='green',
                    bg='white',
                    font="Times 14 bold",
                    command=guess)
num_btn.grid(row=0, column=2)

bottom_label = tk.Label(frame3, text="")
bottom_label.grid(row=0, column=0)

made = tk.Label(window,
                text="Made.by : In-Seong Kim",
                fg='black',
                bg='white',
                font="Times 16 bold")
made.pack(side='right')

success_img = Image.open('success.png')  # 아이유 따봉 사진
IUimg = ImageTk.PhotoImage(success_img)
# success_label = tk.Label(frame30, image = IUimg, pady=20)

gray_img = Image.open('gray.png')  # 회색 사진
grimg = ImageTk.PhotoImage(gray_img)
# gray_label = tk.Label(frame30, image = grimg, pady=20)

fail_img = Image.open('fail.png')  # 실패 사진
faimg = ImageTk.PhotoImage(fail_img)
# fail_label = tk.Label(frame30, image = faimg, pady=20)

random_num = str(random.randrange(1, 100))  # 범위 설정
print(random_num)

num_entry.focus()
num_entry.bind('<Return>', callback)

window.mainloop()
