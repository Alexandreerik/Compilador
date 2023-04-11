def get_tipo(variavel, tabela_simbolos):
    if variavel.lexema in tabela_simbolos:
        if(tabela_simbolos[variavel.lexema].linha <= variavel.linha):
            return tabela_simbolos[variavel.lexema].tipo
        else:
            return False
    return False


def verificar_atribuicao(lista_tokens, tabela_simbolos, look_ahead):
    tipo_declarada = get_tipo(lista_tokens[look_ahead - 2], tabela_simbolos)
    if(tipo_declarada == "int"):
        while lista_tokens[look_ahead].nome != "<fim_comando>":
            if(lista_tokens[look_ahead].nome == "<número>"):
                pass
            elif(lista_tokens[look_ahead].nome == "<identificador>"):
                
                if(get_tipo(lista_tokens[look_ahead], tabela_simbolos) == "int"):
                    pass
                else:
                    print('\033[91m' + "Erro semantico na linha: {0}, variable {1} has a different declaration".format(lista_tokens[look_ahead].linha, lista_tokens[look_ahead].lexema) + '\033[0m')
                    return False
            elif(lista_tokens[look_ahead].nome == "<operador>"):
                pass
            else:
                print('\033[91m' + "Erro semantico na linha: {0}, expected int but receive boolean".format(lista_tokens[look_ahead].linha) + '\033[0m')
                return False
            look_ahead += 1

    return True



def verificar_declaracao(lista_tokens, tabela_simbolos, look_ahead): 
    tipo_declarada = get_tipo(lista_tokens[look_ahead - 1], tabela_simbolos)

    if(lista_tokens[look_ahead + 1].nome=="<chamada de função>"):
        if(tipo_declarada == tabela_simbolos[lista_tokens[look_ahead + 2].lexema].tipoRetorno):
            return True
        else:
            print('\033[91m' + "Erro semantico na linha: {0}, variable {1} has a different declaration".format(lista_tokens[look_ahead].linha, lista_tokens[look_ahead].lexema) + '\033[0m')
            return False


    if lista_tokens[look_ahead + 2].nome != "<fim_comando>":
        return True
    if(tipo_declarada == "int"):
        if(lista_tokens[look_ahead + 1].nome == "<número>"):
            return True
        elif(lista_tokens[look_ahead + 1].nome == "<identificador>"):
            if(get_tipo(lista_tokens[look_ahead], tabela_simbolos) == "int"):
                return True
            else:
                print('\033[91m' + "Erro semantico na linha: {0}, variable {1} has a different declaration".format(lista_tokens[look_ahead].linha, lista_tokens[look_ahead].lexema) + '\033[0m')
                return False
        else:
            print('\033[91m' + "Erro semantico na linha: {0}, expected int but receive boolean".format(lista_tokens[look_ahead].linha) + '\033[0m')
            return False
        
    elif(tipo_declarada == "bool"):
        if(lista_tokens[look_ahead + 1].nome == "<palavraBooleana>"):
            return True
        elif(lista_tokens[look_ahead + 1].nome == "<identificador>"):
            if(get_tipo(lista_tokens[look_ahead], tabela_simbolos) == "bool"):
                return True
            else:
                print('\033[91m' + "Erro semantico na linha: {0}, variable {1} has a different declaration".format(lista_tokens[look_ahead].linha, lista_tokens[look_ahead].lexema) + '\033[0m')
                return False
        else:
            print('\033[91m' + "Erro semantico na linha: {0}, expected boolean but receive int".format(lista_tokens[look_ahead].linha) + '\033[0m')
            return False
        

