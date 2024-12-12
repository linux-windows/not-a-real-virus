import tkinter as tk
from tkinter import messagebox
import random

def show_final_warning():
    """Display the prank warning about deleting the hard drive."""
    response = messagebox.askyesno(
        title="Warning",
        message="Selecting 'OK' will erase the contents of the hard drive. Do you wish to proceed?"
    )
    if response:
        messagebox.showinfo("Action", "This is a test. No data will be erased.")
    else:
        messagebox.showinfo("Action", "Proceeding... Just kidding! No data erased.")

def show_no_escape():
    """Display the 'NO ESCAPE!!!!' warning."""
    messagebox.showerror("NO ESCAPE!!!!", "There is no way out! The end is near!")
    root.after(2000, show_final_warning)  # Delay before showing the final warning

def change_background():
    """Change the background to random shades of red."""
    r = random.randint(100, 255)  # Random red intensity
    color = f'#{r:02x}0000'  # Hex color format for shades of red
    root.configure(background=color)
    root.after(100, change_background)  # Change color every 100ms

# Create the main application window
root = tk.Tk()

# Force fullscreen to cover everything, including taskbar
root.attributes('-fullscreen', True)

# Hide the mouse cursor
root.config(cursor="none")

# Remove Escape key functionality for exiting
# root.bind('<Escape>', lambda e: None)

# Start changing the background colors
root.after(500, change_background)

# Show the "NO ESCAPE!!!!" warning after 2 seconds
root.after(2000, show_no_escape)

# Start the main loop
root.mainloop()
