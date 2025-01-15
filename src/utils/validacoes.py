import re


def valida_cpf_cnpj(cpf_cnpj):
    """
    Valida CPF ou CNPJ baseado no tamanho e nos dígitos verificadores.

    :param cpf_cnpj: String contendo o CPF ou CNPJ
    :return: True se válido, False caso contrário
    """
    cpf_cnpj = re.sub(r'\D', '', cpf_cnpj)
    if len(cpf_cnpj) == 11:
        return valida_cpf(cpf_cnpj)
    elif len(cpf_cnpj) == 14:
        return valida_cnpj(cpf_cnpj)
    return False


def valida_cnpj(cnpj):
    """
    Valida um CNPJ de acordo com os dígitos verificadores.

    :param cnpj: String contendo o CNPJ
    :return: True se válido, False caso contrário
    """
    cnpj = re.sub(r'\D', '', cnpj)
    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False

    def calcula_digito(cnpj, pesos):
        soma = sum(int(cnpj[i]) * pesos[i] for i in range(len(pesos)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6] + pesos1

    digito1 = calcula_digito(cnpj, pesos1)
    digito2 = calcula_digito(cnpj[:12] + str(digito1), pesos2)

    return cnpj[-2:] == f'{digito1}{digito2}'


def valida_cpf(cpf):
    """
    Valida um CPF de acordo com os dígitos verificadores.

    :param cpf: String contendo o CPF
    :return: True se válido, False caso contrário
    """
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calcula_digito(cpf, pesos):
        soma = sum(int(cpf[i]) * pesos[i] for i in range(len(pesos)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    pesos1 = list(range(10, 1, -1))
    pesos2 = list(range(11, 1, -1))

    digito1 = calcula_digito(cpf, pesos1)
    digito2 = calcula_digito(cpf + str(digito1), pesos2)

    return cpf[-2:] == f'{digito1}{digito2}'


def valida_areas(area_total, area_agricultavel, area_vegetacao):
    """
    Valida se as áreas fornecidas são consistentes.

    :param area_total: Área total
    :param area_agricultavel: Área agricultável
    :param area_vegetacao: Área de vegetação
    :return: True se a soma das áreas for válida, False caso contrário
    """
    return area_agricultavel + area_vegetacao <= area_total
