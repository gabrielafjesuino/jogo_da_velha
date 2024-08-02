import tkinter as tk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("JOGO DA VELHA")
        self.root.attributes('-fullscreen', True)  # Tela cheia
        self.root.bind("<Escape>", self.exit_fullscreen)  # Sair da tela cheia com ESC

        self.current_player = 'X'
        self.board = [None] * 9
        self.scores = {'X': 0, 'O': 0}  # Pontuação dos jogadores

        # Configura o layout principal
        self.main_frame = tk.Frame(root, bg='#e0f7fa')
        self.main_frame.pack(expand=True, fill='both')

        # Adiciona o título
        self.title_label = tk.Label(self.main_frame, text="JOGO DA VELHA", font=('Arial', 36, 'bold'), bg='#e0f7fa', fg='#004d40')
        self.title_label.grid(row=0, column=0, pady=10)

        # Adiciona o placar
        self.score_label = tk.Label(self.main_frame, text=self.get_score_text(), font=('Arial', 24, 'bold'), bg='#e0f7fa', fg='#004d40')
        self.score_label.grid(row=1, column=0, pady=10)

        # Cria o frame para o tabuleiro
        self.board_frame = tk.Frame(self.main_frame, bg='#e0f7fa')
        self.board_frame.grid(row=2, column=0, pady=10)

        self.buttons = [tk.Button(self.board_frame, text='', font=('Arial', 24, 'bold'), width=5, height=2, command=lambda i=i: self.on_button_click(i), bg='#ffffff', fg='#000000', relief='raised', bd=5) for i in range(9)]

        for i, button in enumerate(self.buttons):
            button.grid(row=i // 3, column=i % 3, padx=10, pady=10)

        # Adiciona o botão "Jogar Novamente"
        self.restart_button = tk.Button(self.main_frame, text="JOGAR NOVAMENTE", font=('Arial', 18, 'bold'), command=self.reset_game, bg='#4caf50', fg='#ffffff', relief='raised', bd=5)
        self.restart_button.grid(row=3, column=0, pady=20)

        # Centraliza a grid na tela
        self.main_frame.grid_rowconfigure(2, weight=1)  # Dá mais espaço para o frame do tabuleiro
        self.main_frame.grid_columnconfigure(0, weight=1)  # Centraliza na coluna

    def on_button_click(self, index):
        if self.board[index] is None:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, bg='#a5d6a7' if self.current_player == 'X' else '#ef9a9a')
            if self.check_winner(self.current_player):
                self.scores[self.current_player] += 1
                self.show_message(f"JOGADOR {self.current_player} VENCEU!")
                self.update_score_label()
            elif None not in self.board:
                self.show_message("EMPATE!")
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, player):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Linhas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colunas
            (0, 4, 8), (2, 4, 6)              # Diagonais
        ]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def reset_game(self):
        self.current_player = 'X'
        self.board = [None] * 9
        for button in self.buttons:
            button.config(text='', bg='#ffffff')

    def show_message(self, message):
        message_window = tk.Toplevel(self.root)
        message_window.title("FIM DE JOGO")

        # Define o tamanho da janela de mensagem
        width, height = 600, 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        message_window.geometry(f'{width}x{height}+{x}+{y}')

        # Adiciona uma borda para a janela de mensagem
        message_frame = tk.Frame(message_window, bg='#e0f7fa')  # Usando a mesma cor de fundo
        message_frame.pack(expand=True, fill='both')

        # Adiciona a mensagem
        label = tk.Label(message_frame, text=message.upper(), font=('Arial', 36, 'bold'), bg='#e0f7fa', fg='#004d40')  # Usando a mesma paleta de cores
        label.pack(expand=True, padx=20, pady=20)

        # Adiciona um botão para fechar
        button = tk.Button(message_frame, text="FECHAR", font=('Arial', 18, 'bold'), command=message_window.destroy, bg='#4caf50', fg='#ffffff', relief='raised', bd=3)  # Cor consistente com o botão de reinício
        button.pack(pady=20)

        # Centraliza o botão na janela
        button_frame = tk.Frame(message_frame, bg='#e0f7fa')  # Adiciona um frame para centralizar o botão
        button_frame.pack(expand=True, fill='x', side='bottom')
        button_frame.place(relx=0.5, rely=0.9, anchor='center')

        message_window.bind("<Button-1>", lambda e: message_window.destroy())  # Fechar a janela clicando

    def update_score_label(self):
        self.score_label.config(text=self.get_score_text())

    def get_score_text(self):
        return f"PONTOS - X: {self.scores['X']} | O: {self.scores['O']}"

    def exit_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', False)
        self.root.geometry('800x600')  # Define um tamanho padrão

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()