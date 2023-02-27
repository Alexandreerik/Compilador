from analizador_lexico import Lexer


arq = open("codigo.txt","r")
texto = arq.readlines()
#print(texto)
arq.close()

lexer = Lexer(texto)
lexer.tokenizador(texto)
lexer.imprimir_tokens()
lexer.imprimir_tabela_simbolos()