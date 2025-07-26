import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_URL = "http://localhost:8080/itens"

class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca - Cliente Python")

        self.frame = ttk.Frame(root, padding=10)
        self.frame.grid(row=0, column=0)

        self.titulo_var = tk.StringVar()
        self.autor_var = tk.StringVar()
        self.tipo_var = tk.StringVar()

        ttk.Label(self.frame, text="Título:").grid(row=0, column=0)
        self.titulo_entry = ttk.Entry(self.frame, textvariable=self.titulo_var)
        self.titulo_entry.grid(row=0, column=1)

        ttk.Label(self.frame, text="Autor:").grid(row=1, column=0)
        self.autor_entry = ttk.Entry(self.frame, textvariable=self.autor_var)
        self.autor_entry.grid(row=1, column=1)

        ttk.Label(self.frame, text="Tipo:").grid(row=2, column=0)
        self.tipo_combo = ttk.Combobox(self.frame, textvariable=self.tipo_var, values=["livro", "revista", "publicacao"])
        self.tipo_combo.grid(row=2, column=1)

    
        ttk.Button(self.frame, text="Adicionar", command=self.adicionar_item).grid(row=3, column=0, pady=5)
        ttk.Button(self.frame, text="Atualizar", command=self.atualizar_item).grid(row=3, column=1)
        ttk.Button(self.frame, text="Deletar", command=self.deletar_item).grid(row=3, column=2)


        self.tree = ttk.Treeview(self.frame, columns=("id", "titulo", "autor", "tipo"), show="headings")
        for col in ("id", "titulo", "autor", "tipo"):
            self.tree.heading(col, text=col.capitalize())
        self.tree.grid(row=4, column=0, columnspan=3, pady=10)
        self.tree.bind("<ButtonRelease-1>", self.selecionar_item)

        self.selecionado_id = None

        self.carregar_itens()

    def carregar_itens(self):
        try:
            self.tree.delete(*self.tree.get_children())
            resposta = requests.get(API_URL)
            for item in resposta.json():
                self.tree.insert("", tk.END, values=(item["id"], item["titulo"], item["autor"], item["tipo"]))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar itens: {e}")

    def adicionar_item(self):
        dados = {
            
            "titulo": self.titulo_var.get(),
            "autor": self.autor_var.get(),
            "tipo": self.tipo_var.get()
        }
        try:
            requests.post(API_URL, json=dados)
            self.carregar_itens()
            self.limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar item: {e}")

    def selecionar_item(self, event):
        item = self.tree.item(self.tree.focus())["values"]
        if item:
            self.selecionado_id = item[0]
            self.titulo_var.set(item[1])
            self.autor_var.set(item[2])
            self.tipo_var.set(item[3])

    def atualizar_item(self):
        if self.selecionado_id is None:
            messagebox.showwarning("Aviso", "Selecione um item para atualizar.")
            return
        dados = {
            "titulo": self.titulo_var.get(),
            "autor": self.autor_var.get(),
            "tipo": self.tipo_var.get()
        }
        try:
            requests.put(f"{API_URL}/{self.selecionado_id}", json=dados)
            self.carregar_itens()
            self.limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar item: {e}")

    def deletar_item(self):
        if self.selecionado_id is None:
            messagebox.showwarning("Aviso", "Selecione um item para deletar.")
            return
        try:
            requests.delete(f"{API_URL}/{self.selecionado_id}")
            self.carregar_itens()
            self.limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar item: {e}")

    def limpar_campos(self):
        self.titulo_var.set("")
        self.autor_var.set("")
        self.tipo_var.set("")
        self.selecionado_id = None

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()
