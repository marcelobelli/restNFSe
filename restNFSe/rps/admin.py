from django.contrib import admin
from .models import RPS

class RPSModelAdmin(admin.ModelAdmin):
    list_display = ['prestador', 'numero']

    readonly_fields = [
        'identificador_lote_rps',
        'numero_lote',
        'enviado',
        'xml',
    ]
    fieldsets = (
        (
            None, {
                'fields': (
                    'prestador',
                )
            }
        ),
        (
            'Tomador', {
                'fields': (
                    ('nome', 'numero_documento'),
                    ('endereco', 'endereco_numero'),
                    ('bairro', 'codigo_municipio_tomador'),
                    ('uf', 'cep'),
                    ('telefone', 'email'),
                )
            }
        ),
        (
            'Serviço', {
                'fields': (
                    'valor_servico',
                    'discriminacao',
                    ('item_lista', 'codigo_tributacao_municipio'),
                    ('codigo_municipio_servico', 'codigo_cnae'),
                    ('aliquota',
                    'iss_retido')
                )
            }
        ),
        (
            'Opcional', {
                'classes': ('collapse',),
                'fields': (
                    ('valor_deducoes', 'valor_pis'),
                    ('valor_cofins', 'valor_inss'),
                    ('valor_ir', 'valor_csll'),
                    ('outras_retencoes', 'desconto_incondicionado'),
                    'desconto_condicionado',
                )
            }
        ),
        (
            'RPS', {
                'fields': (
                    'identificador',
                    'data_emissao',
                    'simples',
                    'incentivador_cultural',
                    'numero',
                    'serie',
                    'tipo',
                    'natureza_operacao',
                    'regime_especial',
                )
            }
        ),
        (
            'Lote RPS', {
                'classes': ('collapse',),
                'fields': (
                    'identificador_lote_rps',
                    'numero_lote',
                    'enviado',
                    'xml',
                )
            }
        )
    )

admin.site.register(RPS, RPSModelAdmin)
