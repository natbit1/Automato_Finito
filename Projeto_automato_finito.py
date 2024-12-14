#PROJETO AUTÔMATO FINITO

from tkinter import *
import tkinter as tk

class Interface:

    def __init__(self, interface):
        
        self.interface = interface
        self.janela = Tk()

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

        #Frame do input

        self.frame_input_1 = Frame(self.janela, bg=self.cor_frames, highlightbackground=self.cor_bd_frames, highlightthickness=self.larg_bd_frames)
        self.frame_input_1.place(relx=0, rely=0, relwidth=0.3, relheight=0.07)

        self.frame_input_2 = Frame(self.janela, bg=self.cor_frames, highlightbackground=self.cor_bd_frames, highlightthickness=self.larg_bd_frames)
        self.frame_input_2.place(relx=0, rely=0.072, relwidth=0.3, relheight=0.928)

        frame_diag = Frame(self.janela, bg=self.cor_frames, highlightbackground=self.cor_bd_frames, highlightthickness=self.larg_bd_frames)
        frame_diag.place(relx=0.302, rely=0, relwidth=0.698, relheight=1)

        #Entradas de dados

        entry_var1 = tk.StringVar()
        entry_var1.trace_add("write", self.Input1)

        self.entry_alfa = Entry(self.frame_input_1, textvariable=entry_var1, font=(self.font_entries, self.tam_font_entries))
        self.entry_alfa.place(relx=0.2, rely=0.25, relwidth=0.27, relheight=0.5)

        entry_var2 = tk.StringVar()
        entry_var2.trace_add("write", self.Input2)

        self.entry_num_ests = Entry(self.frame_input_1, textvariable=entry_var2, font=(self.font_entries, self.tam_font_entries))
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
        frame_tab.place(relx=(1-self.lrel_cel_tab*(self.num_ests + 1))/2, rely=0.09, relwidth=self.lrel_cel_tab*(self.num_ests + 1), relheight=alt_frame_tab)

        self.frame_input_2_ant = self.frame_input_2

        for i in range(self.num_ests+1):

            frame_tab.rowconfigure(i, weight=1)

            for j in range(self.num_ests+1):

                frame_tab.columnconfigure(j, weight=1) 
                    
                if i==0 and j>0: 

                    lbl_func = Label(frame_tab, text='q'+ str(j-1), bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_lbl_tab, 'bold'))
                    lbl_func.grid(row=i, column=j, sticky=NSEW)

                elif i>0 and j==0:
            
                    lbl_func = Label(frame_tab, text='q'+ str(i-1), bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_lbl_tab, 'bold'))
                    lbl_func.grid(row=i, column=j, sticky=NSEW)

                elif i==0 and j==0:

                    frame_space = Label(frame_tab, text="", bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_lbl_tab, 'bold'))
                    frame_space.grid(row=i, column=j, sticky=NSEW)

                else:

                    self.entry_func = Entry(frame_tab, width=0, font=(self.font_entries, self.tam_font_entries))
                    self.entry_func.grid(row=i, column=j, sticky=NSEW, padx=0.5, pady=0.5)

        rely_lbl_ests_aceit = alt_frame_tab + 0.13

        lbl_ests_aceit = Label(self.frame_input_2, text="Selecionar estados de aceitação", bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_labels, 'bold'))
        lbl_ests_aceit.place(relx=0.04, rely=rely_lbl_ests_aceit)

        lbl_ests_aceit = Label(self.frame_input_2, text="Selecionar estado inicial", bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_labels, 'bold'))
        lbl_ests_aceit.place(relx=0.04, rely=rely_lbl_ests_aceit+0.1)

        lbl_cadeia = Label(self.frame_input_2, text="Cadeia de caracteres", bg=self.cor_frames, fg=self.cor_labels, font=(self.font_labels, self.tam_labels, 'bold'))
        lbl_cadeia.place(relx=0.03, rely=0.9)

        entry_var3 = tk.StringVar()
        entry_var3.trace_add("write", self.Input3)
        
        self.entry_cadeia = Entry(self.frame_input_2, textvariable=entry_var3, font=(self.font_entries, self.tam_font_entries))
        self.entry_cadeia.place(relx=0.4, rely=0.904, relwidth=0.25, relheight=0.03)

        rely_cb_est = rely_lbl_ests_aceit+0.065
        marg_cb_frame = 0.85/self.num_ests
        marg_rel_cb = (1 - 2*marg_cb_frame)/(self.num_ests-1)

        for i in range(self.num_ests):

            cb_est_1 = Checkbutton(self.frame_input_2, text='q'+str(i), bg=self.cor_frames, fg='white', selectcolor="black")
            cb_est_1.place(relx=marg_cb_frame + i*marg_rel_cb, rely=rely_cb_est, anchor=CENTER)

            marg_cb_est_2 = rely_cb_est+0.1

            cb_est_2 = Checkbutton(self.frame_input_2, text='q'+str(i), bg=self.cor_frames, fg='white', selectcolor="black")
            cb_est_2.place(relx=marg_cb_frame + i*marg_rel_cb, rely=marg_cb_est_2, anchor=CENTER)

        button_input = Button(self.frame_input_2, text="Gerar autômato")
        button_input.place(relx=0.375, rely=marg_cb_est_2 + 0.06, relwidth=0.25)

        button_input = Button(self.frame_input_2, text="Processar")
        button_input.place(relx=0.7, rely=0.900, relwidth=0.25)

    def Input1(self,*args):

        self.alfa = self.entry_alfa.get()

        print(self.alfa)

    def Input2(self,*args):

        for widget in self.frame_input_2.winfo_children(): widget.destroy()

        self.num_ests = self.entry_num_ests.get()

        if self.num_ests!='': 
            
            self.num_ests = int(self.num_ests)
            self.Widgets_Input_2()

    def Input3(self,*args):

        self.var = self.entry_func.get()

        print(self.var)        

interface = Interface('USUARIO').Widgets_Input_1()