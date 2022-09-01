import tkinter
import tkinter.messagebox
from tkinter import ttk
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.on_closing = None
        self.title("Retro Technology Collector")
        self.iconbitmap("Files/Images/radio-cassette.ico")
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

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.add_menu_display21 = customtkinter.CTkFrame(master=self.frame_right, corner_radius=15)
        self.add_menu_display211 = customtkinter.CTkFrame(master=self.frame_right,
                                                          corner_radius=15,
                                                          height=385,
                                                          width=600)
        self.add_menu_display22 = customtkinter.CTkLabel(master=self.add_menu_display21, text="ID", width=70)
        self.add_menu_display23 = customtkinter.CTkLabel(master=self.add_menu_display21, text="Item")
        self.add_menu_display24 = customtkinter.CTkLabel(master=self.add_menu_display21, text="Date Added")
        self.add_menu_display25 = customtkinter.CTkLabel(master=self.add_menu_display21, text="Date of Manufacture")

        self.add_menu_display21.columnconfigure((0, 1, 2, 3), weight=1)
        self.add_menu_display21.columnconfigure(1, weight=5)
        self.add_menu_display21.grid(pady=15, padx=15, sticky="nw")
        self.add_menu_display211.grid(pady=0, padx=15, sticky="nws")
        self.add_menu_display22.grid(column=0, row=0, pady=15, padx=0)
        self.add_menu_display23.grid(column=1, row=0, pady=15, padx=70)
        self.add_menu_display24.grid(column=2, row=0, pady=15, padx=0)
        self.add_menu_display25.grid(column=3, row=0, pady=15, padx=20, sticky="ne")

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Menu",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=20, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Add Item",
                                                command=self.button_event1)
        self.button_1.grid(row=2, column=0, pady=15, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Delete Item",
                                                command=self.button_event2)
        self.button_2.grid(row=3, column=0, pady=15, padx=20)

        def optionmenu_callback1(choice):
            print("Type selected:", choice)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left, values=["Type 1", "Type 2"],
                                                        command=optionmenu_callback1)
        self.optionmenu_1.grid(row=4, column=0, pady=15, padx=20)
        self.optionmenu_1.set("Sort by type")

        self.label_creator = customtkinter.CTkLabel(master=self.frame_left, text="Project created by:")
        self.label_creator.grid(row=10, column=0, pady=0, padx=20, sticky="w")

        self.label_creatorname = customtkinter.CTkLabel(master=self.frame_left, text="Alexander Ellul Hunt",
                                                        text_font=("Roboto Medium", -16),
                                                        text_color="#c1c1c1")
        self.label_creatorname.grid(row=11, column=0, pady=10, padx=20, sticky="w")

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
        add_item_menu.geometry("360x550")
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
        entry_label1.grid(row=0, column=0, sticky="nswe", padx=85, pady=(15, 5))

        entry1 = customtkinter.CTkEntry(master=main_add_frame,
                                        placeholder_text="",
                                        width=160,
                                        height=45,
                                        border_width=2,
                                        corner_radius=10)
        entry1.grid(row=1, column=0, sticky="nswe", padx=85, pady=0)

        entry_label2 = customtkinter.CTkLabel(master=main_add_frame, text="Item Type", text_font=("Roboto Medium", -16))
        entry_label2.grid(row=2, column=0, sticky="nswe", padx=85, pady=(15, 5))

        def type_add_optionmenu_callback(choice):
            print("Type selected:", choice)

        type_option_menu = customtkinter.CTkOptionMenu(master=main_add_frame,
                                                       values=['Computer', 'Video player', 'Phone', 'Camera'],
                                                       command=type_add_optionmenu_callback,
                                                       button_color="#565b5e",
                                                       fg_color="#343638",
                                                       corner_radius=10)
        type_option_menu.grid(row=3, column=0, sticky="ns", padx=85, pady=(0, 5))

        entry_label3 = customtkinter.CTkLabel(master=main_add_frame, text="Date of manufacture",
                                              text_font=("Roboto Medium", -16))
        entry_label3.grid(row=4, column=0, sticky="nswe", padx=85, pady=(15, 5))

        entry3 = customtkinter.CTkEntry(master=main_add_frame,
                                        placeholder_text="",
                                        width=160,
                                        height=45,
                                        border_width=2,
                                        corner_radius=10)
        entry3.grid(row=5, column=0, sticky="nwe", padx=85, pady=0)

    def button_event2(self):
        del_item_menu = customtkinter.CTkToplevel(self)
        del_item_menu.title("Delete Item Menu")
        del_item_menu.iconbitmap('Files/Images/minus.ico')
        del_item_menu.geometry("450x300")

        entry1 = customtkinter.CTkEntry(master=del_item_menu,
                                        placeholder_text="Item",
                                        width=120,
                                        height=45,
                                        border_width=2,
                                        corner_radius=10)
        entry1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


if __name__ == "__main__":
    app = App()
    app.mainloop()
