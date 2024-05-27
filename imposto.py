def somaImposto(taxaImposto, Custo):
    # Calcula o valor do custo com o imposto adicionado
    resultado = (1 + taxaImposto/100)*Custo
    # Imprime o valor com imposto
    print('Valor com imposto: {}'.format(resultado))
    # Retorna o resultado
    return resultado 
# Se a função não tiver uma instrução return, ela ainda poderá realizar operações e manipulações de dados dentro dela, mas não retornará nenhum valor específico para o código que a chamou. Isso significa que não poderá usar o resultado dessa função em outras partes do código.

somaImposto(10, 1000)