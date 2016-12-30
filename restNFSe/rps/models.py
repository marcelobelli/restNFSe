from django.db import models

_help_natureza_operacao = '1 - Tributação no município, ' \
                          '2 - Tributação fora do município, ' \
                          '3 - Isenção, ' \
                          '4 - Imune, ' \
                          '5 - Exigibilidade suspensa por decisão judicial, ' \
                          '6 - Exigibilidade suspensa por procedimento administrativo'

_help_regime_especial = '1 - Microempresa Municipal, ' \
                        '2 - Estimativa, ' \
                        '3 - Sociedade de Profissionais, ' \
                        '4 - Cooperativa'


class RPS(models.Model):
    prestador = models.ForeignKey('accounts.User', on_delete=models.CASCADE,
                                  verbose_name='Prestador')

    # Tomador
    nome = models.CharField('Nome/Razão Social', max_length=100)
    numero_documento = models.CharField('CPF/CNPJ', max_length=14)
    endereco = models.CharField('Endereço', max_length=100)
    endereco_numero = models.CharField('Número', max_length=10)
    bairro = models.CharField('Bairro', max_length=20)
    codigo_municipio_tomador = models.CharField('Código do Município', max_length=7)
    uf = models.CharField('Estado', max_length=2)
    cep = models.CharField('CEP', max_length=20)
    telefone = models.CharField('Telefone', max_length=11)
    email = models.EmailField('E-mail')

    # Servico
    valor_servico = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    iss_retido = models.BooleanField('ISS Retido', default=False)
    item_lista = models.CharField('Atividade', max_length=11)
    discriminacao = models.TextField('Descrição do Serviço')
    codigo_municipio_servico = models.CharField('Código do Município', max_length=7)
    codigo_cnae = models.IntegerField('Código CNAE')
    codigo_tributacao_municipio = models.CharField('Código de Tributação', max_length=11)
    aliquota = models.DecimalField('Aliquota', max_digits=6, decimal_places=5)
    ## Opcional
    valor_deducoes = models.DecimalField('Valor Deduções', max_digits=10,
                                         decimal_places=2, null=True, blank=True)
    valor_pis = models.DecimalField('Valor PIS', max_digits=10, decimal_places=2,
                                    null=True, blank=True)
    valor_cofins = models.DecimalField('Valor Cofins', max_digits=10, decimal_places=2,
                                       null=True, blank=True)
    valor_inss = models.DecimalField('Valor INSS', max_digits=10, decimal_places=2,
                                     null=True, blank=True)
    valor_ir = models.DecimalField('Valor IR', max_digits=10, decimal_places=2,
                                   null=True, blank=True)
    valor_csll = models.DecimalField('Valor CSLL', max_digits=10, decimal_places=2,
                                     null=True, blank=True)
    outras_retencoes = models.DecimalField('Outras Retenções', max_digits=10, decimal_places=2,
                                           null=True, blank=True)
    desconto_incondicionado = models.DecimalField('Desconto Incondicionado', max_digits=10,
                                                  decimal_places=2, null=True, blank=True)
    desconto_condicionado = models.DecimalField('Desconto Condicionado', max_digits=10,
                                                decimal_places=2, null=True, blank=True)

    # RPS
    identificador = models.CharField('Identificador', max_length=10)
    data_emissao = models.DateTimeField('Data Emissão')
    simples = models.BooleanField('Simples', default=True)
    incentivador_cultural = models.BooleanField('Incentivador Cultural', default=False)
    numero = models.IntegerField('Número RPS')
    serie = models.CharField('Série', max_length=10)
    tipo = models.CharField('Tipo', max_length=10)
    natureza_operacao = models.IntegerField('Natureza Operação', help_text=_help_natureza_operacao)
    regime_especial = models.IntegerField('Regime Especial', help_text=_help_regime_especial)

    # Lote RPS
    identificador_lote_rps = models.CharField('Identificador', max_length=10, blank=True)
    numero_lote = models.IntegerField('Número Lote', null=True, blank=True)
    enviado = models.BooleanField('Enviado', default=False)
    xml = models.TextField('XML', blank=True)

    class Meta:
        verbose_name = 'RPS'
        verbose_name_plural = 'RPSs'

    def __str__(self):
        return str(self.numero)