from django.db import models


class Student(models.Model):
    student_id = models.IntegerField(unique=True)

    # Perfil
    sexo = models.CharField(max_length=20)
    idade = models.PositiveIntegerField()
    estudante_nis = models.BooleanField(default=False)
    informou_nome_mae = models.BooleanField(default=False)
    informou_nome_pai = models.BooleanField(default=False)
    possui_deficiencia = models.BooleanField(default=False)
    raca_cor = models.CharField(max_length=30)
    tipo_localizacao_endereco_estudante = models.CharField(max_length=30)

    # Situação escolar
    situacao_consolidada = models.CharField(max_length=30)
    etapa_ensino = models.CharField(max_length=20)
    repetente = models.BooleanField(default=False)
    frequencia_escolar = models.FloatField()
    notas_medias = models.FloatField()

    # Condição socioeconômica
    nivel_socioeconomico = models.CharField(max_length=30)
    renda_familiar = models.FloatField()
    trabalha = models.BooleanField(default=False)
    trabalho_domestico_excessivo = models.BooleanField(default=False)

    # Vulnerabilidade
    problemas_de_saude = models.BooleanField(default=False)
    violencia_domestica = models.BooleanField(default=False)
    gravidez_na_adolescencia = models.BooleanField(default=False)
    apoio_familiar = models.CharField(max_length=30)
    necessita_assistencia_social = models.BooleanField(default=False)

    # Relação com a escola
    comportamento_em_sala = models.CharField(max_length=30)
    aceitacao_pelos_pares = models.CharField(max_length=30)
    expectativa_retorno = models.CharField(max_length=30)
    fator_desencadeador_presente = models.BooleanField(default=False)
    engajamento_com_a_escola = models.CharField(max_length=30)

    # Contexto
    distancia_da_escola_km = models.FloatField()
    violencia_na_comunidade = models.BooleanField(default=False)
    infraestrutura_escolar = models.CharField(max_length=30)
    disponibilidade_material_didatico = models.CharField(max_length=30)
    flexibilidade_pedagogica = models.CharField(max_length=30)
    qualidade_pedagogica_percebida = models.CharField(max_length=30)

    # Variável-alvo
    evasao = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Aluno {self.student_id}"