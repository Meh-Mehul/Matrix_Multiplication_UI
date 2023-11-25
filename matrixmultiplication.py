# matrix multiplication with some UI
from tkinter import *
import tkinter as tk
import numpy as np
from tkinter import messagebox


def main():
    def allow_multiply(*args, **kwargs):
        def final_multiply():
            mat1_nondem = np.array([])
            for z in range(arg1*arg2):
                need = int(ar1[z].get())
                mat1_nondem = np.append(mat1_nondem, need)
            mat2_nondem = np.array([])
            for i in range(arg1*arg3):
                need1 = int(ar2[i].get())
                mat2_nondem = np.append(mat2_nondem, need1)
            mat1 = mat1_nondem.reshape(arg2, arg1)
            mat2 = mat2_nondem.reshape(arg1, arg3)
            
            ar10 = mat1

            ar20 = mat2

            ar3 = np.zeros(len(ar10)*len(ar20[0]))
            ar4 = ar3.reshape(len(ar10),len(ar20[0]))



            for i in range(len(ar10)):
                for x in range(len(ar20[0])):
                    for j in range(len(ar20)):
                        ar4[i,x] = ar4[i,x] + ar10[i,j]*ar20[j,x] 
            
            
            winner = Tk()
            winner.title('Result')
            winner.geometry('+850+250')
            ans = tk.Label(winner, text = ar4, font=('Times New Roman', 20)).grid(row=arg1 + arg2 + 3, column =0, columnspan = arg3)



            winner.resizable(False, False)
            winner.mainloop()



        arg1 = int(e1.get())
        arg2 = int(e2.get())
        arg3 = int(e3.get())
        root.destroy()
        win = Tk()
        win.title('Enter details of matrices')
        win.geometry('+850+250')
        f1 = tk.Frame(win).grid(row=0, column=0)
        Label0 = tk.Label(f1, text='Matrix 1:').grid(row=0, column=0, columnspan=arg3)
        ar1 = []
        for y in range(arg2):
            for x in range(arg1):
                ar1.append(tk.Entry(f1, width=2, borderwidth=2))
                ar1[-1].grid(row= y +1, column=x)
        Label1 = tk.Label(f1, text="Matrix 2:").grid(row=arg2+1, column=0, columnspan=arg3)
        ar2 = []
        for y in range(arg1):
            for x in range(arg3):
                ar2.append(tk.Entry(f1, width=2, borderwidth=2))
                ar2[-1].grid(row=y + arg2 + 2, column=x)
        B2 = tk.Button(f1, text='Submit data', command=final_multiply).grid(row= arg1+arg2+2, column=0, columnspan=arg3)
    root = Tk()
    root.title('Matrix Multiplication')
    root.geometry('500x150+800+400')
    Lable0 = tk.Label(root, text='Enter No. of columns in matrix 1:    ', font=('arial', 20)).grid(row=0, column = 0)
    Lable1 = tk.Label(root, text='Enter No. of rows in matrix 1: ', font=('arial', 20)).grid(row=1, column = 0)
    Lable2 = tk.Label(root, text='Enter No. of columns in matrix 2: ', font=('arial', 20)).grid(row=2, column = 0)

    e1 = tk.Entry(root, width=2, borderwidth=2)
    e1.grid(row=0, column=1)
    
    e2 = tk.Entry(root, width=2, borderwidth=2)
    e2.grid(row=1, column=1)

    e3 = tk.Entry(root, width=2, borderwidth=2)
    e3.grid(row=2, column=1)

    B1 = tk.Button(root, text="Submit", command=allow_multiply).grid(row=3, column=0, columnspan=2)
    






    root.resizable(False,False)
    root.mainloop()

main()