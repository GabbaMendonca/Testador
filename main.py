from view import View

class Main():
    def __init__(self):
        self.view = View()

        while True:
            entrada = self.view.entrada()
            self.view.imprimir(entrada)

if __name__ == '__main__':
    Main()