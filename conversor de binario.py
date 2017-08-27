import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label1=tk.Label(self)
        self.label1['text']='numero'
        self.label1.grid(row=0,column=0)
        self.label2=tk.Label(self)
        self.label2['text']='base'
        self.label2.grid(row=1,column=0)
        self.numero=tk.Entry(self)
        self.numero.grid(row=0,column=1)
        self.numero2=tk.Entry(self)
        self.numero2.grid(row=1,column=1)
        self.button=tk.Button(self)
        self.button['text']='converter'
        self.button.grid(row=2,column=0)
        self.button['command']=lambda:self.change(self.numero.get(),self.numero2.get())
        self.result=tk.Label(self)
        self.result.grid(row=2,column=1)
        self.button2=tk.Button(self)
        self.button2['text']='reset'
        self.button2.grid(row=3,column=0)
        self.button2['command']=lambda:self.change(self.reset())
    def hexa(self,num):
        return {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}[num]
    def change(self,num,base):
        bina=[]
        try:
            num=int(num)
            base=int(base)
        except:
            erro=messagebox.showinfo("erro" , "use somente numeros")
            
        while num>0:
            if num%base<=9:
                bina.append(int(num%base))
            else:
                i=num%base
                bina.append(str(self.hexa(i)))
            num=(num-num%base)/base
             #print(i)
        bina.reverse()
        self.result['text']=(str(bina))
        
    def reset(self):
        self.numero.delete(0, 'end')
        self.numero2.delete(0, 'end')
        self.result['text']=' '


root = tk.Tk()
app = Application(master=root)
app.mainloop()


