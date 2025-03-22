from tkinter import*

class calculator:

    def __init__(self, root):

        self.root = root
        self.root.title("Calculator")
        self.root.geometry("618x688+400+100")
        self.root.configure(bg  = 'cadet blue')

        self.MainFrame = Frame(self.root, bd = 18, width = 600, height = 670, relief = RIDGE, bg = 'powder blue')
        self.MainFrame.grid()
        self.WidgetFrame = Frame(self.MainFrame, bd = 18, width = 590, height = 660, relief = RIDGE, bg = 'cadet blue')
        self.WidgetFrame.grid()

        self.lbldisplay = Label(self.WidgetFrame, width = 30, height = 2, bg = 'black', fg = 'white', font = ('arial', 20, 'bold'), anchor='e')
        self.lbldisplay.grid (row = 0, column = 0, columnspan = 4, padx = 10, pady = 10) 

        self.input_button = ""

        self.create_button ("←",  1,0)
        self.create_button ("CE", 1,1)
        self.create_button ("C",  1,2)
        self.create_button ("±",  1,3)

        self.create_button ("7",  2,0)
        self.create_button ("8",  2,1)
        self.create_button ("9",  2,2)
        self.create_button ("+",  2,3)

        self.create_button ("4",  3,0)
        self.create_button ("5",  3,1)
        self.create_button ("6",  3,2)
        self.create_button ("-",  3,3)

        self.create_button ("1",  4,0)
        self.create_button ("2",  4,1)
        self.create_button ("3",  4,2)
        self.create_button ("*",  4,3)

        self.create_button (".",  5,0)
        self.create_button ("0",  5,1)
        self.create_button ("=",  5,2)
        self.create_button ("/",  5,3)

    def create_button (self, text, row, column):
        buttonWidget = Button(self.WidgetFrame, text = text, width = 6, height = 2, bd = 4, bg = 'black', fg = 'white', font = ('arial', 20, 'bold'),
                              command = lambda: self.button_click(text))
        buttonWidget.grid(row =row, column = column, padx = 5, pady = 5)
    
    def button_click(self, text):
        if text == "←":
            self.input_button = self.input_button[:-1]
        
        elif text == "CE" or text == "C":
            self.input_button = ""
        
        elif text == "=":
            try:
                self.input_button = str(eval(self.input_button))
            except Exception as e:
                self.input_button = "Error"
        
        elif text == "±":
            if self.input_button:
                if self.input_button[0] == '-':
                   self.input_button = self.input_button[1:]
                else:
                   self.input_button = '-' + self.input_button
        
        else:
            self.input_button += text
            
        self.lbldisplay.config(text = self.input_button)
        
root = Tk()
app = calculator(root)
root.mainloop()

