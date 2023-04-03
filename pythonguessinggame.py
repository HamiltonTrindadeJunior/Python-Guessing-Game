import random
import tkinter as tk

# Configuração da janela
janela = tk.Tk()
janela.geometry("400x200")
janela.title("Jogo de Adivinhação")
janela.configure(bg="#1c1c1c")

# Configuração dos widgets
titulo = tk.Label(janela, text="Adivinhe o número entre 1 e 10", font=("Helvetica", 12), fg="white", bg="#1c1c1c")
titulo.pack(pady=10)

entrada = tk.Entry(janela, width=3, font=("Helvetica", 12))
entrada.pack(pady=5)

texto_resultado = tk.Label(janela, font=("Helvetica", 12), fg="white", bg="#1c1c1c")
texto_resultado.pack(pady=5)

botao_testar = tk.Button(janela, text="Testar", font=("Helvetica", 12), command=lambda: testar_numero())
botao_testar.pack(pady=5)

botao_reiniciar = tk.Button(janela, text="Jogar Novamente", font=("Helvetica", 12), command=lambda: reiniciar_jogo())
botao_reiniciar.pack(pady=5)

# Variáveis do jogo
numero_secreto = random.randint(1, 10)
tentativas_restantes = 5

# Funções do jogo
def testar_numero():
    global tentativas_restantes
    
    # Verifica se o jogador ainda tem tentativas
    if tentativas_restantes > 1:
        # Decrementa o número de tentativas
        tentativas_restantes -= 1
        
        # Obtém o número inserido pelo jogador
        numero_inserido = int(entrada.get())
        entrada.delete(0, tk.END)
        
        # Verifica se o número inserido está correto
        if numero_inserido == numero_secreto:
            texto_resultado.config(text="Parabéns! Você acertou!")
            botao_testar.pack_forget()
            botao_reiniciar.pack(pady=10)
            entrada.config(state=tk.DISABLED)
            
        elif numero_inserido > numero_secreto:
            texto_resultado.config(text="O número secreto é menor. Tentativas restantes: {}".format(tentativas_restantes))
            
        else:
            texto_resultado.config(text="O número secreto é maior. Tentativas restantes: {}".format(tentativas_restantes))
            
    # Jogador não tem mais tentativas
    else:
        texto_resultado.config(text="Suas tentativas acabaram. O número era {}".format(numero_secreto))
        botao_testar.pack_forget()
        botao_reiniciar.pack(pady=10)
        entrada.config(state=tk.DISABLED)

def reiniciar_jogo():
    global numero_secreto, tentativas_restantes
    
    numero_secreto = random.randint(1, 10)
    tentativas_restantes = 5
    
    texto_resultado.config(text="")
    botao_testar.pack(pady=5)
    botao_reiniciar.pack_forget()
    entrada.config(state=tk.NORMAL)
    
# Inicialização do jogo
janela.mainloop()