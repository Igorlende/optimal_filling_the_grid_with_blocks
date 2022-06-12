from tkinter import *
from Block import Block
import random
from algorithm import algorithm
from tkinter import ttk
from tkinter import messagebox


def show_grid(grid):
    root = Tk()
    root.title("Cітка")

    if len(grid) == 0:
        return False

    width_grid = len(grid[0])*100+6
    height_grid = len(grid)*100+6

    c = Canvas(root, width=width_grid, height=height_grid, bg='white')
    root.maxsize(width_grid+18, height_grid)
    root.minsize(width_grid+18, 650)

    c.config(scrollregion=c.bbox("all"))
    c.pack(expand=YES, fill=BOTH)
    scrbar = Scrollbar(c)
    scrbar.pack(side=RIGHT,fill=Y)
    c.config(yscrollcommand=scrbar.set)
    scrbar.config(command=c.yview)

    set_blocks = set()

    color_block_fill = {
    1:"Light Green",
    2:"Yellow",
    3:"Beige",
    4:"Violet"
    }

    for row in range(0, len(grid)):
        for block in range(0, len(grid[row])):
            if grid[row][block] is not None and grid[row][block] not in set_blocks:
                width = grid[row][block].get_width()
                height = grid[row][block].get_height()
                priority = grid[row][block].get_priority()

                x1 = block*100+6
                y1 = row*100+6
                x2 = block*100+100*width
                y2 = row*100+100*height

                c.create_rectangle(x1, y1, x2, y2, fill=color_block_fill[width],
                       outline="blue",
                       width=2,
                       activedash=(4, 4),
                       activefill='red'
                       )

                x_text = int((x1+x2)/2)
                y_text = int((y1+y2)/2)

                text_info = str(width)+"×"+str(height)+"\n"+str(priority)
                c.create_text(x_text, y_text,
                              text=text_info,
                              justify=CENTER, font="Verdana 14")
                set_blocks.add(grid[row][block])

    # прокрутка колесом мишки
    def on_mousewheel(event):
        shift = (event.state & 0x1) != 0
        scroll = -1 if event.delta > 0 else 1
        if shift:
            c.xview_scroll(scroll, "units")
        else:
            c.yview_scroll(scroll, "units")

    c.bind_all("<MouseWheel>", on_mousewheel)
    c.configure(scrollregio=c.bbox("all"))
    root.mainloop()


def input_data():

    root = Tk()
    root.geometry('350x500')

    root.maxsize(350, 500)
    root.minsize(350, 500)

    root.title("Конфігурація")

    #####################
    list_blocks = []

    #висота

    label_height = Label(root, text="Висота", font="Verdana 12")
    label_height.place(x=30,y=10)

    combobox_height = ttk.Combobox(root, width=5, values=[1,2,3], font="Verdana 12")

    combobox_height.place(x=30,y=33)
    combobox_height.current(0)

    #ширина
    label_width = Label(root,
                        text="Ширина", font="Verdana 12")
    label_width.place(x=30, y=60)

    def callbackFunc(event):
        if int(combobox_width.get()) != 4:
            combobox_height["values"] = [1, 2, 3]
        else:
            combobox_height.current(0)
            combobox_height["values"] = [1]

    combobox_width = ttk.Combobox(root, width=5, values=[1, 2, 3, 4], font="Verdana 12")
    combobox_width.place(x=30, y=83)
    combobox_width.current(0)
    combobox_width.bind("<<ComboboxSelected>>", callbackFunc)

    #пріорітет
    label_priority = Label(root,
                         text="Пріоритет", font="Verdana 12")
    label_priority.place(x=30, y=110)

    values_priority = []
    for i in range(1, 100):
        values_priority.append(i)

    combobox_priority = ttk.Combobox(root, width=5, values=values_priority, font="Verdana 12")

    combobox_priority.place(x=30, y=135)
    combobox_priority.current(0)

    #рандом
    label_random = Label(root,
                         text="Кількість блоків для\n рандому", font="Verdana 12")
    label_random.place(x=130, y=30)

    random_entry_value = StringVar()

    random_entry = Entry(textvariable=random_entry_value, width=10, font="Verdana 12")
    random_entry.insert(1, "1")
    random_entry.place(x=170, y=75)

    def generate_blocks():
        count = random_entry.get()
        try:
            count_blocks = int(count)
            # рандомні блоки
            for i in range(count_blocks):
                temp_width = random.randint(1, 4)
                if temp_width == 4:
                    temp_height = 1
                else:
                    temp_height = random.randint(1, 3)
                temp_priority = random.randint(1, 99)
                temp_block = Block(temp_width, temp_height, temp_priority)
                list_blocks.append(temp_block)
                text.configure(state="normal")
                text.insert(1.0, str(temp_block) + "\n")
                text.configure(state="disabled")
        except Exception:
            return False

    random_button = Button(text="Згенерувати", font="Verdana 13", background="#555", foreground="#ccc", command=generate_blocks)
    random_button.place(x=160, y=110)

    #блоки

    label_blocks = Label(root,
                         text="Блоки", font="Verdana 13")

    label_blocks.place(x=50, y=215)

    text = Text(width=30, height=10, padx=0, pady=0, font="Verdana 12")
    text.place(x=10, y=240)

    scroll = Scrollbar(command=text.yview, width=18)
    scroll.place(x=312, y=240, heigh=180)

    text.config(yscrollcommand=scroll.set)

    #додати
    def add_block():
        height = combobox_height.get()
        width = combobox_width.get()
        priority = combobox_priority.get()
        block = Block(int(width), int(height), int(priority))
        list_blocks.append(block)
        text.configure(state="normal")
        text.insert(1.0, str(block)+"\n")
        text.configure(state="disabled")

    text.configure(state="disabled")

    add_block_button = Button(text="Додати", font="Verdana 13", background="#555", foreground="#ccc", command=add_block)
    add_block_button.place(x=30, y=165)

    def clear_text():
        list_blocks.clear()
        text.configure(state="normal")
        text.delete(1.0, END)
        text.configure(state="disabled")

    clear_area_button = Button(text="Очистити", font="Verdana 13", background="#555", foreground="#ccc",command=clear_text)
    clear_area_button.place(x=30, y=430)

    def submit():
        if len(list_blocks) > 1000:
            messagebox.showinfo("упс", "Щось забагато. Ти сам напросився! Треба почекати...")
        res = algorithm(list_blocks)
        if res is not False:
            show_grid(res)
        else:
            messagebox.showinfo("упс", "По ходу порожньо")

    submit_button = Button(text="Ну покажи,\n що ти можеш",font="Verdana 13",background="green",foreground="black",command=submit)
    submit_button.place(x=150, y=430)

    root.mainloop()
