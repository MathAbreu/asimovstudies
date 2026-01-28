from meu_pacote.moduloA.script_a import var_A
from meu_pacote.moduloB.script_b import var_B
from meu_pacote.moduloC.script_c import var_C

def func():
    print(var_A + var_B + var_C)

if __name__ == '__main__':
    print("Testando: func")
    func()