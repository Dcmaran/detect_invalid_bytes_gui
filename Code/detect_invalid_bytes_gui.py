import tkinter as tk
from tkinter import filedialog, messagebox
import os

def detect_invalid_bytes(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()

    invalid_bytes = []
    for index, byte in enumerate(content):
        try:
            byte.to_bytes(1, 'big').decode('utf-8')
        except UnicodeDecodeError:
            invalid_bytes.append((index, byte))
    
    return invalid_bytes

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        invalid_bytes = detect_invalid_bytes(file_path)
        if invalid_bytes:
            result = "Caractere(s) inválido(s) encontrado(s) nas seguintes posições:\n"
            for index, byte in invalid_bytes:
                result += f"Posição: {index}, Byte: {byte}, Código: {hex(byte)}\n"
            messagebox.showinfo("Resultado", result)
        else:
            messagebox.showinfo("Resultado", "Nenhum caractere inválido encontrado.")

app = tk.Tk()
app.title("Detector de Bytes Inválidos")
app.geometry("400x200")

select_button = tk.Button(app, text="Selecionar Arquivo", command=select_file)
select_button.pack(expand=True)

app.mainloop()
