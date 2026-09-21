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
            if "." in self.auxiliar[-1]:
                pass
            elif "." in self.auxiliar:
                indices = []
                for e in ["+","-","*","/"]:
                    indice = int(self.auxiliar.rfind(e))
                    indices.append(indice)
                maximo = max(indices)
                texto_max = self.auxiliar[maximo:-1]
                texto_min = self.auxiliar[:]
                if "." not in texto_min:
                    self.auxiliar += chars
                    self.entrada_var.set(self.auxiliar)
                    print("primero")
                elif "." not in texto_max and texto_max:
                    self.auxiliar += chars
                    self.entrada_var.set(self.auxiliar)
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
            self.auxiliar = ""
        except ZeroDivisionError:
            self.entrada_var.set("Numero indefinido")
            self.auxiliar = ""
    
    def borrar(self):
        self.entrada_var.set("")
        self.auxiliar = ""
        

    
    def entrada_de_calculadora(self):
        frame_entrada = tk.Frame(self)
        frame_entrada.grid(row=0,column=0,sticky="nsew")
        entrada = tk.Entry(frame_entrada,textvariable=self.entrada_var,bg="sienna2",relief="flat",bd=0)
        entrada.grid(column=0,row=0,sticky="wesn")
        
    
    def botones_numerales(self,event=None):
        
        frame_botones = tk.Frame(self,bg="gray26")
        frame_botones.grid(row=4,column=0,sticky="we",padx=2,pady=2)
        botones = [("7",0,0),("8",0,1),("9",0,2),
                   ("4",1,0),("5",1,1),("6",1,2),
                   ("1",2,0),("2",2,1),("3",2,2),
                   (".",3,0),("0",3,1),("=",3,2)]
        for t,r,c in botones:
            if t == "=":
                boton_de_la_calculadora = tk.Button(frame_botones,text=t,
                                                    bg="DarkOrange4",
                                                    relief="flat",bd=0,font=("Arial",15),
                                                    fg="CadetBlue1",command=lambda :self.resultado())
            else:
                boton_de_la_calculadora = tk.Button(frame_botones,text=t,bg="DarkOrange3",
                                                    relief="flat",bd=0,font=("Arial",15),
                                                    fg="CadetBlue1",command=lambda e=t:self.mostrar_numeros(e))
            boton_de_la_calculadora.grid(row=r,column=c,padx=10,pady=5)
        botones_especiales = [("+",0,3),("-",1,3),("*",2,3),("/",0,4),("CE",3,3)]
        for t,r,c in botones_especiales:
            if t == "CE":
                botones_especiales_calcu = tk.Button(frame_botones,text=t,
                                                 bg="DarkOrange4",
                                                 relief="flat",bd=0,font=("Arial",15),
                                                 fg="CadetBlue1",command=self.borrar)
            else:
                botones_especiales_calcu = tk.Button(frame_botones,text=t,
                                                                 bg="DarkOrange4",
                                                                 relief="flat",bd=0,font=("Arial",15),
                                                                 fg="CadetBlue1",command=lambda e=t:self.mostrar_numeros(e))
            botones_especiales_calcu.grid(row=r,column=c,padx=5,pady=5)
    
    

ventana = Interfaz()
