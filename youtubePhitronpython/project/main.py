import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Prepare language lists
lang_values = list(LANGUAGES.values())
lan_key = list(LANGUAGES.keys())

def translate():
    try:
        txt = text1.get(1.0, tk.END).strip()
        c1 = combo.get()

        if txt and c1 in lang_values:
            pos = lang_values.index(c1)
            c1_code = lan_key[pos]

            translator = Translator()
            result = translator.translate(txt, dest=c1_code)

            # Clear and insert translated text
            text2.delete(1.0, tk.END)
            text2.insert(1.0, result.text)
        else:
            messagebox.showwarning("Input Error", "Please enter text and choose a language!")

    except Exception as e:
        messagebox.showerror("Translation Error", str(e))


# Tkinter window setup
root = tk.Tk()
root.title("Language Translator")
root.minsize(700, 600)
root.resizable(False, False)

# Styling for combobox
root.option_add("*TCombobox*Listbox.font", ("normal", 15))
root.option_add("*TCombobox.font", ("normal", 15))

# Input text box
text1 = tk.Text(root, font=('normal', 15), padx=10, pady=10)
text1.place(width=600, height=200, x=50, y=50)

# Language dropdown
combo = ttk.Combobox(root, values=lang_values, state="readonly")
combo.place(x=50, y=280)
combo.set("Choose a language")

# Translate button
button = tk.Button(root, text="Translate", font=("normal", 15), bg="lightgreen", command=translate)
button.place(x=310, y=270)

# Output text box
text2 = tk.Text(root, font=('normal', 15), padx=10, pady=10)
text2.place(width=600, height=200, x=50, y=350)

root.mainloop()