def verificar_parametros(lista_tokens, tabela_simbolos, look_ahead):
    quantidade_params = tabela_simbolos[lista_tokens[look_ahead].lexema].qtdParam
    quantidade_declarada = 0
    look_ahead_aux = (look_ahead + 2)
    contador = look_ahead_aux
    i = 0

    while(lista_tokens[contador].nome != "<fecha_parenteses>"):
        if(lista_tokens[contador].nome != "<virgula>"):
            quantidade_declarada += 1
        contador += 1
    
    while(lista_tokens[look_ahead_aux].nome != "<fecha_parenteses>" and i < quantidade_params):
        if(lista_tokens[look_ahead_aux].nome != "<virgula>"):
            if(tabela_simbolos[lista_tokens[look_ahead].lexema].listParam[i] == "int"):
                if(lista_tokens[look_ahead_aux].nome == "<número>"):
                    pass
                elif(lista_tokens[look_ahead_aux].nome == "<identificador>"):
                    if(get_tipo(lista_tokens[look_ahead_aux], tabela_simbolos) == "int"):
                        pass
                    else:
                        print('\033[91m' + "Erro semantico na linha: {0}, variable {1} has a different declaration".format(lista_tokens[look_ahead - 2].linha, lista_tokens[look_ahead_aux].lexema) + '\033[0m')
                        return False    
                else:
                    print('\033[91m' + "Erro semantico na linha: {0}, parameter {1} declared wrong".format(lista_tokens[look_ahead - 2].linha, lista_tokens[look_ahead_aux].lexema) + '\033[0m')
                    return False
            elif(tabela_simbolos[lista_tokens[look_ahead].lexema].listParam[i] == "boolean"):
                if(lista_tokens[look_ahead_aux].nome == "<palavraBooleana>"):
                    pass
                elif(lista_tokens[look_ahead_aux].nome == "<variavel>"):
                    if(get_tipo(lista_tokens[look_ahead_aux], tabela_simbolos) == "boolean"):
                        pass
                    else:
                        print('\033[91m' + "Erro semantico na linha: {0}, variable {1} has a different declaration".format(lista_tokens[look_ahead - 2].linha, lista_tokens[look_ahead_aux].lexema) + '\033[0m')
                        return False
                else:
                    print('\033[91m' + "Erro semantico na linha: {0}, parameter {1} declared wrong".format(lista_tokens[look_ahead - 2].linha, lista_tokens[look_ahead_aux].lexema) + '\033[0m')
                    return False
            i += 1
        look_ahead_aux += 1

    if(quantidade_declarada == quantidade_params):
        return True
    else:
        print('\033[91m' + "Erro semantico na linha: {0}, the functions need {1} parameters".format(lista_tokens[look_ahead - 2].linha, quantidade_params) + '\033[0m')
        return False


def verificar_retorno(lista_tokens, tabela_simbolos, look_ahead, posicao):
    if(tabela_simbolos[lista_tokens[posicao].lexema].tipoRetorno == "int"):
        if(lista_tokens[look_ahead + 2].nome == "<número>"):
            return True
        elif(lista_tokens[look_ahead + 2].nome == "<identificador>"):
            if(get_tipo(lista_tokens[look_ahead + 2], tabela_simbolos) == "int"):
                return True
            else:
                print('\033[91m' + "Erro semantico na linha: {0}, variable {1} has a different declaration".format(lista_tokens[look_ahead + 2].linha, lista_tokens[look_ahead + 2].lexema) + '\033[0m')
                return False
        else:
            print('\033[91m' + "Erro semantico na linha: {0}, expected int but receive boolean".format(lista_tokens[look_ahead + 2].linha) + '\033[0m')
            return False
    elif(tabela_simbolos[lista_tokens[posicao].lexema].tipoRetorno == "bool"):
        if(lista_tokens[look_ahead + 2].nome == "<palavraBooleana>"):
            return True
        elif(lista_tokens[look_ahead + 2].nome == "<identificador>"):
            if(get_tipo(lista_tokens[look_ahead + 2], tabela_simbolos) == "bool"):
                return True
            else:
                print('\033[91m' + "Erro semantico na linha: {0}, variable {1} has a different declaration".format(lista_tokens[look_ahead + 2].linha, lista_tokens[look_ahead + 2].lexema) + '\033[0m')
                return False
        else:
            print('\033[91m' + "Erro semantico na linha: {0}, expected boolean but receive int".format(lista_tokens[look_ahead + 2].linha) + '\033[0m')
            return False


    
def verificar_expressao(lista_tokens, tabela_simbolos, look_ahead):
    primeiro_valor = get_tipo(lista_tokens[look_ahead], tabela_simbolos)
    segundo_valor = get_tipo(lista_tokens[look_ahead + 2], tabela_simbolos)
    if(primeiro_valor == segundo_valor):
        return True
    elif(primeiro_valor == "int" and lista_tokens[look_ahead + 2].nome == "<número>"):
        return True
    elif(lista_tokens[look_ahead].nome == "<número>" and segundo_valor == "int"):
        return True
    else:
        print('\033[91m' + "Erro semantico na linha: {0}, expected int but receive boolean".format(lista_tokens[look_ahead].linha) + '\033[0m')
        return False



