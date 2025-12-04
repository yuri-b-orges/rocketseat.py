import tkinter as tk
from tkinter import messagebox

class ListaTarefasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas Simples")
        self.root.geometry("500x400")
        
        # Lista para armazenar tarefas e estados
        self.tarefas = []
        
        # Frame para entrada de nova tarefa
        frame_entrada = tk.Frame(root)
        frame_entrada.pack(pady=10)
        
        tk.Label(frame_entrada, text="Nova Tarefa:", font=("Arial", 10)).pack(side=tk.LEFT)
        
        self.entrada_tarefa = tk.Entry(frame_entrada, width=40, font=("Arial", 10))
        self.entrada_tarefa.pack(side=tk.LEFT, padx=5)
        self.entrada_tarefa.bind("<Return>", lambda e: self.adicionar_tarefa())
        
        btn_adicionar = tk.Button(frame_entrada, text="Adicionar", command=self.adicionar_tarefa, 
                                  bg="#4CAF50", fg="white", font=("Arial", 10))
        btn_adicionar.pack(side=tk.LEFT, padx=5)
        
        # Frame para lista de tarefas
        frame_lista = tk.Frame(root)
        frame_lista.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Scrollbar para a lista
        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Canvas para conter o frame das tarefas (para scroll)
        self.canvas = tk.Canvas(frame_lista, yscrollcommand=scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar.config(command=self.canvas.yview)
        
        # Frame interno para as tarefas
        self.frame_tarefas = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_tarefas, anchor="nw")
        
        # Frame para botões de ação
        frame_botoes = tk.Frame(root)
        frame_botoes.pack(pady=10)
        
        btn_remover = tk.Button(frame_botoes, text="Remover Concluídas", 
                                command=self.remover_concluidas, bg="#f44336", fg="white")
        btn_remover.pack(side=tk.LEFT, padx=5)
        
        btn_limpar = tk.Button(frame_botoes, text="Limpar Todas", 
                               command=self.limpar_todas, bg="#ff9800", fg="white")
        btn_limpar.pack(side=tk.LEFT, padx=5)
        
        # Atualizar configuração do canvas quando o frame interno mudar de tamanho
        self.frame_tarefas.bind("<Configure>", self.configurar_scroll)
        
        # Focar na entrada de texto
        self.entrada_tarefa.focus()
    
    def configurar_scroll(self, event):
        """Configura a área de scroll do canvas"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def adicionar_tarefa(self):
        """Adiciona uma nova tarefa à lista"""
        texto = self.entrada_tarefa.get().strip()
        
        if texto:
            # Adicionar à lista de tarefas
            self.tarefas.append({"texto": texto, "concluida": False})
            
            # Criar widget para a tarefa
            self.criar_widget_tarefa(len(self.tarefas) - 1)
            
            # Limpar entrada
            self.entrada_tarefa.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vazio", "Por favor, digite uma tarefa.")
    
    def criar_widget_tarefa(self, index):
        """Cria os widgets para uma tarefa específica"""
        tarefa = self.tarefas[index]
        
        frame = tk.Frame(self.frame_tarefas)
        frame.pack(fill=tk.X, pady=2)
        
        # Checkbox
        var_check = tk.BooleanVar(value=tarefa["concluida"])
        checkbox = tk.Checkbutton(frame, variable=var_check, 
                                 command=lambda idx=index: self.toggle_conclusao(idx))
        checkbox.pack(side=tk.LEFT)
        
        # Label com texto da tarefa
        label = tk.Label(frame, text=tarefa["texto"], font=("Arial", 10), 
                         anchor="w", width=50)
        label.pack(side=tk.LEFT, padx=5)
        
        # Botão para remover tarefa individual
        btn_remover = tk.Button(frame, text="×", font=("Arial", 10, "bold"),
                               command=lambda idx=index: self.remover_tarefa(idx),
                               bg="#ff5252", fg="white", width=2)
        btn_remover.pack(side=tk.RIGHT)
        
        # Armazenar referências
        tarefa["frame"] = frame
        tarefa["var_check"] = var_check
        tarefa["label"] = label
        
        # Aplicar estilo se já estiver concluída
        if tarefa["concluida"]:
            self.aplicar_estilo_concluido(index)
    
    def toggle_conclusao(self, index):
        """Alterna o estado de conclusão de uma tarefa"""
        self.tarefas[index]["concluida"] = not self.tarefas[index]["concluida"]
        self.aplicar_estilo_concluido(index)
    
    def aplicar_estilo_concluido(self, index):
        """Aplica o estilo visual para tarefas concluídas"""
        tarefa = self.tarefas[index]
        
        if tarefa["concluida"]:
            tarefa["label"].config(fg="gray", font=("Arial", 10, "overstrike"))
        else:
            tarefa["label"].config(fg="black", font=("Arial", 10))
    
    def remover_tarefa(self, index):
        """Remove uma tarefa específica"""
        if 0 <= index < len(self.tarefas):
            # Destruir o frame da tarefa
            self.tarefas[index]["frame"].destroy()
            # Remover da lista
            del self.tarefas[index]
            # Recriar widgets para os índices restantes
            self.recriar_widgets_tarefas()
    
    def remover_concluidas(self):
        """Remove todas as tarefas concluídas"""
        # Filtrar tarefas não concluídas
        novas_tarefas = [t for t in self.tarefas if not t["concluida"]]
        
        if len(novas_tarefas) == len(self.tarefas):
            messagebox.showinfo("Nada para remover", "Não há tarefas concluídas para remover.")
            return
        
        # Destruir todos os frames
        for tarefa in self.tarefas:
            tarefa["frame"].destroy()
        
        # Atualizar lista
        self.tarefas = novas_tarefas
        
        # Recriar widgets
        self.recriar_widgets_tarefas()
        
        messagebox.showinfo("Sucesso", f"Tarefas concluídas removidas. Restam {len(self.tarefas)} tarefas.")
    
    def limpar_todas(self):
        """Remove todas as tarefas"""
        if not self.tarefas:
            return
        
        resposta = messagebox.askyesno("Confirmar", "Tem certeza que deseja remover todas as tarefas?")
        
        if resposta:
            # Destruir todos os frames
            for tarefa in self.tarefas:
                tarefa["frame"].destroy()
            
            # Limpar lista
            self.tarefas = []
    
    def recriar_widgets_tarefas(self):
        """Recria todos os widgets das tarefas (após remoção)"""
        for i in range(len(self.tarefas)):
            self.criar_widget_tarefa(i)

def main():
    root = tk.Tk()
    app = ListaTarefasApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()