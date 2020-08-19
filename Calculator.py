from tkinter import *
import tkinter.messagebox as msg


def input1(event):
    text = event.widget.cget("text")
    # print(text)

    if text == "=":
        try:
            # try evaluating the resulting str
            result = eval(str(value.get()))
            value.set(result)
        except Exception as e:
            # if failed its as error
            a=msg.showerror("Error","Error In Expresion")
            value.set("Error")


    elif text == "DEL":
        try:
            fullstring = value.get()
            # we are replacing the last string item[-1] with blank or ""
            # String slicing method
            newstring = fullstring.replace(fullstring[-1], "")
            value.set(newstring)

            # print(newstring)
            entry1.update()
        except Exception as e:
            a = msg.showerror("Error", "Error Occured")

    elif text == "C":
        """"This will clear the screen"""
        value.set("")
        entry1.update()
    else:
        """if 1st input is 5, 2nd is 4 or + , both will be converted into string ie 54 or 5+"""
        value.set(value.get() + text)
        entry1.update()
        # print(value.get())


root = Tk()
#root.geometry("430x550")
root.geometry("430x500")
root.minsize(430,450)
root.maxsize(500,500)
root.title("Calculator by Anshul")
root.wm_iconbitmap("newCalc.ico")
root.config(background="orange")
value = StringVar() # four variable
entryframe = Frame(root, borderwidth=20, relief=SUNKEN)
entry1 = Entry(entryframe, font="lucida 27 bold", textvariable=value)
entry1.pack()
entryframe.pack(pady=35, padx=5,fill=X)

buttonframe = Frame(root,borderwidth=20)

list1 = ["9", "8", "7", "C", "6", "5", "4", "/", "3", "2", "1", "*", "00", "0", ".", "-", "%", "DEL", "=", "+"]
i = 0
for item in list1:
    # here width of button means 1 text width
    button1 = Button(buttonframe, text=item, font="lucida 20 bold", padx=35, width=1,bg="#000000",fg="#FFFFFF")
    button1.grid(row=int(i / 4), column=i % 4) # divided by four because
    i+=1
    button1.bind("<Button-1>", input1)

buttonframe.pack()

root.mainloop()
