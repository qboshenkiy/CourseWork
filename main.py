import tkinter as tk
from tkinter import ttk
from spellchecker import SpellChecker
import re

class SpellCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Проверка правописания")
        self.root.configure(bg="white")
        self.root.geometry("600x300") 

        bg_color = "white"
        text_color = "black"
        entry_bg_color = "white"
        button_bg_color = "white"

        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12), background=bg_color, foreground=text_color)
        style.configure("TButton", font=("Arial", 12), background=button_bg_color, foreground="black")
        style.configure("TCombobox", font=("Arial", 12), fieldbackground=entry_bg_color, foreground=text_color)
        style.configure("TText", font=("Arial", 12), background=entry_bg_color, foreground=text_color)
        style.map("TButton", background=[("active", button_bg_color)])

        self.language_label = ttk.Label(root, text="Выберите язык:", style="TLabel")
        self.language_combobox = ttk.Combobox(root, values=["en", "ru"], style="TCombobox")

        self.text_edit_label = ttk.Label(root, text="Введите текст для проверки:", style="TLabel")
        self.text_edit = tk.Text(root, height=5, width=40, bg=entry_bg_color, fg="black")

        self.correct_button = ttk.Button(root, text="Проверить", command=self.correct_text, style="TButton")

        self.result_label = ttk.Label(root, text="Исправленный текст:", style="TLabel")
        self.result_text = tk.Text(root, height=5, width=40, state=tk.DISABLED, bg=entry_bg_color, fg="black")

        self.setup_ui()

    def setup_ui(self):
        self.language_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.language_combobox.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.text_edit_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.text_edit.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.correct_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.result_text.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    def correct_text(self):
        try:
            language = self.language_combobox.get()
            text_to_correct = self.text_edit.get("1.0", tk.END)

            corrected_text = self.get_corrected_text(text_to_correct, language)

            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, corrected_text)
            self.result_text.config(state=tk.DISABLED)

        except Exception as e:
            print(f"Ошибка: {e}")

    def get_corrected_text(self, text, language):
        spell = SpellChecker(language=language)
        words = re.findall(r'\b\w+\b', text)  # Разделение текста на слова
        corrected_words = [spell.correction(word) for word in words]
        corrected_text = ' '.join(corrected_words)
        return corrected_text

if __name__ == "__main__":
    root = tk.Tk()
    app = SpellCheckerApp(root)
    root.mainloop()
