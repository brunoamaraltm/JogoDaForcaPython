# -*- coding: cp1252 -*-
import random, os

class JogoDaForca:
    def __init__(self):
        self.vidas = 6
        self.dicas = ["Objeto", "Filme", "Animal", "Fruta"]
        self.palavras = {
            "Objeto": ["Tesoura", "Cadeira", "Mochila", "Apontador", "Computador", "Teclado"],
            "Filme": ["Até que a sorte nos separe", "Divergente", "Efeito borboleta", "Vingadores", "Divergente"],
            "Animal": ["Cacatua", "Jacare", "Leao", "Galinha", "Vaca", "Boi", "Borboleta", "Macaco", "Baleia", "Peixe"],
            "Fruta": ["Laranja", "Banana", "Jabuticaba", "Abacaxi", "Damasco", "Figo", "Tamarindo", "Morango", "Limão"]}
        self.categoria = None
        self.palavra   = None
        self.junc = ""

        self.vazio = ""
        self.juntarDps = []
        self.a = []
        self.letrasUsadas = []
        self.sistema()

    def sistema(self):
        self.categoria = random.choice(self.dicas)
        self.palavra   = random.choice(self.palavras[self.categoria])
        for letra in self.palavra:
            if not letra == " ":
                self.vazio += "_ "
        self.forca()
        
    def forca(self):
        print "Dica da palavra: " + self.categoria
        print "\n" + self.vazio + "\n"
        incluirLetra = raw_input("Digite uma letra: ")

        
        if len(incluirLetra) >= 2:
            print "Digite apenas uma letra"
            self.forca()
        elif not incluirLetra.isalpha():
            print "Somente letras sao aceitas"
            self.forca()
        elif incluirLetra in self.letrasUsadas:
            print "Essa letra ja foi usada."
            self.forca()
        else:
            self.letrasUsadas.append(incluirLetra)

        if not incluirLetra.lower() in self.palavra.lower():
            self.vidas -= 1
            os.system("cls")
            if self.vidas <= 0:
                print "Suas vidas acabaram, feche e abra o console para reiniciar o jogo"
                os.system("pause")
            else:
                print "Você perdeu uma vida, tem apenas: " + str(self.vidas)
                self.forca()
        else:

            for letra in self.palavra:
                self.juntarDps.append(letra)
            i = 0
            for letra in self.vazio:
                if not letra == " ":
                    self.a.append(letra)
            #print self.a, i
                       
            for letra in self.juntarDps:
                if letra.lower() == incluirLetra.lower():
                    self.a[i] = incluirLetra
                i+=1
            
            self.vazio = " ".join(self.a)
            self.vazio = self.vazio.capitalize()
            self.a = []
            self.juntarDps = []

            os.system("cls")

            if not "_" in self.vazio:
                print "Voce ganhou o jogo!"
                self.vazio = ""
                self.vidas = 6
                self.juntarDps = []
                self.a = []
                self.letrasUsadas = []
                os.system("pause")
                self.sistema()

            self.forca()
                
            #print self.palavra
            #print " ".join(self.a)
if __name__ == "__main__":
    JogoDaForca().forca()

    
