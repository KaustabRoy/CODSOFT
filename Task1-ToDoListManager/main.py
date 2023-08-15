# TASK - 1
# A To-Do List application is a useful project that helps users manage and organize their tasks efficiently.
# This project aims to create a command-line or GUI-based application using Python, allowing users to create, update,
# and track their to-do lists.

from tkinter import *
import tkinter.messagebox as msg
import os
from termcolor import colored

class TodoApp(Tk):

    def __init__(self):
        super().__init__()
        # Centering the window when opened.
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        print(colored(f"SCREEN WIDTH : {screen_width} x SCREEN HEIGHT : {screen_height}", "blue"))
        app_width = 1000
        app_height = 800
        print(colored(f"APP WIDTH : {app_width} x APP HEIGHT : {app_height}", "blue"))
        set_x = int((screen_width/2) - (app_width/2))
        set_y = int((screen_height/2) - (app_height/2))
        self.geometry(f'{app_width}x{app_height}+{set_x}+{set_y}')
        self.title("TodoList Manager")
        self.resizable(False, False)
        # Design
        self.create_app_heading()
        self.give_separation_line()
        self.item_input_frame = self.create_input_frame()
        self.item_entry_box = self.create_new_item_entry_box()
        self.create_add_button()
        self.list_display_frame = self.create_display_frame()
        self.todo_display_listbox = self.create_todo_list_box()
        self.listbox_scrollbar = self.add_listbox_scrollbar()
        self.show_scrollbar()
        self.operation_button_frame = self.create_operation_frame()
        self.edit_img = PhotoImage(file='Images/edit.png')
        self.create_edit_button()
        self.clear_img = PhotoImage(file='Images/clear.png')
        self.create_clear_button()
        self.remove_img = PhotoImage(file='Images/remove.png')
        self.create_delete_button()
        self.uncross_img = PhotoImage(file='Images/save.png')
        self.create_uncross_button()
        self.cross_img = PhotoImage(file='Images/cross.png')
        self.create_cross_button()
        # Functions
        self.listbox_load()

    # Designing The application's interface.

    def create_app_heading(self):
        """
        Creates the top heading for the application.
        """
        app_heading = Label(self, text = "TODO-List Manager", font = ('Pristina', 27, 'bold'), pady = 20, bg = "#e9ecf4")
        app_heading.pack(fill = X)

    def give_separation_line(self):
        """
        Adds a separation line after a desired frame or widget.
        """
        frame = Frame(self, bg = "#0b227a", height = 5)
        frame.pack(fill = X)

    def create_input_frame(self):
        """
        Creates the frame on the root window for placing the
        desired widgets related to performing input operations.
        """
        frame = Frame(self, bg = "#38393f", height = 100, padx = 20, pady = 20)
        frame.pack(fill = X)
        return frame

    def create_new_item_entry_box(self):
        """
        Adds an entry box to the input related frame
        for entering the new task item to be added.
        """
        entry = Entry(self.item_input_frame, width = 50, borderwidth = 0, font = ('Helvetica', 22))
        entry.pack(side = LEFT)
        return entry

    def create_add_button(self):
        """
        Creates a button to the input related frame
        for adding the entered task to the list box.
        """
        button = Button(self.item_input_frame, text = "Add to list", width = 18, borderwidth = 0, font = ('Helvetica', 14, 'bold'), bg = "#2e5d72", fg = "#ffffff", command = self.add_item)
        button.pack(side = LEFT)

    def create_display_frame(self):
        """
        Creates the frame on the root window for placing the
        desired widgets related to performing display operations.
        """
        frame = Frame(self, width = 200, height = 700, bg = "#274a5a", padx = 20, pady = 20)
        frame.pack(fill = BOTH)
        return frame

    def create_todo_list_box(self):
        """
        Creates a listbox to display all the items added to the task list.
        """
        listbox = Listbox(self.list_display_frame, width = 78, height = 20, font = ('Helvetica', 16), bg = "#dde1e3", fg = "#0e0c49", selectbackground = "#6016d9", activestyle = NONE, cursor = "hand2")
        listbox.pack(side = LEFT, fill = BOTH)
        return listbox

    def add_listbox_scrollbar(self):
        """
        Adds a scroll bar to the listbox for scrolling vertically
        through the listbox when the list of tasks is too long.
        """
        scrollbar = Scrollbar(self.list_display_frame)
        scrollbar.pack(side = LEFT, fill = BOTH)
        return scrollbar

    def show_scrollbar(self):
        """
        Bind the scroll bar to the display listbox and activate
        its operation.
        """
        self.todo_display_listbox.config(yscrollcommand = self.listbox_scrollbar.set)
        self.listbox_scrollbar.config(command = self.todo_display_listbox.yview)

    def create_operation_frame(self):
        """
        Creates the frame on the root window for placing the
        desired widgets related to performing various operations like:
        disable a task, delete a disabled task, edit a specific task, etc.
        """
        frame = Frame(self, bg = "#38393f")
        frame.pack(fill = BOTH)
        return frame

    def create_edit_button(self):
        """
        Create an edit button with an edit icon to prompt
        the user to edit the selected task upon clicking the button.
        """
        button = Button(self.operation_button_frame, image = self.edit_img, bd = 0, bg = "#38393f", cursor = "hand2", command = self.edit_task)
        button.pack(side = LEFT, pady = 10, padx = 10)

    def create_delete_button(self):
        """
        Create a delete button with a trash icon to delete a
        disabled task.
        """
        button = Button(self.operation_button_frame, image = self.remove_img, bd = 0, bg = "#38393f", cursor = "hand2", command = self.delete_crossed_item)
        button.pack(side = RIGHT, pady = 10, padx = (10, 330))

    def create_uncross_button(self):
        """
        Create an uncross button with a tick icon to enable a
        disabled task.
        """
        button = Button(self.operation_button_frame, image = self.uncross_img, bd = 0, bg = "#38393f", cursor = "hand2", command = self.uncross_item)
        button.pack(side = RIGHT, pady = 10, padx = 10)

    def create_cross_button(self):
        """
        Create a cross button with a times icon to disable
        a desired task.
        """
        button = Button(self.operation_button_frame, image = self.cross_img, bd = 0, bg = "#38393f", cursor = "hand2", command = self.cross_item)
        button.pack(side = RIGHT, pady = 10, padx = 10)

    def create_clear_button(self):
        """
        Create a clear button with a sweep icon to clear all the
        task items present in the list.
        """
        button = Button(self.operation_button_frame, image = self.clear_img, bd = 0, bg = "#38393f", cursor = "hand2", command = self.clear_list)
        button.pack(side = RIGHT, pady = 10, padx = 10)

