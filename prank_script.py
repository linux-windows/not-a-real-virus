import tkinter as tk
from tkinter import messagebox
import time

# Function to create the red screen effect, filling from the corner
def create_red_screen():
    root = tk.Tk()
    root.attributes("-fullscreen", True)  # Make it full screen
    root.configure(bg='white')  # Initially set the background to white
    root.title("NO ESCAPE!!!")

    # Create a canvas to draw the red screen effect
    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack()

    # Start with a small red rectangle in the top-left corner
    rect_width = 1
    rect_height = 1

    # Function to gradually increase the size of the red rectangle
    def expand_red():
        nonlocal rect_width, rect_height
        rect_width += 5  # Increase width by 5 pixels
        rect_height += 5  # Increase height by 5 pixels

        # Draw a red rectangle on the canvas
        canvas.create_rectangle(0, 0, rect_width, rect_height, fill="red", outline="red")

        # If the rectangle hasn't covered the entire screen, keep expanding
        if rect_width < root.winfo_screenwidth() and rect_height < root.winfo_screenheight():
            root.after(10, expand_red)  # Keep calling expand_red every 10ms

        # Once the red screen is fully expanded, show the warning
        else:
            root.after(500, show_warning, root)

    # Start the red expansion
    expand_red()

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
        time.sleep(1000)
        root.quit()  # Close the red screen after the warning

    def ok_action():
        messagebox.showinfo("OK", "Proceeding with the deletion of files.")
        top.destroy()
        time.sleep(1000)
        root.quit()  # Close the red screen after the warning

    # Create the custom buttons (No "Cancel" button)
    ok_button = tk.Button(top, text="OK", command=ok_action)
    proceed_button = tk.Button(top, text="Proceed", command=proceed_action)

    ok_button.pack(side="left", padx=10, pady=10)
    proceed_button.pack(side="right", padx=10, pady=10)

    top.mainloop()

# Run the red screen and warning
create_red_screen()
