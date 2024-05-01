# gui/main_window.py
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from api.openai import get_lyrics


def validate_prompt(new_text):
    return len(new_text) <= 50


def style_configuration():
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TButton', font=('Helvetica', 12), foreground='black')
    style.configure('TEntry', font=('Helvetica', 12), foreground='black')
    style.configure('TRadiobutton', font=('Helvetica', 12), foreground='black')


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.save_button = None
        self.lyrics_text = None
        self.iconbitmap('song-lyrics.ico')
        self.history_button = None
        self.generate_button = None
        self.poem_radiobutton = None
        self.song_radiobutton = None
        self.mode = None
        self.max_tokens_spinbox = None
        self.max_tokens_label = None
        self.loading_label = None
        self.prompt_entry = None
        self.prompt_label = None
        self.title("Lyric Generator")
        self.geometry("800x600")
        style_configuration()
        self.create_widgets()
        self.history = []

    def create_widgets(self):
        self.create_prompt_label()
        self.create_prompt_entry()
        self.create_loading_label()
        self.create_max_tokens_label()
        self.create_max_tokens_spinbox()
        self.create_mode_radiobuttons()
        self.create_generate_button()
        self.create_history_button()
        self.create_lyrics_text()
        self.create_save_button()

    def create_prompt_label(self):
        self.prompt_label = ttk.Label(self, text="Enter your prompt:")
        self.prompt_label.grid(row=0, column=0, sticky='w')

    def create_prompt_entry(self):
        validate_cmd = self.register(validate_prompt)
        self.prompt_entry = ttk.Entry(self, width=50, validate="key", validatecommand=(validate_cmd, '%P'))
        self.prompt_entry.grid(row=1, column=0, sticky='w')

    def create_loading_label(self):
        self.loading_label = ttk.Label(self, text="")
        self.loading_label.grid(row=9, column=0, sticky='w')

    def create_max_tokens_label(self):
        self.max_tokens_label = ttk.Label(self, text="Enter the maximum number of tokens:")
        self.max_tokens_label.grid(row=2, column=0, sticky='w')

    def create_max_tokens_spinbox(self):
        self.max_tokens_spinbox = ttk.Spinbox(self, from_=1, to=500, increment=1)
        self.max_tokens_spinbox.grid(row=3, column=0, sticky='w')

    def create_mode_radiobuttons(self):
        self.mode = tk.StringVar(value="song")
        self.song_radiobutton = ttk.Radiobutton(self, text="Song", variable=self.mode, value="song")
        self.song_radiobutton.grid(row=4, column=0, sticky='w')
        self.poem_radiobutton = ttk.Radiobutton(self, text="Poem", variable=self.mode, value="poem")
        self.poem_radiobutton.grid(row=5, column=0, sticky='w')

    def create_generate_button(self):
        self.generate_button = ttk.Button(self, text="Generate Lyrics", command=self.generate_lyrics)
        self.generate_button.grid(row=6, column=0, columnspan=3)

    def create_history_button(self):
        self.history_button = ttk.Button(self, text="Show History", command=self.show_history)
        self.history_button.grid(row=7, column=0, columnspan=3)

    def create_save_button(self):
        self.save_button = ttk.Button(self, text="Save Lyrics", command=self.save_lyrics)
        self.save_button.grid(row=10, column=0, columnspan=3)

    def save_lyrics(self):
        lyrics = self.lyrics_text.get("1.0", "end").strip()
        if not lyrics:
            messagebox.showerror("Error", "No lyrics to save.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if not file_path:  # If the user cancels the dialog, file_path will be an empty string
            return
        with open(file_path, "w") as file:
            file.write(lyrics)

    def create_lyrics_text(self):
        self.lyrics_text = tk.Text(self, height=10)
        self.lyrics_text.grid(row=8, column=0, sticky='w')

    # Rest of the MainWindow class methods...

    def generate_lyrics(self):
        prompt = self.prompt_entry.get()
        if not prompt.strip():  # Check if the prompt is empty
            messagebox.showerror("Error", "Please enter a prompt.")
            return
        max_tokens = self.max_tokens_spinbox.get()
        if not max_tokens:
            messagebox.showerror("Error", "Please enter a maximum number of tokens.")
            return
        max_tokens = int(max_tokens)
        mode = self.mode.get()
        try:
            lyrics = get_lyrics(prompt, mode, max_tokens)
            self.history.append((mode, lyrics))  # Modify this line to append a tuple
            self.lyrics_text.delete("1.0", "end")  # Clear the text box
            self.lyrics_text.insert(tk.END, lyrics)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_history(self):
        # Create a new Toplevel window
        history_window = tk.Toplevel(self)
        history_window.title("History")

        # Create a Listbox in the new window
        history_listbox = tk.Listbox(history_window)
        history_listbox.pack(fill=tk.BOTH, expand=True)

        # Populate the Listbox with the history of generated lyrics
        for i, (mode, lyrics) in enumerate(self.history, start=1):  # Modify this line to unpack the tuple
            history_listbox.insert(tk.END, f"{mode.capitalize()} {i}: {lyrics}")  # Modify this line to include the type
