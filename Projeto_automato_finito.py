#PROJETO AUTÔMATO FINITO

from tkinter import *

class Interface:

    def __init__(self, interface):
        
        self.interface = interface
        self.janela = Tk()

    def ConfigInterface(self):

        fator_tela = 0.898 #Porcentagem visível da altura da tela (sem a barra de tarefas do Windows)

        self.lar_tela_pxls = self.janela.winfo_screenwidth() #Largura da tela em pixels
        self.alt_tela_pxls = self.janela.winfo_screenheight() #Altura da tela em pixels

        self.lar_jan_pxls = int(self.lar_tela_pxls) #Largura da janela em pixels
        self.alt_jan_pxls = int(fator_tela*self.alt_tela_pxls) #Altura da janela em pixels

        self.janela.title("Autômato finito")
        self.janela.configure(background = 'black')
        self.janela.geometry(str(self.lar_jan_pxls) + "x" + str(self.alt_jan_pxls))
        self.janela.resizable(False, False)

        self.lar_jan_pxls = int(self.lar_tela_pxls) #Largura da janela em pixels
        self.alt_jan_pxls = int(fator_tela*self.alt_tela_pxls) #Altura da janela em pixels

        ajust_hor_tela = -int(self.alt_tela_pxls) // 90

        self.janela.geometry("+{}+{}".format(ajust_hor_tela, 0))

        self.cor_ctrle_frames = '#424242'
        self.cor_borda_frames = '#1c1e3d'
        self.larg_borda_frames = 1.0
        self.marg_frames_x = 0.01 #Margem horizontal do frames
        self.marg_frames_y = 0.01 #Margem dos frames superior e inferior em relação à borda
        self.alt_frame_input = 0.060 #Altura do frame dos inputs

    def Widgets(self):

        self.ConfigInterface()

        frame_input = Frame(self.janela, bd=4, bg=self.cor_ctrle_frames, highlightbackground=self.cor_borda_frames, highlightthickness=self.larg_borda_frames)
        frame_input.place(relx = self.marg_frames_x, rely = self.marg_frames_y, relwidth = 1 - 2*self.marg_frames_x, relheight = self.alt_frame_input)

        self.janela.mainloop() 

interface = Interface('USUARIO').Widgets()