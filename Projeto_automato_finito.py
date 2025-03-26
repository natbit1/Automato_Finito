#PROJETO AUTÔMATO FINITO

from tkinter import *
import tkinter as tk
import math
from tkinter import messagebox
from itertools import chain
from collections import Counter

class Interface:

    def __init__(self):
        
        self.janela = Tk()
        self.tab_val_func_ant = [['']]
        self.limit_est = 10
        self.limit_num_simbs = 10
        self.list_est_conect = []

    def ConfigJanela(self):

        self.alt_pixels_jan = self.janela.winfo_screenheight() #Altura do frame da tabela em pixels
        self.lar_pixels_jan = self.janela.winfo_screenwidth() #Largura do frame da tabela em pixels
        
        self.janela.title("Autômato finito")
        self.janela.configure(background = '#211954')
        self.janela.geometry(str(self.lar_pixels_jan) + "x" + str(self.alt_pixels_jan))
        self.janela.resizable(False, False)

        ajust_hor_tela = -int(self.alt_pixels_jan) // 90

        self.janela.geometry("+{}+{}".format(ajust_hor_tela, 0))

        self.larg_bd_frames = 2
        self.cor_frames = 'black'
        self.cor_bd_frames = 'yellow'

        self.font_labels = 'arial'
        self.cor_labels = 'white'
        self.tam_labels = int(0.014*self.alt_pixels_jan)

        self.font_entries = 'arial'
        self.tam_font_entries = int(0.014*self.alt_pixels_jan)

        self.larg_bd_tab = int(0.002*self.alt_pixels_jan)
        self.cor_bd_tab = 'white'
        self.lrel_cel_tab = 0.06
        self.tam_lbl_tab = int(0.012*self.alt_pixels_jan)

        self.marg_canva_tabela = 0.12 #Margem do canva dos círculos de marcação em relação à tabela
        self.rely_lbl_func_trans = 0.06 #Margem superior label função de transição
        self.rely_lbl_est_inicial = 0.6 #Margem entre os círculos de marcação do estado inicial e dos estados de aceitação
        self.marg_gadget_lbl = 0.02 #margem dos gadgets em relação aos respectivos títulos
        self.diam_cm = 0.019 #diâmetro dos círculos de marcação
        self.marg_lbl_cm = 0.004 #Margem das labels em relação aos respectivos círculos de marcação

        self.diam_circ_est_ext = int(0.09*self.alt_pixels_jan)
        self.diam_circ_est_int = int(0.033*self.alt_pixels_jan)
        self.tam_lbl_est_circ = int(0.015*self.alt_pixels_jan)
        self.cor_circ_est = 'white' #cor dos círculos dos estados

    def Widgets_Input_1(self):

        self.ConfigJanela()

        #Frames do input e do diagrama

        self.frame_input_1 = Frame(self.janela, bg=self.cor_frames, highlightbackground=self.cor_bd_frames, highlightthickness=self.larg_bd_frames)
        self.frame_input_1.place(relx=0, rely=0, relwidth=0.3, relheight=0.07)

        self.frame_input_2 = Frame(self.janela, bg=self.cor_frames, highlightbackground=self.cor_bd_frames, highlightthickness=self.larg_bd_frames)
        self.frame_input_2.place(relx=0, rely=0.072, relwidth=0.3, relheight=0.928)

        self.frame_diag = Frame(self.janela, bg=self.cor_frames, highlightbackground=self.cor_bd_frames, highlightthickness=self.larg_bd_frames)
        self.frame_diag.place(relx=0.302, rely=0, relwidth=0.698, relheight=1)

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
        lbl_func.place(relx=0.34, rely=self.rely_lbl_func_trans, anchor='sw')

        lar_frame_tab = self.lrel_cel_tab*(len(self.lista_alfa) + 1)
        alt_frame_tab = self.lrel_cel_tab*(self.num_ests + 1)*self.alt_pixels_jan/self.lar_pixels_jan

        frame_tab = Frame(self.frame_input_2, bg=self.cor_frames, highlightbackground=self.cor_bd_tab, highlightthickness=self.larg_bd_tab)
        frame_tab.place(relx=(1-self.lrel_cel_tab*(len(self.lista_alfa) + 1))/2, rely=self.rely_lbl_func_trans + self.marg_gadget_lbl, relwidth=lar_frame_tab, relheight=alt_frame_tab, anchor='nw')

        lbl_cadeia = Label(self.frame_input_2, text="Cadeia de caracteres", bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_labels, 'bold'))
        lbl_cadeia.place(relx=0.03, rely=0.9)

        self.entry_var3 = tk.StringVar()
        self.entry_var3.trace_add("write", self.Ler_cadeia)
        
        self.entry_cadeia = Entry(self.frame_input_2, textvariable=self.entry_var3, font=(self.font_entries, self.tam_font_entries))
        self.entry_cadeia.place(relx=0.4, rely=0.904, relwidth=0.25, relheight=0.03)

        lar_pixels_canva_cm = self.lar_pixels_jan*0.297 #Largura do canva em pixels
        alt_pixels_canva_cm = self.alt_pixels_jan*0.24 #Altura do canva em pixels

        self.canva_cm = Canvas(self.frame_input_2, width = lar_pixels_canva_cm, height = alt_pixels_canva_cm, bg=self.cor_frames, highlightthickness = 0) #Canva dos círculos de marcação

        lbl_ests_aceit = Label(self.canva_cm, text="Estados de aceitação", bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_labels, 'bold')) #Label estados de aceitação
        lbl_est_inicial = Label(self.canva_cm, text="Estado inicial", bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_labels, 'bold')) #Label estado inicial
        
        self.canva_cm.place(relx = 0.0, rely = alt_frame_tab + self.marg_canva_tabela) #Posicionando o canva dos círculos de marcação na janela

        lbl_est_final = Label(self.canva_cm, text="q" + str(self.num_ests-1), bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_labels, 'bold')) #Criando a label do estado final para obter o seu tamanho em pixels 
        
        self.marg_gadget_lbl_pixels = self.marg_gadget_lbl*self.alt_pixels_jan #Margem entre os gadgets e os títulos
        self.diam_pixels_cm = self.diam_cm*self.alt_pixels_jan #diâmetro dos círculos de marcação em pixels

        marg_cm_bd = (lar_pixels_canva_cm - self.diam_pixels_cm)/(2*self.num_ests) #Margem em pixels dos círculos de marcação extremos em relação à borda do canva
        marg_cm = (lar_pixels_canva_cm - self.num_ests*self.diam_pixels_cm - 2*marg_cm_bd - self.marg_lbl_cm - lbl_est_final.winfo_reqwidth())/(self.num_ests-int(self.num_ests>1)) #Margem entre os círculos de marcação

        lbl_ests_aceit.place(relx = marg_cm_bd*self.num_ests/(self.limit_est*lar_pixels_canva_cm), rely = 0.15, anchor='sw') #Posicionando label dos estados de aceitação no canva
        lbl_est_inicial.place(relx = marg_cm_bd*self.num_ests/(self.limit_est*lar_pixels_canva_cm), rely = self.rely_lbl_est_inicial, anchor='sw') #Posicionando label do estado inicial no canva

        self.coords_cm = [[],[]] #Inicializando lista das coordenadas dos círculos de marcação
        self.val_logico_cm = [[],[]] #Inicializando lista de valor lógico dos círculos de marcação
        self.tab_str_var = []
        self.tab_entry = []
        self.lista_ests = []

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
                    self.lista_ests.append('q'+str(i-1))

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

                x_esq_1, y_esq_1 = int(marg_cm_bd + (i-1)*(self.diam_pixels_cm + marg_cm)), int(0.15*alt_pixels_canva_cm + self.marg_gadget_lbl_pixels) #coordenadas em pixels do ponto esquerdo superior do círculo de marcação do estado qi (estados de aceitação)
                x_dir_1, y_dir_1 = int(x_esq_1 + self.diam_pixels_cm), int(y_esq_1 + self.diam_pixels_cm) #coordenadas em pixels do ponto direito inferior do círculo de marcação do estado qi (estados de aceitação)

                x_esq_2, y_esq_2 = int(x_esq_1), int(self.rely_lbl_est_inicial*alt_pixels_canva_cm + self.marg_gadget_lbl_pixels) #coordenadas em pixels do ponto esquerdo superior do círculo de marcação do estado qi (estado inicial)
                x_dir_2, y_dir_2 = int(x_esq_2 + self.diam_pixels_cm), int(y_esq_2 + self.diam_pixels_cm) #coordenadas em pixels do ponto direito inferior do círculo de marcação do estado qi (estado inicial)
                    
                lbl_est_1 = Label(self.canva_cm, text="q" + str(i-1), bd=0, bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_labels, 'bold')) #Label do estado qi
                lbl_est_2 = Label(self.canva_cm, text="q" + str(i-1), bd=0, bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_labels, 'bold')) #Label do estado qi

                lbl_est_1.place(relx=x_dir_1/lar_pixels_canva_cm + self.marg_lbl_cm, rely = (y_esq_1 + y_dir_1)/(2*alt_pixels_canva_cm), anchor="w") #Posicionando label do estado qi ao lado direito do respectivo círculo de marcação
                lbl_est_2.place(relx=x_dir_2/lar_pixels_canva_cm + self.marg_lbl_cm, rely = (y_esq_2 + y_dir_2)/(2*alt_pixels_canva_cm), anchor="w") #Posicionando label do estado qi ao lado direito do respectivo círculo de marcação
                
                self.coords_cm[0].append((x_esq_1, y_esq_1, x_dir_1, y_dir_1)) #Guardando as coordenadas do círculo de marcação do estado qi (estados de aceitação)
                self.coords_cm[1].append((x_esq_2, y_esq_2, x_dir_2, y_dir_2)) #Guardando as coordenadas do círculo de marcação do estado qi (estado inicial)
                self.val_logico_cm[0].append(False) #Inicializando o valor lógico dos circulos de marcação (estados de aceitação)
                self.val_logico_cm[1].append(False) #Inicializando o valor lógico dos circulos de marcação (estado inicial)

        self.canva_cm.bind("<Button-1>", self.SelecionarCB) #Ação de seleção do círculo de marcação

        self.Marcar_Desmarcar_Cm()

        button_input = Button(self.frame_input_2, text="Processar")
        button_input.place(relx=0.7, rely=0.900, relwidth=0.25)

    def Ler_input_1(self,*args):

        for widget in self.frame_input_2.winfo_children(): widget.destroy()
        
        self.alfa = self.entry_alfa.get() #Pegando os símbolos inseridos pelo usuário
        self.num_ests = self.entry_var2.get() #Pegando o número de estados inserido pelo usuário

        self.alfa = self.alfa.replace(' ','') #removendo os espaços vazios

        #Contando as vírgulas no final da string dos sínbolos

        if self.alfa!='':

            num_virg_final = 0

            while self.alfa!='' and self.alfa[-1]==',':

                num_virg_final+=1
                self.alfa = self.alfa[0:-1]

        else: num_virg_final=0

        list_pos_virg = [a[0] for a in enumerate(self.alfa) if a[1]==','] #Guardando a posição das vírgulas que separam os símbolos

        #Construindo a lista dos símbolos do alfabeto

        if len(list_pos_virg)>0: self.lista_alfa = [self.alfa[0:list_pos_virg[0]]] + [self.alfa[list_pos_virg[i]+1:list_pos_virg[i+1]] for i in range(len(list_pos_virg)-1)] + [self.alfa[list_pos_virg[-1]+1:len(self.alfa)]]
        else: self.lista_alfa = [self.alfa]

        #Tratamento de erros

        try:

            #Se os símbolos inseridos pelo usuário forem distintos e um número inteiro maior que zero for dado, a tabela da função de transição é construída

            if self.alfa!='' and len(self.lista_alfa)==len(set(self.lista_alfa)) and ((len(self.lista_alfa)==self.limit_num_simbs and num_virg_final==0) or (len(self.lista_alfa)<self.limit_num_simbs and num_virg_final<2)) and (self.num_ests.isdigit()==True and (int(self.num_ests)>0 and int(self.num_ests)<=self.limit_est)): 
                
                self.num_ests = int(self.num_ests)
                self.Widgets_Input_2()
                self.Auto_preencher_tab()
                
            #Caso contrário, o programa acusará os seguintes erros

            else:

                #ERRO 1: símbolos repetidos

                if num_virg_final==1 and len(self.lista_alfa)!=len(set(self.lista_alfa)): 
                    
                    self.entry_alfa.delete(len(self.alfa)-1, tk.END)

                    raise ValueError("o alfabeto do autômato não deve conter símbolos repetidos!")
                
                #ERRO 2: vírgula como símbolo do alfabeto

                if (self.alfa=='' and num_virg_final==1) or (self.alfa!='' and num_virg_final==2):

                    if self.alfa=='': self.entry_alfa.delete(0, tk.END)
                    else:

                        self.entry_alfa.delete(len(self.alfa)+1, tk.END)
                        self.Ler_input_1()

                    raise ValueError("vírgula não pode ser um símbolo do alfabeto! Ela deve ser usada somente para separar os símbolos")

                #ERRO 3: número de símbolos acima do limite pré-definido

                if num_virg_final==1 and len(self.lista_alfa)>=self.limit_num_simbs:

                    self.entry_alfa.delete(len(self.alfa), tk.END)
                    self.Ler_input_1()

                    raise ValueError("O número de símbolos de alfabeto deve ser menor ou igual a " + str(self.limit_num_simbs) + "!")

                #ERRO 4: a entrada para o número de estados não é um número inteiro positivo menor ou igual ao limite pré-definido

                if (self.num_ests!='' and self.num_ests.isdigit()==False) or (self.num_ests.isdigit()==True and (int(self.num_ests)<1 or int(self.num_ests)>self.limit_est)): 
                    
                    self.entry_num_ests.delete(0, tk.END)

                    raise ValueError("o número de estados do autômato deve ser um inteiro positivo menor ou igual a " + str(self.limit_est) + "!")

        except ValueError as ve: messagebox.showerror("Erro", f"Entrada incorreta: {ve}") #Exibe o alerta de erro na tela

    def Ler_cadeia(self,*args):

        self.cadeia = self.entry_var3.get()

    def Ler_tabela(self,*args):

        self.tab_val_func = []

        for i in range(len(self.tab_str_var)):

            lin_val_func = []

            for j in range(len(self.tab_str_var[i])):

                val_func = self.tab_str_var[i][j].get()

                #Tratamento de erros

                try:

                    #Se não há dado inserido na célula, a string vazia é guardada

                    if val_func=='' or val_func in self.lista_ests: lin_val_func.append(val_func)

                    else: 

                        lin_val_func.append('')

                        #Erro 2: se o dado inserido não for a letra q seguida de um número

                        if val_func[0]!='q' or (len(val_func)>1 and not val_func[1:].isdigit()): 

                            self.tab_entry[i][j].delete(0, tk.END)

                            raise ValueError("os estados devem ser compostos pela letra ""q"" seguida de um número!")
                        
                        #Erro 3: se o dado corresponder a um estado inexistente

                        if len(val_func)>1 and val_func[1:len(val_func)].isdigit() and int(val_func[1:])>=self.num_ests: 

                            self.tab_entry[i][j].delete(0, tk.END)

                            raise ValueError("estado não existente! Os estados são de " + self.lista_ests[0] + " até " + self.lista_ests[-1])
                
                except ValueError as ve: messagebox.showerror("Erro", f"Entrada incorreta: {ve}") #Exibe o alerta de erro na tela

            self.tab_val_func.append(lin_val_func)

        self.tab_val_func_ant = self.tab_val_func.copy()

        if '' in chain(*self.tab_val_func): self.Diagrama()
        else: 
            
            est_conect = self.Ler_Tabela_2()

            try:

                if len(est_conect)==self.num_ests: self.Diagrama()
                else:
                    
                    for i in range(self.num_ests):
                        for j in range(len(self.lista_alfa)): self.tab_entry[i][j].delete(0,tk.END)

                    self.canva_diagrama.delete("all")

                    raise ValueError("os estados devem estar num único grafo!")

            except ValueError as ve: messagebox.showerror("Erro", f"Entrada incorreta: {ve}") #Exibe o alerta de erro na tela

    def Ler_Tabela_2(self):

        grupo_ests_lig = self.Map_est(self.lista_ests[0])['fonte'] + self.Map_est(self.lista_ests[0])['alvo']
        grupos_nlig = []

        for est in self.lista_ests[1:]:

            ests_lig = self.Map_est(est)['fonte'] + self.Map_est(est)['alvo']
            lista_grupos_nlig = list(chain(*grupos_nlig))

            if est in grupo_ests_lig and Counter(lista_grupos_nlig)[est]==len(grupos_nlig): grupo_ests_lig = grupo_ests_lig + lista_grupos_nlig + ests_lig
            else: 
                
                if est in lista_grupos_nlig: grupos_nlig = [lista if est not in lista else lista + ests_lig for lista in grupos_nlig]
                else: grupos_nlig.append(ests_lig)

        return sorted(list(set(grupo_ests_lig)))
    
    def Ciclos(self): 

        list_comb_ests = []
        lista_ciclos = []

        for i in range(3, self.num_ests+1):

            lista_pos_est = [pos for pos in range(0,i)]
            list_comb_ests.append([self.lista_ests[pos] for pos in lista_pos_est])
            j=-1

            while lista_pos_est[0]<self.num_ests-i:

                if lista_pos_est[j]<self.num_ests+j: 
                    
                    lista_pos_est[j] = lista_pos_est[j]+1

                    if j<-1: 
                        
                        lista_pos_est[j+1] = lista_pos_est[j]+1
                        j+=1

                    list_comb_ests.append([self.lista_ests[pos] for pos in lista_pos_est])

                else:
 
                    if j>-self.num_ests: j-=1

        for comb_ests in list_comb_ests:

            list_grupo_ests_lig = []

            for est in comb_ests: 
                
                grupo_ests_lig = self.Map_est(est)['fonte'] + self.Map_est(est)['alvo']

                if est in grupo_ests_lig: grupo_ests_lig.remove(est)

                list_grupo_ests_lig = list_grupo_ests_lig + grupo_ests_lig

            if any(Counter(list_grupo_ests_lig)[est]<2 for est in comb_ests): lista_ciclos = lista_ciclos + []
            else: lista_ciclos = lista_ciclos + [comb_ests]

        return lista_ciclos

    def Auto_preencher_tab(self):

        tab_val_func_ant = self.tab_val_func_ant.copy()

        for i in range(len(self.tab_entry)):

            for j in range(len(self.tab_entry[i])):

                if i<len(tab_val_func_ant) and j<len(tab_val_func_ant[i]) and tab_val_func_ant[i][j] in self.lista_ests: self.tab_entry[i][j].insert(0, tab_val_func_ant[i][j])
                else: self.tab_entry[i][j].insert(0, '')

    def SelecionarCB(self, evento): #Essa função permite que a seleção do círculo seja feita com o mouse

            x, y = evento.x, evento.y #capturando as coordenadas do botão esquerdo do mouse ao ser pressionado

            #SELEÇÃO DOS ESTADOS DE ACEITAÇÃO 

            for i, (x0, y0, x1, y1) in enumerate(self.coords_cm[0]): 

                if x0 <= x <= x1 and y0 <= y <= y1: #se as coordenadas do botão esquerdo do mouse estiver sobre o círculo de marcação do estado qi
                
                    if self.val_logico_cm[0][i] == False: #e se o valor lógico dele for falso

                        self.val_logico_cm[0][i] = True #ele muda para verdadeiro
                        self.Marcar_Desmarcar_Cm() #e a marcação no interior do checkbox aparece

                    else: self.val_logico_cm[0][i] = False ##se o valor lógico for verdadeiro ele muda para falso

                    self.Marcar_Desmarcar_Cm() #chamando a função para marcar/desmarcar o círculo

            #SELEÇÃO DO ESTADO INICIAL

            for i, (x0, y0, x1, y1) in enumerate(self.coords_cm[1]): 

                if x0 <= x <= x1 and y0 <= y <= y1: #se as coordenadas do botão esquerdo do mouse estiver sobre o círculo de marcação do estado qi

                    if self.val_logico_cm[1][i] == False: #e se o valor lógico dele for falso

                        self.val_logico_cm[1] = self.num_ests*[False] #todos os círculos de marcação são colocados em falso
                        self.val_logico_cm[1][i] = True #e o circulo de marcação do estado qi é alterado para verdadeiro

                    else: self.val_logico_cm[1][i] = False ##se o valor lógico for verdadeiro ele muda para falso

                    self.Marcar_Desmarcar_Cm() #chamando a função para marcar/desmarcar o círculo

    def Marcar_Desmarcar_Cm(self): #Essa função cria/deleta a marcação no interior do círculo quando ele é selecionado

        self.canva_cm.delete("all") #limpando o canva dos círculos de marcação

        self.coords_cm_2 = self.coords_cm[0] + self.coords_cm[1]
        self.val_logico_cm_2 = self.val_logico_cm[0] + self.val_logico_cm[1]

        for i, (valor_logico, (x0, y0, x1, y1)) in enumerate(zip(self.val_logico_cm_2, self.coords_cm_2)):

            self.canva_cm.create_oval(x0, y0, x1, y1, outline="black", width=0.5, fill="white" if valor_logico else "white") #Criando o círculo dos checkboxes

            if valor_logico: #se o valor lógico de um círculo for TRUE,

                #as coordenadas do centro do círculo são calculadas

                centro_cb_x = (x0 + x1) / 2 
                centro_cb_y = (y0 + y1) / 2
                espaçamento = 5.49

                self.canva_cm.create_oval(centro_cb_x - espaçamento, centro_cb_y - espaçamento, centro_cb_x + espaçamento, centro_cb_y + espaçamento, outline="black", width=0, fill="black") #e o círculo interno é criado com uma margem especificada

    def Map_est(self, est):

        est_font = []

        for i in range(len(self.tab_val_func)):

            if i==self.lista_ests.index(est): est_alvo = sorted(list(set([j for j in self.tab_val_func[i] if j!=''])))
            else: 
                
                if est in self.tab_val_func[i]: est_font = list(set(est_font + [self.lista_ests[i]]))

        return {'fonte': est_font, 'alvo': est_alvo}

    def Diagrama(self):
        
        lar_pixels_cv_diag = self.lar_pixels_jan*0.703 #Largura do canva do diagrama em pixels
        alt_pixels_cv_diag = self.alt_pixels_jan #Altura do canva do diagrama em pixels

        self.canva_diagrama = Canvas(self.frame_diag, width=lar_pixels_cv_diag, height=alt_pixels_cv_diag, bg=self.cor_frames, highlightthickness=0)
        self.canva_diagrama.place(relx=0, rely=0)

        ciclos = {}
        lista_ciclos_max = []
        i=0

        for ciclo in self.Ciclos():

            if len(ciclo) in list(ciclos.keys()): ciclos[len(ciclo)].append(ciclo)
            else: ciclos.update({len(ciclo): [ciclo]})

        print(f"\n inicial {ciclos} : ")

        while ciclos:

            lista_num_ests = list(ciclos.keys())
            max_num_ests = max(lista_num_ests)

            if ciclos[max_num_ests]: 
                
                ciclo_max = ciclos[max_num_ests].pop(-1)
                lista_ciclos_max.append(ciclo_max)

                for num_ests in lista_num_ests:

                    for ciclo in ciclos[num_ests]:

                        if list(set(ciclo + ciclo_max))==ciclo_max: 
                            
                            if ciclos[num_ests]: ciclos[num_ests].remove(ciclo)
                            else: del(ciclos[num_ests])

            else: del(ciclos[max_num_ests])

        print(f"{lista_ciclos_max}")

        for ciclo_max in self.Ciclos():

            x_cent_ciclo, y_cent_ciclo = lar_pixels_cv_diag/2, alt_pixels_cv_diag/2 #Coordenadas do centro do ciclo
            dist_cent_ciclo_est = 100 #Distância padrão em pixels entre os centros do ciclo e dos estados

            for i in range(len(ciclo_max)):

                x_est_1 = int(x_cent_ciclo + dist_cent_ciclo_est*math.cos(math.pi/2*(4*i/len(ciclo_max) - 1)) - self.diam_circ_est_ext/2)
                y_est_1 = int(y_cent_ciclo + dist_cent_ciclo_est*math.sin(math.pi/2*(4*i/len(ciclo_max) - 1)) - self.diam_circ_est_ext/2)

                x_est_2 = int(x_est_1 + self.diam_circ_est_ext)
                y_est_2 = int(y_est_1 + self.diam_circ_est_ext)

                centro_x_est = (x_est_1 + x_est_2)/2
                centro_y_est = (y_est_1 + y_est_2)/2

                self.canva_diagrama.create_oval(x_est_1, y_est_1, x_est_2, y_est_2, outline=self.cor_circ_est, width=4, fill=self.cor_frames)
                self.canva_diagrama.create_oval(centro_x_est - self.diam_circ_est_int, centro_y_est - self.diam_circ_est_int, centro_x_est + self.diam_circ_est_int, centro_y_est + self.diam_circ_est_int, outline=self.cor_circ_est, width=4, fill=self.cor_frames)

                lbl_est_circ = Label(self.canva_diagrama, text=ciclo_max[i], bd=0, bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_lbl_est_circ, 'bold'))
                lbl_est_circ.place(relx=centro_x_est/lar_pixels_cv_diag, rely = centro_y_est/alt_pixels_cv_diag, anchor='center')

interface = Interface().Widgets_Input_1()