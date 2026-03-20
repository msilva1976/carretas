
from tkinter import *
from tkinter import ttk, StringVar
from tkinter import messagebox
import tkinter.ttk as ttk

# from main import mostrar_carretas
from viewCavalo import *
from view import *
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

frame_baixo_esquerda = Frame(frame_baixo, width=700, height=470, bg=co0, relief="flat")
frame_baixo_esquerda.grid(row=3, column=0, pady=1, padx=0, sticky=NSEW)

app_logo = Label(frame_cima, text="Cavalos", width=20, height=1, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co1)
app_logo.place(x=10, y=5)

    # entrada de dados

global tree

    # mostrar cavalos


def mostrar_bob():
        global tree
        tabela_bob = ['Item', 'Frota', 'Placa', 'PTB']
        lista_bob = verCavalos()
        tree = ttk.Treeview(frame_baixo_esquerda, columns=(
            "Frota", "Placa","PTB"), show="headings")
        tree = ttk.Treeview(frame_baixo_esquerda, selectmode="extended",
                            columns=tabela_bob, show="headings")

        # tree.column
        tree.column("Frota", width=50)
        tree.column("Placa", width=40)
        tree.column("PTB", width=100)
        tree.heading("Frota", text="Frota")
        tree.heading("Placa", text="Placa")
        tree.heading("PTB", text="PTB")
        tree.place(x=10, y=120)

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_baixo_esquerda,
                            orient="vertical", command=tree.yview)
        vsb.place(x=511, y=121, height=222)
        tree.configure(yscrollcommand=vsb.set)
        frame_baixo_esquerda.grid_rowconfigure(0, weight=12)

        hd = ["center", "center", "center"]
        h = [50, 50, 70, 100]
        n = 0    
        for col in tabela_bob:
            tree.heading(col, text=col.title(), anchor=CENTER)
            tree.column(col, width=h[n], anchor=hd[n])
            n += 1

        for item in lista_bob:
            tree.insert("", "end", values=item)

        mostrar_bob()

    # função para adicionar novo cavalo


def adicionar_bob():
        global tree
        frota = txtfrota.get()
        placa = txtplaca.get().upper()
        ptb = txtptb.get()

        lista_adicionar = [frota, placa,ptb]

        for item in lista_adicionar:
            if item == "":
                messagebox.showerror(
                    "Erro", "Por favor, preencha todos os campos.")
                return
        inserirbob(lista_bob)

        messagebox.showinfo("Sucesso", "Bob adicionado com sucesso!")

        txtfrota.delete(0, END)
        txtplaca.delete(0, END)
        txtptb.delete(0, END)

        for widget in frame_baixo_esquerda.winfo_children():
            widget.destroy()

        mostrar_bob()

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

                lista_atualizar = [frota, placa,ptb, id]

                for i in lista_atualizar:
                    if i == "":
                        messagebox.showerror("Erro", "Preencha todos os campos")
                        return
                updateCavalos(lista_bob)

                messagebox.showinfo("Sucesso!", "Dados atualizados!")
                txtfrota.delete(0, END)
                txtplaca.delete(0, END)
                txtptb.delete(0, END)

                btnconfirma.destroy

                mostrar_bob()

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

            mostrar_bob()

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


labelptb = Label(frame_baixo, text="PTB".upper(), height=1,
                    anchor=NW, font=("Ivy 10 bold"), bg=co0, fg=co1)
labelptb.place(x=150, y=10)
txtptb = Entry(frame_baixo, width=10, justify="left", relief="solid")
txtptb.place(x=150, y=40)

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