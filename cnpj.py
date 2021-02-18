def calcular_digitos(cnpj):
    reverso = 5
    total = 0
    for index in range(25):  # 0 1 2 3 4 5 6 7 8 9 10 11
        if index > 11:       # 0 4 2 5 2 0 1 1 0 0  0  1
            index -= 12

        total += int(cnpj[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 9

            if index == 12 and len(cnpj) == 13:
                d = 11 - (total % 11)

                if d > 9:
                    d = 0
                total = 0
                cnpj += str(d)
            elif index == 11 and len(cnpj) == 12:
                d = 11 - (total % 11)

                if d > 9:
                    d = 0
                total = 0
                cnpj += str(d)
                reverso = 6
    cnpj = formata_cnpj(cnpj)
    return cnpj


def formata_cnpj(cnpj):
    cnpj_formatado = cnpj[0:2] + '.' + cnpj[2:5] + '.' + cnpj[5:8] + '/' + cnpj[8:12] + '-' + cnpj[12:]
    return cnpj_formatado
