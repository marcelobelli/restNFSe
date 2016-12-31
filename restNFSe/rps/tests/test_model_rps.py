from django.test import TestCase

from model_mommy import mommy

from ..models import RPS
from restNFSe.accounts.models import User
from restNFSe.utils.to_dict import _retira_none_dict, _bool_to_ts_sim_nao


class RPSModelTest(TestCase):
    maxDiff = None

    def setUp(self):
        self.prestador1 = mommy.make(User)
        self.prestador2 = mommy.make(User)
        self.rps_without_opt = mommy.make(RPS, prestador = self.prestador1)
        self.rps_with_opt = mommy.make(RPS, prestador = self.prestador2, _fill_optional=True)

    def test_create(self):
        self.assertTrue(RPS.objects.exists())

    def test_numero_lote_exists(self):
        self.assertTrue(self.rps_without_opt.numero_lote)

    def test_se_numero_lote_e_igual_no_usuario(self):
        numero_lote_user = User.objects.values_list('numero_lote_rps',
                                                    flat=True).get(id=self.rps_without_opt.prestador_id)
        self.assertEqual(self.rps_without_opt.numero_lote, numero_lote_user)

    def test_to_dict_without_opt(self):
        rps = self.rps_without_opt.__dict__
        dicionario_prestador = self.prestador1.to_dict()

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

        dict_lote_rps_expected = {
            'identificador': rps['identificador_lote_rps'],
            'numero_lote': rps['numero_lote'],
            'cnpj': dicionario_prestador['cnpj'],
            'inscricao_municipal': dicionario_prestador['inscricao_municipal'],
            'quantidade_rps': 1,
            'lista_rps': [dict_rps]
        }

        self.assertEqual(self.rps_without_opt.to_dict(), dict_lote_rps_expected)

    def test_to_dict_with_opt(self):
        rps = self.rps_with_opt.__dict__
        dicionario_prestador = self.prestador2.to_dict()

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

        dict_lote_rps_expected = {
            'identificador': rps['identificador_lote_rps'],
            'numero_lote': rps['numero_lote'],
            'cnpj': dicionario_prestador['cnpj'],
            'inscricao_municipal': dicionario_prestador['inscricao_municipal'],
            'quantidade_rps': 1,
            'lista_rps': [dict_rps]
        }

        self.assertEqual(self.rps_with_opt.to_dict(), dict_lote_rps_expected)