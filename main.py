from terminal import Terminal

import view
import server_teste



class Main():
    def __init__(self):
        self.terminal = Terminal()

        saida = self.terminal.escreva(server_teste.login, "10.121.2.8", "oi369932", "1234")
        view.imprimir(saida)


if __name__ == '__main__':
    Main()

"""
ssh 10.121.2.8
Login : oi369932
Senha : 1234
"""