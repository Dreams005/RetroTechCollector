import datetime
import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import ttk
import sqlite3

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    COUNT = 0
    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        style = ttk.Style()

        style.theme_use("default")

        style.configure("Treeview",
                        background="#2a2d2e",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#343638",
                        bordercolor="#343638",
                        borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])

        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat")
        style.map("Treeview.Heading",
                  background=[('active', '#3484F0')])

        self.on_closing = None
        self.title("Retro Technology Collector")
        self.iconbitmap("Files/Images/camera.ico")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=200,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=15, pady=15)

        # Data stuff

        # conn = sqlite3.connect('item_data.db')
        # c = conn.cursor()
        #
        # c.execute("""CREATE TABLE if not exists items (
        #     id integer,
        #     item text,
        #     date_added text,
        #     date_of_manufacture text,)
        #     """)

        # conn.commit()
        #
        # conn.close()  # TODO CONTINUE HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.add_menu_display211 = customtkinter.CTkFrame(master=self.frame_right,
                                                          corner_radius=15,
                                                          height=385,
                                                          width=600)
        self.add_menu_display211.grid(pady=15, padx=15, sticky="nws")

        columns = ('id', 'item', 'date_added', 'date_of_manufacture')

        self.table = ttk.Treeview(master=self.add_menu_display211,
                                  columns=columns,
                                  height=14,
                                  show='headings')

        self.table.column("#1", anchor="c", minwidth=50, width=50)
        self.table.column("#2", anchor="w", minwidth=220, width=220)
        self.table.column("#3", anchor="c", minwidth=120, width=120)
        self.table.column("#4", anchor="c", minwidth=120, width=120)

        self.table.heading('id', text='ID')
        self.table.heading('item', text='Item')
        self.table.heading('date_added', text='Date Added')
        self.table.heading('date_of_manufacture', text='Date of Manufacture')

        # -----TEMP DATA-----
        self.data = []

        for index, record in enumerate(self.data):
            self.table.insert(parent='', index='end', iid=index, text="", values=(record[0],
                                                                                  record[1],
                                                                                  record[2],
                                                                                  record[3]))
            App.COUNT += 1

        self.table.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        self.table.bind('<Motion>', 'break')

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Menu",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=20, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Add Item",
                                                corner_radius=15,
                                                border_width=1.5,
                                                border_color="#3484F0",  # alternative green: #33f05f
                                                fg_color="#343638",
                                                command=self.button_event1)
        self.button_1.grid(row=2, column=0, pady=15, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Delete Item",
                                                corner_radius=15,
                                                border_width=1.5,
                                                border_color="#3484F0",  # alternative red: #f03933
                                                fg_color="#343638",
                                                command=self.button_event2)
        self.button_2.grid(row=3, column=0, pady=15, padx=20)

        def optionmenu_callback1(choice):
            print("Type selected:", choice)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left, values=["Type 1", "Type 2"],
                                                        corner_radius=15,
                                                        button_color="#565b5e",
                                                        fg_color="#343638",
                                                        button_hover_color="#3484F0",
                                                        command=optionmenu_callback1)
        self.optionmenu_1.grid(row=4, column=0, pady=15, padx=20)
        self.optionmenu_1.set("Sort by type")

        self.label_creator = customtkinter.CTkLabel(master=self.frame_left, text="Project created by:")
        self.label_creator.grid(row=10, column=0, pady=0, padx=20, sticky="w")

        self.label_creatorname = customtkinter.CTkLabel(master=self.frame_left, text="Alexander Ellul Hunt",
                                                        text_font=("Roboto Medium", -16),
                                                        text_color="#c1c1c1")
        self.label_creatorname.grid(row=11, column=0, pady=(0, 10), padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

    def button_event1(self):
        add_item_menu = customtkinter.CTkToplevel(self)
        add_item_menu.title("Add Item Menu")
        add_item_menu.iconbitmap('Files/Images/plus.ico')
        add_item_menu.geometry("360x520")
        add_item_menu.resizable(False, False)
        add_item_menu.grid_columnconfigure(0, weight=1)
        add_item_menu.grid_rowconfigure(0, weight=1)

        main_add_frame = customtkinter.CTkFrame(master=add_item_menu, corner_radius=10, height=240, width=400)
        main_add_frame.grid(row=0, column=0, sticky="nswe")
        main_add_frame.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        main_add_frame.grid_rowconfigure(5, weight=1)  # empty row as spacing
        main_add_frame.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
        main_add_frame.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing
        main_add_frame.grid(row=0, column=0, sticky="nswe", padx=15, pady=15)

        entry_label1 = customtkinter.CTkLabel(master=main_add_frame, text="Item Name", text_font=("Roboto Medium", -16))
        entry_label1.grid(row=0, column=0, sticky="nswe", padx=65, pady=(40, 5))

        entry1 = customtkinter.CTkEntry(master=main_add_frame,
                                        placeholder_text="",
                                        width=160,
                                        height=45,
                                        border_width=2,
                                        corner_radius=10)
        entry1.grid(row=1, column=0, sticky="nswe", padx=65, pady=0)

        entry_label2 = customtkinter.CTkLabel(master=main_add_frame, text="Item Type", text_font=("Roboto Medium", -16))
        entry_label2.grid(row=2, column=0, sticky="nswe", padx=65, pady=(15, 5))

        def type_add_optionmenu_callback(choice):
            print("Type selected:", choice)

        type_option_menu = customtkinter.CTkOptionMenu(master=main_add_frame,
                                                       values=['Computer', 'Video player', 'Phone', 'Camera'],
                                                       command=type_add_optionmenu_callback,
                                                       button_color="#565b5e",
                                                       fg_color="#343638",
                                                       button_hover_color="#3484F0",
                                                       corner_radius=10)
        type_option_menu.grid(row=3, column=0, sticky="ns", padx=65, pady=(0, 5))

        entry_label3 = customtkinter.CTkLabel(master=main_add_frame, text="Date of manufacture",
                                              text_font=("Roboto Medium", -16))
        entry_label3.grid(row=4, column=0, sticky="nswe", padx=65, pady=(15, 5))

        entry3 = customtkinter.CTkEntry(master=main_add_frame,
                                        placeholder_text="",
                                        width=160,
                                        height=45,
                                        border_width=2,
                                        corner_radius=10)
        entry3.grid(row=5, column=0, sticky="nwe", padx=65, pady=0)

        def check_input():

            now = datetime.datetime.now()
            item_name = entry1.get()
            item_type = type_option_menu.get()
            item_dom = entry3.get()

            if len(item_name) == 0 or len(item_dom) == 0:
                tkinter.messagebox.showerror("No input error",
                                             "Please make sure you filled out "
                                             "all the fields before you press Add Item.")
            else:
                self.table.insert(parent='', index='end', iid=App.COUNT, text="Parent", values=(App.COUNT+1, item_name,
                                                                                                now.strftime(
                                                                                                    "%d/%m/%Y"
                                                                                                            ),
                                                                                                item_dom))
                App.COUNT += 1

                add_item_menu.destroy()
                tkinter.messagebox.showinfo("Item added Successfully",
                                            "Your new item has been added successfully.")

        button1 = customtkinter.CTkButton(master=main_add_frame,
                                          text="Add Item",
                                          width=200,
                                          height=50,
                                          border_width=2,
                                          border_color="#3484F0",
                                          fg_color="#343638",
                                          corner_radius=20,
                                          command=check_input)
        button1.grid(row=7, column=0, sticky="nwe", padx=65, pady=0)

    def button_event2(self):
        del_item_menu = customtkinter.CTkToplevel(self)
        del_item_menu.title("Del Item Menu")
        del_item_menu.iconbitmap('Files/Images/minus.ico')
        del_item_menu.geometry("360x300")
        del_item_menu.resizable(False, False)
        del_item_menu.grid_columnconfigure(0, weight=1)
        del_item_menu.grid_rowconfigure(0, weight=1)

        main_del_frame = customtkinter.CTkFrame(master=del_item_menu, corner_radius=10, height=240, width=400)
        main_del_frame.grid(row=0, column=0, sticky="nswe")
        main_del_frame.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        main_del_frame.grid(row=0, column=0, sticky="nswe", padx=15, pady=15)

        entry_label1 = customtkinter.CTkLabel(master=main_del_frame, text="Item ID (1, 2, 3)",
                                              text_font=("Roboto Medium", -16))
        entry_label1.grid(row=0, column=0, sticky="nswe", padx=65, pady=(40, 5))

        entry_var = customtkinter.StringVar()

        entry1 = customtkinter.CTkEntry(master=main_del_frame,
                                        placeholder_text="",
                                        width=160,
                                        height=45,
                                        border_width=2,
                                        corner_radius=10,
                                        textvariable=entry_var)
        entry1.grid(row=1, column=0, sticky="nswe", padx=65, pady=(5, 15))

        #  Expand on this when you get the table to work

        def check_input():
            try:
                del_id = entry1.get()
                if len(entry1.get()) == 0:
                    tkinter.messagebox.showerror("No input error",
                                                 "Please input a valid ID before you press delete item.")
                elif len(entry1.get()) >= 5:
                    tkinter.messagebox.showerror("Number too big error",
                                                 "There is no way you have this many items.")

            except ValueError:
                tkinter.messagebox.showerror("Not a number error",
                                             "Please input a number.")

        button1 = customtkinter.CTkButton(master=main_del_frame,
                                          text="Delete Item",
                                          width=200,
                                          height=50,
                                          border_width=2,
                                          border_color="#3484F0",
                                          fg_color="#343638",
                                          corner_radius=20,
                                          command=check_input)
        button1.grid(row=3, column=0, sticky="nsw", padx=65, pady=(50, 0))


if __name__ == "__main__":
    app = App()
    app.mainloop()
