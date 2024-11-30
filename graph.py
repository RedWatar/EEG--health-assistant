import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import threading
import time

# Brainwave Band Information
BAND_INFO = {
    "Alpha": "Associated with relaxation and calmness during meditation or light activities.",
    "Beta": "Represents active thinking and problem-solving. Dominant in focused tasks.",
    "Theta": "Linked to deep relaxation, creativity, and light sleep states.",
    "Delta": "Seen in deep sleep or unconscious states. Associated with restoration and healing.",
}

# Initialize Tkinter
root = tk.Tk()
root.title("NeuroGuard: EEG Band Visualization")
root.geometry("900x700")

# Data Variables
brainwave_bands = {"Alpha": 0, "Beta": 0, "Theta": 0, "Delta": 0}
running = False

# Function to Simulate Data
def simulate_data():
    while running:
        # Randomize band values for simulation
        brainwave_bands["Alpha"] = random.randint(50, 100)
        brainwave_bands["Beta"] = random.randint(100, 200)
        brainwave_bands["Theta"] = random.randint(30, 80)
        brainwave_bands["Delta"] = random.randint(10, 40)
        update_graph()
        time.sleep(1)

# Function to Start Data Simulation
def start_simulation():
    global running
    running = True
    threading.Thread(target=simulate_data, daemon=True).start()
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

# Function to Stop Data Simulation
def stop_simulation():
    global running
    running = False
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

# Function to Update Graph
def update_graph():
    # Clear the figure
    ax.clear()
    
    # Plot bar chart
    bands = list(brainwave_bands.keys())
    values = list(brainwave_bands.values())
    ax.bar(bands, values, color=["blue", "green", "yellow", "red"])
    
    # Set plot titles and labels
    ax.set_title("EEG Brainwave Bands", fontsize=16)
    ax.set_ylabel("Amplitude", fontsize=12)
    ax.set_xlabel("Band", fontsize=12)
    ax.set_ylim(0, 250)
    
    # Redraw the canvas
    canvas.draw()

# GUI Layout
ttk.Label(root, text="NeuroGuard EEG Band Graph", font=("Helvetica", 16)).pack(pady=10)

# Add Matplotlib Figure
fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack()

# Add Band Explanations
info_frame = ttk.Frame(root)
info_frame.pack(pady=10, fill=tk.BOTH, expand=True)

ttk.Label(info_frame, text="Brainwave Band Explanations", font=("Helvetica", 14)).pack(anchor="w", padx=10, pady=5)

for band, info in BAND_INFO.items():
    ttk.Label(info_frame, text=f"{band}: {info}", wraplength=800, font=("Helvetica", 10), justify="left").pack(anchor="w", padx=10, pady=2)

# Add Buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

start_button = ttk.Button(button_frame, text="Start Simulation", command=start_simulation)
start_button.grid(row=0, column=0, padx=5)

stop_button = ttk.Button(button_frame, text="Stop Simulation", command=stop_simulation, state=tk.DISABLED)
stop_button.grid(row=0, column=1, padx=5)

# Run Tkinter Mainloop
root.mainloop()
