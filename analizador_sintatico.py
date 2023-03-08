from TokenDaGramatica import token

class AnalizadorSintatico:
     
     
     def __init__(self, lista_tokens, tabela_simbolos):
        self.tabela_simbolos = tabela_simbolos
        self.lista_tokens = lista_tokens
        self.look_ahead = 0

     def match(self, token_esperado):
        if self.lista_tokens[self.look_ahead].nome == token_esperado:
            self.look_ahead += 1
            print ("Token esperado: " + token_esperado + " encontrado: " + self.lista_tokens[self.look_ahead-1].nome + " na linha: " + str(self.lista_tokens[self.look_ahead-1].linha))
        else:
            print("Erro sintático: token esperado: " + token_esperado + " encontrado: " + self.lista_tokens[self.look_ahead].nome + " na linha: " + str(self.lista_tokens[self.look_ahead].linha))
            exit()

     def programa(self):
        self.match("<programa>")
        self.match("<abre_chaves>")
        self.bloco()
        self.match("<fecha_chaves>")

        
     def bloco(self):
        token_atual = self.lista_tokens[self.look_ahead]
        if token_atual.nome == "<tipo>":
            self.declaracao_variavel()
            self.bloco()
        elif token_atual.nome == "<atribuição>":
            self.atribuicao()
            
        elif token_atual.nome == "<declaração de função>":
            self.declaracao_funcao()
            self.bloco()
        elif token_atual.nome == "<laço>":
            self.laço()
            self.bloco()
        elif token_atual.nome == "<chamada do if>":
            self.condicao()
            self.bloco()

        elif token_atual.nome == "<declaração de função>":
            self.chamada_funcao()
            self.bloco()
        elif token_atual.nome == "<chamada de função>":
            self.chamada_funcao()
            self.bloco()
        elif token_atual.nome == "<chamada de impressão>":
            self.chamada_impressao()
            self.bloco()
        
        elif token_atual.nome == "<chamada de retorno>":
            self.chamada_retorno()
            self.bloco()
        elif token_atual.nome == "<identificador>":
            if self.lista_tokens[self.look_ahead+1].nome == "<atribuição>":
                self.atribuicao()
                self.bloco()
            elif token_atual.nome[self.look_ahead+1].nome == "<booleanas>":
                self.expressao()
                self.bloco()

        elif token_atual.nome == "<declaração de procedimento>":
            self.declaracao_procedimento()
            self.bloco()

        elif token_atual.nome == "<chamada de procedimento>":
            self.chamada_procedimento()
            self.bloco()
        
    

     

     def declaracao_procedimento(self):
        self.match("<declaração de procedimento>")
        self.match("<identificador>")
        self.match("<abre_parenteses>")
        self.parametros()
        self.match("<fecha_parenteses>")
        self.match("<abre_chaves>")
        self.bloco()
        self.match("<fecha_chaves>")

     def chamada_procedimento(self):
        self.match("<chamada de procedimento>")
        self.match("<identificador>")
        self.match("<abre_parenteses>")
        self.parametros()
        self.match("<fecha_parenteses>")
        self.match("<fim_comando>")

     def expressao(self):
        self.match("<identificador>")
        self.match("<booleanas>")
        if self.lista_tokens[self.look_ahead].nome == "<identificador>":
            self.match("<identificador>")
        elif self.lista_tokens[self.look_ahead].nome == "<número>":
            self.match("<número>")
        elif self.lista_tokens[self.look_ahead].nome == "<string>":
            self.match("<string>")
        elif self.lista_tokens[self.look_ahead].nome == "<booleano>":
            self.match("<booleano>")
        if self.lista_tokens[self.look_ahead].nome == "<operador>":
            self.match("<operador>")
            self.expressao()
        
          

     def atribuicao(self):
        if self.lista_tokens[self.look_ahead].nome == "<atribuição>": #atribuição que pode ocasionar erro
            self.match("<atribuição>")

        if self.lista_tokens[self.look_ahead].nome == "<identificador>":
            self.match("<identificador>")
        elif self.lista_tokens[self.look_ahead].nome == "<número>":
            self.match("<número>")
        elif self.lista_tokens[self.look_ahead].nome == "<string>":
            self.match("<string>")
        elif self.lista_tokens[self.look_ahead].nome == "<booleano>":
            self.match("<booleano>")
        if self.lista_tokens[self.look_ahead].nome == "<operador>":
            self.match("<operador>")
            self.atribuicao()

        if self.lista_tokens[self.look_ahead].nome == "<fim_comando>":
            self.match("<fim_comando>")
            self.bloco()



     def chamada_retorno(self):
        self.match("<chamada de retorno>")
        self.match("<abre_parenteses>")
        if self.lista_tokens[self.look_ahead].nome == "<identificador>":
            self.match("<identificador>")
        elif self.lista_tokens[self.look_ahead].nome == "<numero>":
            self.match("<numero>")
        elif self.lista_tokens[self.look_ahead].nome == "<booleano>":
            self.match("<booleano>")
        self.match("<fecha_parenteses>")
        self.match("<fim_comando>")


     def chamada_impressao(self):
        self.match("<chamada de impressão>")
        self.match("<abre_parenteses>")
        if(self.lista_tokens[self.look_ahead].nome == "<identificador>"):
            self.match("<identificador>")
        elif(self.lista_tokens[self.look_ahead].nome == "<numero>"):
            self.match("<numero>")
        elif(self.lista_tokens[self.look_ahead].nome == "<chamada de função>"):
            self.chamada_funcao()
        self.match("<fecha_parenteses>")
        self.match("<fim_comando>")
            

     def laço(self):
        self.match("<laço>")
        self.match("<abre_parenteses>")
        self.match("<identificador>")
        self.match("<booleanas>")
        if self.lista_tokens[self.look_ahead].nome == "<número>":
            self.match("<número>")
        elif self.lista_tokens[self.look_ahead].nome == "<identificador>":
            self.match("<identificador>")
        self.match("<fecha_parenteses>")
        self.match("<abre_chaves>")
        self.bloco2()
        print("entrou no laço")
        if self.lista_tokens[self.look_ahead].nome == "<incondicional>":
            self.match("<incondicional>") 
            self.match("<fim_comando>")
        
        self.match("<fecha_chaves>")
     
     def declaracao_funcao(self):
        self.match("<declaração de função>")
        self.match("<tipo>")
        self.match("<identificador>")
        self.match("<abre_parenteses>")
        self.parametros()
        self.match("<fecha_parenteses>")
        self.match("<abre_chaves>")
        self.bloco()
        self.match("<fecha_chaves>")

     def chamada_funcao(self):
        self.match("<chamada de função>")
        self.match("<identificador>")
        self.match("<abre_parenteses>")
        self.parametros()
        self.match("<fecha_parenteses>")
        if self.lista_tokens[self.look_ahead].nome == "<fim_comando>":
            self.match("<fim_comando>")

     def condicao(self):
        self.match("<chamada do if>")
        self.match("<abre_parenteses>")
        self.match("<identificador>")
        self.match("<booleanas>")
        if self.lista_tokens[self.look_ahead].nome == "<número>":
            self.match("<número>")
        elif self.lista_tokens[self.look_ahead].nome == "<identificador>":
            self.match("<identificador>")
        self.match("<fecha_parenteses>")
        self.match("<abre_chaves>")
        self.bloco3()
        self.match("<fecha_chaves>")
        self.match("<fim_condicao>")
        if self.lista_tokens[self.look_ahead].nome == "<chamada do if>":
            self.match("<chamada do if>")
            self.match("<abre_chaves>")
            self.bloco()
            self.match("<fecha_chaves>")
            

     def declaracao_variavel(self):
        print("entrou na declaracao de variavel")
        self.match("<tipo>")
        self.match("<identificador>")
        if(self.lista_tokens[self.look_ahead].nome == "<atribuição>"):
            self.atribuicao()
        if self.lista_tokens[self.look_ahead].nome == "<fim_comando>":
            self.match("<fim_comando>")
        



     def declaracao_funcao(self):
        self.match("<declaração de função>")
        self.match("<tipo>")
        self.match("<identificador>")
        self.match("<abre_parenteses>")
        self.parametros()
        self.match("<fecha_parenteses>")
        self.match("<abre_chaves>")
        self.bloco()
        self.match("<fecha_chaves>")


     def parametros(self):
        token_atual = self.lista_tokens[self.look_ahead]

        if token_atual.nome == "<tipo>":
            self.match("<tipo>")
            self.match("<identificador>")
            self.parametros()

        elif token_atual.nome == "<virgula>":
            self.match("<virgula>")
            if(self.lista_tokens[self.look_ahead].nome == "<tipo>"):
                self.match("<tipo>")
                self.match("<identificador>")
            self.parametros()

        elif token_atual.nome == "<variavel>":
            self.match("<variavel>")
            self.parametros()
        elif token_atual.nome == "<numero>":
            self.match("<numero>")
            self.parametros()
        elif token_atual.nome == "<bool>":
            self.match("<bool>")
            self.parametros()
        elif token_atual.nome == "<identificador>":
            self.match("<identificador>")
            self.parametros()


     def bloco2(self):
        if self.lista_tokens[self.look_ahead].nome == "<declaração de variável>":
            self.declaracao_variavel()
            self.bloco2()
        elif self.lista_tokens[self.look_ahead].nome == "<chamada do if>":
            self.condicao2()
            self.bloco2()
        elif self.lista_tokens[self.look_ahead].nome == "<laço>":
            self.laço()
            self.bloco2()
        elif self.lista_tokens[self.look_ahead].nome == "<atribuição>":
            self.atribuicao2()
        elif self.lista_tokens[self.look_ahead].nome == "<chamada de função>":
            self.chamada_funcao()
            self.bloco2()
        elif self.lista_tokens[self.look_ahead].nome == "<chamada de impressão>":
            self.chamada_impressao()
            self.bloco2()
        elif self.lista_tokens[self.look_ahead].nome == "<chamada de retorno>":
            self.chamada_retorno()
            self.bloco2()
        elif self.lista_tokens[self.look_ahead].nome == "<identificador>":
            self.match("<identificador>")
            if self.lista_tokens[self.look_ahead].nome == "<atribuição>":
                self.match("<atribuição>")
                self.atribuicao2()
            elif self.lista_tokens[self.look_ahead+1].nome == "<booleanas>":
                self.expressao()
        elif self.lista_tokens[self.look_ahead].nome == "<chamada de procedimento>":
            self.chamada_procedimento()
            self.bloco2()
        elif self.lista_tokens[self.look_ahead].nome == "<incondicional>":
            self.match("<incondicional>")
            self.bloco2()
        elif self.lista_tokens[self.look_ahead].nome == "<fim_comando>":
            self.match("<fim_comando>")
            self.bloco2()
        elif self.lista_tokens[self.look_ahead].nome == "<fecha_chaves>":
            
            return
        

     def condicao2(self):
        self.match("<chamada do if>")
        self.match("<abre_parenteses>")
        self.expressao()
        self.match("<fecha_parenteses>")
        self.match("<abre_chaves>")
        self.bloco2()
        self.match("<fecha_chaves>")
        self.match("<fim_condicao>")
        if self.lista_tokens[self.look_ahead].nome == "<chamada do if>":
            self.match("<chamada do if>")
            self.match("<abre_chaves>")
            self.bloco2()
            self.match("<fecha_chaves>")


     def atribuicao2(self):
        if self.lista_tokens[self.look_ahead].nome == "<identificador>":
            self.match("<identificador>")
        elif self.lista_tokens[self.look_ahead].nome == "<número>":
            self.match("<número>")
        elif self.lista_tokens[self.look_ahead].nome == "<string>":
            self.match("<string>")
        elif self.lista_tokens[self.look_ahead].nome == "<booleano>":
            self.match("<booleano>")
        if self.lista_tokens[self.look_ahead].nome == "<operador>":
            self.match("<operador>")
            self.atribuicao2()

        if self.lista_tokens[self.look_ahead].nome == "<fim_comando>":
            self.match("<fim_comando>")
            self.bloco2()
    


     def bloco3(self):
         
         if self.lista_tokens[self.look_ahead].nome == "<declaração de variável>":  
            self.declaracao_variavel()
            self.bloco3()
         elif self.lista_tokens[self.look_ahead].nome == "<chamada de procedimento>":
             self.chamada_procedimento()
             self.bloco3()
         elif self.lista_tokens[self.look_ahead].nome == "<chamada de função>":
             self.chamada_funcao()
             self.bloco3()
         elif self.lista_tokens[self.look_ahead].nome == "<identificador>":
                self.match("<identificador>")
                if self.lista_tokens[self.look_ahead].nome == "<atribuição>":
                    self.match("<atribuição>")
                    self.atribuicao2()
                elif self.lista_tokens[self.look_ahead+1].nome == "<booleanas>":
                    self.expressao()
         elif self.lista_tokens[self.look_ahead].nome == "<chamada do if>":
            self.condicao2()
            self.bloco3()
         elif self.lista_tokens[self.look_ahead].nome == "<laço>":
            self.laço() 
            self.bloco3()   
         elif self.lista_tokens[self.look_ahead].nome == "<chamada de impressão>":
             self.chamada_impressao()
             self.bloco3()