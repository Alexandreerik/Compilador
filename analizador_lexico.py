from TokenDaGramatica import token
from simbolo import *

class Lexer:
    def __init__(self,texto):
        self.texto = texto
        self.tokens = []
        self.tabela_simbolos = {}
    
    def tokenizador(self,texto):
        buffer=''
        linha_atual=1
        for linha in texto:
            for i in range(len(linha)):
                if((i + 1) < len(linha)): 
                    buffer += linha[i]
                    if(self.verifica_delimitadores(buffer, linha_atual)):
                        buffer = ""
                    elif(linha[i + 1] == " " or linha[i + 1] == "\n" or linha[i + 1] == "{" or linha[i + 1] == "}" or linha[i + 1] == "(" or linha[i + 1] == ")" or linha[i + 1] == ";" or linha[i + 1] == ","):
                        buffer = buffer.strip()
                        self.palavras_reservadas(buffer, linha_atual, linha, i)
                        buffer = ""
                                           
                        
            buffer = ""
            linha_atual += 1
       
    def palavras_reservadas(self, buffer, linha, texto, i):
        if (buffer == "program"):
            self.tokens.append(token("<programa>","program",linha))
            return True
        elif (buffer == "end"):
            self.tokens.append(token("<Fimprograma>","end",linha))
            return True
        elif (buffer == "int"):
            self.tokens.append(token("<tipo>","int",linha))
            return True
        elif (buffer == "bool"):
            self.tokens.append(token("<tipo>","bool",linha))
            return True
        elif (buffer == "func"):
            self.tokens.append(token("<declaração de função>","func",linha))
            return True
        elif (buffer == "callfunc"):
            self.tokens.append(token("<chamada de função>","callfunc",linha))
            return True
        elif (buffer == "proc"):
            self.tokens.append(token("<declaração de procedimento>","proc",linha))
            return True
        elif (buffer == "callproc"):
            self.tokens.append(token("<chamada de procedimento>","callproc",linha))
            return True
        elif (buffer == "return"):
            self.tokens.append(token("<chamada de retorno>","return",linha))
            return True
        elif (buffer == "if"):
            self.tokens.append(token("<condicao>","if",linha))
            return True
        elif (buffer == "else"):
            self.tokens.append(token("<condicao>","else",linha))
            return True
        elif (buffer == "while"):
            self.tokens.append(token("<laco>","while",linha))
            return True
        elif (buffer == "break"):
            self.tokens.append(token("<parar>","break",linha))
            return True
        elif (buffer == "continue"):
            self.tokens.append(token("<continuar>","continue",linha))
            return True
        elif (buffer == "print"):
            self.tokens.append(token("<chamada de impressão>","printf",linha))
            return True
        elif (buffer == "=="):
            self.tokens.append(token("<booleanas>","==",linha))
            return True
        elif (buffer == "!="):
            self.tokens.append(token("<booleanas>","!=",linha))
            return True
        elif (buffer == "<="):
            self.tokens.append(token("<booleanas>","<=",linha))
            return True
        elif (buffer == ">="):
            self.tokens.append(token("<booleanas>",">=",linha))
            return True
        elif (buffer == ">"):
            self.tokens.append(token("<booleanas>",">",linha))
            return True
        elif (buffer == "<"):
            self.tokens.append(token("<booleanas>","<",linha))
            return True
        elif (buffer == "+"):
            self.tokens.append(token("<aritmeticas>","+",linha))
            return True
        elif (buffer == "-"):
            self.tokens.append(token("<aritmeticas>","-",linha))
            return True
        elif (buffer == "*"):
            self.tokens.append(token("<aritmeticas>","*",linha))
            return True
        elif (buffer == "/"):
            self.tokens.append(token("<aritmeticas>","/",linha))
            return True
        elif (buffer == "="):
            self.tokens.append(token("<atribuicao>","=",linha))
            return True
        elif (buffer == ","):
            self.tokens.append(token("<virgula>",",",linha))
            return True
        elif (buffer == "true"):
            self.tokens.append(token("<palavraBooleana>","true",linha))
            return True
        elif(buffer == "false"):
            self.tokens.append(token("<palavraBooleana>","false",linha))
            return True
        else:
            self.varivel(buffer, linha , texto, i)
    def imprimir_tokens(self):
        for t in self.tokens:
            print(t.nome + " " + t.lexema + " " + str(t.linha))
            

    def verifica_delimitadores(self, p, linha):
        if(p == " "):
            return True
        elif(p == "{"):
            self.tokens.append(token("<abre_chaves>","{",linha))
            return True
        elif(p == "}"):
            self.tokens.append(token("<fecha_chaves>","}",linha))
            return True
        elif(p == "("):
            self.tokens.append(token("<abre_parenteses>","(",linha))
            return True
        elif(p == ")"):
            self.tokens.append(token("<fecha_parenteses>",")",linha))
            return True
        elif(p == ";"):
            self.tokens.append(token("<fim_comando>",";",linha))
            return True
        else:
            return False



    def varivel(self, buffer, linha, texto, i):   
        #print(buffer)
        if((buffer[0] >= 'a' and buffer[0] <= 'z')):
            for c in buffer:
                #print(c)
                if((c >= 'a' and c <= 'z') or (c >= '0' and c <= '9')):
                    continue
                else:
                    print("Erro de variavel na linha: " + str(linha))
                    quit()

            last_token = self.tokens[len(self.tokens) -1] #pega o ultimo token adicionado
            if(buffer not in self.tabela_simbolos): ##### VERIFICA SE A VARIAVEL JÁ EXISTE NA LISTA
                if(last_token.nome == "<tipo>"): #adicionando na tabela de simbolos
                        if(last_token.lexema == "int"):
                            self.tabela_simbolos[buffer] = Simbolo("int",linha)
                        
                        elif(last_token.lexema == "bool"):
                            self.tabela_simbolos[buffer] = Simbolo("bool",linha)
                        

                elif(last_token.lexema == "func"):
                    j = i
                    listParam = []
                    qtdParam = 0
                    
                    while texto[j]!= ")":
                        checkInt = texto[j-2] + texto[j-1] + texto[j]
                        checkBoolean = texto[j-6] + texto[j-5] + texto[j-4]+ texto[j-3]+ texto[j-2]+ texto[j-1]+ texto[j]

                        if(checkInt == "int"):
                            qtdParam += 1
                            listParam.append("int")
                        elif(checkBoolean == "bool"):
                            qtdParam += 1
                            listParam.append("bool")
                        j += 1

                   
                    self.tabela_simbolos[buffer] = SimboloCaracteristica("func",linha,qtdParam,listParam)

                elif(last_token.lexema == "callfunc"):
                    j = i
                    listParam = []
                    qtdParam = 0
                    
                    while texto[j]!= ")":
                        checkInt = texto[j-2] + texto[j-1] + texto[j]
                        checkBoolean = texto[j-6] + texto[j-5] + texto[j-4]+ texto[j-3]+ texto[j-2]+ texto[j-1]+ texto[j]

                        if(checkInt == "int"):
                            qtdParam += 1
                            listParam.append("int")
                        elif(checkBoolean == "bool"):
                            qtdParam += 1
                            listParam.append("bool")
                        j += 1

                    
                    self.tabela_simbolos[buffer] = SimboloCaracteristica("callfunc",linha,qtdParam,listParam)

                elif(last_token.lexema == "proc"):
                    j = i
                    listParam = []
                    qtdParam = 0
                    
                    while texto[j]!= ")":
                        checkInt = texto[j-2] + texto[j-1] + texto[j]
                        checkBoolean = texto[j-6] + texto[j-5] + texto[j-4]+ texto[j-3]+ texto[j-2]+ texto[j-1]+ texto[j]

                        if(checkInt == "int"):
                            qtdParam += 1
                            listParam.append("int")
                        elif(checkBoolean == "bool"):
                            qtdParam += 1
                            listParam.append("bool")
                        j += 1

                    self.tabela_simbolos[buffer] = SimboloCaracteristica("proc",linha,qtdParam,listParam)


             #   elif(last_token.nome == "<constante>"):
            #        self.tabela_simbolos[buffer] = Simbolo("const",linha)

            #    elif(self.tokens[len(self.tokens) -1].nome == "<abre_parenteses>" or self.tokens[len(self.tokens) -1].nome == "<virgula>"):
           #         print('\033[91m' + "Error variable {0} uninitialized ".format(buffer) + '\033[0m')
            #        quit()

                self.tokens.append(token("<variavel>",buffer,linha))
            else:
                if(self.tokens[len(self.tokens) -1].nome != "<tipo>" and self.tokens[len(self.tokens) -1].nome != "<constante>" and self.tokens[len(self.tokens) -1].nome != "<declaracao_func>") :
                    self.tokens.append(token("<variavel>",buffer,linha))
                else:
                    print('\033[91m' + "Error variable {0} already exists ".format(buffer) + '\033[0m')
                    quit()
        else:
            for c in buffer:
                 #print(c)
                 if(c >= '0' and c <= '9'):
                     continue
                 else:
                    print('\033[91m' + "Error line: " + str(linha) + '\033[0m')
                    quit()
                    return False
            self.tokens.append(token("<número>",buffer,linha))

    
            
    
            
            
    def imprimir_lista_tokens(self):
        for t in self.tokens:
            print(t.nome + " " + t.lexema + " " + str(t.linha))
    
    def imprimir_tabela_simbolos(self):
        print('\033[34m' + "SIMBOLOS" + '\033[0m')
        for t in self.tabela_simbolos:
            if type(self.tabela_simbolos[t]) is Simbolo:
                print(self.tabela_simbolos[t].tipo + " " + t + " " + str(self.tabela_simbolos[t].linha))
            else:
                print(self.tabela_simbolos[t].tipo + " " + t + " " + str(self.tabela_simbolos[t].linha) + " " + str(self.tabela_simbolos[t].qtdParam) + " " + str(self.tabela_simbolos[t].listParam))
