class ValidacionesYLogica():
    def validacion_punto(self,chars,caracteres,texto_auxiliar):
        indices = []
        for e in caracteres:
            indice = int(texto_auxiliar.rfind(e))
            if indice != -1:
                indices.append(indice)
        if indices:
            maximo = max(indices)
            texto_max = texto_auxiliar[maximo:]
            contar_caracteres_despues_del_signo = len(texto_max)
            if contar_caracteres_despues_del_signo >= 2 and "." not in texto_max:
                texto_auxiliar += chars
                return texto_auxiliar
            else:
                return texto_auxiliar
        elif "." not in texto_auxiliar:
            texto_auxiliar += chars
            return texto_auxiliar
        else:
            return texto_auxiliar
        
    def mostrar_numeros(self,chars,texto_auxiliar):
        caracteres = ["+","-","*","/"]
        if chars in caracteres:
            if texto_auxiliar:
                if texto_auxiliar[-1] == chars:
                    return texto_auxiliar
                elif texto_auxiliar[-1] in caracteres and chars != texto_auxiliar[-1]:
                    texto_auxiliar = texto_auxiliar[0:-1]
                    texto_auxiliar += chars
                    return texto_auxiliar
                elif texto_auxiliar[-1] != ".":
                    texto_auxiliar += chars
                    return texto_auxiliar
                else:
                    return texto_auxiliar
            elif chars == "-":
                texto_auxiliar += chars
                return texto_auxiliar
            else:
                return texto_auxiliar
        elif chars == ".":
            if texto_auxiliar:
                if "." in texto_auxiliar[-1]:
                    return texto_auxiliar
                elif "." in texto_auxiliar:
                    texto_auxiliar = self.validacion_punto(chars,caracteres,texto_auxiliar)
                    return texto_auxiliar
                else:
                    texto_auxiliar = self.validacion_punto(chars,caracteres,texto_auxiliar)
                    return texto_auxiliar
        elif chars == "()":
            buscar_parentesis_izq = int(texto_auxiliar.rfind("("))
            buscar_parentesis_der = int(texto_auxiliar.rfind(")"))
            if texto_auxiliar:
                if buscar_parentesis_izq == -1:
                    texto_auxiliar += chars[0]
                    return texto_auxiliar
                elif ")" not in texto_auxiliar[buscar_parentesis_izq:]:
                    texto_auxiliar += chars[1]
                    return texto_auxiliar
                elif "(" not in texto_auxiliar[buscar_parentesis_der:]:
                    texto_auxiliar += chars[0]
                    return texto_auxiliar
                else:
                    return texto_auxiliar
            else:
                texto_auxiliar += "-("
                return texto_auxiliar
        else:
            texto_auxiliar += chars
            return texto_auxiliar
    
    def resultado(self,texto_auxiliar):
            try:
                resultado = eval(texto_auxiliar)
                texto_auxiliar = str(resultado)
                return texto_auxiliar
            except SyntaxError:
                texto_auxiliar = ""
                return texto_auxiliar
            except ZeroDivisionError:
                texto_auxiliar = ""
                return texto_auxiliar
        
    def borrar(self,chars,texto_auxiliar):
        if chars == "CE":
            texto_auxiliar = ""
            return texto_auxiliar
        elif chars == "⌫":
            texto_auxiliar = texto_auxiliar[:-1]
            return texto_auxiliar
        else:
            return texto_auxiliar