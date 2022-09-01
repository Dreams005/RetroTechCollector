import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

visiblea = False
visibleb = False
visiblec = False


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520


    def __init__(self):
        super().__init__()

        self.add_menu_display = None
        self.title("Retro Technology Collector")
        self.iconbitmap("Files/radio-cassette.ico")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.minsize(App.WIDTH, App.HEIGHT)
        self.maxsize(App.WIDTH, App.HEIGHT)
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

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Menu",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=20, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Add Item",
                                                command=self.button_event1)
        self.button_1.grid(row=2, column=0, pady=15, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Show Items",
                                                command=self.button_event2)
        self.button_2.grid(row=3, column=0, pady=15, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Delete Items",
                                                command=self.button_event3)
        self.button_3.grid(row=4, column=0, pady=15, padx=20)

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

        # ============ frame_info ============

        # configure grid layout (1x1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text="Please select something from the menu to start :)",
                                                   text_color="gray")
        self.label_info_1.grid(column=0, row=0, sticky="nwe")
        self.label_info_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # ============ frame_right ============

        #self.entry = customtkinter.CTkEntry(master=self.frame_right,
        #                                    width=120,
        #                                    placeholder_text="CTkEntry")
        #self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        # set default values

    def button_event1(self):
        global visiblea
        global visibleb
        global visiblec

        visiblea = not visiblea

        if visiblea:
            self.add_menu_display1 = customtkinter.CTkTextbox(master=self.frame_right)
            self.add_menu_display1.configure(width=550)
            self.add_menu_display1.grid(column=0, row=0, pady=15, padx=15, sticky="nwe")
            try:
                visibleb = False
                visiblec = False
                self.add_menu_display2.destroy()
                self.add_menu_display3.destroy()
            except AttributeError:
                pass
        else:
            self.add_menu_display1.destroy()

        self.label_info_1.destroy()

    def button_event2(self):
        global visiblea
        global visibleb
        global visiblec

        visibleb = not visibleb

        if visibleb:
            self.add_menu_display2 = customtkinter.CTkTextbox(master=self.frame_right)
            self.add_menu_display2.configure(width=700)
            self.add_menu_display2.grid(column=0, row=0, pady=15, padx=15, sticky="nwe")
            try:
                visiblea = False
                visiblec = False
                self.add_menu_display1.destroy()
                self.add_menu_display3.destroy()
            except AttributeError:
                pass
        else:
            self.add_menu_display2.destroy()

    def button_event3(self):
        global visiblea
        global visibleb
        global visiblec

        visiblec = not visiblec

        if visiblec:
            self.add_menu_display3 = customtkinter.CTkTextbox(master=self.frame_right)
            self.add_menu_display3.configure(width=900)
            self.add_menu_display3.grid(column=0, row=0, pady=0, padx=0, sticky="nwe")
            try:
                visiblea = False
                visibleb = False
                self.add_menu_display1.destroy()
                self.add_menu_display2.destroy()
            except AttributeError:
                pass
        else:
            self.add_menu_display3.destroy()

        self.label_info_1.destroy()

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
