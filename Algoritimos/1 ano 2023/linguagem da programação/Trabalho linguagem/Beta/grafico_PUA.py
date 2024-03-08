from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def adicionar():
    if variavel_nome_tarefa.get() == "":
        messagebox.showinfo(
            title="Erro de valor", message="Não é possivel adicionar uma tarefa sem nome, digite um nome a sua tarefa")
        return

    variavel_status = 'Pendente'
    tabela_ver.insert("", "end", values=(variavel_id.get(), variavel_nome_tarefa.get(
    ), variavel_descriacao_tarefa.get(), variavel_status))

    variavel_id.delete(0, END)
    variavel_nome_tarefa.delete(0, END)
    variavel_descriacao_tarefa.delete(0, END)
    variavel_id.focus()


def remover():
    try:
        item_selecionado = tabela_ver.selection()[0]
        tabela_ver.delete(item_selecionado)
    except:
        messagebox.showinfo(
            title="Erro de exclusão", message="Não é possivel excluir algo não selecionado, por favor! selecione a tarefa a ser excluida")
        return


def marca_concluida():
    variavel_status = 'Concluido'

    try:
        item_selecionado = tabela_ver.selection()[0]
        tabela_ver.set(item_selecionado, "Status", variavel_status)
    except:
        messagebox.showinfo(
            title="Erro de marcação", message="Não é possivel marca como concluido algo não selecionado, por favor! selecione a tarefa a ser marcada como concluida")
        return


def marca_pendente():
    variavel_status = 'Pendente'

    try:
        item_selecionado = tabela_ver.selection()[0]
        tabela_ver.set(item_selecionado, "Status", variavel_status)
    except:
        messagebox.showinfo(
            title="Erro de marcação", message="Não é possivel marca como pendente algo não selecionado, por favor! selecione a tarefa a ser marcada como pendente")
        return

# -----------------------------------------------------------


aplicativo = Tk()
aplicativo.title("Gerenciador de Tarefa")
aplicativo.geometry("700x490")

# ---------------------------------------------------------------

tabela_tarefa = LabelFrame(aplicativo, text="Lista das Tarefas")
tabela_tarefa.pack(fill="both", expand="yes", padx=13, pady=13)

tabela_ver = ttk.Treeview(tabela_tarefa, columns=(
    'Id', 'Nome_tarefa', 'Detalhe_tarefa', 'Status'), show='headings')

tabela_ver.column('Id', minwidth=0, width=98)
tabela_ver.column('Nome_tarefa', minwidth=0, width=208)
tabela_ver.column('Detalhe_tarefa', minwidth=0, width=225)
tabela_ver.column('Status', minwidth=0, width=120)

tabela_ver.heading('Id', text='Contagem')
tabela_ver.heading('Nome_tarefa', text='Nomes das tarefas')
tabela_ver.heading('Detalhe_tarefa', text='Descrição das Tarefas')
tabela_ver.heading('Status', text='Status')
tabela_ver.pack()

ver_id = Label(tabela_tarefa, text="Contagem")
variavel_id = Entry(tabela_tarefa)

ver_status = Label(tabela_tarefa, text="Status")
variavel_status = Entry(tabela_tarefa)

# ------------------------------------------------------------------------

tabela_escrever_tarefa = LabelFrame(aplicativo, text="Adiconar Tarefas")
tabela_escrever_tarefa.pack(fill="both", expand="yes", padx=8, pady=8)

ver_nome_tarefa = Label(tabela_escrever_tarefa, text="Nome da Tarefa")
variavel_nome_tarefa = Entry(tabela_escrever_tarefa)

ver_descriacao_tarefa = Label(
    tabela_escrever_tarefa, text="Descrição da Tarefa")
variavel_descriacao_tarefa = Entry(tabela_escrever_tarefa)

ver_nome_tarefa.grid(column=1, row=2, sticky='w')
variavel_nome_tarefa.grid(column=2, row=2)

ver_descriacao_tarefa.grid(column=3, row=2, sticky='w')
variavel_descriacao_tarefa.grid(column=4, row=2)

bt_inserir = Button(tabela_escrever_tarefa,
                    text="Adicionar", command=adicionar)
bt_inserir.grid(column=5, row=2)

# ---------------------------------------------------------------------
tabela_botao = LabelFrame(aplicativo, text="Opção de Marcação")
tabela_botao.pack(fill="both", expand="yes", padx=8, pady=8)

bt_marca_concluido = Button(
    tabela_botao, text="Marcar como Concluida", command=marca_concluida)
bt_marca_pendente = Button(
    tabela_botao, text="Marcar como Pendente", command=marca_pendente)
bt_deletar = Button(tabela_botao, text="Excluir Tarefa", command=remover)

bt_marca_concluido.grid(column=1, row=5)
bt_marca_pendente.grid(column=2, row=5)
bt_deletar.grid(column=3, row=5)

# ---------------------------------------------------------------------------

aplicativo.mainloop()
