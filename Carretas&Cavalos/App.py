# importar modulo

from tkinter import *
#from tkinter import ttk, StringVar
from tkinter import messagebox
import tkinter.ttk as ttk

# from main import mostrar_carretas
from viewCavalo import *
from view import *
# from viewBob import *
# from viewMotorista import *
# from viewDestinos import *
# from viewCentroCusto import *


def janelaCarreta():
    exec(open("main.py").read())
def janelaCavalo():
    exec(open("mainCavalo.py").read())
def janelaBob():
    exec(open("mainBob.py").read())
def janelaMotorista():
    exec(open("mainMotorista.py").read())
def janelaDestinos():
    exec(open("mainDestinos.py").read())
def janelaCentroCusto():
    exec(open("mainCentroCusto.py").read())
app=Tk()
app.title("CopaEnergia")
app.geometry("900x610")
app.resizable(width=FALSE, height=FALSE)
app.configure(background="#403d3d")

barradeMenu=Menu(app)
menuArquivo=Menu(barradeMenu, tearoff=0)
menuArquivo.add_command(label="Carretas", command=janelaCarreta)
menuArquivo.add_command(label="Cavalos", command=janelaCavalo)
menuArquivo.add_command(label="Bobs")
menuArquivo.add_command(label="Motorista")
menuArquivo.add_command(label="Destinos")
menuArquivo.add_command(label="Centro de Custo")
menuArquivo.add_separator()
menuArquivo.add_command(label="Sair", command=app.quit)
barradeMenu.add_cascade(label="Cadastro", menu=menuArquivo)
app.config(menu=barradeMenu)


app.mainloop()
