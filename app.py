import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import openai  # Or your relevant API for generating responses

# Constants for colors and styles
BG_COLOR = "#f0f0f0"
TEXT_COLOR = "#333"
BUTTON_COLOR = "#4CAF50"
FONT = ("Helvetica", 12)

# Initialize the main window
root = tk.Tk()
root.title("EEG Data Collection and Question Assistant")
root.geometry("700x600")

# Notebook (Tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

# Tab 1: Data Collection Tab
data_frame = tk.Frame(notebook, bg=BG_COLOR)
notebook.add(data_frame, text="EEG Data Collection")

# Data Collection Widgets
name_var = tk.StringVar()
age_var = tk.StringVar()
gender_var = tk.StringVar()
file_content_var = tk.StringVar()

# Helper function to create label-entry pairs
def create_label_entry(frame, label_text, variable):
    label = tk.Label(frame, text=label_text, fg=TEXT_COLOR, bg=BG_COLOR)
    label.pack(pady=5)
    entry = ttk.Entry(frame, textvariable=variable, width=40)
    entry.pack(pady=5)
    return entry

# Create label-entry pairs for data collection
create_label_entry(data_frame, "Name:", name_var)
create_label_entry(data_frame, "Age:", age_var)
create_label_entry(data_frame, "Gender:", gender_var)

# File content (for EEG data input)
file_content_label = tk.Label(data_frame, text="EEG Data Content:", fg=TEXT_COLOR, bg=BG_COLOR)
file_content_label.pack(pady=10)

file_content_entry = scrolledtext.ScrolledText(data_frame, wrap=tk.WORD, width=50, height=10)
file_content_entry.pack(pady=5)

# Button to submit EEG data (simulated here)
def submit_data():
    try:
        # Collect data and display message (just for simulation)
        name = name_var.get()
        age = age_var.get()
        gender = gender_var.get()
        file_content = file_content_var.get()
        
        if not name or not age or not gender or not file_content:
            messagebox.showwarning("Input Error", "All fields must be filled!")
            return

        # Simulate saving data (in a real-world scenario, you would save to a database or file)
        messagebox.showinfo("Data Submitted", f"Data for {name} submitted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Submit Button for Data Collection
submit_button = tk.Button(data_frame, text="Submit EEG Data", command=submit_data, bg=BUTTON_COLOR, fg="white", font=FONT)
submit_button.pack(pady=10)

# Tab 2: EEG Question Assistant Tab
assistant_frame = tk.Frame(notebook, bg=BG_COLOR)
notebook.add(assistant_frame, text="EEG Question Assistant")

# Helper function to create a question assistant interface
def submit_question():
    try:
        background_prompt = (
            f"Name: {name_var.get()}\nAge: {age_var.get()}\nGender: {gender_var.get()}\n\n"
            f"EEG Data Content: {file_content_var.get()}"
        )
        user_question = question_entry.get()

        if not user_question:
            messagebox.showwarning("Input Error", "Please enter a question.")
            return
        
        complete_prompt = f"{background_prompt}\nUser's Question: {user_question}"

        # Simulate OpenAI API request (replace with your actual API call)
        response_text = "This is a simulated response based on the EEG data provided."

        # Display response in the scrolled text area
        response_display.delete(1.0, tk.END)
        response_display.insert(tk.END, response_text)

    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# GUI for EEG Question Assistant
question_label = tk.Label(assistant_frame, text="Enter your question:", fg=TEXT_COLOR, bg=BG_COLOR)
question_label.pack(pady=10)

question_entry = ttk.Entry(assistant_frame, width=50)
question_entry.pack(pady=5)

# Button to submit question
submit_question_button = tk.Button(assistant_frame, text="Submit Question", command=submit_question, bg=BUTTON_COLOR, fg="white", font=FONT)
submit_question_button.pack(pady=10)

# Response display area
response_display = scrolledtext.ScrolledText(assistant_frame, wrap=tk.WORD, bg=BUTTON_COLOR, fg=TEXT_COLOR, height=10, width=60)
response_display.pack(pady=10)

# Run the application
root.mainloop()
