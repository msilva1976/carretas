# importar modulo


from tkinter import *
from tkinter import ttk, StringVar
from tkinter import messagebox
import tkinter.ttk as ttk
import sqlite3
import customtkinter
import customtkinter as ctk
customtkinter.set_appearance_mode("dark")



# from main import mostrar_carretas
from viewCavalo import *
from view import *
from viewbob import *
from viewFilial import *
from viewindustria import *



co0 = "#000000"  # black
co1 = "#feffff"  # whitw
co2 = "#4fa882"  # green
co3 = "#38576b"  # value
co4 = "#403d3d"  # dark
co5 = "#e06636"  # red
co6 = "#038cfc"  # blue
co7 = "#3fbfb9"  # cya
co8 = "#263438"  # gray
co9 = "#e9edf5"  # light gray
co10 = "#6e8b3d"  # green
co11 = "#AF0606"  # RED
co12 = "#1877F2"  # blue
co14 = "#00C300"  # green


app = Tk()
#app = ctk.CTk()
app.title("CopaEnergia")
app.geometry("900x610")
app.resizable(width=FALSE, height=FALSE)
app.configure(background="#403d3d")


def cavalo():
    janela = Tk()
    janela.title("CopaEnergia")
    janela.geometry("700x510")
    janela.configure(background=co6)
    janela.resizable(width=FALSE, height=FALSE)

    # creating the frames

    frame_cima = Frame(janela, width=700, height=25, bg=co3, relief="flat")
    frame_cima.grid(row=0, column=0, sticky=NSEW)

    frame_baixo = Frame(janela, width=700, height=475, bg=co1, relief="flat")
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    frame_baixo_esquerda = Frame(
        frame_baixo, width=700, height=470, bg=co0, relief="flat")
    frame_baixo_esquerda.grid(row=3, column=0, pady=1, padx=0, sticky=NSEW)

    app_logo = Label(frame_cima, text="Cavalos", width=20, height=1, padx=0,
                     relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co1)
    app_logo.place(x=10, y=5)

    # entrada de dados

    global tree

    # mostrar cavalos

    def mostrar_cavalos():
        global tree
        tabela_cavalos = ['Item', 'Frota', 'Placa', 'Nome', 'Eixo', 'PTB']
        lista_cavalos = verCavalos()
        tree = ttk.Treeview(frame_baixo_esquerda, columns=(
            "Frota", "Placa", "Nome", "Eixo", "PTB"), show="headings")
        tree = ttk.Treeview(frame_baixo_esquerda, selectmode="extended",
                            columns=tabela_cavalos, show="headings")

        # tree.column
        tree.column("Frota", width=50)
        tree.column("Placa", width=40)
        tree.column("Nome", width=160)
        tree.column("Eixo", width=50)
        tree.column("PTB", width=100)
        tree.heading("Frota", text="Frota")
        tree.heading("Placa", text="Placa")
        tree.heading("Nome", text="Nome")
        tree.heading("Eixo", text="Eixo")
        tree.heading("PTB", text="PTB")
        tree.place(x=10, y=120)

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_baixo_esquerda,
                            orient="vertical", command=tree.yview)
        vsb.place(x=511, y=121, height=222)
        tree.configure(yscrollcommand=vsb.set)
        frame_baixo_esquerda.grid_rowconfigure(0, weight=12)

        hd = ["center", "center", "center", "center", "center", "center"]
        h = [50, 50, 70, 200, 50, 100]
        n = 0
        for col in tabela_cavalos:
            tree.heading(col, text=col.title(), anchor=CENTER)
            tree.column(col, width=h[n], anchor=hd[n])
            n += 1

        for item in lista_cavalos:
            tree.insert("", "end", values=item)

    mostrar_cavalos()
      

    # função para adicionar novo cavalo

    def adicionar_cavalo():
        global tree
        frota = txtfrota.get()
        placa = txtplaca.get().upper()
        nome = txtnome.get().upper()
        eixo = txteixo.get()
        ptb = txtptb.get()

        lista_adicionar = [frota, placa, nome, eixo, ptb]

        for item in lista_adicionar:
            if item == "":
                messagebox.showerror(
                    "Erro", "Por favor, preencha todos os campos.")
                return
        inserirCavalos(lista_adicionar)

        messagebox.showinfo("Sucesso", "Cavalo adicionado com sucesso!")

        txtfrota.delete(0, END)
        txtplaca.delete(0, END)
        txtnome.delete(0, END)
        txteixo.delete(0, END)
        txtptb.delete(0, END)

        for widget in frame_baixo_esquerda.winfo_children():
            widget.destroy()

        mostrar_cavalos()

    # função atualizar dados

    def atulizar():
        global tree
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            treev_lista = treev_dicionario["values"]

            valor = treev_lista[0]

            txtfrota.delete(0, END)
            txtplaca.delete(0, END)
            txtnome.delete(0, END)
            txteixo.delete(0, END)
            txtptb.delete(0, END)

            id = int(treev_lista[0])
            txtfrota.insert(0, treev_lista[1])
            txtplaca.insert(0, treev_lista[2])
            txtnome.insert(0, treev_lista[3])
            txteixo.insert(0, treev_lista[4])
            txtptb.insert(0, treev_lista[5])

            def update():
                global tree
                frota = txtfrota.get()
                placa = txtplaca.get().upper()
                nome = txtnome.get().upper()
                eixo = txteixo.get()
                ptb = txtptb.get()

                lista_atualizar = [frota, placa, nome, eixo, ptb, id]

                for i in lista_atualizar:
                    if i == "":
                        messagebox.showerror(
                            "Erro", "Preencha todos os campos")
                        return
                updateCavalos(lista_atualizar)

                messagebox.showinfo("Sucesso!", "Dados atualizados!")
                txtfrota.delete(0, END)
                txtplaca.delete(0, END)
                txtnome.delete(0, END)
                txteixo.delete(0, END)
                txtptb.delete(0, END)

                btnconfirma.destroy

                mostrar_cavalos()

            btnconfirma = Button(frame_baixo, command=update, text="Confirma".upper(
            ), width=10, height=1, bg=co4, fg=co1, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
            btnconfirma.place(x=310, y=80)

        except IndexError:
            messagebox.showerror("Erro!", "Selecione um dos dodos da tabela")

    # funcção deletar dados

    def deletar():
        global tree
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            treev_lista = treev_dicionario["values"]
            valor = treev_lista[0]

            deletarCavalos([valor])

            messagebox.showinfo("Sucesso!", "Dados deletados com sucesso!")

            mostrar_cavalos()

        except IndexError:
            messagebox.showerror("Erro!", "Selecione um dos dodos da tabela")

    # label textbox
    labelfrotas = Label(frame_baixo, text="Frota".upper(),
                        height=1, anchor=NW, font=("Ivy 10 bold"), bg=co0, fg=co1)
    labelfrotas.place(x=10, y=10)
    txtfrota = Entry(frame_baixo, width=10, justify="left", relief="solid")
    txtfrota.place(x=10, y=40)

    labelplaca = Label(frame_baixo, text="Placa".upper(), height=1,
                       anchor=NW, font=("Ivy 10 bold"), bg=co0, fg=co1)
    labelplaca.place(x=80, y=10)
    txtplaca = Entry(frame_baixo, width=10, justify="left", relief="solid")
    txtplaca.place(x=80, y=40)

    labelnome = Label(frame_baixo, text="Nome".upper(), height=1,
                      anchor=NW, font=("Ivy 10 bold"), bg=co0, fg=co1)
    labelnome.place(x=150, y=10)
    txtnome = Entry(frame_baixo, width=40, justify="left", relief="solid")
    txtnome.place(x=150, y=40)

    labeleixo = Label(frame_baixo, text="Eixo".upper(), height=1,
                      anchor=NW, font=("Ivy 10 bold"), bg=co0, fg=co1)
    labeleixo.place(x=400, y=10)
    txteixo = Entry(frame_baixo, width=10, justify="left", relief="solid")
    txteixo.place(x=400, y=40)

    labelptb = Label(frame_baixo, text="PTB".upper(), height=1,
                     anchor=NW, font=("Ivy 10 bold"), bg=co0, fg=co1)
    labelptb.place(x=470, y=10)
    txtptb = Entry(frame_baixo, width=10, justify="left", relief="solid")
    txtptb.place(x=470, y=40)

    # botoes CRUD

    btnadiconar = Button(frame_baixo, command=adicionar_cavalo, text="Adicionar", width=10,
                         height=1, bg=co14, fg=co0, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
    btnadiconar.place(x=10, y=80)
    btneditar = Button(frame_baixo, command=atulizar, text="Editar", width=10, height=1,
                       bg=co12, fg=co1, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
    btneditar.place(x=110, y=80)
    btnexcluir = Button(frame_baixo, command=deletar, text="Excluir", width=10, height=1,
                        bg=co11, fg=co1, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
    btnexcluir.place(x=210, y=80)


def carreta():
    janela = Tk()
    janela.title("CopaEnergia")
    janela.geometry("700x510")
    janela.configure(background=co6)
    janela.resizable(width=FALSE, height=FALSE)

    # creating the frames
    frame_cima = Frame(janela, width=700, height=25, bg=co3, relief="flat")
    frame_cima.grid(row=0, column=0, sticky=NSEW)

    frame_baixo = Frame(janela, width=700, height=475, bg=co1, relief="flat")
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    frame_baixo_esquerda = Frame(
        frame_baixo, width=700, height=470, bg=co0, relief="flat")
    frame_baixo_esquerda.grid(row=3, column=0, pady=1, padx=0, sticky=NSEW)

    # logo
    app_logo = Label(frame_cima, text="Carretas", width=20, height=1,
                     padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co1)
    app_logo.place(x=10, y=5)

    # entrada de dados
    global tree

    # mostrar carretas

    def mostrar_carretas():
        # criando a treeview para mostrar os dados das carretas
        global tree
        tabela_carretas = ['Item', 'Frota','Placa', 'Capacidade', 'Eixo', 'PTB']
        lista_carreta = ver_dados()
        tree = ttk.Treeview(frame_baixo_esquerda, columns=(
            "Frota", "Placa", "Capacidade", "Eixo", "PTB"), show="headings")
        tree = ttk.Treeview(frame_baixo_esquerda, selectmode="extended",
                            columns=tabela_carretas, show="headings")

        # tree.column("Itens", width=50)
        tree.column("Frota", width=100)
        tree.column("Placa", width=100)
        tree.column("Capacidade", width=120)
        tree.column("Eixo", width=50)
        tree.column("PTB", width=100)
    # tree.heading("Itens", text="Itens")
        tree.heading("Frota", text="Frota")
        tree.heading("Placa", text="Placa")
        tree.heading("Capacidade", text="Capacidade")
        tree.heading("Eixo", text="Eixo")
        tree.heading("PTB", text="PTB")
        tree.place(x=10, y=120)

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_baixo_esquerda,
                            orient="vertical", command=tree.yview)
        vsb.place(x=511, y=121, height=222)
        tree.configure(yscrollcommand=vsb.set)
        frame_baixo_esquerda.grid_rowconfigure(0, weight=12)

        hd = ["center", "center", "center", "center", "center", "center"]
        h = [50, 100, 100, 120, 50, 100]
        n = 0
        for col in tabela_carretas:
            tree.heading(col, text=col.title(), anchor=CENTER)
            tree.column(col, width=h[n], anchor=hd[n])
            n += 1

        for item in lista_carreta:
            tree.insert("", "end", values=item)

    mostrar_carretas()

    # função para adicionar nova carreta--------------------------------------------------------------------

    def adicionar_carreta():
        global tree
        frota = txtfrota.get()
        placa = txtplaca.get().upper()
        capacidade = txtcapacidade.get()
        eixo = txteixo.get()
        ptb = txtptb.get()

        lista_adicionar = [frota, placa, capacidade, eixo, ptb]

        for item in lista_adicionar:
            if item == "":
                messagebox.showerror(
                    "Erro", "Por favor, preencha todos os campos.")
                return
        inserir_dados(lista_adicionar)

        messagebox.showinfo("Sucesso", "Carreta adiconada com sucesso!")

        txtfrota.delete(0, END)
        txtplaca.delete(0, END)
        txtcapacidade.delete(0, END)
        txteixo.delete(0, END)
        txtptb.delete(0, END)

        for widget in frame_baixo_esquerda.winfo_children():
            widget.destroy()

        mostrar_carretas()

    # função atualizar dados---------------------------------------------------------------------------

    def atulizar():
        global tree
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            treev_lista = treev_dicionario["values"]

            valor = treev_lista[0]

            txtfrota.delete(0, END)
            txtplaca.delete(0, END)
            txtcapacidade.delete(0, END)
            txteixo.delete(0, END)
            txtptb.delete(0, END)

            id = int(treev_lista[0])
            txtfrota.insert(0, treev_lista[1])
            txtplaca.insert(0, treev_lista[2])
            txtcapacidade.insert(0, treev_lista[3])
            txteixo.insert(0, treev_lista[4])
            txtptb.insert(0, treev_lista[5])

            def update():
                global tree

                frota = txtfrota.get()
                placa = txtplaca.get().upper()
                capacidade = txtcapacidade.get()
                eixo = txteixo.get()
                ptb = txtptb.get()

                lista_atualizar = [frota, placa, capacidade, eixo, ptb, id]

                for i in lista_atualizar:
                    if i == "":
                        messagebox.showerror(
                            "Erro", "Preencha todos os campos")
                        return
                update_dados(lista_atualizar)

                messagebox.showinfo("Sucesso!", "Dados atualizados!")

                txtfrota.delete(0, END)
                txtplaca.delete(0, END)
                txtcapacidade.delete(0, END)
                txteixo.delete(0, END)
                txtptb.delete(0, END)

                btnconfirma.destroy

                mostrar_carretas()

            btnconfirma = Button(frame_baixo, command=update, text="Confirma".upper(
            ), width=10, height=1, bg=co4, fg=co1, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
            btnconfirma.place(x=310, y=80)

        except IndexError:
            messagebox.showerror("Erro!", "Selecione um dos dodos da tabela")

    # funcção deletar dados----------------------------------------------------------------------------------------

    def deletar():
        global tree
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            treev_lista = treev_dicionario["values"]
            valor = treev_lista[0]

            deletar_dados([valor])

            messagebox.showinfo("Sucesso!", "Dados deletados com sucesso!")

            mostrar_carretas()

        except IndexError:
            messagebox.showerror("Erro!", "Selecione um dos dodos da tabela")

    # label itens e textbox

    labelfrotas = Label(frame_baixo, text="Frota".upper(), height=1,
                        anchor=NW,  font=("Ivy 10 bold"), bg=co0, fg=co1)
    labelfrotas.place(x=10, y=10)
    txtfrota = Entry(frame_baixo, width=10, justify="left", relief="solid")
    txtfrota.place(x=10, y=40)

    labelplaca = Label(frame_baixo, text="Placa".upper(), height=1,
                       anchor=NW,  font=("Ivy 10 bold"), bg=co0, fg=co1)
    labelplaca.place(x=80, y=10)
    txtplaca = Entry(frame_baixo, width=10, justify="left", relief="solid")
    txtplaca.place(x=80, y=40)

    labelcapacidade = Label(frame_baixo, text="Capacidade".upper(),
                            height=1, anchor=NW,  font=("Ivy 10 bold"), bg=co0, fg=co1)
    labelcapacidade.place(x=150, y=10)
    txtcapacidade = Entry(frame_baixo, width=14,
                          justify="left", relief="solid")
    txtcapacidade.place(x=150, y=40)

    labeleixo = Label(frame_baixo, text="Eixo".upper(), height=1,
                      anchor=NW,  font=("Ivy 10 bold"), bg=co0, fg=co1)
    labeleixo.place(x=244, y=10)
    txteixo = Entry(frame_baixo, width=10, justify="left", relief="solid")
    txteixo.place(x=244, y=40)

    labeptb = Label(frame_baixo, text="PTB".upper(), height=1, anchor=NW,
                    font=("Ivy 10 bold"), bg=co0, fg=co1)
    labeptb.place(x=312, y=10)
    txtptb = Entry(frame_baixo, width=10, justify="left", relief="solid")
    txtptb.place(x=312, y=40)

    # botoes CRUD

    btnadiconar = Button(frame_baixo, command=adicionar_carreta, text="Adicionar", width=10,
                         height=1, bg=co14, fg=co0, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
    btnadiconar.place(x=10, y=80)

    btneditar = Button(frame_baixo, command=atulizar, text="Editar", width=10, height=1,
                       bg=co12, fg=co1, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
    btneditar.place(x=110, y=80)

    btnexcluir = Button(frame_baixo, command=deletar, text="Excluir", width=10, height=1,
                        bg=co11, fg=co1, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
    btnexcluir.place(x=210, y=80)


def bobs():
    # creating the main windows

    janela = Tk()
    janela.title("CopaEnergia")
    janela.geometry("400x379")
    janela.configure(background=co6)
    janela.resizable(width=FALSE, height=FALSE)

    # creating the frames
    frame_cima = Frame(janela, width=700, height=25, bg=co3, relief="flat")
    frame_cima.grid(row=0, column=0, sticky=NSEW)

    frame_baixo = Frame(janela, width=700, height=475, bg=co1, relief="flat")
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    frame_baixo_esquerda = Frame(
        frame_baixo, width=700, height=470, bg=co0, relief="flat")
    frame_baixo_esquerda.grid(row=3, column=0, pady=1, padx=0, sticky=NSEW)

    # logo
    app_logo = Label(frame_cima, text="Bobs", width=20, height=1, padx=0,
                     relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co1)
    app_logo.place(x=10, y=5)

    # entrada de dados
    global tree

    # mostrar carretas

    def mostrar_bob():
        # criando a treeview para mostrar os dados das carretas
        global tree
        tabela_bob = ['Item', 'Frota', 'Placa', 'PTB']
        lista_bob = ver_dado_bobs()
        tree = ttk.Treeview(frame_baixo_esquerda, columns=(
            "Frota", "Placa", "PTB"), show="headings")
        tree = ttk.Treeview(frame_baixo_esquerda, selectmode="extended",
                            columns=tabela_bob, show="headings")

        tree.column("Frota", width=100)
        tree.column("Placa", width=100)
        tree.column("PTB", width=100)

        tree.heading("Frota", text="Frota")
        tree.heading("Placa", text="Placa")
        tree.heading("PTB", text="PTB")
        tree.place(x=10, y=120)

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_baixo_esquerda,
                            orient="vertical", command=tree.yview)
        vsb.place(x=361, y=121, height=225)
        tree.configure(yscrollcommand=vsb.set)
        frame_baixo_esquerda.grid_rowconfigure(0, weight=12)

        hd = ["center", "center", "center", "center"]
        h = [50, 110, 100, 100]
        n = 0
        for col in tabela_bob:
            tree.heading(col, text=col.title(), anchor=CENTER)
            tree.column(col, width=h[n], anchor=hd[n])
            n += 1

        for item in lista_bob:
            tree.insert("", "end", values=item)

    mostrar_bob()

    # função para adicionar nova carreta--------------------------------------------------------------------

    def adicionar_bob():
        global tree
        frota = txtfrota.get()
        placa = txtplaca.get().upper()
        ptb = txtptb.get()

        lista_bob = [frota, placa, ptb]

        for item in lista_bob:
            if item == "":
                messagebox.showerror(
                    "Erro", "Por favor, preencha todos os campos.")
                return
        inserir_dados_bob(lista_bob)

        messagebox.showinfo("Sucesso", "Carreta adiconada com sucesso!")

        txtfrota.delete(0, END)
        txtplaca.delete(0, END)
        txtptb.delete(0, END)

        for widget in frame_baixo_esquerda.winfo_children():
            widget.destroy()

        mostrar_bob()

    # função atualizar dados---------------------------------------------------------------------------

    def atulizar():
        global tree
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            treev_lista = treev_dicionario["values"]

            valor = treev_lista[0]

            txtfrota.delete(0, END)
            txtplaca.delete(0, END)
            txtptb.delete(0, END)

            id = int(treev_lista[0])
            txtfrota.insert(0, treev_lista[1])
            txtplaca.insert(0, treev_lista[2])
            txtptb.insert(0, treev_lista[3])

            def update():
                global tree

                frota = txtfrota.get()
                placa = txtplaca.get().upper()
                ptb = txtptb.get()

                lista_bob = [frota, placa, ptb, id]

                for i in lista_bob:
                    if i == "":
                        messagebox.showerror(
                            "Erro", "Preencha todos os campos")
                        return
                update_dados_bob(lista_bob)

                messagebox.showinfo("Sucesso!", "Dados atualizados!")

                txtfrota.delete(0, END)
                txtplaca.delete(0, END)
                txtptb.delete(0, END)

                btnconfirma.destroy

            mostrar_bob()

            btnconfirma = Button(frame_baixo, command=update, text="Gravar".upper(
            ), width=8, height=1, bg=co4, fg=co1, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
            btnconfirma.place(x=310, y=80)

        except IndexError:
            messagebox.showerror("Erro!", "Selecione um dos dodos da tabela")

    # funcção deletar dados----------------------------------------------------------------------------------------

    def deletar():
        global tree
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            treev_lista = treev_dicionario["values"]
            valor = treev_lista[0]

            deletar_dados_bob([valor])

            messagebox.showinfo("Sucesso!", "Dados deletados com sucesso!")

            mostrar_bob()

        except IndexError:
            messagebox.showerror("Erro!", "Selecione um dos dodos da tabela")

    def quit():
        janela.quit()
        janela.destroy()

    # label itens e textbox

    labelfrotas = Label(frame_baixo, text="Frota".upper(), height=1,
                        anchor=NW,  font=("Ivy 10 bold"), bg=co0, fg=co1)
    labelfrotas.place(x=10, y=10)
    txtfrota = Entry(frame_baixo, width=10, justify="left", relief="solid")
    txtfrota.place(x=10, y=40)

    labelplaca = Label(frame_baixo, text="Placa".upper(), height=1,
                       anchor=NW,  font=("Ivy 10 bold"), bg=co0, fg=co1)
    labelplaca.place(x=80, y=10)
    txtplaca = Entry(frame_baixo, width=10, justify="left", relief="solid")
    txtplaca.place(x=80, y=40)

    labeptb = Label(frame_baixo, text="PTB".upper(), height=1, anchor=NW,
                    font=("Ivy 10 bold"), bg=co0, fg=co1)
    labeptb.place(x=148, y=10)
    txtptb = Entry(frame_baixo, width=10, justify="left", relief="solid")
    txtptb.place(x=148, y=40)

    # botoes CRUD

    btnadiconar = Button(frame_baixo, command=adicionar_bob, text="Adicionar", width=10,
                         height=1, bg=co14, fg=co0, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
    btnadiconar.place(x=10, y=80)

    btneditar = Button(frame_baixo, command=atulizar, text="Editar", width=10, height=1,
                       bg=co12, fg=co1, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
    btneditar.place(x=110, y=80)

    btnexcluir = Button(frame_baixo, command=deletar, text="Excluir", width=10, height=1,
                        bg=co11, fg=co1, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
    btnexcluir.place(x=210, y=80)

    janela.mainloop()


def centroCusto():

    janela = Tk()
    janela.title("CopaEnergia")
    janela.geometry("530x379")
    janela.configure(background=co6)
    janela.resizable(width=FALSE, height=FALSE)

    # creating the frames
    frame_cima = Frame(janela, width=700, height=25, bg=co3, relief="flat")
    frame_cima.grid(row=0, column=0, sticky=NSEW)

    frame_baixo = Frame(janela, width=700, height=475, bg=co1, relief="flat")
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    frame_baixo_esquerda = Frame(
        frame_baixo, width=700, height=470, bg=co0, relief="flat")
    frame_baixo_esquerda.grid(row=3, column=0, pady=1, padx=0, sticky=NSEW)

    # logo
    app_logo = Label(frame_cima, text="Bobs", width=20, height=1, padx=0,
                     relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co1)
    app_logo.place(x=10, y=5)

    # entrada de dados
    global tree

    # mostrar carretas

    def mostrar_centro_custo():
        # criando a treeview para mostrar os dados das carretas
        global tree
        tabela_filial = ['Item', 'Codigo', 'Filial']
        lista_filial = ver_dados_filial()
        tree = ttk.Treeview(frame_baixo_esquerda, columns=(
            "Codigo", "Filial"), show="headings")
        tree = ttk.Treeview(frame_baixo_esquerda, selectmode="extended",
                            columns=tabela_filial, show="headings")

        tree.column("Codigo", width=100)
        tree.column("Filial", width=100)

        tree.heading("Codigo", text="Codigo")
        tree.heading("Filial", text="Filial")

        tree.place(x=10, y=120)

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_baixo_esquerda,
                            orient="vertical", command=tree.yview)
        vsb.place(x=501, y=121, height=225)
        tree.configure(yscrollcommand=vsb.set)
        frame_baixo_esquerda.grid_rowconfigure(0, weight=12)

        hd = ["center", "center", "sw"]
        h = [50, 150, 300]
        n = 0
        for col in tabela_filial:
            tree.heading(col, text=col.title(), anchor=CENTER)
            tree.column(col, width=h[n], anchor=hd[n])
            n += 1

        for item in lista_filial:
            tree.insert("", "end", values=item)

    mostrar_centro_custo()

    # função para adicionar nova carreta--------------------------------------------------------------------

    def adicionar_centro_custo():
        global tree
        codigo = txtcodigo.get()
        filial = txtfilial.get().upper()

        lista_filial = [codigo, filial]

        for item in lista_filial:
            if item == "":
                messagebox.showerror(
                    "Erro", "Por favor, preencha todos os campos.")
                return
        inserir_dados_filial(lista_filial)

        messagebox.showinfo("Sucesso", "Carreta adiconada com sucesso!")

        txtcodigo.delete(0, END)
        txtfilial.delete(0, END)

        for widget in frame_baixo_esquerda.winfo_children():
            widget.destroy()

        mostrar_centro_custo()

    # função atualizar dados---------------------------------------------------------------------------

    def atulizar_centro_custo():
        global tree
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            treev_lista = treev_dicionario["values"]

            valor = treev_lista[0]

            txtcodigo.delete(0, END)
            txtfilial.delete(0, END)

            id = int(treev_lista[0])
            txtcodigo.insert(0, treev_lista[1])
            txtfilial.insert(0, treev_lista[2])

            def update():
                global tree

                codigo = txtcodigo.get()
                filial = txtfilial.get().upper()

                lista_filial = [codigo, filial, id]

                for i in lista_filial:
                    if i == "":
                        messagebox.showerror(
                            "Erro", "Preencha todos os campos")
                        return
                update_dados_filial(lista_filial)

                messagebox.showinfo("Sucesso!", "Dados atualizados!")

                txtcodigo.delete(0, END)
                txtfilial.delete(0, END)

                btnconfirma.destroy

                mostrar_centro_custo()

            btnconfirma = Button(frame_baixo, command=update, text="Gravar".upper(
            ), width=8, height=1, bg=co4, fg=co1, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
            btnconfirma.place(x=310, y=80)

        except IndexError:
            messagebox.showerror("Erro!", "Selecione um dos dodos da tabela")

    # funcção deletar dados----------------------------------------------------------------------------------------

    def deletar_centro_custo():
        global tree
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            treev_lista = treev_dicionario["values"]
            valor = treev_lista[0]

            deletar_dados_filial([valor])

            messagebox.showinfo("Sucesso!", "Dados deletados com sucesso!")

            mostrar_centro_custo()

        except IndexError:
            messagebox.showerror("Erro!", "Selecione um dos dodos da tabela")

    def quit():
        janela.quit()
        janela.destroy()

    # label itens e textbox

    labelcodigo = Label(frame_baixo, text="Codigo".upper(
    ), height=1, anchor=NW,  font=("Ivy 10 bold"), bg=co0, fg=co1)
    labelcodigo.place(x=10, y=10)
    txtcodigo = Entry(frame_baixo, width=10, justify="left", relief="solid")
    txtcodigo.place(x=10, y=40)

    labelfilial = Label(frame_baixo, text="Filial".upper(
    ), height=1, anchor=NW,  font=("Ivy 10 bold"), bg=co0, fg=co1)
    labelfilial.place(x=80, y=10)
    txtfilial = Entry(frame_baixo, width=10, justify="left", relief="solid")
    txtfilial.place(x=80, y=40)

    # botoes CRUD

    btnadiconar = Button(frame_baixo, command=adicionar_centro_custo, text="Adicionar", width=10,
                         height=1, bg=co14, fg=co0, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
    btnadiconar.place(x=10, y=80)

    btneditar = Button(frame_baixo, command=atulizar_centro_custo, text="Editar", width=10,
                       height=1, bg=co12, fg=co1, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
    btneditar.place(x=110, y=80)

    btnexcluir = Button(frame_baixo, command=deletar_centro_custo, text="Excluir", width=10,
                        height=1, bg=co11, fg=co1, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
    btnexcluir.place(x=210, y=80)


def industrial():

    janela = Tk()
    janela.title("CopaEnergia")
    janela.geometry("530x379")
    janela.configure(background=co6)
    janela.resizable(width=FALSE, height=FALSE)

    # creating the frames
    frame_cima = Frame(janela, width=700, height=25, bg=co3, relief="flat")
    frame_cima.grid(row=0, column=0, sticky=NSEW)

    frame_baixo = Frame(janela, width=700, height=475, bg=co1, relief="flat")
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    frame_baixo_esquerda = Frame(
        frame_baixo, width=700, height=470, bg=co0, relief="flat")
    frame_baixo_esquerda.grid(row=3, column=0, pady=1, padx=0, sticky=NSEW)

    # logo
    app_logo = Label(frame_cima, text="Bobs", width=20, height=1, padx=0,
                    relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co1)
    app_logo.place(x=10, y=5)

    # entrada de dados
    global tree

    # mostrar carretas

  
    def mostrar_industrial():
        # criando a treeview para mostrar os dados das carretas
        global tree
        tabela_industria = ['Item', 'Codigo', 'Industria']
        lista_industria = ver_dados_industrial()
        tree = ttk.Treeview(frame_baixo_esquerda, columns=("Codigo", "Industria"), show="headings")
        tree = ttk.Treeview(frame_baixo_esquerda, selectmode="extended",columns=tabela_industria, show="headings")

        tree.column("Codigo", width=100)
        tree.column("Industria", width=300)

        tree.heading("Codigo", text="Codigo")
        tree.heading("Industria", text="Industria")

        tree.place(x=10, y=120)

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_baixo_esquerda,orient="vertical", command=tree.yview)
        vsb.place(x=501, y=121, height=225)
        tree.configure(yscrollcommand=vsb.set)
        frame_baixo_esquerda.grid_rowconfigure(0, weight=12)

        hd = ["center", "center", "sw"]
        h = [50, 150, 300]
        n = 0
        for col in tabela_industria:
            tree.heading(col, text=col.title(), anchor=CENTER)
            tree.column(col, width=h[n], anchor=hd[n])
            n += 1

        for item in lista_industria:
            tree.insert("", "end", values=item)

    mostrar_industrial()

    # função para adicionar nova carreta--------------------------------------------------------------------

    def adicionar_centro_industrial():
        global tree
        codigo = txtcodigo.get()
        filial = txtindustria.get().upper()

        lista_industria = [codigo, filial]

        for item in lista_industria:
            if item == "":
                messagebox.showerror(
                    "Erro", "Por favor, preencha todos os campos.")
                return
        inserir_dados_industrial(lista_industria)

        messagebox.showinfo("Sucesso", "Carreta adiconada com sucesso!")

        txtcodigo.delete(0, END)
        txtindustria.delete(0, END)

        for widget in frame_baixo_esquerda.winfo_children():
            widget.destroy()

        mostrar_industrial()

    # função atualizar dados---------------------------------------------------------------------------

    def atulizar_centro_industrial():
        global tree
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            treev_lista = treev_dicionario["values"]

            valor = treev_lista[0]

            txtcodigo.delete(0, END)
            txtindustria.delete(0, END)

            id = int(treev_lista[0])
            txtcodigo.insert(0, treev_lista[1])
            txtindustria.insert(0, treev_lista[2])

            def update():
                global tree

                codigo = txtcodigo.get()
                industria = txtindustria.get().upper()

                lista_industria = [codigo, industria, id]

                for i in lista_industria:
                    if i == "":
                        messagebox.showerror(
                            "Erro", "Preencha todos os campos")
                        return
                update_dados_industrial(lista_industria)

                messagebox.showinfo("Sucesso!", "Dados atualizados!")

                txtcodigo.delete(0, END)
                txtindustria.delete(0, END)

                btnconfirma.destroy

                mostrar_industrial()

            btnconfirma = Button(frame_baixo, command=update, text="Gravar".upper(
            ), width=8, height=1, bg=co4, fg=co1, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
            btnconfirma.place(x=310, y=80)

        except IndexError:
            messagebox.showerror("Erro!", "Selecione um dos dodos da tabela")

    # funcção deletar dados----------------------------------------------------------------------------------------

    def deletar_centro_industrial():
        global tree
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            treev_lista = treev_dicionario["values"]
            valor = treev_lista[0]

            deletar_dados_industrial([valor])

            messagebox.showinfo("Sucesso!", "Dados deletados com sucesso!")

            mostrar_industrial()

        except IndexError:
            messagebox.showerror("Erro!", "Selecione um dos dodos da tabela")

    def quit():
        janela.quit()
        janela.destroy()

    # label itens e textbox

    labelcodigo = Label(frame_baixo, text="Codigo".upper(), height=1, anchor=NW,  font=("Ivy 10 bold"), bg=co0, fg=co1)
    labelcodigo.place(x=10, y=10)
    txtcodigo = Entry(frame_baixo, width=10, justify="left", relief="solid")
    txtcodigo.place(x=10, y=40)

    labelindustria = Label(frame_baixo, text="Industria".upper(
    ), height=1, anchor=NW,  font=("Ivy 10 bold"), bg=co0, fg=co1)
    labelindustria.place(x=80, y=10)
    txtindustria = Entry(frame_baixo, width=30, justify="left", relief="solid")
    txtindustria.place(x=80, y=40)

    # botoes CRUD

    btnadiconar = Button(frame_baixo, command=adicionar_centro_industrial, text="Adicionar", width=10,
                        height=1, bg=co14, fg=co0, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
    btnadiconar.place(x=10, y=80)

    btneditar = Button(frame_baixo, command=atulizar_centro_industrial, text="Editar", width=10,
                    height=1, bg=co12, fg=co1, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
    btneditar.place(x=110, y=80)

    btnexcluir = Button(frame_baixo, command=deletar_centro_industrial, text="Excluir", width=10,
                        height=1, bg=co11, fg=co1, font=("Ivy 10 bold"), relief="raised", overrelief="ridge")
    btnexcluir.place(x=210, y=80)

    
    janela.mainloop()


barradeMenu = Menu(app)
menuArquivo = Menu(barradeMenu, tearoff=0)
menuArquivo.add_command(label="Carretas", command=carreta)
menuArquivo.add_command(label="Cavalos", command=cavalo)
menuArquivo.add_command(label="Bobs", command=bobs)
menuArquivo.add_command(label="Motorista")
menuArquivo.add_command(label="Industrial",command=industrial)
menuArquivo.add_command(label="Centro de Custo", command=centroCusto)
menuArquivo.add_separator()
menuArquivo.add_command(label="Sair", command=app.quit)
barradeMenu.add_cascade(label="Cadastro", menu=menuArquivo)
app.config(menu=barradeMenu)

def carregar_dados():   

    frota_cavalo = entry_frota_cavalo.get()
    conexao = sqlite3.connect("cavalo.db")
    cursor = conexao.cursor()
    
    buscar = frota_cavalo
    comando_sql = "SELECT placa FROM cavalo WHERE frota = ?"
    cursor.execute(comando_sql, (buscar,))
    resultado = "".join(cursor.fetchone())

    #Nnome

    buscar = frota_cavalo
    comando_sql = "SELECT nome FROM cavalo WHERE frota = ?"
    cursor.execute(comando_sql, (buscar,))
    nome = "".join(cursor.fetchone())

    # eixo

    buscar = frota_cavalo
    comando_sql = "SELECT eixo FROM cavalo WHERE frota = ?"
    cursor.execute(comando_sql, (buscar,))
    eixo = (cursor.fetchone())

    # ptb
    buscar = frota_cavalo
    comando_sql = "SELECT ptb FROM cavalo WHERE frota = ?"  
    cursor.execute(comando_sql, (buscar,))
    ptb = (cursor.fetchone())


    dados_do_cavalo.configure(text="Placa do cavalo: {}".format(resultado) + "   |   Eixo: {}".format(eixo[0]) + "   |    PTB: {}".format(ptb[0]))
    nome_motorista.configure(text="Motorista: {}".format(nome))

def carregar_carreta():
    frota_carreta = entry_frota_carreta.get()
    conexao = sqlite3.connect("carretas.db")
    cursor = conexao.cursor()
    
    buscar = frota_carreta
    comando_sql = "SELECT placa FROM carreta WHERE frota = ?"
    cursor.execute(comando_sql, (buscar,))
    resultado2 = "".join(cursor.fetchone())

    #capacidade

    buscar = frota_carreta
    comando_sql = "SELECT capacidade FROM carreta WHERE frota = ?"
    cursor.execute(comando_sql, (buscar,))
    capacidade = (cursor.fetchone())

    # eixo

    buscar = frota_carreta
    comando_sql = "SELECT eixo FROM carreta WHERE frota = ?"
    cursor.execute(comando_sql, (buscar,))
    eixo2 = (cursor.fetchone())

    # ptb
    buscar = frota_carreta
    comando_sql = "SELECT ptb FROM carreta WHERE frota = ?"  
    cursor.execute(comando_sql, (buscar,))
    ptb2 = (cursor.fetchone())


    dados_da_carreta.configure(text="Placa da carreta: {}".format(resultado2) + "   |    Eixo: {}".format(eixo2[0]) + "   |    PTB: {}".format(ptb2[0]))
    capacidade_carreta.configure(text=f"Capacidade Geométrica: {capacidade[0]}") 
                              

    conexao.close()

def comandoscombinados():
    carregar_dados()
    carregar_carreta()
    calcular_soma_total()

def calcular_soma_total():
    try:
        # 1. Conectar ao Banco de Dados 1
        conn1 = sqlite3.connect('carretas.db')
        cursor1 = conn1.cursor()
        cursor1.execute("SELECT SUM(eixo) FROM carreta WHERE frota = ?", (entry_frota_carreta.get(),))
        total1 = cursor1.fetchone()[0] or 0 # Retorna 0 se for NULL
        conn1.close()

        # 2. Conectar ao Banco de Dados 2
        conn2 = sqlite3.connect('cavalo.db')
        cursor2 = conn2.cursor()
        cursor2.execute("SELECT SUM(eixo) FROM cavalo WHERE frota = ?", (entry_frota_cavalo.get(),))
        total2 = cursor2.fetchone()[0] or 0
        conn2.close()

        # 3. Somar os dois
        resultado_final = total1 + total2

        # 4. Atualizar o label no customtkinter
        label_resultado_eixo.configure(text=f"Quantidade de eixos: {resultado_final:.0f}")

    except Exception as e:
        label_resultado_eixo.configure(text="Erro")
        print(f"Erro ao acessar banco: {e}")

# --- Função de Callback ---
def combobox_callback(choice):
    # Atualiza o texto da label com a escolha atual
    label_resultado.configure(text=f"Centro de Custo: {choice}")
    print("Opção escolhida:", choice)

# --- Criando o ComboBox ---
combobox = ctk.CTkComboBox(app, values=["1005 DAC", "1201 CO"],command=combobox_callback )
combobox.place(x=280 , y=9)
combobox.set("Selecione...") # Define um valor inicial opcional

#entrada da placa do cavalo
label_frota_cavalo = customtkinter.CTkLabel(app, text="Frota do Cavalo")
label_frota_cavalo.place(x=10, y= 15)
entry_frota_cavalo = customtkinter.CTkEntry(app)
entry_frota_cavalo.place(x=110, y=9)

#entrada da plca da carreta

label_frota_carreta = customtkinter.CTkLabel(app, text="Frota da Carreta")
label_frota_carreta.place(x=10, y=60  )   
entry_frota_carreta = customtkinter.CTkEntry(app)
entry_frota_carreta.place(x=110, y=60)



#botão para carregar dados
botao_carregar = customtkinter.CTkButton(app, text="Carregar Dados", command=comandoscombinados)
botao_carregar.place(x=10, y=100)



def carregar_dados_banco():

    try:
        # Conecta ao banco de dados
        conn = sqlite3.connect('industrial.db')
        cursor = conn.cursor()
        
        # Seleciona os dados (ex: nomes de uma tabela 'clientes')
        cursor.execute("SELECT filial FROM industria")
        dados = cursor.fetchall() # Retorna uma lista de tuplas: [('Ana',), ('Pedro',)]
        
        # Converte lista de tuplas para lista plana: ['Ana', 'Pedro']
        lista_final = [item[0] for item in dados]
        
        conn.close()
        return lista_final
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return []
# Busca os dados e cria o ComboBox
dados_combobox = carregar_dados_banco()
def combobox_callback2  (choice):
    # Atualiza o texto da label com a escolha atual
    label_resultado3.configure(text=f"Centro de Custo: {choice}")
    print("Opção escolhida:", choice)

combobox = customtkinter.CTkComboBox(master=app,values=dados_combobox,width=200,command=combobox_callback2) # Chama a função ao selecionar
combobox.place(x=280 , y=60)
combobox.set("Destino...") # Define um valor inicial opcional
# Define um valor padrão se houver dados
if dados_combobox:
    combobox.set(dados_combobox[0])

# --- Criando a Label ---

dados_do_cavalo = customtkinter.CTkLabel(app, text="")
dados_do_cavalo.place(x=10, y=140)

dados_da_carreta = customtkinter.CTkLabel(app, text="")
dados_da_carreta.place(x=10, y=180)

nome_motorista = customtkinter.CTkLabel(app, text="")
nome_motorista.place(x=10, y=220)

capacidade_carreta = customtkinter.CTkLabel(app, text="")
capacidade_carreta.place(x=10, y=260)

label_resultado_eixo = customtkinter.CTkLabel(app, text="")
label_resultado_eixo.place(x=220, y=260)

label_resultado = ctk.CTkLabel(app, text="Centro de Custo: ", font=("Arial", 14))
label_resultado.place(x=10, y=320 )

label_resultado3 = customtkinter.CTkLabel(app, text="Centro de Custo: ", font=("Arial", 14))
label_resultado3.place(x=250, y=320)








app.mainloop()
