#PROJETO AUTÔMATO FINITO

from tkinter import *

class Interface:

    def __init__(self, interface):
        
        self.interface = interface
        self.janela = Tk()
        #ghghghghgh

    #def ConfigInterface(self):

    def Widgets(self):

        frame_input = Frame(self.janela, bd=4, bg=self.cor_ctrle_frames, highlightbackground=self.cor_borda_frames, highlightthickness=self.larg_borda_frames)