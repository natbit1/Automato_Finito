#PROJETO AUTÔMATO FINITO

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from itertools import chain

class Interface:

    def __init__(self):
        
        self.janela = Tk()
        self.tab_val_func_ant = [['']]

    def ConfigJanela(self):

        self.indice_diag = 0 #indice tela inicial para dados do diagrama
        fator_tela = 0.898 #Porcentagem visível da altura da tela (sem a barra de tarefas do Windows)

        self.lar_tela_pxls = self.janela.winfo_screenwidth() #Largura da tela em pixels
        self.alt_tela_pxls = self.janela.winfo_screenheight() #Altura da tela em pixels

        self.lar_jan_pxls = int(self.lar_tela_pxls) #Largura da janela em pixels
        self.alt_jan_pxls = int(fator_tela*self.alt_tela_pxls) #Altura da janela em pixels
        
        self.janela.title("Autômato finito")
        self.janela.configure(background = '#211954')
        self.janela.geometry(str(self.lar_jan_pxls) + "x" + str(self.alt_jan_pxls))
        self.janela.resizable(False, False)

        ajust_hor_tela = -int(self.alt_tela_pxls) // 90

        self.janela.geometry("+{}+{}".format(ajust_hor_tela, 0))

        self.larg_bd_frames = 2
        self.cor_frames = 'black'
        self.cor_bd_frames = 'yellow'

        self.font_labels = 'arial'
        self.cor_labels = 'white'
        self.tam_labels = 10

        self.font_entries = 'arial'
        self.tam_font_entries = 10

        self.larg_bd_tab = 1
        self.cor_bd_tab = 'white'
        self.lrel_cel_tab = 0.06
        self.tam_lbl_tab = 8

    def Widgets_Input_1(self):

        self.ConfigJanela()

        #Frames do input e do diagrama

        self.frame_input_1 = Frame(self.janela, bg=self.cor_frames, highlightbackground=self.cor_bd_frames, highlightthickness=self.larg_bd_frames)
        self.frame_input_1.place(relx=0, rely=0, relwidth=0.3, relheight=0.07)

        self.frame_input_2 = Frame(self.janela, bg=self.cor_frames, highlightbackground=self.cor_bd_frames, highlightthickness=self.larg_bd_frames)
        self.frame_input_2.place(relx=0, rely=0.072, relwidth=0.3, relheight=0.928)

        frame_diag = Frame(self.janela, bg=self.cor_frames, highlightbackground=self.cor_bd_frames, highlightthickness=self.larg_bd_frames)
        frame_diag.place(relx=0.302, rely=0, relwidth=0.698, relheight=1)

        #Entradas de dados

        entry_var1 = tk.StringVar()
        entry_var1.trace_add("write", self.Ler_input_1)

        self.entry_alfa = Entry(self.frame_input_1, textvariable=entry_var1, font=(self.font_entries, self.tam_font_entries))
        self.entry_alfa.place(relx=0.2, rely=0.25, relwidth=0.27, relheight=0.5)

        self.entry_var2 = tk.StringVar()
        self.entry_var2.trace_add("write", self.Ler_input_1)

        self.entry_num_ests = Entry(self.frame_input_1, textvariable=self.entry_var2, font=(self.font_entries, self.tam_font_entries))
        self.entry_num_ests.place(relx=0.85, rely=0.25, relwidth=0.08, relheight=0.5)

        lbl_alfa = Label(self.frame_input_1, text="Alfabeto", bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_labels, 'bold'))
        lbl_alfa.place(relx=0.04, rely=0.25)

        lbl_num_ests = Label(self.frame_input_1, text='Número de estados', bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_labels, 'bold'))
        lbl_num_ests.place(relx=0.52, rely=0.25)

        #Tabela

        self.janela.mainloop()

    def Widgets_Input_2(self):

        lbl_func = Label(self.frame_input_2, text="Função de transição", bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_labels, 'bold'))
        lbl_func.place(relx=0.34, rely=0.04)

        alt_frame_tab = self.lrel_cel_tab*(self.num_ests + 1)*self.frame_input_2.winfo_screenheight()/self.frame_input_2.winfo_screenwidth()

        frame_tab = Frame(self.frame_input_2, bg=self.cor_frames, highlightbackground=self.cor_bd_tab, highlightthickness=self.larg_bd_tab)
        frame_tab.place(relx=(1-self.lrel_cel_tab*(len(self.lista_alfa) + 1))/2, rely=0.09, relwidth=self.lrel_cel_tab*(len(self.lista_alfa) + 1), relheight=alt_frame_tab)

        self.tab_str_var = []
        self.tab_entry = []

        for i in range(self.num_ests+1):

            frame_tab.rowconfigure(i, weight=1)

            lin_str_var = []
            lin_entry = []

            for j in range(len(self.lista_alfa)+1):

                frame_tab.columnconfigure(j, weight=1) 
                    
                if i==0 and j>0: 

                    lbl_func = Label(frame_tab, text=self.lista_alfa[j-1], bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_lbl_tab, 'bold'))
                    lbl_func.grid(row=i, column=j, sticky=NSEW)

                elif i>0 and j==0:
            
                    lbl_func = Label(frame_tab, text='q'+ str(i-1), bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_lbl_tab, 'bold'))
                    lbl_func.grid(row=i, column=j, sticky=NSEW)

                elif i==0 and j==0:

                    frame_space = Label(frame_tab, text="", bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_lbl_tab, 'bold'))
                    frame_space.grid(row=i, column=j, sticky=NSEW)

                else:

                    str_var = tk.StringVar()
                    str_var.trace_add("write", self.Ler_tabela)

                    entry_func = Entry(frame_tab, width=0, textvariable=str_var, font=(self.font_entries, self.tam_font_entries))
                    entry_func.grid(row=i, column=j, sticky=NSEW, padx=0.5, pady=0.5)

                    lin_str_var.append(str_var)
                    lin_entry.append(entry_func)

            if i>0: 
                
                self.tab_str_var.append(lin_str_var)
                self.tab_entry.append(lin_entry)

        rely_lbl_ests_aceit = alt_frame_tab + 0.13

        lbl_ests_aceit = Label(self.frame_input_2, text="Selecionar estados de aceitação", bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_labels, 'bold'))
        lbl_ests_aceit.place(relx=0.04, rely=rely_lbl_ests_aceit)

        lbl_ests_aceit = Label(self.frame_input_2, text="Selecionar estado inicial", bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_labels, 'bold'))
        lbl_ests_aceit.place(relx=0.04, rely=rely_lbl_ests_aceit+0.1)

        lbl_cadeia = Label(self.frame_input_2, text="Cadeia de caracteres", bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_labels, 'bold'))
        lbl_cadeia.place(relx=0.03, rely=0.9)

        self.entry_var3 = tk.StringVar()
        self.entry_var3.trace_add("write", self.Ler_cadeia)
        
        self.entry_cadeia = Entry(self.frame_input_2, textvariable=self.entry_var3, font=(self.font_entries, self.tam_font_entries))
        self.entry_cadeia.place(relx=0.4, rely=0.904, relwidth=0.25, relheight=0.03)

        rely_cb_est = rely_lbl_ests_aceit+0.065
        marg_cb_frame = 0.5/self.num_ests**(0.0755*self.num_ests)

        if self.num_ests==1: marg_rel_cb=0
        else: marg_rel_cb = (1 - 2*marg_cb_frame)/(self.num_ests-1)

        self.lista_ests = ['q' + str(i) for i in range(self.num_ests)]

        for i in range(self.num_ests):

            cb_est_1 = Checkbutton(self.frame_input_2, text=self.lista_ests[i], bg=self.cor_frames, fg='white', selectcolor="black")
            cb_est_1.place(relx=marg_cb_frame + i*marg_rel_cb, rely=rely_cb_est, anchor=CENTER)

            self.marg_cb_est_2 = rely_cb_est+0.1

            cb_est_2 = Checkbutton(self.frame_input_2, text=self.lista_ests[i], bg=self.cor_frames, fg='white', selectcolor="black")
            cb_est_2.place(relx=marg_cb_frame + i*marg_rel_cb, rely=self.marg_cb_est_2, anchor=CENTER)

        button_input = Button(self.frame_input_2, text="Processar")
        button_input.place(relx=0.7, rely=0.900, relwidth=0.25)

    def Botao_input_2(self):

        button_input = Button(self.frame_input_2, text="Gerar autômato")
        button_input.place(relx=0.375, rely=self.marg_cb_est_2 + 0.06, relwidth=0.25)

    def Ler_input_1(self,*args):

        for widget in self.frame_input_2.winfo_children(): widget.destroy()
        
        self.alfa = self.entry_alfa.get() #Pegando os símbolos inseridos pelo usuário
        self.num_ests = self.entry_var2.get() #Pegando o número de estados inserido pelo usuário

        self.alfa = self.alfa.replace(' ','') #removendo os espaços vazios

        #Contando as vírgulas no final da string dos sínbolos

        if self.alfa!='':

            num_virg_final = 0
            i=-1

            while self.alfa[i]==',':

                num_virg_final+=1
                i-=1

        else: num_virg_final=0

        self.alfa = self.alfa[0:len(self.alfa)-num_virg_final] #Removendo as vírgulas no final da string

        list_pos_virg = [a[0] for a in enumerate(self.alfa) if a[1]==','] #Guardando a posição das vírgulas que separam os símbolos

        #Construindo a lista dos símbolos do alfabeto

        if len(list_pos_virg)>0: self.lista_alfa = [self.alfa[0:list_pos_virg[0]]] + [self.alfa[list_pos_virg[i]+1:list_pos_virg[i+1]] for i in range(len(list_pos_virg)-1)] + [self.alfa[list_pos_virg[-1]+1:len(self.alfa)]]
        else: self.lista_alfa = [self.alfa]

        #Tratamento de erros

        try:

            #Se os símbolos inseridos pelo usuário forem distintos e um número inteiro maior que zero for dado, a tabela da função de transição é construída

            if self.alfa!='' and num_virg_final<2 and len(self.lista_alfa)==len(set(self.lista_alfa)) and (self.num_ests.isdigit()==True and int(self.num_ests)>0): 
                
                self.num_ests = int(self.num_ests)
                self.Widgets_Input_2()
                self.Auto_preencher_tab()
                
            #Caso contrário, o programa acusará os seguintes erros

            else:

                #ERRO 1: símbolos repetidos

                if num_virg_final==1 and len(self.lista_alfa)!=len(set(self.lista_alfa)): 
                    
                    self.entry_alfa.delete(len(self.alfa), tk.END)
                    raise ValueError("o alfabeto do autômato não deve conter símbolos repetidos!")
                
                #ERRO 2: vírgula como símbolo do alfabeto

                if num_virg_final==2:

                    self.entry_alfa.delete(len(self.alfa)+1, tk.END)
                    self.Ler_input_1()
                    raise ValueError("vírgula não pode ser um símbolo do alfabeto! Ela deve ser usada somente para separar os símbolos")

                #ERRO 3: a entrada para o número de estados não é um número inteiro positivo

                if (self.num_ests!='' and self.num_ests.isdigit()==False) or (self.num_ests.isdigit()==True and int(self.num_ests)==0): 
                    
                    self.entry_num_ests.delete(0, tk.END)
                    raise ValueError("o número de estados do autômato deve ser inteiro positivo!")

        except ValueError as ve: messagebox.showerror("Erro", f"Entrada incorreta: {ve}")

    def Ler_cadeia(self,*args):

        self.cadeia = self.entry_var3.get()

    def Ler_tabela(self,*args):

        tab_val_func = []

        for i in range(len(self.tab_str_var)):

            lin_val_func = []

            for j in range(len(self.tab_str_var[i])):

                val_func = self.tab_str_var[i][j].get()
                lin_val_func.append(val_func)

                val_func = val_func.replace(' ','') #removendo os espaços vazios da string

                try:

                    if val_func in self.lista_ests or val_func=='': lin_val_func.append(val_func)
                    else: 
                        
                        if val_func[0]!='q' or (len(val_func)>1 and not val_func[1:len(val_func)].isdigit()): 

                            self.tab_entry[i][j].delete(0, tk.END)
                            raise ValueError("os estados devem ser compostos pela letra ""q"" seguida de um número!")
                        
                        if len(val_func)>1 and val_func[1:len(val_func)].isdigit() and int(val_func[1:len(val_func)])>=self.num_ests: 
                            
                            self.tab_entry[i][j].delete(0, tk.END)
                            raise ValueError("estado não existente! Os estados são de " + str(self.lista_ests[0]) + " até " + str(self.lista_ests[-1]))

                except ValueError as ve: messagebox.showerror("Erro", f"Entrada incorreta: {ve}")

            tab_val_func.append(lin_val_func)

        if '' not in list(chain(*tab_val_func)): self.Botao_input_2()

        self.tab_val_func_ant = tab_val_func.copy()

    def Auto_preencher_tab(self):

        tab_val_func_ant = self.tab_val_func_ant.copy()

        for i in range(len(self.tab_entry)):

            for j in range(len(self.tab_entry[i])):

                if i<len(tab_val_func_ant) and j<len(tab_val_func_ant[i]): self.tab_entry[i][j].insert(0, tab_val_func_ant[i][j])
                else: self.tab_entry[i][j].insert(0, '')

interface = Interface().Widgets_Input_1()