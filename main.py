from tkinter import *
import random

intro_list = [
    ["Byl hezký letní den, když v tom "],
    ["Podívala se na jeho tvář, v níž viděla náznak "],
    ["Dřevěná židle, na které seděl a na které se houpal, náhle "],
]


class DisappTextWritingApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Disappearing Text Writing App")
        self.window.config(padx=120, pady=70)
        self.canvas = Canvas(width=700, height=500)

        # formatting options
        self.FONT = "Verdana"
        self.SIZE = 14

        # counting and time
        self.timer_on = True
        self.seconds_limit = 10
        self.seconds_actual = 0

        # counting bar
        self.bar_list = []
        for x in range(self.seconds_limit):
            self.bar = Label()
            self.bar.grid(row=1, column=x, sticky="w")
            self.bar.config(height=1, width=8, bg='white')
            self.bar_list.append(self.bar)

        # setting the widgets on the grid
        self.label_appname = Label()
        self.label_appname.grid(row=0, column=0, sticky="ew", columnspan=22)

        self.label_header = Label()
        self.label_header.grid(row=2, column=0, sticky="w", columnspan=22)

        self.entry_text = Text()
        self.entry_text.grid(row=3, column=0, sticky="ew", columnspan=22)

        self.button_reset = Button()
        self.button_reset.grid(row=4, column=2, sticky="e", columnspan=22)

        # running the app
        self.set_widgets_to_start_condition()
        self.window.after(1000, self.timer)
        self.window.mainloop()

    def set_widgets_to_start_condition(self):
        self.label_appname.config(text="Disappearing Text Writing App", font=(self.FONT, self.SIZE + 10), pady=20)
        self.label_header.config(text="Pište zde:", font=(self.FONT, self.SIZE), pady=10)
        self.entry_text.config(height=10, width=50, font=(self.FONT, self.SIZE), state="normal")
        self.entry_text.delete(1.0, END)
        intro = str(random.choice(intro_list)[0])
        self.entry_text.insert(END, intro)
        self.entry_text.focus()
        self.button_reset.config(text="Znovu", command=self.reset, font=(self.FONT, self.SIZE),
                                 state="disabled")

    def timer(self):
        if self.timer_on:
            self.window.bind("<Key>", self.key_pressed)
            if self.seconds_actual <= self.seconds_limit - 1:
                self.bar_list[self.seconds_actual].config(bg="light gray")
                self.seconds_actual += 1
                self.window.after(1000, self.timer)
            else:
                self.button_reset.config(state="active")
                self.entry_text.config(state="disabled")

    def key_pressed(self, event):
        for item in self.bar_list:
            item.config(bg="white")
        self.seconds_actual = 0

    def reset(self):
        self.timer_on = False
        self.set_widgets_to_start_condition()
        for item in self.bar_list:
            item.config(bg="white")
        self.seconds_actual = 0
        self.timer_on = True
        self.window.after(1000, self.timer)


app = DisappTextWritingApp()
