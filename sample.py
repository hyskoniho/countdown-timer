from timer import start_timer
from multiprocessing import Process, freeze_support

def timer(secs: int) -> int:
    process = Process(target=start_timer, args=(secs,))
    process.start()
    return process.pid
    # Cria um processo para a contagem regressiva e retorna o PID do processo

if __name__ == '__main__':
    freeze_support()
    # Necessário para proteger o código de execução em sistemas Windows

    timer(100)
    # Inicia a contagem regressiva de 100 segundos