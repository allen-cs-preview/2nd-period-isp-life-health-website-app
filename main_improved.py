import tkinter as tk
from tkinter import ttk

# creating the main window
window = tk.Tk()
window.title("Health Diagnosis Tool")
window.geometry("500x400")  # increased window size for better layout
window.configure(bg="#d4f1f9")  # changed background color for a more pleasant look

# Creating the notebook (tabbed interface) for switching between pages
notebook = ttk.Notebook(window)
notebook.pack(fill='both', expand=True)

# Tab 1 - Main Interface
main_frame = ttk.Frame(notebook, width=500, height=400)
main_frame.pack(fill='both', expand=True)
notebook.add(main_frame, text="Diagnosis Tool")

# Tab 2 - Explanation Page
explanation_frame = ttk.Frame(notebook, width=500, height=400)
explanation_frame.pack(fill='both', expand=True)
notebook.add(explanation_frame, text="How it Works")

# Main Interface

# Title Label
title_label = tk.Label(
    main_frame, 
    text="Health Diagnosis Tool", 
    font=("Helvetica", 16, "bold"),
    bg="#d4f1f9",
    fg="#003366",
    pady=20
)
title_label.pack()

# Explanation text on the second page
explanation_text = """
This tool uses machine learning to predict possible conditions
based on the symptoms you provide. It processes your input
using a vectorizer to convert symptoms into numbers and then
finds the best match using a k-nearest neighbor algorithm.

It helps identify potential conditions like flu, cold, cancer, 
diabetes, and more based on the description of symptoms you provide.
"""
explanation_label = tk.Label(
    explanation_frame, 
    text=explanation_text, 
    font=("Helvetica", 12),
    bg="#d4f1f9", 
    fg="#003366", 
    justify="left", 
    padx=20, 
    pady=20
)
explanation_label.pack()

# Label for user input
input_label = tk.Label(
    main_frame, 
    text="Enter your symptoms below:", 
    font=("Helvetica", 12),
    bg="#d4f1f9",
    fg="#003366"
)
input_label.pack(pady=10)

# Input Textbox
entry = tk.Entry(main_frame, font=("Helvetica", 12), width=35, bd=2, relief="solid")
entry.pack(pady=5)

# This is where our backend function is
def backend(sym):
    # keeping the backend code unchanged
    stuff = [
        ["cancer", "bald, balding, weight loss, fatigue"],
        ["flu", "fever, headache, body aches, chills, sore throat"],
        ["cold", "runny nose, congestion, sneezing, mild cough"],
        ["migraine", "severe headache, nausea, sensitivity to light"],
        ["diabetes", "frequent urination, increased thirst, fatigue, blurred vision"],
        ["allergy", "sneezing, itchy eyes, runny nose, rash"],
        ["covid-19", "fever, cough, loss of taste or smell, fatigue, shortness of breath"],
        ["pneumonia", "chest pain, shortness of breath, fever, coughing"],
        ["anemia", "fatigue, weakness, pale skin, shortness of breath"],
        ["depression", "fatigue, loss of interest, difficulty concentrating, changes in sleep"]
    ]

    cond = [i[0] for i in stuff]
    symp = [i[1] for i in stuff]

    return back.backend(sym, cond, symp)

# return the text from backend into a label
def get_text():
    text = entry.get()
    processed_text = backend(text)
    result_label = tk.Label(
        main_frame, 
        text=f"Predicted Condition: {processed_text}", 
        font=("Helvetica", 12), 
        bg="#d4f1f9",
        fg="#003366",
        pady=10
    )
    result_label.pack()

# Submit Button
submit_button = tk.Button(
    main_frame, 
    text="Submit", 
    font=("Helvetica", 12, "bold"), 
    bg="#006699", 
    fg="white", 
    activebackground="#005580",
    activeforeground="white",
    relief="raised",
    command=get_text
)
submit_button.pack(pady=20)

# Run the application
window.mainloop()