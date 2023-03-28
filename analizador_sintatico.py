from TokenDaGramatica import token

class AnalizadorSintatico:
        
     def __init__(self, lista_tokens, tabela_simbolos):
        self.tabela_simbolos = tabela_simbolos
        self.lista_tokens = lista_tokens
        self.look_ahead = 0

     def match(self, token_esperado):
        if self.lista_tokens[self.look_ahead].nome == token_esperado:
            self.look_ahead += 1
           # print ("Token esperado: " + token_esperado + " encontrado: " + self.lista_tokens[self.look_ahead-1].nome + " na linha: " + str(self.lista_tokens[self.look_ahead-1].linha))
        else:
            print("Erro sintático: token esperado: " + token_esperado + " encontrado: " + self.lista_tokens[self.look_ahead].nome + " na linha: " + str(self.lista_tokens[self.look_ahead].linha))
            exit()

     def programa(self):
        self.match("<programa>")
        self.match("<abre_chaves>")
        self.bloco()
        self.match("<fecha_chaves>")
        self.match("<Fimprograma>")
        
     def bloco(self):
        token_atual = self.lista_tokens[self.look_ahead]
        if token_atual.nome == "<tipo>":
            self.declaracao_variavel()
            self.bloco()
        elif token_atual.nome == "<declaração de função>":
            self.declaracao_funcao()
            self.bloco()
        elif token_atual.nome == "<declaração de procedimento>":
            self.declaracao_procedimento()
            self.bloco()
        elif token_atual.nome == "<chamada de procedimento>":
            self.chamada_procedimento()
            self.bloco()
        elif token_atual.nome == "<chamada de impressão>":
            self.chamada_impressao()
            self.bloco()
        elif token_atual.nome == "<chamada do if>":
            self.condicao()
            self.bloco()
        elif token_atual.nome == "<laço>":
            self.laço()
            self.bloco()
        elif token_atual.nome == "<identificador>":
            self.match("<identificador>")
            self.match("<atribuição>")
            self.atribuicao()
            self.bloco()             
        else:
            return     


     def declaracao_variavel(self):
        self.match("<tipo>")
        self.match("<identificador>")      
        self.match("<atribuição>")
        self.atribuicao()
        

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
        self.chamada_parametros()
        self.match("<fecha_parenteses>")
        self.match("<fim_comando>")

     def expressao(self):
        if self.lista_tokens[self.look_ahead].nome == "<palavraBooleana>":
            self.match("<palavraBooleana>")
        else:
            if self.lista_tokens[self.look_ahead].nome == "<identificador>":
                self.match("<identificador>")
                self.match("<operador booleano>")
                self.expressao2()
            elif self.lista_tokens[self.look_ahead].nome == "<número>":
                self.match("<número>")
                self.match("<operador booleano>")
                self.expressao2()
            else:
                print("Erro sintático: token esperado: <identificador>" + " ou " + "<número>" + " encontrado: " + self.lista_tokens[self.look_ahead].nome + " na linha: " + str(self.lista_tokens[self.look_ahead].linha))
                exit()
            
     def expressao2(self):
        if self.lista_tokens[self.look_ahead].nome == "<identificador>":
            self.match("<identificador>")
        elif self.lista_tokens[self.look_ahead].nome == "<número>":
            self.match("<número>")
        else:
            print("Erro sintático: token esperado: <identificador>" + " ou " + "<número>" + " encontrado: " + self.lista_tokens[self.look_ahead].nome + " na linha: " + str(self.lista_tokens[self.look_ahead].linha))
            exit()
        
        
     def atribuicao(self):
        if self.lista_tokens[self.look_ahead+1].nome == "<operador>":
            self.chamada_operador()
            self.match("<fim_comando>")
        elif self.lista_tokens[self.look_ahead].nome == "<identificador>":
            self.match("<identificador>")
            self.match("<fim_comando>")
        elif self.lista_tokens[self.look_ahead].nome == "<número>":
            self.match("<número>")
            self.match("<fim_comando>")
        elif self.lista_tokens[self.look_ahead].nome == "<chamada de função>":
            self.chamada_funcao()
            self.match("<fim_comando>")
        elif self.lista_tokens[self.look_ahead].nome == "<palavraBooleana>":
            self.match("<palavraBooleana>")
            self.match("<fim_comando>")
        else:
            print("Erro sintático: token esperado: <identificador>" + " ou " + "<número>" + " ou " + "<chamada de função>" + " ou " + "<palavraBooleana>" + " encontrado: " + self.lista_tokens[self.look_ahead].nome + " na linha: " + str(self.lista_tokens[self.look_ahead].linha))
            exit()


     def chamada_operador(self):
        while True:
            if self.lista_tokens[self.look_ahead].nome == "<identificador>":
                self.match("<identificador>")
                self.match("<operador>")
                self.chamada_operador2()
            elif self.lista_tokens[self.look_ahead].nome == "<número>":
                self.match("<número>")
                self.match("<operador>")
                self.chamada_operador2()
            elif self.lista_tokens[self.look_ahead].nome == "<operador>":
                self.match("<operador>")
                self.chamada_operador2()
            else:
                break

     def chamada_operador2(self):
        if self.lista_tokens[self.look_ahead].nome == "<identificador>":
            self.match("<identificador>")
        elif self.lista_tokens[self.look_ahead].nome == "<número>":
            self.match("<número>")
        else:
            print("Erro sintático: token esperado: <identificador>" + " ou " + "<número>" + " encontrado: " + self.lista_tokens[self.look_ahead].nome + " na linha: " + str(self.lista_tokens[self.look_ahead].linha))
            exit()


     def chamada_retorno(self):
        self.match("<chamada de retorno>")
        self.match("<abre_parenteses>")
        if self.lista_tokens[self.look_ahead].nome == "<identificador>":
            self.match("<identificador>")
        elif self.lista_tokens[self.look_ahead].nome == "<número>":
            self.match("<número>")
        elif self.lista_tokens[self.look_ahead].nome == "<palavraBooleana>":
            self.match("<palavraBooleana>")
        elif self.lista_tokens[self.look_ahead].nome == "<chamada de função>":
            self.chamada_funcao()
        else:
            print("Erro sintático: token esperado: <identificador>" + " ou " + "<numero>" + " ou " + "<palavraBooleana>" + " ou " + "<chamada de função>" + " encontrado: " + self.lista_tokens[self.look_ahead].nome + " na linha: " + str(self.lista_tokens[self.look_ahead].linha))
            exit()
        self.match("<fecha_parenteses>")
        self.match("<fim_comando>")


     def chamada_impressao(self):
        self.match("<chamada de impressão>")
        self.match("<abre_parenteses>")
        if (self.lista_tokens[self.look_ahead+1].nome == "<operador>"):
            self.chamada_operador()
        elif(self.lista_tokens[self.look_ahead].nome == "<identificador>"):
            self.match("<identificador>")
        elif(self.lista_tokens[self.look_ahead].nome == "<numero>"):
            self.match("<numero>")
        elif(self.lista_tokens[self.look_ahead].nome == "<chamada de função>"):
            self.chamada_funcao()
        elif(self.lista_tokens[self.look_ahead].nome == "<palavraBooleana>"):
            self.match("<palavraBooleana>")
        else:
            print("Erro sintático: token esperado: <identificador>" + " ou " + "<numero>" + " ou " + "<chamada de função>" + " ou " + "<palavraBooleana>" + " encontrado: " + self.lista_tokens[self.look_ahead].nome + " na linha: " + str(self.lista_tokens[self.look_ahead].linha))
            exit()
        self.match("<fecha_parenteses>")
        self.match("<fim_comando>")
            

     def laço(self):
        self.match("<laço>")
        self.match("<abre_parenteses>")
        self.expressao()
        self.match("<fecha_parenteses>")
        self.match("<abre_chaves>")
        self.bloco2()
        if self.lista_tokens[self.look_ahead].nome == "<incondicional>":
            self.match("<incondicional>") 
            self.match("<fim_comando>")
        self.match("<fecha_chaves>")
        self.match("<fim_laco>")   
     
     def declaracao_funcao(self):
        self.match("<declaração de função>")
        self.match("<tipo>")
        self.match("<identificador>")
        self.match("<abre_parenteses>")
        self.parametros()
        self.match("<fecha_parenteses>")
        self.match("<abre_chaves>")
        self.bloco()
        self.chamada_retorno()
        self.match("<fecha_chaves>")

     def chamada_funcao(self):
        self.match("<chamada de função>")
        self.match("<identificador>")
        self.match("<abre_parenteses>")
        self.chamada_parametros()
        self.match("<fecha_parenteses>")
       # self.match("<fim_comando>")
     
     def parametros(self):
        self.match("<tipo>")
        self.match("<identificador>")
        if self.lista_tokens[self.look_ahead].nome == "<virgula>":
            self.match("<virgula>")            
            self.parametros()

     def chamada_parametros(self):  
        self.match("<identificador>")
        if self.lista_tokens[self.look_ahead].nome == "<virgula>":
            self.match("<virgula>")
            self.chamada_parametros()

     def condicao(self):
        self.match("<chamada do if>")
        self.match("<abre_parenteses>")
        self.expressao()
        self.match("<fecha_parenteses>")
        self.match("<abre_chaves>")
        self.bloco3()
        self.match("<fecha_chaves>")
        self.match("<fim_if>")
        if self.lista_tokens[self.look_ahead].nome == "<else_part>":
            self.match("<else_part>")
            self.match("<abre_chaves>")
            self.bloco3()
            self.match("<fecha_chaves>")
            self.match("<fim_else>")
    


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
        elif self.lista_tokens[self.look_ahead].nome == "<chamada de impressão>":
            self.chamada_impressao()
            self.bloco2()
        elif self.lista_tokens[self.look_ahead].nome == "<identificador>":
            self.match("<identificador>")
            self.match("<atribuição>")
            self.atribuicao()
            self.bloco2()    
        elif self.lista_tokens[self.look_ahead].nome == "<chamada de procedimento>":
            self.chamada_procedimento()
            self.bloco2()
        elif self.lista_tokens[self.look_ahead].nome == "<incondicional>":
            self.match("<incondicional>")
            self.match("<fim_comando>")
            self.bloco2()
        
        
        
  
     def condicao2(self):
        self.match("<chamada do if>")
        self.match("<abre_parenteses>")
        self.expressao()
        self.match("<fecha_parenteses>")
        self.match("<abre_chaves>")
        self.bloco2()
        self.match("<fecha_chaves>")
        self.match("<fim_if>")
        if self.lista_tokens[self.look_ahead].nome == "<else_part>":
            self.match("<else_part>")
            self.match("<abre_chaves>")
            self.bloco2()
            self.match("<fecha_chaves>")
            self.match("<fim_else>")
        


     def bloco3(self):
         if self.lista_tokens[self.look_ahead].nome == "<declaração de variável>":  
            self.declaracao_variavel()
            self.bloco3()
         elif self.lista_tokens[self.look_ahead].nome == "<chamada de procedimento>":
             self.chamada_procedimento()
             self.bloco3()
         elif self.lista_tokens[self.look_ahead].nome == "<identificador>":
            self.match("<identificador>")
            self.match("<atribuição>")
            self.atribuicao()
            self.bloco3()    
         elif self.lista_tokens[self.look_ahead].nome == "<chamada do if>":
            self.condicao()
            self.bloco3()
         elif self.lista_tokens[self.look_ahead].nome == "<laço>":
            self.laço() 
            self.bloco3()   
         elif self.lista_tokens[self.look_ahead].nome == "<chamada de impressão>":
             self.chamada_impressao()
             self.bloco3()