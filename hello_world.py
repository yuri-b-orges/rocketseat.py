import tkinter as tk
from tkinter import font

class HelloWorldApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Meu Primeiro App")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")
        
        # Variável para controlar se a mensagem está visível
        self.mensagem_visivel = False
        
        # Criar widgets
        self.criar_widgets()
        
        # Centralizar a janela
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def criar_widgets(self):
        """Cria todos os elementos da interface"""
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Título
        titulo = tk.Label(
            main_frame,
            text="App Hello World",
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        titulo.pack(pady=(0, 30))
        
        # Instrução
        instrucao = tk.Label(
            main_frame,
            text="Clique no botão para mostrar a mensagem:",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#666666"
        )
        instrucao.pack(pady=(0, 20))
        
        # Botão Iniciar
        self.botao_iniciar = tk.Button(
            main_frame,
            text="INICIAR",
            command=self.mostrar_mensagem,
            font=("Arial", 14, "bold"),
            bg="#4CAF50",  # Verde
            fg="white",
            activebackground="#45a049",
            activeforeground="white",
            relief="raised",
            padx=30,
            pady=10,
            cursor="hand2"
        )
        self.botao_iniciar.pack(pady=10)
        
        # Botão Limpar
        self.botao_limpar = tk.Button(
            main_frame,
            text="LIMPAR",
            command=self.limpar_mensagem,
            font=("Arial", 12),
            bg="#f44336",  # Vermelho
            fg="white",
            activebackground="#d32f2f",
            activeforeground="white",
            relief="raised",
            padx=20,
            pady=5,
            cursor="hand2",
            state="disabled"  # Inicialmente desabilitado
        )
        self.botao_limpar.pack(pady=10)
        
        # Área da mensagem (inicialmente vazia)
        self.frame_mensagem = tk.Frame(main_frame, bg="#f0f0f0", height=100)
        self.frame_mensagem.pack(pady=20, fill="x")
        self.frame_mensagem.pack_propagate(False)  # Mantém o tamanho fixo
        
        # Label da mensagem (será criada/ocultada)
        self.label_mensagem = tk.Label(
            self.frame_mensagem,
            text="",
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="#2196F3"  # Azul
        )
    
    def mostrar_mensagem(self):
        """Mostra a mensagem Hello World"""
        if not self.mensagem_visivel:
            # Atualiza o texto
            self.label_mensagem.config(text="Hello World!")
            
            # Centraliza a mensagem no frame
            self.label_mensagem.pack(expand=True)
            
            # Atualiza estado
            self.mensagem_visivel = True
            
            # Altera o botão iniciar
            self.botao_iniciar.config(
                text="MENSAGEM VISÍVEL",
                bg="#2196F3",  # Azul
                state="disabled"
            )
            
            # Habilita o botão limpar
            self.botao_limpar.config(state="normal")
            
            # Feedback visual
            print("Mensagem 'Hello World' exibida!")
    
    def limpar_mensagem(self):
        """Remove a mensagem Hello World"""
        if self.mensagem_visivel:
            # Esconde a mensagem
            self.label_mensagem.pack_forget()
            
            # Atualiza estado
            self.mensagem_visivel = False
            
            # Restaura o botão iniciar
            self.botao_iniciar.config(
                text="INICIAR",
                bg="#4CAF50",  # Verde
                state="normal"
            )
            
            # Desabilita o botão limpar
            self.botao_limpar.config(state="disabled")
            
            # Feedback visual
            print("Mensagem removida!")

def main():
    # Cria a janela principal
    root = tk.Tk()
    
    # Cria a aplicação
    app = HelloWorldApp(root)
    
    # Inicia o loop principal
    root.mainloop()

if __name__ == "__main__":
    main()
