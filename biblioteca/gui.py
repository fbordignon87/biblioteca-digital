import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, Listbox, Scrollbar
from biblioteca.gerenciador import listar_documentos, adicionar_documento, renomear_documento, remover_documento

class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 Biblioteca Digital")
        self.root.geometry("600x400")

        self.label = tk.Label(root, text="Arquivos disponíveis:")
        self.label.pack()

        self.scrollbar = Scrollbar(root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = Listbox(root, width=80, height=15, yscrollcommand=self.scrollbar.set)
        self.listbox.pack(padx=10)
        self.scrollbar.config(command=self.listbox.yview)

        self.btn_atualizar = tk.Button(root, text="🔄 Atualizar Lista", command=self.atualizar_lista)
        self.btn_adicionar = tk.Button(root, text="➕ Adicionar Documento", command=self.adicionar)
        self.btn_renomear = tk.Button(root, text="✏️ Renomear Documento", command=self.renomear)
        self.btn_remover = tk.Button(root, text="🗑️ Remover Documento", command=self.remover)

        self.btn_atualizar.pack(pady=2)
        self.btn_adicionar.pack(pady=2)
        self.btn_renomear.pack(pady=2)
        self.btn_remover.pack(pady=2)

        self.atualizar_lista()

    def atualizar_lista(self):
        self.listbox.delete(0, tk.END)
        arquivos = listar_documentos("biblioteca")
        for a in arquivos:
            self.listbox.insert(tk.END, f"{a['nome']} ({a['extensao']}, {a['ano']})")

    def adicionar(self):
        caminho_origem = filedialog.askopenfilename(title="Selecione o arquivo para adicionar")
        if not caminho_origem:
            return
        nome_arquivo = os.path.basename(caminho_origem)
        destino = os.path.join("biblioteca", nome_arquivo)
        try:
            adicionar_documento(caminho_origem, destino)
            messagebox.showinfo("Sucesso", "Documento adicionado com sucesso.")
            self.atualizar_lista()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def renomear(self):
        selecao = self.listbox.curselection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione um documento para renomear.")
            return
        nome_atual = self.listbox.get(selecao[0]).split(" ")[0]
        novo_nome = simpledialog.askstring("Renomear", "Digite o novo nome do arquivo:")
        if not novo_nome:
            return
        caminho_antigo = os.path.join("biblioteca", nome_atual)
        try:
            renomear_documento(caminho_antigo, novo_nome)
            messagebox.showinfo("Sucesso", "Documento renomeado com sucesso.")
            self.atualizar_lista()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def remover(self):
        selecao = self.listbox.curselection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione um documento para remover.")
            return
        nome = self.listbox.get(selecao[0]).split(" ")[0]
        caminho = os.path.join("biblioteca", nome)
        confirmacao = messagebox.askyesno("Confirmação", f"Tem certeza que deseja remover '{nome}'?")
        if confirmacao:
            try:
                remover_documento(caminho)
                messagebox.showinfo("Sucesso", "Documento removido com sucesso.")
                self.atualizar_lista()
            except Exception as e:
                messagebox.showerror("Erro", str(e))

def iniciar_interface():
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()

