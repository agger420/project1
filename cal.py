from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

class input_display(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    def clear_num(self):
        self.ids.input_box.text = "0"
        #print("ok")

    def delete(self):
        prev_num = self.ids.input_box.text
        self.ids.input_box.text = prev_num[:-1]

    def pos_neg(self):
        prev_num = self.ids.input_box.text
        if "-" not in prev_num:
            if prev_num == "0":
                self.ids.input_box.text = "-"
            else:
                self.ids.input_box.text = f"-{prev_num}"
        else:
            new_input = prev_num.replace("-","")
            self.ids.input_box.text = str(new_input)
            
    def value(self,num):
        prev_num = self.ids.input_box.text
        
        if str(num).isdigit() == True and prev_num == "0":
            #self.ids.input_box.text = ""
            self.ids.input_box.text = str(num)
        else:
            self.ids.input_box.text = f"{prev_num}{num}"
        
    def result(self):
        input=self.ids.input_box.text
        while True:
            if "x" in input:
                ctd_input = input.replace("x","*")
                input=ctd_input
            if "÷" in input:
                ctd_input = input.replace("÷","/")
                input=ctd_input
            if "%" in input:
                temp_list=[]
                for index,input_num in enumerate(input):
                    if input_num == "%":
                        ctd_input = input.replace("%","")
                        for i in range(1,len(ctd_input)):
                            if str(ctd_input[index-i]).isdigit() == False:
                                break
                            temp_list.append(ctd_input[index-i])
                temp_list ="".join(temp_list[::-1])
                if str(temp_list) in ctd_input:
                    ctd_result = eval(temp_list)/100
                    final_op = ctd_input.replace(str(temp_list),str(ctd_result))
                    input=final_op
            try:
                result=eval(input)
                self.ids.input_box.text = str(result)
            except:
                self.ids.input_box.text = "Error"
            break
            

class Gridlayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_list = []
    
class CalculatorApp(App):
    def build(self):
        return input_display()

CalculatorApp().run()