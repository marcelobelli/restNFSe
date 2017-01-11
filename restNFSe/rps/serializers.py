from rest_framework.serializers import ModelSerializer

from .models import RPS


class RPSSerializer(ModelSerializer):

    class Meta:
        model = RPS
        fields = (
            'id',
            'nome',
            'numero_documento',
            'endereco',
            'endereco_numero',
            'bairro',
            'codigo_municipio_tomador',
            'uf',
            'cep',
            'telefone',
            'email',
            'valor_servico',
            'iss_retido',
            'item_lista',
            'discriminacao',
            'codigo_municipio_servico',
            'codigo_cnae',
            'codigo_tributacao_municipio',
            'aliquota',
            'valor_deducoes',
            'valor_pis',
            'valor_cofins',
            'valor_inss',
            'valor_ir',
            'valor_csll',
            'outras_retencoes',
            'desconto_incondicionado',
            'desconto_condicionado',
            'identificador',
            'data_emissao',
            'simples',
            'incentivador_cultural',
            'numero',
            'serie',
            'tipo',
            'natureza_operacao',
            'regime_especial',
            'identificador_lote_rps',
            'numero_lote',
            'enviado',
        )
        read_only_fields = (
            'identificador_lote_rps',
            'numero_lote',
            'enviado',
        )
