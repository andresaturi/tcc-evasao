from pathlib import Path

import pandas as pd
from django.core.management.base import BaseCommand, CommandError

from students.models import Student


class Command(BaseCommand):
    help = "Importa o dataset de evasão escolar para o banco de dados."

    def handle(self, *args, **options):
        # Raiz do projeto: tcc-evasao/
        base_dir = Path(__file__).resolve().parents[4]

        # Caminho relativo dentro do projeto
        dataset_path = base_dir / "dataset" / "dataset_evasao_sintetico.csv"

        self.stdout.write(f"Lendo dataset: {dataset_path}")

        if not dataset_path.exists():
            raise CommandError(
                f"Arquivo não encontrado: {dataset_path}"
            )

        df = pd.read_csv(dataset_path)

        self.stdout.write(
            self.style.SUCCESS(
                f"Dataset carregado: {len(df)} registros."
            )
        )

        self.stdout.write("Salvando registros no PostgreSQL...")

        students = []

        for _, row in df.iterrows():
            students.append(
                Student(
                    student_id=int(row["id_aluno"]),
                    sexo=row["sexo"],
                    idade=int(row["idade"]),
                    estudante_nis=row["estudante_nis"],
                    informou_nome_mae=row["informou_nome_mae"],
                    informou_nome_pai=row["informou_nome_pai"],
                    possui_deficiencia=row["possui_deficiencia"],
                    raca_cor=row["raca_cor"],
                    tipo_localizacao_endereco_estudante=row[
                        "tipo_localizacao_endereco_estudante"
                    ],
                    situacao_consolidada=row[
                        "situacao_consolidada_no_ano"
                    ],
                    etapa_ensino=row["etapa_ensino"],
                    repetente=row["repetente"],
                    frequencia_escolar=float(row["frequencia_escolar"]),
                    notas_medias=float(row["notas_medias"]),
                    nivel_socioeconomico=row["nivel_socioeconomico"],
                    renda_familiar=float(row["renda_familiar"]),
                    trabalha=row["trabalha"],
                    trabalho_domestico_excessivo=row[
                        "trabalho_domestico_excessivo"
                    ],
                    problemas_de_saude=row["problemas_de_saude"],
                    violencia_domestica=row["violencia_domestica"],
                    gravidez_na_adolescencia=row[
                        "gravidez_na_adolescencia"
                    ],
                    apoio_familiar=row["apoio_familiar"],
                    comportamento_em_sala=row["comportamento_em_sala"],
                    aceitacao_pelos_pares=row["aceitacao_pelos_pares"],
                    necessita_assistencia_social=row[
                        "necessita_assistencia_social"
                    ],
                    expectativa_retorno=row["expectativa_retorno"],
                    fator_desencadeador_presente=row[
                        "fator_desencadeador_presente"
                    ],
                    distancia_da_escola_km=float(
                        row["distancia_da_escola_km"]
                    ),
                    violencia_na_comunidade=row[
                        "violencia_na_comunidade"
                    ],
                    engajamento_com_a_escola=row[
                        "engajamento_com_a_escola"
                    ],
                    infraestrutura_escolar=row[
                        "infraestrutura_escolar"
                    ],
                    disponibilidade_material_didatico=row[
                        "disponibilidade_material_didatico"
                    ],
                    flexibilidade_pedagogica=row[
                        "flexibilidade_pedagogica"
                    ],
                    qualidade_pedagogica_percebida=row[
                        "qualidade_pedagogica_percebida"
                    ],
                    evasao=row["evasao"],
                )
            )

        Student.objects.bulk_create(
            students,
            batch_size=500,
            ignore_conflicts=True,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"{len(students)} registros processados com sucesso."
            )
        )