<div align="center">
  <h1>Timer ⏱️</h1>
</div>

# Sobre
O intuito deste projeto é gerar na tela um timer de contagem regressiva, com o tempo relativo a conversão de um número inteiro total que represente os segundos. Esse projeto é útil pra mim para controlar visivelmente a execução dos meus códigos, principalmente projetos que envolvam automação. 
</br>
<div  align="center"><img src="assets/Screenshot_1.png"></div>

# Requisitos
Linguagem:
- [Python 3](https://www.python.org/)<br></br>

Bibliotecas e tecnologias:
- [Tkinter](https://tkdocs.com/)
- [time](https://docs.python.org/3/library/time.html)

# Como instalar:
Clone o projeto para o seu computador
```bash
$ git clone https://github.com/hyskoniho/countdown-timer
```
</br>

Instale as bibliotecas necessárias (Tkinter)<br></br>
No Windows:
```bash
pip install tkinter
```
No Linux/MacOS:
```bash
pip3 install tkinter
```

# Adicione o timer a um projeto existente:

⚠️ Importante: para o script funcionar, você precisa da estrutura de controle para a variável *__name__*:
```bash
if __name__ == '__main__':
    # código...
```
<br></br>
Primeiro, adicione o arquivo *[timer.py](https://github.com/hyskoniho/countdown-timer/blob/main/timer.py)* ao diretório do seu projeto
Em seguida, insira a seguinte linha de código:
```bash
from timer import start_timer
```
<br></br>
Agora, para iniciar o contador, é só acrescentar a seguinte linha:
```bash
start_timer(valor)
```
(lembre-se de alterar o nome "valor" para a sua variável ou número de segundos para o timer!)
