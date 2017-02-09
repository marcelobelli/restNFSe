from PyNFSe.nfse.pr.curitiba import NFSeCuritiba
from lxml import etree


def envio_rps(rps):
    homologacao = True if not rps.prestador.producao else False
    nfse = NFSeCuritiba(rps.prestador.certificado_pfx.path, rps.prestador.senha_certificado,
                        homologacao=homologacao)
    xml_resposta = nfse.recepcionar_lote_rps(rps.to_dict())

    xml = etree.fromstring(xml_resposta)

    for child in xml.getchildren():
        if child.tag == 'Protocolo':
            return child.text

    return xml_resposta

# def consulta_rps_por_protocolo(prestador, protocolo):
#     homologacao = True if not prestador.producao else False
#     nfse = NFSeCuritiba(prestador.certificado_pfx.path, prestador.senha_certificado,
#                         homologacao=homologacao)


'''
lxml

for x in xml.getchildren():
    print('{0} - {1}'.format(x.tag, x.text))
'''