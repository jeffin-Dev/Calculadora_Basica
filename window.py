import tkinter as tk
from BackendCalculation import Functions


class Calculadora():
    def __init__(self):
        self.app = tk.Tk()
        self.title = self.app.title('CALCULATION NUMBERS')
        self.app.minsize(340, 330)
        self.app.maxsize(340, 330)


        self.titulo = tk.Label(text='CALCULADORA BÁSICA', bg='black', fg='white')
        self.titulo.grid(row=0, columnspan=2,pady= 10,sticky='snwe')

        self.n1 = tk.IntVar()
        self.numero1 = tk.Entry(width=5, textvariable=self.n1)
        self.numero1.grid(column=0, row=1, padx=10, pady=10)

        self. n2 = tk.IntVar()
        self.numero2 = tk.Entry(width=5, textvariable=self.n2)
        self.numero2.grid(column=1, row=1, padx=10, pady=10)

        self.operadores = Functions(self.numero1, self.numero2, self.app)
        self.operadores.center(self.app)


        self.botao_somar = tk.Button(text='SOMAR', width=20, command=self.operadores.soma, activebackground='#78d6ff')
        self.botao_somar.grid(row=2, column=0, pady=10, padx=10)

        self.botao_multiplicar = tk.Button(text='MULTIPLICAR', width=20, command=self.operadores.mult, activebackground='#78d6ff')
        self.botao_multiplicar.grid(row=2, column=1, pady=10, padx=10)

        self.botao_dividir = tk.Button(text='DIVIDIR', width=20, command=self.operadores.dividir, activebackground='#78d6ff')
        self.botao_dividir.grid(row=3, column=0, pady=10, padx=10)

        self.botao_subtrair = tk.Button(text='SUBTRAIR', width=20, command=self.operadores.sub, activebackground='#78d6ff')
        self.botao_subtrair.grid(row=3, column=1, pady=10, padx=10)

        self.botao_potencia = tk.Button(text='POTÊNCIA', width=20, command=self.operadores.potencia, activebackground='#78d6ff')
        self.botao_potencia.grid(row=4, column = 0, pady=10, padx=10)

        self.botao_porcentagem = tk.Button(text = 'PORCENTAGEM', width=20, command = self.operadores.porcentagem, activebackground='#78d6ff')
        self.botao_porcentagem.grid(row=4, column=1, pady=10, padx=10)

        self.botao_fechar = tk.Button(text='FECHAR', width=10, command=self.operadores.fechar_app,activebackground='#78d6ff' )
        self.botao_fechar.grid(row=6, column=0,columnspan=2, padx=10, pady=10)


        self.operadores.direitos_reservados()

        self.app.mainloop()



if '__main__' == __name__:

    a = Calculadora()
