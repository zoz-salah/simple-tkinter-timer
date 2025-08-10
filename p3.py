import tkinter as tk
import time
from threading import Thread

#Function to start the timer
def startTimer():
    try:
        minutes = int(entry.get())  # Get user input
    except ValueError:
        label_status.config(text="❌ Please enter a valid number", fg="red" , font =("arial" , 20 , "bold"))
        return
    
    totalSec = minutes * 60  # Convert minutes to seconds
    
    label_status.config(text="⏳ Timer is running...", fg="green",font =("arial" , 20 ,"bold"))
    
    # Run the timer in a separate thread so UI won't freeze
    def run():
        nonlocal totalSec
        while totalSec > 0:
            mins = totalSec // 60
            secs = totalSec % 60
            timer_label.config(text=f"{mins:02d}:{secs:02d}")  # Show time
            time.sleep(1)  # Wait 1 second
            totalSec -= 1
        
        label_status.config(text="🔔 DING DING DING!", fg="black" , font =("arial" , 30 , "bold"))
        timer_label.config(text="00:00")
    
    Thread(target=run, daemon=True).start()


#Create Tkinter window
root = tk.Tk()
root.title("⏲️ Simple Timer")  # Window title
root.geometry("420x620")  # Window size


tk.Label(root, text="Enter time in minutes:", font=("Arial",20)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 15), justify="center")
entry.pack(pady=5)

timer_label = tk.Label(root, text="00:00", font=("Arial", 30), fg="black")
timer_label.pack(pady=10)

label_status = tk.Label(root, text="", font=("Arial", 10))
label_status.pack()

start_button = tk.Button(root, text="Start", font=("Arial", 12),                   cursor = "hand2",
                    bd = 6,
                    activebackground = "green",
                    command=startTimer)
start_button.pack(pady=10)


root.mainloop()
