from tkinter import *
from tkinter import Tk
from tkinter import ttk
#Importando tkCalendar e DateTime
from tkcalendar import DateEntry
##
from datetime import date
##
from tkinter import messagebox

from tkinter import filedialog as fd
#Importando view que tem a conexão com o banco
from View import *
from Login import *
#Importando Pillow
from PIL import Image, ImageTk

#Main Window
JanelaPrincipal = Tk()
JanelaPrincipal.title("")
JanelaPrincipal.geometry("1100x620")
JanelaPrincipal.config(background="#e9edf5")
JanelaPrincipal.resizable(width=FALSE, height=FALSE)

#Style q divide frame cima e meio
style = ttk.Style(JanelaPrincipal)  
style.theme_use("clam")

#Frame Cima
Frame_Cima = Frame(JanelaPrincipal,width=1100,height=50,bg="#e9edf5",relief=FLAT)
Frame_Cima.grid(row=0, column=0)
#Frame Meio
Frame_Meio = Frame(JanelaPrincipal,width=1100,height=303,bg="#e9edf5",pady=20,relief=FLAT)
Frame_Meio.grid(row=1, column=0, pady=1,padx=0,sticky=NSEW)
#Frame Baixo
Frame_Baixo = Frame(JanelaPrincipal,width=1100,height=300,bg="#e9edf5",pady=20,relief=FLAT)
Frame_Baixo.grid(row=2, column=0, pady=0,padx=1,sticky=NSEW)


