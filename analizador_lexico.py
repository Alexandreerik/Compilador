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
            self.tokens.append(token("<chamada do if>","if",linha))
            return True
        elif (buffer == "else"):
            self.tokens.append(token("<else_part>","else",linha))
            return True
        elif (buffer == "while"):
            self.tokens.append(token("<laço>","while",linha))
            return True
        elif (buffer == "break"):
            self.tokens.append(token("<incondicional>","break",linha))
            return True
        elif (buffer == "continue"):
            self.tokens.append(token("<incondicional>","continue",linha))
            return True
        elif (buffer == "print"):
            self.tokens.append(token("<chamada de impressão>","print",linha))
            return True
        elif (buffer == "=="):
            self.tokens.append(token("<operador booleano>","==",linha))
            return True
        elif (buffer == "!="):
            self.tokens.append(token("<operador booleano>","!=",linha))
            return True
        elif (buffer == "<="):
            self.tokens.append(token("<operador booleano>","<=",linha))
            return True
        elif (buffer == ">="):
            self.tokens.append(token("<operador booleano>",">=",linha))
            return True
        elif (buffer == ">"):
            self.tokens.append(token("<operador booleano>",">",linha))
            return True
        elif (buffer == "<"):
            self.tokens.append(token("<operador booleano>","<",linha))
            return True
        elif (buffer == "+"):
            self.tokens.append(token("<operador>","+",linha))
            return True
        elif (buffer == "-"):
            self.tokens.append(token("<operador>","-",linha))
            return True
        elif (buffer == "*"):
            self.tokens.append(token("<operador>","*",linha))
            return True
        elif (buffer == "/"):
            self.tokens.append(token("<operador>","/",linha))
            return True
        elif (buffer == "="):
            self.tokens.append(token("<atribuição>","=",linha))
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
        elif(p == "endif"):
            self.tokens.append(token("<fim_if>","endif",linha))
            return True
        elif(p == "endelse"):
            self.tokens.append(token("<fim_else>","endif",linha))
            return True
        elif(p == "endwhile"):
            self.tokens.append(token("<fim_laco>","endwhile",linha))
            return True
        else:
            return False



    def varivel(self, buffer, linha, texto, i):   
        if((buffer[0] >= 'a' and buffer[0] <= 'z')):
            for c in buffer:
                if((c >= 'a' and c <= 'z') or (c >= '0' and c <= '9')):
                    continue
                else:
                    print("Erro de variavel na linha: " + str(linha))
                    quit()

            last_token = self.tokens[len(self.tokens) -1] 
            pre_last_token = self.tokens[len(self.tokens) -2] 
            if(buffer not in self.tabela_simbolos): 
                
                if(last_token.nome == "<tipo>" and pre_last_token.nome != '<declaração de função>'): 
                        if(last_token.lexema == "int"):
                            self.tabela_simbolos[buffer] = Simbolo("int",linha)
                        
                        elif(last_token.lexema == "bool"):
                            self.tabela_simbolos[buffer] = Simbolo("bool",linha)
                        
            
                elif(pre_last_token.lexema == "func"):
                    j = i
                    listParam = []
                    qtdParam = 0
                    if(last_token.lexema == "int"):
                        while texto[j]!= ")":
                            checkInt = texto[j-2] + texto[j-1] + texto[j]
                            checkBoolean = texto[j-3]+ texto[j-2]+ texto[j-1]+ texto[j]

                            if(checkInt == "int"):
                                qtdParam += 1
                                listParam.append("int")
                            elif(checkBoolean == "bool"):
                                qtdParam += 1
                                listParam.append("bool")
                            j += 1

                        
                        self.tabela_simbolos[buffer] = SimboloFuncao("func","int",linha,qtdParam,listParam)
                    elif(last_token.lexema == "bool"):
                        while texto[j]!= ")":
                            checkInt = texto[j-2] + texto[j-1] + texto[j]
                            checkBoolean = texto[j-3]+ texto[j-2]+ texto[j-1]+ texto[j]

                            if(checkInt == "int"):
                                qtdParam += 1
                                listParam.append("int")
                            elif(checkBoolean == "bool"):
                                qtdParam += 1
                                listParam.append("bool")
                            j += 1

                        
                        self.tabela_simbolos[buffer] = SimboloFuncao("func","bool",linha,qtdParam,listParam)

                

                elif(last_token.lexema == "proc"):
                    j = i
                    listParam = []
                    qtdParam = 0
                    
                    while texto[j]!= ")":
                        checkInt = texto[j-2] + texto[j-1] + texto[j]
                        checkBoolean = texto[j-3]+ texto[j-2]+ texto[j-1]+ texto[j]

                        if(checkInt == "int"):
                            qtdParam += 1
                            listParam.append("int")
                        elif(checkBoolean == "bool"):
                            qtdParam += 1
                            listParam.append("bool")
                        j += 1

                    self.tabela_simbolos[buffer] = SimboloCaracteristica("proc",linha,qtdParam,listParam)

            
                elif(self.tokens[len(self.tokens) -1].nome == "<abre_parenteses>" or self.tokens[len(self.tokens) -1].nome == "<virgula>"):
                    print('\033[91m' + "Erro variavel {0} não inicializada ".format(buffer) + '\033[0m')
                    quit()

                self.tokens.append(token("<identificador>",buffer,linha))
            else:
                if(self.tokens[len(self.tokens) -1].nome != "<tipo>" and self.tokens[len(self.tokens) -1].nome != "<declaração de procedimento>" and self.tokens[len(self.tokens) -2].nome != "<declaração de função>") :
                    self.tokens.append(token("<identificador>",buffer,linha))
                else:
                    print('\033[91m' + "Erro variavel {0} já existe ".format(buffer) + '\033[0m')
                    quit()
        else:
            for c in buffer:
                 if(c >= '0' and c <= '9'):
                     continue
                 else:
                    print('\033[91m' + "Erro na linha: " + str(linha) + '\033[0m')
                    quit()
                    return False
            self.tokens.append(token("<número>",buffer,linha))
            
    def imprimir_lista_tokens(self):
        for t in self.tokens:
            print(t.nome + " " + t.lexema + " " + str(t.linha))
    
    def imprimir_tabela_simbolos(self):
        print("SIMBOLOS")
        for t in self.tabela_simbolos:
            if type(self.tabela_simbolos[t]) is Simbolo:
                print(self.tabela_simbolos[t].tipo + " " + t + " " + str(self.tabela_simbolos[t].linha))
            elif type(self.tabela_simbolos[t]) is SimboloCaracteristica:
                print(self.tabela_simbolos[t].tipo + " " + t + " " + str(self.tabela_simbolos[t].linha) + " " + str(self.tabela_simbolos[t].qtdParam) + " " + str(self.tabela_simbolos[t].listParam))
            elif type(self.tabela_simbolos[t]) is SimboloFuncao:
                print(self.tabela_simbolos[t].tipo + " " +str(self.tabela_simbolos[t].tipoRetorno) + " " + t + " "  + str(self.tabela_simbolos[t].linha) + " " + str(self.tabela_simbolos[t].qtdParam) + " " + str(self.tabela_simbolos[t].listParam))