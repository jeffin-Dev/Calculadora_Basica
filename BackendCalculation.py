import tkinter as tk
from tkinter import messagebox


class Functions:
    def __init__(self, number1, number2, app):
        self.numero1 = number1
        self.numero2 = number2
        self.app = app
    def soma(self):
        somar = float(self.numero1.get())+float(self.numero2.get())
        resposta = tk.Label(text=f'Resposta da soma: {somar}',bg='#DCDCDC', font=("Arial", 10))
        resposta.grid(columnspan=2, row=5, pady=10, padx=5, sticky='nswe')

    def mult(self):
        multiplicar = float(self.numero1.get())*float(self.numero2.get())
        resposta = tk.Label(text=f'Resposta da Multiplicação: {multiplicar}', bg='#DCDCDC', font=("Arial", 10))
        resposta.grid(columnspan=2, row= 5, pady=10, padx=10,sticky='nswe')

    def dividir(self):
        try:
            divisao = float(self.numero1.get())/float(self.numero2.get())
            resposta = tk.Label(text=f'Resposta da divisão: {divisao:.2f}', bg='#DCDCDC', font=("Arial", 10))
            resposta.grid(columnspan=2, row=5, pady=10, padx=10, sticky='nswe')
        except ZeroDivisionError:
            resposta = tk.Label(text= 'Você esta tentando dividir um numero por 0',bg='#DCDCDC', font=("Arial", 10))
            resposta.grid(columnspan=2, row=5, pady=10, padx=10, sticky='nswe')

    def sub(self):
        subtrair = float(self.numero1.get()) - float(self.numero2.get())
        resposta = tk.Label(text=f'Resposta da subtração: {subtrair}', bg='#DCDCDC', font=("Arial", 10))
        resposta.grid(columnspan=2, row=5, pady=10, sticky='nswe')

    def potencia(self):
        potenciacao = float(self.numero1.get())**float(self.numero2.get())
        resposta = tk.Label(text=f'Resposta da potenciação: {potenciacao}', bg='#DCDCDC', font=("Arial", 10))
        resposta.grid(columnspan=2, row=5, pady=10, sticky='nswe')

    def porcentagem(self):
        porc = float(self.numero1.get())*float(self.numero2.get()) / 100
        resposta = tk.Label(text=f'Resposta da porcentagem: {porc}', bg='#DCDCDC', font=("Arial", 10))
        resposta.grid(columnspan=2, row=5, pady=10, sticky='nswe')

    def direitos_reservados(self):
        vazio = tk.Label()
        vazio.grid(row = 5, columnspan=2, padx=10, pady=10)
        mensagem = tk.Label(text='Todos os direitos reservados. @Jefferson.python', fg='black',bg='#D3D3D3',font=("-weight bold-size 10", 8))
        mensagem.grid(columnspan=2, row=7, sticky='nswe')

    def fechar_app(self):
        confirmacao = tk.messagebox.askquestion('Fechando calculadora','Deseja realmente sair?')
        if confirmacao == 'yes':
            self.app.destroy()
        else:
            pass
    def center(self, win):

        win.update_idletasks()

        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width

        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width

        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2

        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        win.deiconify()

if '__main__' == __name__:

    pass