from analizador_lexico import Lexer
from analizador_sintatico import AnalizadorSintatico
from gerador_de_codigo import GeradorCodigoIntermediario

arq = open("codigo.txt","r")
texto = arq.readlines()
arq.close()

lexer = Lexer(texto)
lexer.tokenizador(texto)
#lexer.imprimir_lista_tokens()
#lexer.imprimir_tabela_simbolos()
parser = AnalizadorSintatico(lexer.tokens, lexer.tabela_simbolos)
instrucoes=parser.programa()

gerador = GeradorCodigoIntermediario(instrucoes)
gerador.imprimirListainstrucoes()
gerador.gerar_codigo()