# import tkinter as tk
# from tkinter import messagebox
# from gtts import gTTS
# import os

# def play_text():
#     text = text_entry.get("1.0", tk.END).strip()
#     if text:
#         try:
#             tts = gTTS(text, lang='en')
#             tts.save("output.mp3")
#             os.system("start output.mp3" if os.name == "nt" else "open output.mp3")
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {e}")
#     else:
#         messagebox.showwarning("Warning", "Please enter some text to play.")

# def clear_text():
#     text_entry.delete("1.0", tk.END)

# def exit_app():
#     root.destroy()

# # Create the main window
# root = tk.Tk()
# root.title("Text-to-Speech App")
# root.geometry("400x300")

# # Create a text entry widget
# text_entry = tk.Text(root, wrap=tk.WORD, height=10, width=40)
# text_entry.pack(pady=10)

# # Create buttons
# play_button = tk.Button(root, text="Play", command=play_text)
# play_button.pack(pady=5)

# set_button = tk.Button(root, text="Set", command=clear_text)
# set_button.pack(pady=5)

# exit_button = tk.Button(root, text="Exit", command=exit_app)
# exit_button.pack(pady=5)

# # Run the application
# root.mainloop()
import tkinter as tk
from tkinter import messagebox, ttk
from gtts import gTTS
import subprocess
import platform

# Define supported languages manually
SUPPORTED_LANGUAGES = {"English": "en", "Arabic": "ar", "French": "fr", "Spanish": "es"}

def play_text():
    """Convert text to speech and play the audio."""
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        try:
            language = SUPPORTED_LANGUAGES.get(lang_var.get(), "en")  # Get selected language
            
            tts = gTTS(text, lang=language)
            audio_file = "output.mp3"
            tts.save(audio_file)
            
            # Platform-independent audio playback
            if platform.system() == "Windows":
                subprocess.run(["start", audio_file], shell=True)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["afplay", audio_file])
            else:  # Linux/Other
                subprocess.run(["xdg-open", audio_file])
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter some text to play.")

def clear_text():
    """Clear the text entry."""
    text_entry.delete("1.0", tk.END)

def exit_app():
    """Exit the application."""
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Text-to-Speech App")
root.geometry("400x350")
root.resizable(False, False)

# Set background color
root.configure(bg="#eaf4f4")

# Define styles
style = ttk.Style()
style.theme_use("default")  # Use the default theme
style.configure(
    "TButton",
    font=("Arial", 12, "bold"),
    padding=5,
    background="#007ACC",
    foreground="white",
    borderwidth=2,
)
style.map(
    "TButton",
    background=[("active", "#005A9E")],
    foreground=[("active", "white")],
)
style.configure("TLabel", background="#eaf4f4", font=("Arial", 12, "bold"), foreground="#333333")
style.configure("TFrame", background="#eaf4f4")
style.configure("TOptionMenu", background="#eaf4f4", foreground="#333333", font=("Arial", 12))

# Language selection
lang_var = tk.StringVar(value="English")
ttk.Label(root, text="Select Language:").pack(pady=5)
lang_menu = ttk.OptionMenu(root, lang_var, "English", *SUPPORTED_LANGUAGES.keys())
lang_menu.pack(pady=5)

# Create a text entry widget
text_entry = tk.Text(root, wrap=tk.WORD, height=10, width=40, font=("Arial", 12), bg="#ffffff", fg="#333333", bd=2, relief="solid")
text_entry.pack(pady=10)

# Create buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

play_button = ttk.Button(button_frame, text="Play", command=play_text)
play_button.grid(row=0, column=0, padx=5)

clear_button = ttk.Button(button_frame, text="Clear", command=clear_text)
clear_button.grid(row=0, column=1, padx=5)

exit_button = ttk.Button(button_frame, text="Exit", command=exit_app)
exit_button.grid(row=0, column=2, padx=5)
footer_label = tk.Label(root, text="eslam  ahmede lsherbiny", font=("Arial", 10, "italic"), bg="black", fg="gray")
footer_label.pack(side="bottom", pady=5)

# Run the application
root.mainloop()