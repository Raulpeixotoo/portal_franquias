from django.db import models
from django.contrib.auth.models import User

class Unidade(models.Model):
    # Opções para campos de status (Sim, Não, Cobrado)
    STATUS_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
        ('cobrado', 'Cobrado'),
        ('pendente', 'Pendente'),
        ('ativa', 'Ativa'),
    ]

    

    # Dados Gerais
    uf = models.CharField(max_length=2, verbose_name="UF")
    tipo_unidade = models.CharField(max_length=50, verbose_name="Tipo de Unidade")
    unidade = models.CharField(max_length=100, verbose_name="Unidade")
    start_process = models.DateField(null=True, blank=True, verbose_name="Início do Processo")
    candidato = models.CharField(max_length=100, verbose_name="Candidato")
    contato_telefone = models.CharField(max_length=20, verbose_name="Contato Telefone")
    email_candidato = models.EmailField(verbose_name="E-mail do Candidato")

    # Status
    primeira_meeting_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='nao', verbose_name="1ª Meeting")
    direx_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='nao', verbose_name="Direx")
    planej_rotas_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='nao', verbose_name="Planej. (Rotas)")
    cnpj_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='nao', verbose_name="CNPJ")
    contrato_social_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='nao', verbose_name="Contrato Social")
    im_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='nao', verbose_name="I.M.")
    ie_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='nao', verbose_name="I.E.")
    rg_socio_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='nao', verbose_name="RG (Sócio)")
    cpf_socio_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='nao', verbose_name="CPF (Sócio)")
    comprovante_residencia_socio_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='nao', verbose_name="Comprovante de Residência (Sócio)")
    rg_fiador_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='nao', verbose_name="RG (Fiador)")
    cpf_fiador_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='nao', verbose_name="CPF (Fiador)")
    comprovante_residencia_fiador_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='nao', verbose_name="Comprovante de Residência (Fiador)")
    escritura_imovel_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='nao', verbose_name="Escritura Imóvel")
    dados_bancario_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='nao', verbose_name="Dados Bancários")
    imovel_franquia_analise_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='nao', verbose_name="Imóvel Franquia (Análise)")

    # Datas
    email_cnaes_data = models.DateField(null=True, blank=True, verbose_name="E-mail CNAE's")
    mae_data = models.DateField(null=True, blank=True, verbose_name="MAE (Manual Assinatura Eletrônica)")
    pedido_analise_fin_data = models.DateField(null=True, blank=True, verbose_name="Pedido Análise Fin.")
    confirma_analise_fin_data = models.DateField(null=True, blank=True, verbose_name="Confirmação Análise Fin.")
    email_equipamentos_data = models.DateField(null=True, blank=True, verbose_name="E-mail Equipamentos")
    mkt_projeto_arquitetura_data = models.DateField(null=True, blank=True, verbose_name="MKT (Projeto Arquitetura)")
    envio_paf_data = models.DateField(null=True, blank=True, verbose_name="Envio PAF")
    assinatura_paf_data = models.DateField(null=True, blank=True, verbose_name="Assinatura PAF")
    envio_ccf_data = models.DateField(null=True, blank=True, verbose_name="Envio CCF")
    assinatura_ccf_data = models.DateField(null=True, blank=True, verbose_name="Assinatura CCF")
    envio_cof_data = models.DateField(null=True, blank=True, verbose_name="Envio COF")
    assinatura_cof_data = models.DateField(null=True, blank=True, verbose_name="Assinatura COF")
    subir_projuris_data = models.DateField(null=True, blank=True, verbose_name="Subir para Projuris")
    assinado_projuris_data = models.DateField(null=True, blank=True, verbose_name="Assinado Projuris")
    solicitacao_senha_franchising_data = models.DateField(null=True, blank=True, verbose_name="Solicitação Senha Franchising")
    validacao_helpdesk_data = models.DateField(null=True, blank=True, verbose_name="Validação Helpdesk")
    inclusao_planilha_data = models.DateField(null=True, blank=True, verbose_name="Inclusão Planilha")
    central_lat_long_data = models.DateField(null=True, blank=True, verbose_name="(Central) Lat e Long")
    pedido_ativacao_fin_data = models.DateField(null=True, blank=True, verbose_name="Pedido Ativação Fin.")
    confirma_ativacao_fin_data = models.DateField(null=True, blank=True, verbose_name="Confirmação Ativação Fin.")

    # Sim/Não
    pgto_taxa_adesao = models.BooleanField(default=False, verbose_name="Pgto Taxa Adesão")
    segunda_meeting_update = models.BooleanField(default=False, verbose_name="2ª Meeting/Update")
    treinamento = models.BooleanField(default=False, verbose_name="Treinamento")
    inclusao_planilha = models.BooleanField(default=False, verbose_name="Inclusão Planilha")

    # Outros Campos
    email_oficial = models.EmailField(blank=True, null=True, verbose_name="E-mail Oficial")
    codigo_etiqueta_teca = models.CharField(max_length=50, blank=True, null=True, verbose_name="Código Etiqueta Teca")
    ponto_numero = models.CharField(max_length=50, blank=True, null=True, verbose_name="Ponto Número")
    numero_contrato = models.CharField(max_length=50, blank=True, null=True, verbose_name="Nº Contrato")
    infow_week = models.CharField(max_length=50, blank=True, null=True, verbose_name="InfoW (Week)")

    # Relacionamento com o Franqueado
    usuarios = models.ManyToManyField(User, related_name='unidades', verbose_name="Usuários Associados")

    #inserção de Anexos
    anexo = models.FileField(upload_to='anexos/', blank=True, null=True, verbose_name="Anexo")

    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='pendente',verbose_name="Status")

    def __str__(self):
        return self.unidade