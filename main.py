import tkinter as tk
from tkinter import messagebox, LEFT, RIGHT
import secrets
import string


class Application(tk.Frame):

    _ERROR_MESSAGE = "You need to select at least one checkbox"
    _SIZE = "400x300"

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(pady=10)
        self.master.title("Password Generator")
        self.master.geometry(self._SIZE)
        self.master.minsize(400, 300)
        self.master.resizable(0, 0)
        self.create_widgets()

    def create_widgets(self):
        # password label
        self.label_value = tk.StringVar()
        self.label_value.set("Hello")
        self.label = tk.Label(textvariable=self.label_value)
        self.label.pack()
        self.label.config(font=("Helvetica", 18, "bold"))

        self.password_length_scale = tk.Scale(orient="horizontal", from_=8, to=24)
        self.password_length_scale.pack()

        # lowercase radiobutton
        self.lower_value = tk.BooleanVar()
        self.lower_value.set(True)
        self.lower_radio_btn = tk.Checkbutton(
            text="LowerCase", variable=self.lower_value
        )
        self.lower_radio_btn.pack()

        # uppercase radiobutton
        self.upper_value = tk.BooleanVar()
        self.upper_value.set(False)
        self.upper_radio_btn = tk.Checkbutton(
            text="UpperCase", variable=self.upper_value
        )
        self.upper_radio_btn.pack()

        # symbols radiobutton
        self.symbols_value = tk.BooleanVar()
        self.symbols_value.set(False)
        self.symbols_radio_btn = tk.Checkbutton(
            text="Symbols", variable=self.symbols_value
        )
        self.symbols_radio_btn.pack()

        # digits radiobutton
        self.digits_value = tk.BooleanVar()
        self.digits_value.set(False)
        self.digits_radio_btn = tk.Checkbutton(
            text="Digits", variable=self.digits_value
        )
        self.digits_radio_btn.pack()

        # generate button
        generate_btn = tk.Button(
            text="Generate Password!", command=self.generate_password, padx=5, pady=5
        )
        generate_btn.pack(pady=5)

        # copy button
        copy_btn = tk.Button(text="Copy!", command=self.copy_clipboard, padx=5, pady=5)
        copy_btn.pack(pady=5)

    def generate_password(self):
        islower = self.lower_value.get()
        isupper = self.upper_value.get()
        issymbols = self.symbols_value.get()
        isdigits = self.digits_value.get()

        if not any([islower, isupper, issymbols, isdigits]):
            messagebox.showerror(title="Error", message=self._ERROR_MESSAGE)
        else:
            base = self.generate_base()
            pass_length = self.password_length_scale.get()
            password = "".join(secrets.choice(base) for i in range(pass_length))
            self.label_value.set(password)

    def copy_clipboard(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.label_value.get())
        self.master.update()

    def generate_base(self):
        base = ""
        if self.lower_value.get():
            base += string.ascii_lowercase
        if self.upper_value.get():
            base += string.ascii_uppercase
        if self.symbols_value.get():
            base += string.punctuation
        if self.digits_value.get():
            base += string.digits
        return base


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
