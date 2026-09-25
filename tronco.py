import tkinter as tk

class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("330x550+700+200")
        self.attributes("-alpha",0.95)
        self.config(bg="black")
        self.iconbitmap("icono_calculadora.ico")
        self.entrada_var = tk.StringVar()
        self.auxiliar = ""
        self.entrada_de_calculadora()
        self.botones_numerales()
        self.mainloop()
    
    def validacion_punto(self,chars,caracteres):
        indices = []
        for e in caracteres:
            indice = int(self.auxiliar.rfind(e))
            if indice != -1:
                indices.append(indice)
        if indices:
            maximo = max(indices)
            texto_max = self.auxiliar[maximo:]
            contar_caracteres_despues_del_signo = len(texto_max)
            if contar_caracteres_despues_del_signo >= 2 and "." not in texto_max:
                self.auxiliar += chars
                self.entrada_var.set(self.auxiliar)
        elif "." not in self.auxiliar:
            self.auxiliar += chars
            self.entrada_var.set(self.auxiliar)
    
    def mostrar_numeros(self,chars):
        caracteres = ["+","-","*","/"]
        if chars in caracteres:
            try:
                print(self.auxiliar[-1])
                if self.auxiliar[-1] == chars:
                    print("A")
                    pass
                elif self.auxiliar[-1] in caracteres and chars != self.auxiliar[-1]:
                    print("B")
                    self.auxiliar = self.auxiliar[0:-1]
                    self.auxiliar += chars
                    self.entrada_var.set(self.auxiliar)
                elif self.auxiliar[-1] != ".":
                    print("C")
                    self.auxiliar += chars
                    self.entrada_var.set(self.auxiliar)
            except IndexError:
                pass
        elif chars == ".":
            if self.auxiliar:
                if "." in self.auxiliar[-1]:
                    pass
                elif "." in self.auxiliar:
                    self.validacion_punto(chars,caracteres)
                else:
                    self.validacion_punto(chars,caracteres)
        else:
            self.auxiliar += chars
            self.entrada_var.set(self.auxiliar)
    
    def resultado(self):
        try:
            resultado = eval(self.auxiliar)
            self.entrada_var.set(resultado)
            self.auxiliar = str(resultado)
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
        entrada = tk.Entry(frame_entrada,textvariable=self.entrada_var,bg="sienna2",relief="flat",bd=0,font=("Arial",25))
        entrada.grid(column=0,row=0,sticky="wesn")
        frame_entrada.columnconfigure(0,weight=1)
        frame_entrada.rowconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        
    
    def botones_numerales(self,event=None):
        
        frame_botones = tk.Frame(self,bg="gray26")
        frame_botones.grid(row=1,column=0,sticky="nswe",padx=2,pady=2)
        self.rowconfigure(1,weight=1)
        self.columnconfigure(0,weight=1)
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
            boton_de_la_calculadora.grid(row=r,column=c,padx=20,pady=20,sticky="nesw")
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
            botones_especiales_calcu.grid(row=r,column=c,padx=20,pady=20,sticky="nesw")
    
    

ventana = Interfaz()
