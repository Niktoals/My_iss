# Импорт всех классов
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from plane import main

# Глобальные настройки
Window.size = (250, 200)
Window.clearcolor = (255/255, 186/255, 3/255, 1)
Window.title = "PLANE"

class MyApp(App):
    def __init__(self):
        super().__init__()
        self.box = GridLayout(cols=7)
        self.box.padding=5
    
    def build(self):
        seats, no=main()
        print(no)
        for row in seats:
            aisle=0
            for col in row:                
                self.box.add_widget(Button(text=col[0]))
                self.box.add_widget(Button(text=col[1]))
                self.box.add_widget(Button(text=col[2]))
                if aisle==0:
                    self.box.add_widget(Button(text='_'))
                aisle+=1
 
        return self.box


# Запуск проекта
if __name__ == "__main__":
	MyApp().run()