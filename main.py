from analizador_lexico import Lexer
from analizador_sintatico import AnalizadorSintatico

arq = open("codigo.txt","r")
texto = arq.readlines()
#print(texto)
arq.close()

lexer = Lexer(texto)
lexer.tokenizador(texto)
#lexer.imprimir_tokens()
#lexer.imprimir_tabela_simbolos()
print ("Analisador léxico finalizado com sucesso!")
parser = AnalizadorSintatico(lexer.tokens, lexer.tabela_simbolos)
parser.programa()