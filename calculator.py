from tkinter import *
import math
class Calculator:
    root=None
    width=425
    height=475
    entryHeight=90
    entryWidth=width-2
    buttonSize=70
    def __init__(self):
        self.root=Tk()
        self.root.title("Calculator")
        self.root.geometry(str(self.width)+'x'+str(self.height))
        self.output=Entry(self.root,justify='right',font=('Roboto',25),state='disabled',disabledbackground='white',disabledforeground='black')
        self.output.place(x=1,y=1,height=self.entryHeight,width=self.entryWidth)
        self.output.config({'state':'normal'})
        self.output.insert(0,'0')
        self.output.config({'state':'disabled'})
        self.input=Entry(self.root,justify='right',font=('Roboto',25),state='disabled',disabledbackground='white',disabledforeground='black')
        self.input.place(x=1,y=self.entryHeight+2,height=self.entryHeight,width=self.entryWidth)
        self.input.config({'state':'normal'})
        self.input.insert(0,'0')
        self.input.config({'state':'disabled'})
        self.addButtons(self.root,self.entryHeight*2+5,self.buttonSize)
    def addButtons(self,root,start,size):
        buttons={
                '7':{'x':0,'y':0,'width':1,'height':1},'8':{'x':1,'y':0,'width':1,'height':1},'9':{'x':2,'y':0,'width':1,'height':1},'C':{'x':3,'y':0,'width':1,'height':1,'command':self.backspace},'AC':{'x':4,'y':0,'width':1,'height':1,'command':lambda :self.clear(self.input),'activebackground':'red','activeforeground':'white'},'ceil':{'x':5,'y':0,'width':1,'height':1,'command':self.ceilup},
                '4':{'x':0,'y':1,'width':1,'height':1},'5':{'x':1,'y':1,'width':1,'height':1},'6':{'x':2,'y':1,'width':1,'height':1},'+':{'x':3,'y':1,'width':1,'height':1},'-':{'x':4,'y':1,'width':1,'height':1},'floor':{'x':5,'y':1,'width':1,'height':1,'command':self.floorup},
                '1':{'x':0,'y':2,'width':1,'height':1},'2':{'x':1,'y':2,'width':1,'height':1},'3':{'x':2,'y':2,'width':1,'height':1},'*':{'x':3,'y':2,'width':1,'height':1},'/':{'x':4,'y':2,'width':1,'height':1},'*':{'x':3,'y':2,'width':1,'height':1},'=':{'x':5,'y':2,'width':1,'height':2,'command':self.equal,'activebackground':'blue','activeforeground':'white'},
                '0':{'x':0,'y':3,'width':1,'height':1},'00':{'x':1,'y':3,'width':2,'height':1},'%':{'x':3,'y':3,'width':1,'height':1},'pow':{'x':4,'y':3,'width':1,'height':1,'command':lambda m='**':self.insert(m)},}
        for i in buttons:
            b=Button(root,text=i,command=lambda m=i:self.insert(m),font=('Roboto',20))
            if 'command' in buttons[i]:
                b.config({'command':buttons[i]['command']})
            if 'activebackground' in buttons[i]:
                b.config({'activebackground':buttons[i]['activebackground']})
            if 'activeforeground' in buttons[i]:
                b.config({'activeforeground':buttons[i]['activeforeground']})
            b.place(x=2+size*buttons[i]['x'],y=start+buttons[i]['y']*size,width=buttons[i]['width']*size,height=buttons[i]['height']*size)
    def insert(self,v):
        if (self.input.get()=='0' and v in '00') or len(self.input.get())>20:
            return
        self.input.config({'state':'normal'})
        if self.input.get()=='0':
            if v[0] in '123456789':
                self.input.delete(0)
            if v in '+-**/%':
                if self.output.get() not in 'Value Error' and self.output.get() not in 'Division By Zero':
                    self.insert(self.output.get())
                    self.input.config({'state':'normal'})
        if len(self.input.get()) and (self.input.get()[-1] in '+-/**%' and v in '+-/%**'):
            self.input.delete(len(self.input.get())-1)
            if self.input.get()[-1]=='*':
                self.input.delete(len(self.input.get())-1)
        self.input.insert(END,v)
        self.input.config({'state':'disabled'})
    def backspace(self):
        if self.input.get()=='0':
            return
        self.input.config({'state':'normal'})
        self.input.delete(len(self.input.get())-1)
        if len(self.input.get())==0:
            self.insert(0)
        self.input.config({'state':'disabled'})
    def clear(self,el):
        el.config({'state':'normal'})
        el.delete(0,END)
        el.insert(0,'0')
        el.config({'state':'disabled'})
    def equal(self):
        self.clear(self.output)
        self.output.config({'state':'normal'})
        self.output.delete(0,END)
        try:
            self.output.insert(0,eval(self.input.get()))
        except ZeroDivisionError:
            self.output.insert(0,'Division By Zero')
        except:
            self.output.insert(0,'Value Error')
        self.clear(self.input)
        self.output.config({'state':'disabled'})
    def floorup(self):
        v=float(self.output.get())
        self.clear(self.output)
        self.output.config({'state':'normal'})
        self.output.delete(0)
        self.output.insert(END,math.floor(v))
        self.output.config({'state':'disabled'})
    def ceilup(self):
        v=float(self.output.get())
        self.clear(self.output)
        self.output.config({'state':'normal'})
        self.output.delete(0)
        self.output.insert(END,math.ceil(v))
        self.output.config({'state':'disabled'})
        
c=Calculator()
c.root.mainloop()
