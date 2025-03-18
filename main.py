# Import libraries
from tkinter import *

class FinanceGUI:
    #Method for submitting TopLevel Form
    def on_submit_click(self):
        print("Filler code for time being")

    #Method for adding in a new allocation
    def on_add_click(self):
        #Create Top Level
        add_window = Toplevel()
        add_window.title("Add Money Allocation")
        add_window.geometry("1000x500")

        #Create input fields
        #Title
        name_title = Label(add_window, text="Name of Allocation:")
        name_title.pack(anchor=CENTER)
        name_entry = Entry(add_window)
        name_entry.pack(anchor= CENTER)
        #Radio buttons
        radio1 = Radiobutton(add_window, text="Value")
        radio2 = Radiobutton(add_window, text="Percentage")
        radio1.pack(anchor= CENTER)
        radio2.pack(anchor= CENTER)
        #Value
        value_title = Label(add_window, text="Value:")
        value_title.pack(anchor=CENTER)
        value_entry = Entry(add_window)
        value_entry.pack(anchor=CENTER)
        #Submit button
        submit_button = Button(add_window, command=self.on_submit_click, text="Add", bg="blue", fg="white")
        submit_button.pack(anchor=CENTER)

    def main(self):
        root = Tk()

        # Window properties
        root.title("Finance GUI")
        root.minsize(1700, 900)

        # Frames
        #Income frame
        income_frame = Frame(root)
        income_frame.pack(pady=40, fill="x")
        #Income elements
        #label
        income_label = Label(income_frame, text="Income:", justify=LEFT)
        income_label.grid(row=0, column=0)
        #dropdown
        options = [
            "Weekly",
            "Fortnightly",
            "Monthly"
        ]

        clicked = StringVar()
        income_drop = OptionMenu(income_frame, clicked, *options)
        income_drop.grid(row=1, column=0)
        #input field
        income_input = Entry(income_frame)
        income_input.grid(row=1, column=1)

        #Allocation frame
        allocation_frame = Frame(root)
        allocation_frame.pack(pady=40, fill="x")
        #allocation elements
        #button
        add_button = Button(allocation_frame, text="+", command=self.on_add_click, bg="blue", fg="white", justify=CENTER, height=6, width=12)
        add_button.grid(row=0, column=0)

        #Remaining frame
        remaining_frame = Frame(root)
        remaining_frame.pack(pady=40, fill="x")
        #remaining elements
        #label
        remaining_label = Label(remaining_frame, text="Remaining:", justify=CENTER)
        remaining_label.grid(row=0, column=0)


        # Close main loop
        root.mainloop()

if __name__ == "__main__":
    FinanceGUI().main()