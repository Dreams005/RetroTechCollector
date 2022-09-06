import datetime
import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import ttk, END
import sqlite3

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


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
        self.var = customtkinter.StringVar(self)
        self.title("Retro Technology Collector")
        self.iconbitmap("Files/Images/camera.ico")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        conn = sqlite3.connect('item_data_rtc.db')

        c = conn.cursor()

        c.execute("""CREATE TABLE if not exists items (
                    item_name text,
                    item_type text,
                    date_added text,
                    item_dom text)
                    """)

        conn.commit()
        conn.close()

        def query_database():
            conn = sqlite3.connect('item_data_rtc.db')

            c = conn.cursor()

            c.execute("SELECT rowid, * FROM items")
            records = c.fetchall()

            for record in records:
                print(record)

            for record in records:
                self.table.insert(parent='', index='end', iid=record[0], text='',
                                  values=(record[0], record[1], record[3], record[4]))

            conn.commit()
            conn.close()

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=200,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=15, pady=15)

        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(8, minsize=20)
        self.frame_left.grid_rowconfigure(11, minsize=10)

        self.add_menu_display211 = customtkinter.CTkFrame(master=self.frame_right,
                                                          corner_radius=15,
                                                          height=400,
                                                          width=600)
        self.add_menu_display211.grid(pady=15, padx=15, sticky="nws")

        columns = ('id', 'item', 'date_added', 'date_of_manufacture')

        self.table = ttk.Treeview(master=self.add_menu_display211,
                                  columns=columns,
                                  height=17,
                                  selectmode='browse',
                                  show='headings')

        self.table.column("#1", anchor="c", minwidth=50, width=50)
        self.table.column("#2", anchor="w", minwidth=220, width=220)
        self.table.column("#3", anchor="c", minwidth=120, width=120)
        self.table.column("#4", anchor="c", minwidth=120, width=120)

        self.table.heading('id', text='ID')
        self.table.heading('item', text='Item')
        self.table.heading('date_added', text='Date Added')
        self.table.heading('date_of_manufacture', text='Date of Manufacture')

        self.table.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        self.table.bind('<Motion>', 'break')

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Menu",
                                              text_font=("Roboto Medium", -16))
        self.label_1.grid(row=1, column=0, pady=20, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Add Item",
                                                corner_radius=15,
                                                border_width=1.5,
                                                border_color="#3484F0",  # alternative green: #33f05f
                                                fg_color="#343638",
                                                command=self.button_event1)
        self.button_1.grid(row=2, column=0, pady=(15, 15), padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Delete Item",
                                                corner_radius=15,
                                                border_width=1.5,
                                                border_color="#3484F0",  # alternative red: #f03933
                                                fg_color="#343638",
                                                command=self.button_event2)
        self.button_2.grid(row=3, column=0, pady=15, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Edit Item",
                                                corner_radius=15,
                                                border_width=1.5,
                                                border_color="#3484F0",
                                                fg_color="#343638",
                                                command=self.button_event3)
        self.button_3.grid(row=4, column=0, pady=15, padx=20)

        self.optionmenu_1_values = []

        with open("Files/Data/option_menu_options.txt", 'r') as f:
            options = f.readlines()
            for i in options:
                self.optionmenu_1_values.append(i.rstrip())
            f.close()
            print(self.optionmenu_1_values)

        def optionmenu_callback1(choice):
            with open("Files/Data/option_menu_options.txt", 'r') as f:
                types = f.readlines()
                self.optionmenu_1_values = []
                for i in types:
                    self.optionmenu_1_values.append(i.rstrip())
                print(choice)
                if choice == "All":
                    conn = sqlite3.connect('item_data_rtc.db')

                    c = conn.cursor()

                    c.execute("SELECT rowid, * FROM items")
                    records = c.fetchall()

                    self.table.delete(*self.table.get_children())

                    for record in records:
                        self.table.insert(parent='', index='end', iid=record[0], text='',
                                          values=(record[0], record[1], record[3], record[4]))

                    conn.commit()
                    conn.close()

                elif choice in self.optionmenu_1_values:
                    conn = sqlite3.connect('item_data_rtc.db')

                    c = conn.cursor()

                    c.execute("SELECT rowid, * FROM items WHERE item_type = ?", (choice,))
                    records = c.fetchall()

                    self.table.delete(*self.table.get_children())

                    for record in records:
                        self.table.insert(parent='', index='end', iid=record[0], text='',
                                          values=(record[0], record[1], record[3], record[4]))

                    conn.commit()
                    conn.close()

        self.om_variable = tkinter.StringVar(self)
        self.om_variable.set(self.optionmenu_1_values[0])
        self.om_variable.trace('w', self.option_select)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left, values=self.optionmenu_1_values,
                                                        corner_radius=15,
                                                        button_color="#565b5e",
                                                        fg_color="#343638",
                                                        button_hover_color="#3484F0",
                                                        command=optionmenu_callback1)
        self.optionmenu_1.grid(row=5, column=0, pady=(15, 140), padx=20)
        self.optionmenu_1.set("Sort by type")

        self.label_creator = customtkinter.CTkLabel(master=self.frame_left, text="Project created by:")
        self.label_creator.grid(row=10, column=0, pady=0, padx=20, sticky="w")

        self.label_creatorname = customtkinter.CTkLabel(master=self.frame_left, text="Alexander Ellul Hunt",
                                                        text_font=("Roboto Medium", -16),
                                                        text_color="#c1c1c1")
        self.label_creatorname.grid(row=11, column=0, pady=(0, 10), padx=20, sticky="w")

        # ============ frame_right ============

        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        def selection_remove(selection):
            self.table.selection_remove(self.table.focus())
            print("Deselected item")

        self.table.bind("<Escape>", selection_remove)

        query_database()

    def option_select(self, *args):
        return self.om_variable.get()

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
        main_add_frame.grid_rowconfigure(0, minsize=10)
        main_add_frame.grid_rowconfigure(5, weight=1)
        main_add_frame.grid_rowconfigure(8, minsize=20)
        main_add_frame.grid_rowconfigure(11, minsize=10)
        main_add_frame.grid(row=0, column=0, sticky="nswe", padx=15, pady=15)

        add_item_menu.grab_set()

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

        type_option_menu = customtkinter.CTkComboBox(master=main_add_frame,
                                                     values=self.optionmenu_1_values[1:],
                                                     command=type_add_optionmenu_callback,
                                                     button_color="#565b5e",
                                                     fg_color="#343638",
                                                     button_hover_color="#3484F0",
                                                     corner_radius=10)
        type_option_menu.grid(row=3, column=0, sticky="ns", padx=65, pady=(0, 5))

        type_option_menu.update()

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

            item_name = entry1.get()
            item_type = type_option_menu.get()
            item_dom = entry3.get()

            if len(item_name) == 0 or len(item_dom) == 0:
                tkinter.messagebox.showerror("No input error",
                                             "Please make sure you filled out "
                                             "all the fields before you press Add Item.")
            else:
                with open("Files/Data/option_menu_options.txt", 'r+') as f:
                    options = f.readlines()
                    if item_type.upper() in options or item_type.lower() in options or item_type in options:
                        print(f"{item_type} is already in options")
                    else:
                        f.write(f"\n{item_type}")
                        f.close()
                        with open("Files/Data/option_menu_options.txt", 'r') as file:
                            options = file.readlines()
                            self.optionmenu_1_values = ["All"]
                            for i in options[1:]:
                                self.optionmenu_1_values.append(i.rstrip())
                            f.close()
                            self.optionmenu_1.configure(values=self.optionmenu_1_values)

                conn = sqlite3.connect('item_data_rtc.db')

                c = conn.cursor()

                c.execute("SELECT rowid, * FROM items")
                records = c.fetchall()

                c.execute("INSERT INTO items VALUES (:item_name, :item_type, :date_added, :item_dom)",
                          {
                              'item_name': item_name,
                              'item_type': item_type,
                              'date_added': datetime.datetime.now().strftime("%d/%m/%Y"),
                              'item_dom': item_dom
                          })

                conn.commit()

                conn.close()

                self.table.delete(*self.table.get_children())

                conn = sqlite3.connect('item_data_rtc.db')

                c = conn.cursor()

                c.execute("SELECT rowid, * FROM items")
                records = c.fetchall()

                for record in records:
                    print(record)

                for record in records:
                    self.table.insert(parent='', index='end', iid=record[0], text='',
                                      values=(record[0], record[1], record[3], record[4]))

                conn.commit()

                conn.close()

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
        selected = self.table.selection()
        if selected:
            rowid = selected[0]

            conn = sqlite3.connect('item_data_rtc.db')
            conn.execute(f"DELETE FROM items WHERE rowid = {rowid}")

            self.table.delete(rowid)
            conn.commit()
            conn.close()
        else:
            tkinter.messagebox.showerror("No item selected error",
                                         "You have to select an item to delete from the database before deleting")

    def button_event3(self):
        edit_item_menu = customtkinter.CTkToplevel(self)
        edit_item_menu.title("Edit Item Menu")
        edit_item_menu.iconbitmap('Files/Images/compose.ico')
        edit_item_menu.geometry("360x520")
        edit_item_menu.resizable(False, False)
        edit_item_menu.grid_columnconfigure(0, weight=1)
        edit_item_menu.grid_rowconfigure(0, weight=1)

        main_edit_frame = customtkinter.CTkFrame(master=edit_item_menu, corner_radius=10, height=240, width=400)
        main_edit_frame.grid(row=0, column=0, sticky="nswe")
        main_edit_frame.grid_rowconfigure(0, minsize=10)
        main_edit_frame.grid_rowconfigure(5, weight=1)
        main_edit_frame.grid_rowconfigure(8, minsize=20)
        main_edit_frame.grid_rowconfigure(11, minsize=10)
        main_edit_frame.grid(row=0, column=0, sticky="nswe", padx=15, pady=15)

        edit_item_menu.grab_set()

        entry_label1 = customtkinter.CTkLabel(master=main_edit_frame, text="Item Name", text_font=(
            "Roboto Medium", -16))
        entry_label1.grid(row=0, column=0, sticky="nswe", padx=65, pady=(40, 5))

        entry1 = customtkinter.CTkEntry(master=main_edit_frame,
                                        placeholder_text="",
                                        width=160,
                                        height=45,
                                        border_width=2,
                                        corner_radius=10)
        entry1.grid(row=1, column=0, sticky="nswe", padx=65, pady=0)

        entry_label2 = customtkinter.CTkLabel(master=main_edit_frame, text="Item Type", text_font=(
            "Roboto Medium", -16))
        entry_label2.grid(row=2, column=0, sticky="nswe", padx=65, pady=(15, 5))

        def type_add_optionmenu_callback(choice):
            print("Type selected:", choice)

        type_option_menu = customtkinter.CTkOptionMenu(master=main_edit_frame,
                                                       values=self.optionmenu_1_values[1:],
                                                       command=type_add_optionmenu_callback,
                                                       button_color="#565b5e",
                                                       fg_color="#343638",
                                                       button_hover_color="#3484F0",
                                                       corner_radius=10)
        type_option_menu.grid(row=3, column=0, sticky="ns", padx=65, pady=(0, 5))

        entry_label3 = customtkinter.CTkLabel(master=main_edit_frame, text="Date of manufacture",
                                              text_font=("Roboto Medium", -16))
        entry_label3.grid(row=4, column=0, sticky="nswe", padx=65, pady=(15, 5))

        entry3 = customtkinter.CTkEntry(master=main_edit_frame,
                                        placeholder_text='',
                                        width=160,
                                        height=45,
                                        border_width=2,
                                        corner_radius=10)
        entry3.grid(row=5, column=0, sticky="nwe", padx=65, pady=0)

        def check_input():
            selected = self.table.focus()
            values = self.table.item(selected, 'values')
            rowid = selected[0]

            item_name = entry1.get()
            item_type = type_option_menu.get()
            item_dom = entry3.get()

            if len(item_name) == 0 or len(item_dom) == 0:
                tkinter.messagebox.showerror("No input error",
                                             "Please make sure you filled out "
                                             "all the fields before you try to edit the item.")
            else:
                conn = sqlite3.connect('item_data_rtc.db')

                c = conn.cursor()

                c.execute("SELECT rowid, * FROM items")
                records = c.fetchall()

                c.execute(f"""UPDATE items SET
                    item_name = :item_name,
                    item_type = :item_type,
                    date_added = :date_added,
                    item_dom = :item_dom
                    
                    WHERE rowid = {rowid}""",
                          {
                              'item_name': item_name,
                              'item_type': item_type,
                              'date_added': values[2],
                              'item_dom': item_dom
                          })

                conn.commit()

                conn.close()

                self.table.delete(*self.table.get_children())

                conn = sqlite3.connect('item_data_rtc.db')

                c = conn.cursor()

                c.execute("SELECT rowid, * FROM items")
                records = c.fetchall()

                for record in records:
                    print(record)

                for record in records:
                    self.table.insert(parent='', index='end', iid=record[0], text='',
                                      values=(record[0], record[1], record[3], record[4]))

                conn.commit()

                conn.close()

                edit_item_menu.destroy()
                tkinter.messagebox.showinfo("Item edited Successfully",
                                            "Your item has been edited successfully.")

        button1 = customtkinter.CTkButton(master=main_edit_frame,
                                          text="Edit Item",
                                          width=200,
                                          height=50,
                                          border_width=2,
                                          border_color="#3484F0",
                                          fg_color="#343638",
                                          corner_radius=20,
                                          command=check_input)
        button1.grid(row=7, column=0, sticky="nwe", padx=65, pady=0)

        try:
            selected = self.table.focus()
            values = self.table.item(selected, 'values')
            entry1.insert(0, values[1])
            entry3.insert(0, values[3])
        except IndexError:
            edit_item_menu.destroy()
            tkinter.messagebox.showerror("Item not selected error",
                                         "You have to select an item before attempting to edit it.")


if __name__ == "__main__":
    app = App()
    app.mainloop()
