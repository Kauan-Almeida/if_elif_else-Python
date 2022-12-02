media = float(input('Entre com a média do aluno:'))
if media <= 5:
    conceito = str("RECULAR")
elif media < 7:
    conceito = "BOM"
else:
    conceito = "EXELENTE"
print("Conceito: ", conceito)
