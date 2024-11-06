def calculo_imposto(salario, aliquota):
    if salario < 0:
        raise ValueError("Vai trabalhar vagabundo!!!")
    if aliquota < 0 or aliquota > 1:
        raise ValueError("Aliquota entre 1 e 0!")

    return (salario-100) * aliquota 