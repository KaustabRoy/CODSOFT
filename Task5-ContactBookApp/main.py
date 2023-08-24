# Contact Information: Store name, phone number, email, and address for each contact.
# Add Contact: Allow users to add new contacts with their details.
# View Contact List: Display a list of all saved contacts with names and phone numbers.
# Search Contact: Implement a search function to find contacts by name or phone number.
# Update Contact: Enable users to update contact details.
# Delete Contact: Provide an option to delete a contact.
# User Interface: Design a user-friendly interface for easy interaction.

from tkinter import *
from tkinter import ttk
import sqlite3
from termcolor import colored

class Database:
    pass

class ContactBook(Tk):

    def __init__(self):
        super().__init__()
        # Centering the window when opened.
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # print(colored(f"SCREEN WIDTH : {screen_width} x SCREEN HEIGHT : {screen_height}", "blue"))
        app_width = 1500
        app_height = 700
        # print(colored(f"APP WIDTH : {app_width} x APP HEIGHT : {app_height}", "blue"))
        set_x = int((screen_width / 2) - (app_width / 2))
        set_y = int((screen_height / 2) - (app_height / 2))
        self.geometry(f'{app_width}x{app_height}+{set_x}+{set_y}')
        self.title("Contact Book")
        # self.resizable(False, False)
        # application design and event components
        self.style_ttk()
        self.header_frame = self.create_header_frame()
        self.contact_logo = PhotoImage(file = 'images/contact.png')
        self.create_logo_label()
        self.create_heading_label()
        self.table_frame = self.create_contact_table_frame()
        self.contact_table = self.create_contact_table()
        self.table_scrollbar = self.create_table_scrollbar()
        self.show_scrollbar()
        self.add_contact_table_field()
        self.add_heading_to_contact_table_field()
        self.create_contact_table_stripped_rows()
        # testing with fake data
        self.fake_data = self.demo_data()
        self.insert_fake_data()
        self.insert_frame = self.create_insert_data_frame()
        self.command_frame = self.create_command_options_frame()

        self.first_name_entry = self.create_insert_first_name_label_entry()
        self.last_name_entry = self.create_insert_last_name_label_entry()
        self.phone_entry = self.create_insert_phone_label_entry()
        self.email_entry = self.create_insert_email_label_entry()
        self.address_entry = self.create_insert_address_label_entry()

        self.create_add_contact_button()
        self.create_edit_contact_button()
        self.create_delete_contact_button()
        self.create_delete_all_contact_button()
        self.create_save_button()

    def style_ttk(self):
        # Add some style
        style = ttk.Style()
        # Select a theme
        style.theme_use('default')
        # Configure the Treeview Colors
        style.configure("Treeview", background = "#ffffff", foreground = "#000000", rowheight = 25)
        # Change the selected row color
        style.map("Treeview", background = [("selected", "#329b51")])

    def create_header_frame(self):
        frame = Frame(self, width = 20, height = 20, bg = "#034f31")
        frame.pack(fill = X)
        return frame

    def create_logo_label(self):
        label = Label(self.header_frame, image = self.contact_logo, bg = "#034f31")
        label.pack(side = LEFT, padx = (20, 0))

    def create_heading_label(self):
        label = Label(self.header_frame, text = "Contact Book", font = ("Helvetica", 16, "bold"), fg = "#d0e8de", bg = "#034f31")
        label.pack(padx = (10, 20), pady = 15, anchor = W)

    def create_contact_table_frame(self):
        frame = Frame(self)
        frame.pack(fill = X, padx = 20, pady = 10)
        return frame

    def create_contact_table(self):
        treeview = ttk.Treeview(self.table_frame, selectmode = EXTENDED)
        treeview.pack(side = LEFT, fill = X, expand = True)
        return treeview

    def create_table_scrollbar(self):
        scrollbar = Scrollbar(self.table_frame)
        scrollbar.pack(side = LEFT, fill = Y)
        return scrollbar

    def show_scrollbar(self):
        """
        Bind the scroll bar to the contact list table and activate
        its operation.
        """
        self.contact_table.config(yscrollcommand = self.contact_table.set)
        self.table_scrollbar.config(command = self.contact_table.yview)

    def add_contact_table_field(self):
        # name, phone number, email, and address
        self.contact_table['columns'] = ("First Name", "Last Name", "Phone No.", "Email", "Address")
        self.contact_table.column("#0", width = 0, stretch = NO)
        self.contact_table.column("First Name", width = 200, anchor = W)
        self.contact_table.column("Last Name", width = 200, anchor = W)
        self.contact_table.column("Phone No.", width = 180, anchor = W)
        self.contact_table.column("Email", width = 200, anchor = W)
        self.contact_table.column("Address", width = 200, anchor = W)

    def add_heading_to_contact_table_field(self):
        self.contact_table.heading("#0", text = "", anchor = W)
        self.contact_table.heading("First Name", text = "First Name", anchor = W)
        self.contact_table.heading("Last Name", text = "Last Name", anchor = W)
        self.contact_table.heading("Phone No.", text = "Phone No.", anchor = W)
        self.contact_table.heading("Email", text = "Email", anchor = W)
        self.contact_table.heading("Address", text = "Address", anchor = W)

    def demo_data(self):
        data = [
            ["Kaustab", "Roy", "9903782617", "roy.kaustab.03@gmail.com", "Manikpur Nabapally, Dum Dum Airport, Kolkata-700079"],
            ["Prantik", "Sen", "9872537238", "pran.20.tik@gmail.com", "Sahanagar, 12/7, Block-II Main Ground, Kolkata-700054"],
            ["Soma", "Chowdhury", "9234088723", "chow.soma@gmail.com", "Ratnagar Kalibari lane-4, Kolkata-700123"],
        ]
        return data
    
    def create_contact_table_stripped_rows(self):
        self.contact_table.tag_configure('oddrow', background = "#eff4f0")
        self.contact_table.tag_configure('evenrow', background = "#dceae0")

    def insert_fake_data(self):
        global count
        count = 0
        for dt in self.fake_data:
            if count % 2 == 0:
                self.contact_table.insert(parent = '', index = END, iid = f"{count}", text = '', values = (dt[0], dt[1], dt[2], dt[3], dt[4],), tags = ('evenrow',))
            else:
                self.contact_table.insert(parent = '', index = END, iid = f"{count}", text = '', values = (dt[0], dt[1], dt[2], dt[3], dt[4],), tags = ('oddrow',))
            count += 1

    def create_insert_data_frame(self):
        frame = LabelFrame(self, text = "Data View")
        frame.pack(fill = X, padx = 20)
        return frame
    
    def create_command_options_frame(self):
        frame = LabelFrame(self, text = "Commands")
        frame.pack(fill = X, padx = 20)
        return frame
    
    def create_insert_first_name_label_entry(self):
        label = Label(self.insert_frame, text = "First Name")
        label.grid(row = 0, column = 0, padx = 10, pady = 20)
        entry = Entry(self.insert_frame, width = 50)
        entry.grid(row = 0, column = 1, padx = 10, pady = 20)
        return entry
    
    def create_insert_last_name_label_entry(self):
        label = Label(self.insert_frame, text = "Last Name")
        label.grid(row = 0, column = 2, padx = 10, pady = 20)
        entry = Entry(self.insert_frame, width = 50)
        entry.grid(row = 0, column = 3, padx = 10, pady = 20)
        return entry
    
    def create_insert_phone_label_entry(self):
        label = Label(self.insert_frame, text = "Phone No.")
        label.grid(row = 0, column = 4, padx = 10, pady = 20)
        entry = Entry(self.insert_frame, width = 50)
        entry.grid(row = 0, column = 5, padx = 10, pady = 20)
        return entry
    
    def create_insert_email_label_entry(self):
        label = Label(self.insert_frame, text = "Email")
        label.grid(row = 1, column = 0, padx = 10, pady = 20)
        entry = Entry(self.insert_frame, width = 50)
        entry.grid(row = 1, column = 1, padx = 10, pady = 20)
        return entry
    
    def create_insert_address_label_entry(self):
        label = Label(self.insert_frame, text = "Address")
        label.grid(row = 1, column = 2, padx = 10, pady = 20)
        entry = Entry(self.insert_frame, width = 50)
        entry.grid(row = 1, column = 3, padx = 10, pady = 20)
        return entry
    
    def create_save_button(self):
        button = Button(self.insert_frame, text = "Save")
        button.grid(row = 1, column = 5, padx = 10, pady = 10)
    
    def create_add_contact_button(self):
        button = Button(self.command_frame, text = "Create New Contact")
        button.grid(row = 0, column = 0, padx = 10, pady = 10)

    def create_edit_contact_button(self):
        button = Button(self.command_frame, text = "Edit Contact Details")
        button.grid(row = 0, column = 1, padx = 10, pady = 10)

    def create_delete_contact_button(self):
        button = Button(self.command_frame, text = "Delete Contact", command = self.delete_selected_row)
        button.grid(row = 0, column = 2, padx = 10, pady = 10)

    def create_delete_all_contact_button(self):
        button = Button(self.command_frame, text = "Create New Contact")
        button.grid(row = 0, column = 3, padx = 10, pady = 10)

    def delete_selected_row(self):
        pass

    def run(self):
        self.mainloop()

if __name__ == '__main__':
    app = ContactBook()
    app.run()
