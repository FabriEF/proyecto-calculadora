import tkinter as tk

class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("450x650+700+200")
        self.attributes("-alpha",0.95)
        self.config(bg="black")
        self.iconbitmap("icono_calculadora.ico")
        self.entrada_var = tk.StringVar()
        self.auxiliar = ""
        self.entrada_de_calculadora()
        self.botones_numerales()
        self.botones_especiales()
        self.mainloop()
    
    def mostrar_numeros(self,chars):
        if chars in ["+","-","*","/"]:
            try:
                if self.auxiliar[-1] == chars:
                    pass
                else:
                    self.auxiliar += chars
                    self.entrada_var.set(self.auxiliar)
            except IndexError:
                pass
        elif chars == ".":
            if "." in self.auxiliar:
                pass
            else:
                self.auxiliar += chars
                self.entrada_var.set(self.auxiliar)
        else:
            self.auxiliar += chars
            self.entrada_var.set(self.auxiliar)
    
    def resultado(self):
        try:
            resultado = eval(self.auxiliar)
            self.entrada_var.set(resultado)
            self.auxiliar = ""
        except SyntaxError:
            self.entrada_var.set("")
        except ZeroDivisionError:
            self.entrada_var.set("Numero indefinido")
            self.auxiliar = ""
    
    def borrar(self):
        self.entrada_var.set("")
        self.auxiliar = ""
        

    
    def entrada_de_calculadora(self):
        entrada = tk.Entry(self,textvariable=self.entrada_var,bg="sienna2",relief="flat",bd=0)
        entrada.grid(column=0,row=0,pady=5,padx=3,rowspan=3,columnspan=3,sticky="wesn")
        
    
    def botones_numerales(self,event=None):
        frame_botones = tk.Frame(self,bg="gray26")
        frame_botones.grid(row=4,column=0,sticky="we")
        botones = [("7",0,0),("8",0,1),("9",0,2),
                   ("4",1,0),("5",1,1),("6",1,2),
                   ("1",2,0),("2",2,1),("3",2,2)]
        for t,r,c in botones:
            botono_de_la_calculadora = tk.Button(frame_botones,text=t,bg="DarkOrange3",
                                                 relief="flat",bd=0,font=("Arial",15),
                                                 fg="CadetBlue1",command=lambda e=t:self.mostrar_numeros(e))
            botono_de_la_calculadora.grid(row=r,column=c,padx=10,pady=5)
    
    def botones_especiales(self,event=None):
        frame_botones_especiales_laterales = tk.Frame(self,bg="gray26")
        frame_botones_especiales_laterales.grid(row=4,column=99,sticky="we",padx=5,pady=5)
        frame_botones_especiales_inferiores = tk.Frame(self,bg="gray26")
        frame_botones_especiales_inferiores.grid(row=5,column=0,sticky="ew")
        botones_especiales = [("+",0,0),("-",1,0),("*",2,0),("/",0,1),("CE",1,1)]
        botones_inferiores = [(".",0,0),("0",0,1),("=",0,2)]
        for t,r,c in botones_especiales:
            if t == "CE":
                botones_especiales_calcu = tk.Button(frame_botones_especiales_laterales,text=t,
                                                 bg="DarkOrange4",
                                                 relief="flat",bd=0,font=("Arial",15),
                                                 fg="CadetBlue1",command=self.borrar)
            else:
                botones_especiales_calcu = tk.Button(frame_botones_especiales_laterales,text=t,
                                                                 bg="DarkOrange4",
                                                                 relief="flat",bd=0,font=("Arial",15),
                                                                 fg="CadetBlue1",command=lambda e=t:self.mostrar_numeros(e))
            botones_especiales_calcu.grid(row=r,column=c,padx=5,pady=5)
        for t,r,c in botones_inferiores:
            if t == "=":
                botones_inferiores_calcu = tk.Button(frame_botones_especiales_inferiores,text=t,
                                                 bg="DarkOrange4",
                                                 relief="flat",bd=0,font=("Arial",15),
                                                 fg="CadetBlue1",command=lambda :self.resultado())
            else:
                botones_inferiores_calcu = tk.Button(frame_botones_especiales_inferiores,text=t,
                                                                 bg="DarkOrange4",
                                                                 relief="flat",bd=0,font=("Arial",15),
                                                                 fg="CadetBlue1",command=lambda e=t:self.mostrar_numeros(e))
            botones_inferiores_calcu.grid(row=r,column=c,padx=10,pady=5)
    
    

ventana = Interfaz()
