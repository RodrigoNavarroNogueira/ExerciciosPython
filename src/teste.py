string_numero = "0507"
numero_inteiro = int(string_numero)
print(numero_inteiro)  # Isso imprimirá 507

# Se você deseja preservar os zeros à esquerda, você pode fazer o seguinte:
string_com_zeros_preservados = string_numero  # Armazena a string original
print(string_com_zeros_preservados)  # Isso imprimirá "0507"

# Se você quiser adicionar zeros à esquerda para um comprimento específico, por exemplo, 6 dígitos:
comprimento_desejado = 6
string_com_zeros_preservados = string_numero.zfill(comprimento_desejado)
print(string_com_zeros_preservados)  # Isso imprimirá "00507"
