import tkinter as tk
from buttons import Buttons
from result import Result
from calculator import Calculator

#colors:
"""
#95B8D1
#8BAAD0
#86A3CF
#839FCF
#809BCE
"""

calculator = Calculator()

window = tk.Tk()
window.title("Example")
window.geometry("220x300+500+500")
window.resizable(True,True)

window.columnconfigure(0,weight=1) 
window.rowconfigure(1,weight=1)

output_frame = tk.Frame(window,bg="#809BCE")
buttons_frame = tk.Frame(window,bg="#95B8D1")


output_frame.grid(row=0,column=0,sticky="NSEW")
buttons_frame.grid(row=1,column=0,sticky="NSEW")

result = Result(output_frame)
result.add_label("#809BCE","black")

def update_result(operation):
    operation()
    result.update_result(calculator)

buttons = Buttons(buttons_frame)
buttons.add_button("AC","#95B8D1","black",0,0,lambda:update_result(calculator.clean_number))
buttons.add_button("+/-","#95B8D1","black",0,1,lambda:update_result(calculator.invert_number))
buttons.add_button("%","#95B8D1","black",0,2,lambda:update_result(calculator.percent_number))
buttons.add_button("+","#95B8D1","black",0,3,lambda:calculator.change_operator("+"))
buttons.add_button("-","#95B8D1","black",1,3,lambda:calculator.change_operator("-"))
buttons.add_button("*","#95B8D1","black",2,3,lambda:calculator.change_operator("*"))
buttons.add_button("/","#95B8D1","black",3,3,lambda:calculator.change_operator("/"))
# buttons.add_button("=","#95B8D1","black",4,3,lambda:calculator.calculate(result.show_result))
buttons.add_button("=","#95B8D1","black",4,3,lambda:update_result(calculator.calculate))
buttons.add_button("0","#95B8D1","black",4,0,lambda:result.write_number(0,calculator),2)
buttons.add_button(".","#95B8D1","black",4,2,lambda:update_result(calculator.decimal_dot))



row = 1
col = 0
for i in range(1,10):
    buttons.add_button(str(i),"#95B8D1","black",row,col,lambda i=i:result.write_number(i,calculator))
    col+=1
    if(col>=3):
        col = 0
        row += 1

window.mainloop()