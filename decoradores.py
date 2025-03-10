from typing import Any


def meu_decorador(func):
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada.")

minha_funcao()

class MeuDecoradorDeClasses:
    def __unit__(self) -> None:
      self.fun = func

    def __call__(self) -> Any:
        print("Antes da função ser chamada (decorador de classe)")
        self.func()
        print("Depois da função ser chamda (decorador de classe)")

@MeuDecoradorDeClasses
def segunda_funcao():
        print("Segunda função foi chamada.")
        pass



