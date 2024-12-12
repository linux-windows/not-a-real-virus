import tkinter as tk
from tkinter import messagebox

# Function to create the red screen
def create_red_screen():
    root = tk.Tk()
    root.attributes("-fullscreen", True)  # Make it full screen
    root.configure(bg='red')  # Set the background color to red
    root.title("NO ESCAPE!!!")

    # Add a label to the screen for effect
    label = tk.Label(root, text="NO ESCAPE!!!", font=("Helvetica", 40), fg="white", bg="red")
    label.pack(expand=True)

    # After 2 seconds, show the warning message with custom buttons
    root.after(2000, show_warning, root)

    root.mainloop()

# Function to display the warning with custom buttons
def show_warning(root):
    # Hide the main window (red screen)
    root.withdraw()

    # Create the warning window
    top = tk.Toplevel(root)
    top.title("Warning")

    # Add the warning message
    label = tk.Label(top, text="Selecting 'OK' will erase the contents of the hard drive. Do you wish to proceed?")
    label.pack(pady=20)

    # Define the button actions
    def proceed_action():
        messagebox.showinfo("Proceeding", "Files will be deleted.")
        top.destroy()
        root.quit()  # Close the red screen after the warning

    def ok_action():
        messagebox.showinfo("OK", "Proceeding with the deletion of files.")
        top.destroy()
        root.quit()  # Close the red screen after the warning

    # Create the custom buttons
    ok_button = tk.Button(top, text="OK", command=ok_action)
    proceed_button = tk.Button(top, text="Proceed", command=proceed_action)

    ok_button.pack(side="left", padx=10, pady=10)
    proceed_button.pack(side="right", padx=10, pady=10)

    top.mainloop()

# Run the red screen and warning
create_red_screen()
