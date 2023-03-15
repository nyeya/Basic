# Import the necessary modules
from tkinter import *
import time

# Create a new window using the Tk class
root = Tk()

# Set the size of the window to 270x100 pixels
root.geometry("270x100")

# Set the title of the window to "Simple Clock - NYEYA"
root.title("Simple Clock - NYEYA")

# Make the window non-resizable
root.resizable(0, 0)

# Set the background color of the window to blue
root.config(bg='blue')

# Define a function that will update the clock time and AM/PM label every second
def reClock():
    # Update the clock time label with the current time
    clock.config(text=f"{time.strftime('%I:%M:%S')}")

    # Determine whether the current time is AM or PM and update the label accordingly
    am.config(text=f"{'AM' if int(time.strftime('%H')) < 12 else 'PM'}")

    # Schedule the function to run again in 1000ms (1 second)
    clock.after(1000, reClock)

# Create a label to display the clock time
clock = Label(root, bg='blue', fg='yellow', font=('arial', 40, 'bold'))

# Position the clock label to the left side of the window
clock.pack(side=LEFT)

# Create a label to display whether the time is AM or PM
am = Label(root, background='blue', fg="yellow", text="AM", font=('arial', 20, 'bold'))

# Position the AM/PM label below the clock label with some padding
am.pack(side=LEFT, pady=(14, 0))

# Call the reClock function to start updating the clock time and AM/PM label
reClock()

# Start the main event loop to display the window and run the program
root.mainloop()
