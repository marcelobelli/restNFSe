def dict_prestador(prestador):
    prestador = prestador.__dict__

    dict_prestador = {
        'cnpj': prestador['cnpj'],
        'inscricao_municipal': prestador['inscricao_municipal']
    }

    return dict_prestador


def dict_lote_rps(rps, prestador):
    rps = rps.__dict__

    dicionario_prestador = prestador.to_dict()

    dict_tomador = {
        'razao_social': rps['nome'],
        'numero_documento': rps['numero_documento'],
        'endereco': rps['endereco'],
        'endereco_numero': rps['endereco_numero'],
        'bairro': rps['bairro'],
        'codigo_municipio': rps['codigo_municipio_tomador'],
        'uf': rps['uf'],
        'cep': rps['cep'],
        'telefone': rps['telefone'],
        'email': rps['email']
    }

    dict_tomador = _retira_none_dict(dict_tomador)

    dict_servico = {
        'valor_servico': rps['valor_servico'],
        'iss_retido': _bool_to_ts_sim_nao(rps['iss_retido']),
        'item_lista': rps['item_lista'],
        'discriminacao': rps['discriminacao'],
        'codigo_municipio': rps['codigo_municipio_servico'],
        'codigo_cnae': rps['codigo_cnae'],
        'codigo_tributacao_municipio': rps['codigo_tributacao_municipio'],
        # Opcional 
        'valor_deducoes': rps['valor_deducoes'],
        'valor_pis': rps['valor_pis'],
        'valor_cofins': rps['valor_cofins'],
        'valor_inss': rps['valor_inss'],
        'valor_ir': rps['valor_ir'],
        'valor_csll': rps['valor_csll'],
        'outras_retencoes': rps['outras_retencoes'],
        'aliquota': rps['aliquota'],
        'desconto_incondicionado': rps['desconto_incondicionado'],
        'desconto_condicionado': rps['desconto_condicionado']
    }

    dict_servico = _retira_none_dict(dict_servico)

    dict_rps = {
        'identificador': rps['identificador'],
        'data_emissao': rps['data_emissao'],
        'servico': dict_servico,
        'prestador': dicionario_prestador,
        'tomador': dict_tomador,
        'simples': _bool_to_ts_sim_nao(rps['simples']),
        'incentivo': _bool_to_ts_sim_nao(rps['incentivador_cultural']),
        'numero': rps['numero'],
        'serie': rps['serie'],
        'tipo': rps['tipo'],
        'natureza_operacao': rps['natureza_operacao'],
        'regime_especial': rps['regime_especial']
    }

    dict_lote_rps = {
        'identificador': rps['identificador_lote_rps'],
        'numero_lote': rps['numero_lote'],
        'cnpj': dicionario_prestador['cnpj'],
        'inscricao_municipal': dicionario_prestador['inscricao_municipal'],
        'quantidade_rps': 1,
        'lista_rps': [dict_rps]
    }

    return dict_lote_rps


def _retira_none_dict(dicionario):
    novo_dict = {k: v for k, v in dicionario.items() if v is not None}

    return novo_dict


def _bool_to_ts_sim_nao(value):
    return 1 if value else 2
