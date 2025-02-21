cpf = "609.543.598-81"
cpf = cpf.replace(".", "")
# verifique se o cpf possui 11 digitos
if len(cpf) == 11 and \
cpf[0] == cpf[1] == cpf[2] == cpf[3] == cpf[4] == cpf[5] == cpf[6] == cpf[7] == cpf[8] == cpf[9] == cpf[10]:

  # calcule o digito verificador 1
  soma = 0
  for i in range(9):
    soma += int(cpf[i]) * (10 - i)
  resto = soma % 11
  digito1 = (0 if resto < 2 else 11 - resto) if resto < 2 else 11 - resto
  # calcule o digito verificador 2
  soma = 0
  for i in range(10):
    soma += int(cpf[i]) * (11 - i)
  resto = soma % 11
  resto = soma % 11
  digito2 = 0 if resto < 2 else 11 - resto  # compare os digitos verificadores calculados com os do cpf
  # compare os digitos verificadores calculados com os do cpf
  if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
    print("cpf valido")
  else:
    print("cpf invalido")