# Adding the functionalities and events to the application.

    def blank_line_handler(self):
        """
        Handle the text file if there is a blank line,
        remove the blank unnecessary blank line and save
        the changes to the assigned text file.
        """
        with open("todo.txt", "r") as tdf:
            lines = tdf.readlines()
        for line in lines:
            if line.strip("\n"):
                os.rename('todo.txt', 'old_todo.txt')
                break
            else:
                pass
        try:
            with open("old_todo.txt", "r") as old_tdf:
                new_tdf = open('todo.txt', "w")
                lines = old_tdf.readlines()
                for line in lines:
                    if line.strip("\n"):
                        new_tdf.write(line)
            os.remove("old_todo.txt")
        except FileNotFoundError:
            message = colored("No blank lines in the file.")
            print(message)

    def add_item(self):
        """
        Function for the add item button. Adds the entered
        new task and add to the list items in the file and save
        the changes to the text file.
        """
        new_item = self.item_entry_box.get()
        with open('todo.txt', "r+") as tdf:
            number_of_lines = len(tdf.readlines())
            print(colored(f"The total number of tasks in the list: {number_of_lines+1}", "magenta"))
            if number_of_lines >= 1:
                tdf.write(f"\n{new_item}")
            else:
                tdf.write(new_item)
        self.listbox_load()
        self.item_entry_box.delete(0, END)

    def listbox_load(self):
        """
        Function for the add item button. Adds the entered
        new task and add to the list items in the file and save
        the changes to the text file.
        """
        self.blank_line_handler()
        self.todo_display_listbox.delete(0, END)
        try:
            with open('todo.txt', "r") as tdf:
                lines = tdf.readlines()
            for line in lines:
                self.todo_display_listbox.insert(END, line)
        except Exception as e:
            warning = colored(f"SORRY! EXCEPTION OCCURRED: {e}", "red")
            print(warning)
            tdf = open('todo.txt', "w")
            tdf.close()

    def cross_item(self):
        """
        Function for the cross button. Greys the desired selected
        text to indicate the task is disabled by the user
        """
        try:
            self.todo_display_listbox.itemconfig(self.todo_display_listbox.curselection(), fg = "#b7b3bd")
            self.todo_display_listbox.selection_clear(0, END)
        except Exception:
            print(colored(f"CROSS EVENT ERROR : empty task list ", "light_yellow"))
            msg.showwarning(title = "WARNING", message = "Task list is empty.")

    def uncross_item(self):
        """
        Function for the uncross item button. Converts a selected
        disabled task to its default color to indicate the task is
        an active task.
        """
        try:
            self.todo_display_listbox.itemconfig(self.todo_display_listbox.curselection(), fg = "#0e0c49")
            self.todo_display_listbox.selection_clear(0, END)
        except Exception:
            print(colored(f"UNCROSS EVENT ERROR : empty task list ", "light_yellow"))
            msg.showwarning(title = "WARNING", message = "Task list is empty.")

    def save_edit_task(self, line_number, task):
        """
        Function to save the new edited task to the corresponding
        line number passed as parameter and save the changes to the text file.
        Closes the pop-up edit wizard upon saving the changes.
        :param line_number: the index number of the selected task
        :param task: the selected task
        """
        new_task = f"LINE NUMBER : {line_number}\tTASK : {task}"
        print(new_task)
        with open("todo.txt", "r") as tdf:
            lines = tdf.readlines()
            lines[line_number] = task+"\n"
            message = colored(f"The edited list of tasks: {lines}", "green")
            print(message)
        with open("todo.txt", "w") as tdf:
            for line in lines:
                tdf.write(line)
        self.listbox_load()
        edit_task_popup_window.destroy()
        msg.showinfo(title = "Edited", message = f"Successfully edited Task {line_number+1}!")

    def popup_edit_task(self, item_number, editable_task):
        """
        Creates a pop-up wizard to edit the desired task after
        clicking on the edit button.
        :param item_number: index number of the task
        :param editable_task: the selected task to be edited
        """
        global edit_task_popup_window
        edit_task_popup_window = Toplevel(self)
        edit_task_popup_window.geometry("700x215")
        edit_task_popup_window.resizable(False, False)
        edit_task_popup_window.title(f"Edit task {item_number+1}")
        label = Label(edit_task_popup_window, text = f"EDIT TASK:\n{editable_task}", fg = "#1d3b64", font = ("Helvetica", 16))
        label.pack()
        task = Entry(edit_task_popup_window, width = 60, font = ("Helvetica", 14), fg = "#1d3b64")
        task.insert(0, editable_task)
        task.pack(pady = 20)
        btn_frame = Frame(edit_task_popup_window, padx = 20, pady = 20)
        btn_frame.pack()
        btn_save = Button(btn_frame, text = "SAVE", width = 13, bd = 0, bg = "#3c8bdf", fg = "#ffffff", font = ("Helvetica", 13, "bold"), command = lambda : self.save_edit_task(item_number, task.get()))
        btn_save.pack(side = LEFT, padx = (370, 10))
        btn_cancel = Button(btn_frame, text = "CANCEL", width = 13, bd = 0, bg = "#3c8bdf", fg = "#ffffff", font = ("Helvetica", 13, "bold"), command = edit_task_popup_window.destroy)
        btn_cancel.pack(side = LEFT)
        edit_task_popup_window.mainloop()

    def edit_task(self):
        """
        Gets the selected task and its corresponding line number and
        passes it on to the editing pop-up wizard for the user.
        """
        try:
            selected_item = self.todo_display_listbox.curselection()
            if selected_item:
                print(f"You have selected item number: {selected_item}")
                with open("todo.txt", "r+") as tdf:
                    lines = tdf.readlines()
                    selected_task = lines[selected_item[0]]
                    print(f"You have selected task: {selected_task}")
                win_title = selected_item[0]
                self.popup_edit_task(item_number = win_title, editable_task = selected_task)
            else:
                msg.showwarning(title = "WARNING", message = "Please select a task to edit.")
        except Exception:
            print(colored("EDIT EVENT ERROR : empty task list", "light_yellow"))
            msg.showwarning(title = "WARNING", message = "Task list is empty.")

    def delete_crossed_item(self):
        """
        Deletes the item(s) that is/are disabled or crossed i.e. greyed by
        the user upon clicking the delete or trash icon.
        """
        index = 0
        length_diff = 0
        while index < self.todo_display_listbox.size():
            if self.todo_display_listbox.itemcget(index, 'fg') == "#b7b3bd":
                line_no = self.todo_display_listbox.index(index)
                item = self.todo_display_listbox.get(index)
                info = colored(f"DELETE LINE NO.: {line_no}, TASK: {item}", "red")
                print(info)
                operation = msg.askyesno(title = "Confirm", message = f"Do you want to delete task - {item}")
                print(f"DELETE : {operation}")
                if operation is True:
                    try:
                        with open("todo.txt", "r") as tdf:
                            lines = tdf.readlines()
                            del lines[line_no]
                            length_diff += 1
                        print(f"length difference = {length_diff}")
                    except IndexError:
                        print(colored("HANDLING GENERATED INDEX ERROR", "cyan"))
                        error_index = index
                        print(f"ERROR INDEX = {error_index}")
                        print(f"LENGTH DIFFERENCE = {length_diff}")
                        del_index = (error_index - length_diff)
                        print(f"DELETE INDEX: {del_index}")
                        del lines[del_index]
                    finally:
                        with open("todo.txt", "w") as new_tdf:
                            for line in lines:
                                new_tdf.write(line)
                else:
                    message = colored(f"Operation Delete - {item}\tCancelled by user!", "red")
                    print(message)
            index += 1
        self.blank_line_handler()
        self.listbox_load()

    def clear_list(self):
        """
        This event is triggered when user clicks the clear icon.
        It clears all the tasks in the task list irrespective of
        their status(disabled or active).
        """
        operation = msg.askyesno(title = "CLEAR LIST", message = "Do you want to clear the complete list?")
        if operation is True:
            try:
                with open("todo.txt", "w+") as tdf:
                    lines = tdf.readlines()
                    lines.clear()
            except Exception as e:
                print(f"Exception : {e}")
            finally:
                self.listbox_load()
        else:
            message = colored("Operation CLEAR THE COMPLETE LIST is cancelled by the user!", "red")
            print(message)

    def run(self):
        """
        Executes the application on a loop.
        """
        self.mainloop()

if __name__ == '__main__':
    app = TodoApp()
    app.run()