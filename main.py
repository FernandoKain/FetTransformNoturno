# Bibliotecas a serem usadas
import pyautogui
import time

# pyautogui.click(x=713, y=700)

# Solicita entrada do usuário em relação ao número de atividades entregues.
# var = int(input("Insira o número de alunos que entregaram as atividades: "))


# Funções para otimizar o código
def alttab():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

def controlc():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    pyautogui.keyUp('c')
    pyautogui.keyUp('ctrl')

def alttab2():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

def f2():
    pyautogui.press('f2')

def controlv():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('v')
    pyautogui.keyUp('ctrl')

def enter():
    pyautogui.press('enter')

def down():
    pyautogui.press("down")

def up():
    pyautogui.press("up")

def right():
    pyautogui.press("right")

def left():
    pyautogui.press('left')


# -------------Código começa------------------------

# -------------Ajuste das janelas-------------------
alttab()
alttab2()
alttab()
down()
up()
# --------Inicia a transferência-----------
for i in range (5):
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()

    #----------------Intervalo no Excel------------------------
    enter()
    #----------------Intervalo no Excel------------------------

    alttab()

    #----------------Intervalo no FET------------------------
    down()
    #----------------Intervalo no FET------------------------
    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    alttab()

    down()
    controlc()
    alttab()
    f2()
    controlv()
    enter()
    #----------------Próximo dia no Excel---------------
    enter()
    #----------------Próximo dia no Excel--------------
    alttab()

    #----------------Próximo dia no FET--------------
    up()
    up()
    up()
    up()
    up()
    right()

    #----------------Próximo dia no FET--------------
    #----------------Próxima Sala--------------
for i in range(5):
    left()
alttab()
for i in range(35):
    up()
right()
alttab()

