from abc import abstractmethod, ABC

class Teminal():
    def __init__(self):
        self.pingando = 'pingando'
    
    
# ----- *** -----

        
class RouterBase(ABC):
    # @abstractmethod
    # def login(self, terminal):
    #     pass
    
    @abstractmethod
    def ping(self, terminal):
        pass

class RouterAlcatel(RouterBase):
    
    def ping(self, terminal):
        print(terminal.pingando) 
        terminal.pingando = 'pinguei'   

class RouterCisco(RouterBase):
    def ping(self, terminal):
        print(terminal.pingando)
        terminal.pingando = 'pinguei'


# ----- *** -----        


class Router(RouterBase):
    def __init__(self, terminal):
        self.terminal = terminal
        self.timeout = None

    # ----- *** -----        
    
    def set_router(self, router):
        self.router = router
    
    def set_user(self, user):
        self.user = user
    
    def set_senha(self, senha):
        self.senha = senha        
    
    def set_ip(self, ip):
        self.ip = ip        
        
    def set_timeout(self, timeout):
        self.timeout = timeout        
        
    # ----- *** -----        
    
    def ping(self):
        self.router.ping(self.terminal)
    
    # ----- *** -----        
        
    def telnet(self):
        self.terminal.child.sendline("telnet {0}".format(self.ip))

        # Digita a senha TACACS
        self.terminal.child.expect(':', timeout=self.timeout)  # Espera Username
        self.terminal.child.sendline(self.user)

        self.terminal.child.expect(':', timeout=self.timeout)  # Espera Senha
        self.terminal.child.sendline(self.senha)

        index = self.terminal.child.expect(['>', 'failed'], timeout=self.timeout)

        if index == 0:
            # Entra em modo privilegiado
            self.terminal.child.sendline("ena")
            self.terminal.child.sendline(self.senha)
            index = self.terminal.child.expect(['#', '>'], timeout=self.timeout)
            if index == 0:
                print("Router Alcatel : Modo Privilegiado UP")
            if index == 1:
                print("Router Alcatel : Modo Privilegiado DOWN")
            return True
        if index == 1:
            return False