#Imagem Logo
app_img = Image.open('bebidas.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)


#Imagem logo em label
app_logo = Label(Frame_Cima,image=app_img, text="  Bebidas em Geral",
width=1100,
compound=LEFT,
relief=RAISED,
anchor=NW,
font=("Verdana 20"),
bg="#e9edf5",
fg="#000000")
app_logo.place(x=0,y=0)

#Funções
global tree

def Clear():
    global imagem, imagem_string
    Entry_ID.delete(0, END)
    Entry_Nome.delete(0, END)
    Combobox_ProdutoGrupo.delete(0, END)
    Entry_Descricao.delete(0, END)
    Entry_Data.delete(0, END)
    Entry_Compra.delete(0, END)
    Entry_Qtd.delete(0, END)
    Entry_Nome.focus()
    imagem = imagem_string = ""
    #imagem.delete(0, END)




def Add():
    global imagem, imagem_string, label_imagem
    nome = Entry_Nome.get()
    grupoprod = Combobox_ProdutoGrupo.get()
    descricao = Entry_Descricao.get()
    data_compra = Entry_Data.get_date()
    valor = Entry_Compra.get()
    qtd = Entry_Qtd.get()
    imagem = imagem_string 
   
    

    

    try:
       if nome == "":
        messagebox.showerror("Alert","Informe o Nome do Produto!!")          
       elif grupoprod == "":
        messagebox.showerror("Alert","Informe o Grupo do Produto!!")          
       elif descricao == "":
        messagebox.showerror("Alert","Informe a Descrição do Produto!!")          
       elif data_compra == "":
        messagebox.showerror("Alert","Informe a Data de Venda do Produto!!")          
       elif valor == "":
        messagebox.showerror("Alert","Informe o Valor do Produto!!") 
       elif qtd == "":
        messagebox.showerror("Alert","Informe a Quatidade do Produto!!") 
       else:
         cursor = conexao.cursor()
         query = "INSERT INTO Produtos(Nome_Produto,Produto_Grupo,Descricao,Data_Compra,Valor_Compra,Qtd,Imagem_Produto) Values (%s,%s,%s,%s,%s,%s,%s)"
         val = (nome,grupoprod,descricao,data_compra,valor,qtd,imagem)
         cursor.execute(query, val)
         conexao.commit()
         Clear()
         Mostrar()       
         messagebox.showinfo("Sucesso","Produto Adicionado com Sucesso!")   
          
    except:
        messagebox.showerror("Erro","Erro ao Adicionar um Produto!!")
        cursor.close()
        conexao.close()

def Update():
    
    global imagem, imagem_string, label_imagem
    id = Entry_ID.get()
    nome = Entry_Nome.get()
    grupoprod = Combobox_ProdutoGrupo.get()
    descricao = Entry_Descricao.get()
    data_compra = Entry_Data.get_date()
    valor = Entry_Compra.get()
    qtd = Entry_Qtd.get()
    imagem = imagem_string 
    
    try:
       if id == "":
        messagebox.showerror("Alert","Informe o ID do Produto!!")  
       elif nome == "":
        messagebox.showerror("Alert","Informe o Nome do Produto!!")             
       elif grupoprod == "":
        messagebox.showerror("Alert","Informe o Grupo do Produto!!")          
       elif descricao == "":
        messagebox.showerror("Alert","Informe a Descrição do Produto!!")          
       elif data_compra == "":
        messagebox.showerror("Alert","Informe a Data de Venda do Produto!!")          
       elif valor == "":
        messagebox.showerror("Alert","Informe o Valor do Produto!!") 
       elif qtd == "":
        messagebox.showerror("Alert","Informe a Quatidade do Produto!!") 
       else:            
        cursor = conexao.cursor()
        query = "Update Produtos SET Nome_Produto=%s,Produto_Grupo=%s,Descricao=%s,Data_Compra=%s,Valor_Compra=%s,Qtd=%s,Imagem_Produto=%s WHERE Produto_ID=%s"
        val = (nome,grupoprod,descricao,data_compra,valor,qtd,imagem,id)
        cursor.execute(query, val)
        conexao.commit()
        #conexao.close() 
        Clear()
        Mostrar()
        messagebox.showinfo("Sucesso","Produto Atualizado com Sucesso!")       
    except:
        messagebox.showerror("Erro","Erro...")    
        cursor.close()
        conexao.close()
 
   
   

def Delete():
    id = Entry_ID.get()
    asnwer = messagebox.askyesno(title='Confirmation',
                          message='Você quer mesmo Excluir esse Produto?')
    try:
      if id == "":
        messagebox.showerror("Alerta","Informe o ID!!")
      elif asnwer == True:
        cursor = conexao.cursor()
        query = "Delete from Produtos Where Produto_ID = %s"
        val = (id,)
        cursor.execute(query,val)
        conexao.commit()
        Clear()
        Mostrar()
       
        messagebox.showinfo("Aviso","Produto Excluido com Sucesso!")
    except:
      messagebox.showerror("Erro","Erro!")
      cursor.close()
      conexao.close()

def Select():
    
    id = Entry_ID.get()
    try:
        if id == "":
            messagebox.showinfo("Alert","Informe o ID para Buscar um Produto")
        else:
            cursor = conexao.cursor()
            query = "SELECT * FROM Produtos Where Produto_ID = %s"
            val = (id,)
            cursor.execute(query,val)
            result = cursor.fetchall()
            Clear()
            
            for row in result:
                Entry_Nome.insert(0, row[1])
                Combobox_ProdutoGrupo.insert(0,row[2])
                Entry_Descricao.insert(0, row[3])
                Entry_Data.insert(0, row[4])
                Entry_Compra.insert(0, row[5])
    except: 
      pass


 #funcao para mostrar no grid(treeview) todos os dados da tabela produtos
def ver_form():
    ver_dados = []
    cursor = conexao.cursor()
    query = "SELECT * FROM Produtos "
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
       ver_dados.append(row)
    return ver_dados  

#Metodo para escolher imagem e colocar na label_imagem
def EscolherImagem():
    global imagem, imagem_string, label_imagem
    
    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((175,175))
    imagem = ImageTk.PhotoImage(imagem)

    label_imagem = Label(Frame_Meio,image=imagem, fg="#000000",bg="#e9edf5")
    label_imagem.place(x=860,y=10)

#funcao q pega todos os produtos pelo id passado como argumento
def ver_item(id):
    ver_item = []
    cursor = conexao.cursor(prepared=True)
    query = "SELECT * FROM Produtos where Produto_ID = ?"
    cursor.execute(query,id)

    rows = cursor.fetchall()
    for row in rows:
       ver_item.append(row)
    return ver_item  

global imagem, imagem_string, label_imagem

def ver_imagem():
   global imagem, imagem_string, label_imagem

   treev_dados = tree.focus()
   treev_dicionario = tree.item(treev_dados)
   treev_lista = treev_dicionario['values']

   valor = [int(treev_lista[0])]

   item = ver_item(valor)

   imagem = item[0][7]

   imagem = Image.open(imagem)
   imagem = imagem.resize((175,175))
   imagem = ImageTk.PhotoImage(imagem)

   label_imagem = Label(Frame_Meio,image=imagem,fg="#000000",bg="#e9edf5")
   label_imagem.place(x=860,y=10)


def Click(event):
  #Lista de Entrys
  entrys = [Entry_ID, Entry_Nome, Combobox_ProdutoGrupo, Entry_Descricao,Entry_Data,Entry_Compra,Entry_Qtd]
  # Obtém o item selecionado na TreeView
  item = tree.selection()[0]
  values = tree.item(item,"values")
  #for para passar valores do TreeView clicado para os Entry
  for i in range(len(entrys)):
    entrys[i].delete(0, END)
    entrys[i].insert(0, values[i])
  ver_imagem()
    
  
  

#Label ID
Label_ID = Label(Frame_Meio,text="ID Produto:",height=1,font=("Verdana",12),fg="#000000",bg="#e9edf5")
Label_ID.place(x=10,y=10)
#Label Nome
Label_Nome = Label(Frame_Meio,text="Nome:",font=("Verdana",12),fg="#000000",bg="#e9edf5")
Label_Nome.place(x=50,y=40)
#Label Produto Grupo
Label_ProdutoGrupo = Label(Frame_Meio,text="Grupo:",font=("Verdana",12),fg="#000000",bg="#e9edf5")
Label_ProdutoGrupo.place(x=50,y=70)
#Label Descrição
Label_Descricao = Label(Frame_Meio,text="Descrição:",font=("Verdana",12),fg="#000000",bg="#e9edf5")
Label_Descricao.place(x=20,y=100)
#Label Data
Label_Data = Label(Frame_Meio,text="Data Venda:",font=("Verdana", 12),fg="#000000",bg="#e9edf5")
Label_Data.place(x=3,y=130)
#Label Compra
Label_Compra = Label(Frame_Meio,text="Valor:",font=("Verdana", 12),fg="#000000",bg="#e9edf5")
Label_Compra.place(x=55,y=160)
#Label Quantidade Itens
Label_Qtd = Label(Frame_Meio,text="Quantidade: ",font=("Verdana",12),fg="#000000",bg="#e9edf5")
Label_Qtd.place(x=3,y=190)
#Label Carregar Imagem
Label_Img = Label(Frame_Meio,text="Imagem:",font=("Verdana",12),fg="#000000",bg="#e9edf5")
Label_Img.place(x=30,y=220)


#Entry ID
Entry_ID = Entry(Frame_Meio,font=("Verdana",12),width=8,justify="left",relief=SOLID)
Entry_ID.place(x=130,y=10)
#Entry Nome
Entry_Nome = Entry(Frame_Meio,font=("Verdana", 12),justify="left", relief=SOLID)
Entry_Nome.place(x=130, y=40)
#Entry Produto Grupo
Combobox_ProdutoGrupo = ttk.Combobox(Frame_Meio,font=("Verdana", 12),justify="left",width=12)
Combobox_ProdutoGrupo.place(x=130,y=70)
Combobox_ProdutoGrupo['values'] = ('Água','Cervejas','Destilados','Refrigerante','Sucos')
#Entry Descrição
Entry_Descricao = Entry(Frame_Meio,font=("Verdana",12),justify="left", relief=SOLID)
Entry_Descricao.place(x=130,y=100)
#Entry Data
Entry_Data = DateEntry(Frame_Meio,Background="darkblue",width=12,font=("Verdana", 10))
Entry_Data.place(x=130,y=130)
#Entry_Compra
Entry_Compra = Entry(Frame_Meio,font=("Verdana",12),justify="left", relief=SOLID)
Entry_Compra.place(x=130,y=160)
#Entry_Quantidade
Entry_Qtd = Entry(Frame_Meio,font=("Verdana",12),justify="left", relief=SOLID)
Entry_Qtd.place(x=130,y=190)

#Buttons
#Button Carregar Imagem
img_camera = Image.open('imagem.png')
img_camera = img_camera.resize((25,25))
img_camera = ImageTk.PhotoImage(img_camera)

Btn_Carregar = Button(Frame_Meio,image=img_camera,width=150,command=EscolherImagem,text=" Carregar Imagem",compound=LEFT, font=("Verdana",10),anchor=NW,fg="#000000",bg="#e9edf5",overrelief=RIDGE)
Btn_Carregar.place(x=130,y=215)

#Button Add e Imagem Botão Adicionar
img_add = Image.open('adicionar.png')
img_add = img_add.resize((25,25))
img_add = ImageTk.PhotoImage(img_add)

Btn_Add = Button(Frame_Meio,image=img_add,text="  Adicionar",compound=LEFT,width=150, font=("Verdana",10),anchor=NW,fg="#000000",bg="#e9edf5",overrelief=RIDGE,command=Add)
Btn_Add.place(x=400,y=10)

#Button Update e Imagem Botão Update
img_upd = Image.open('atualizar.png')
img_upd = img_upd.resize((25,25))
img_upd = ImageTk.PhotoImage(img_upd)

Btn_Upd = Button(Frame_Meio,image=img_upd,text="  Atualizar",compound=LEFT,width=150,font=("Verdana",10),anchor=NW,fg="#000000",bg="#e9edf5",overrelief=RIDGE,command=Update)
Btn_Upd.place(x=400,y=60)

#Button Delete e Imagem Button Delete
img_del = Image.open('deletar.png')
img_del = img_del.resize((25,25))
img_del = ImageTk.PhotoImage(img_del)

Btn_Delete = Button(Frame_Meio,image=img_del,text="  Deletar",compound=LEFT,width=150,font=("Verdana",10),anchor=NW,fg="#000000",bg="#e9edf5",overrelief=RIDGE,command=Delete)
Btn_Delete.place(x=400,y=110)

#Button Ver Imagem e Imagem Button Ver Imagem
#img_verimagem = Image.open('verimagem.png')
#img_verimagem = img_verimagem.resize((25,25))
#img_verimagem = ImageTk.PhotoImage(img_verimagem)

#Btn_VerImagem = Button(Frame_Meio,image=img_verimagem,command=ver_imagem,text="  Ver Item",compound=LEFT,width=150,font=("Verdana",10),anchor=NW,fg="#000000",bg="#e9edf5",overrelief=RIDGE)
#Btn_VerImagem.place(x=300,y=190)

#Button Cancelar e Imagem Button Cancelar
imagem_cancelar = Image.open('cancelar.png')
imagem_cancelar = imagem_cancelar.resize((25,25))
imagem_cancelar = ImageTk.PhotoImage(imagem_cancelar)

Btn_Cancelar = Button(Frame_Meio,image=imagem_cancelar,command=Clear,text="  Limpar",compound=LEFT,width=150,font=("Verdana",10),anchor=NW,fg="#000000",bg="#e9edf5",overrelief=RIDGE)
Btn_Cancelar.place(x=400,y=160)
#Labels Quantidade e Valor Total
Label_ValorTotal = Label(Frame_Meio,text= " ",width=20,height=3,anchor=CENTER, font=("Verdana",12),fg="#000000",bg="#008b77")
Label_ValorTotal.place(x=600,y=28)

Label_ValorTotal2 = Label(Frame_Meio,text= "Valor Total Itens: ",width=20,height=2,anchor=CENTER, font=("Verdana",12),fg="#000000",bg="#008b77")
Label_ValorTotal2.place(x=600,y=10)

Label_Quantidade = Label(Frame_Meio,text= " ",width=20,height=3,anchor=CENTER, font=("Verdana",12),fg="#000000",bg="#008b77")
Label_Quantidade.place(x=600,y=118)

Label_Quantidade2 = Label(Frame_Meio,text= "Quantidade Itens:",width=20,height=2,anchor=CENTER, font=("Verdana",12),fg="#000000",bg="#008b77")
Label_Quantidade2.place(x=600,y=100)


# tabela 
def Mostrar():

  global tree
# creating a treeview com duas scrollbar
#cabecalho do grid
  tabela_head = ['#Id','Produto',  'Grupo','Descrição', 'Data Compra', 'Valor Unit.','Quantidade']

  lista_itens = ver_form()
#criando grid
  tree = ttk.Treeview(Frame_Baixo, selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
  vsb = ttk.Scrollbar(Frame_Baixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
  hsb = ttk.Scrollbar(Frame_Baixo, orient="horizontal", command=tree.xview)

  tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
  tree.grid(column=0, row=0, sticky='nsew')
  vsb.grid(column=1, row=0, sticky='ns')
  hsb.grid(column=0, row=1, sticky='ew')
  Frame_Baixo.grid_rowconfigure(0, weight=12)
  tree.bind("<Double-1>", Click)


  hd=["center","center","center","center","center","center","center"]
  h=[80,200,200,180,150,135,135]
  n=0

  for col in tabela_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
      # adjust the column's width to the header string
    tree.column(col, width=h[n],anchor=hd[n])
    n+=1




    # inserindo os itens dentro da tabela
  for item in lista_itens:
    tree.insert('', 'end', values=item)


  valortotal = []
  quantidade = [] 
  Total_valor = []

  #for para ir acrescentando o valor 
  for iten in lista_itens:
    valortotal.append(iten[5])
    quantidade.append(iten[6])
  
  #for para percorrer a lista e ir somando as colunas valor e quantidade para retornar o valor total de tudo
  for i in range(len(lista_itens)):
    total = valortotal[i] * quantidade[i]
    Total_valor.append(total)
    

  
  Total_itens = sum(quantidade)
 

  Label_ValorTotal['text'] = 'R$ {:,.2f}'.format(sum(Total_valor))
  Label_Quantidade['text'] = Total_itens

Mostrar()

JanelaPrincipal.mainloop()
 