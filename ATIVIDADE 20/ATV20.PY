import pandas as pd

df = pd.read_csv("notas_alunos.csv")
df.head()

print(f"\n{df}\n")

alunos = df["aluno"]
media = (df["nota_1"] + df["nota_2"]) / 2

df["media"] = media
df["situacao"] = ""

m_faltas = max(df["faltas"])
media_turma = df["media"].mean()
maior_media = max(df["media"])

df.loc[df["media"] >= 7, "situacao"] = "APROVADO"
df.loc[df["media"] < 7, "situacao"] = "REPROVADO"
df.loc[df["faltas"] > 5, "situacao"] = "REPROVADO"


print(df)

print(f"""
Faltas: {m_faltas}
Média da turma: {media_turma}
Maior média: {maior_media}
""")

df.to_csv("situacao_aluno.csv")