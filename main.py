# print("Hello World") TESTE

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# ── Configuração visual global ──────────────────────────────────────────────
sns.set_theme(style="whitegrid", palette="muted", font_scale=1.05)
plt.rcParams["figure.dpi"] = 150
plt.rcParams["font.family"] = "DejaVu Sans"

# ── Leitura e limpeza ────────────────────────────────────────────────────────
df_raw = pd.read_excel(
    r"C:\Users\W10\OneDrive\Desktop\estatistica_python\Planilha_Estatística_Exploratória.xlsx",
    sheet_name="Dados", 
    header=None
)

df = df_raw.iloc[7:].copy()
df.columns = ["Microrregião", "Código",
               "Adm_Pública", "Outros_Serviços",
               "Agropecuária", "Indústria"]
df = df.dropna(subset=["Microrregião"]).reset_index(drop=True)

for col in ["Adm_Pública", "Outros_Serviços", "Agropecuária", "Indústria"]:
    df[col] = pd.to_numeric(df[col], errors="coerce") / 1_000  # R$ milhões

df["Total"] = df[["Adm_Pública", "Outros_Serviços",
                   "Agropecuária", "Indústria"]].sum(axis=1)

df["Microrregião"] = df["Microrregião"].str.strip()

CORES = ["#4C72B0", "#DD8452", "#55A868", "#C44E52"]

# ════════════════════════════════════════════════════════════════════════════
# 1. HISTOGRAMA – Distribuição do PIB da Agropecuária
# ════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9, 5))

sns.histplot(df["Agropecuária"], bins=10, color=CORES[2],
             edgecolor="white", linewidth=0.8, ax=ax)

media = df["Agropecuária"].mean()
mediana = df["Agropecuária"].median()

ax.axvline(media,   color="#C44E52", lw=1.8, ls="--", label=f"Média: R$ {media:.0f} mi")
ax.axvline(mediana, color="#DD8452", lw=1.8, ls=":",  label=f"Mediana: R$ {mediana:.0f} mi")

ax.set_title("Distribuição do PIB da Agropecuária\nMicorregiões do RS — 2021", fontsize=13, fontweight="bold")
ax.set_xlabel("PIB Agropecuário (R$ milhões)", fontsize=11)
ax.set_ylabel("Frequência (Nº de Micorregiões)", fontsize=11)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"R$ {x:,.0f} mi"))
ax.legend(fontsize=10)
fig.tight_layout()
fig.savefig("1_histograma.png")
plt.close()
print("✔ 1_histograma.png salvo")

# ════════════════════════════════════════════════════════════════════════════
# 2. GRÁFICO DE DISPERSÃO – Agropecuária vs Indústria
# ════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(10, 6))

scatter = ax.scatter(df["Agropecuária"], df["Indústria"],
                     c=df["Total"], cmap="viridis", s=80,
                     edgecolors="white", linewidths=0.5, zorder=3)

cbar = fig.colorbar(scatter, ax=ax, pad=0.01)
cbar.set_label("PIB Total (R$ mi)", fontsize=10)

# linha de tendência
m, b = np.polyfit(df["Agropecuária"], df["Indústria"], 1)
x_line = np.linspace(df["Agropecuária"].min(), df["Agropecuária"].max(), 200)
ax.plot(x_line, m * x_line + b, color="red", lw=1.5, ls="--",
        label="Linha de tendência", zorder=2)

# rótulos dos pontos extremos
destaques = df.nlargest(3, "Indústria").index.tolist() + df.nlargest(3, "Agropecuária").index.tolist()
for i in set(destaques):
    ax.annotate(df.loc[i, "Microrregião"],
                (df.loc[i, "Agropecuária"], df.loc[i, "Indústria"]),
                textcoords="offset points", xytext=(6, 4),
                fontsize=7.5, color="#333333")

ax.set_title("Dispersão: PIB Agropecuário × PIB Industrial\nMicorregiões do RS — 2021",
             fontsize=13, fontweight="bold")
ax.set_xlabel("PIB Agropecuário (R$ milhões)", fontsize=11)
ax.set_ylabel("PIB Industrial (R$ milhões)", fontsize=11)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
ax.legend(fontsize=10)
fig.tight_layout()
fig.savefig("2_dispersao.png")
plt.close()
print("✔ 2_dispersao.png salvo")

# ════════════════════════════════════════════════════════════════════════════
# 3. HEATMAP – Correlação entre os setores econômicos
# ════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(7, 5.5))

cols_setor = ["Adm_Pública", "Outros_Serviços", "Agropecuária", "Indústria"]
labels = ["Adm. Pública", "Outros Serviços", "Agropecuária", "Indústria"]
corr = df[cols_setor].rename(columns=dict(zip(cols_setor, labels))).corr()

mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
            vmin=-1, vmax=1, linewidths=0.5,
            annot_kws={"size": 12, "weight": "bold"},
            ax=ax)

ax.set_title("Correlação entre Setores Econômicos\nMicorregiões do RS — 2021",
             fontsize=13, fontweight="bold", pad=12)
ax.tick_params(axis="x", rotation=20, labelsize=10)
ax.tick_params(axis="y", rotation=0,  labelsize=10)
fig.tight_layout()
fig.savefig("3_heatmap.png")
plt.close()
print("✔ 3_heatmap.png salvo")

# ════════════════════════════════════════════════════════════════════════════
# 4. GRÁFICO DE BARRAS EMPILHADAS – Top 15 Micorregiões por PIB Total
# ════════════════════════════════════════════════════════════════════════════
top15 = df.nlargest(15, "Total").sort_values("Total")

fig, ax = plt.subplots(figsize=(11, 7))

setores = ["Adm_Pública", "Outros_Serviços", "Agropecuária", "Indústria"]
labels_s = ["Adm. Pública", "Outros Serviços", "Agropecuária", "Indústria"]
left = np.zeros(len(top15))

for setor, label, cor in zip(setores, labels_s, CORES):
    valores = top15[setor].values
    bars = ax.barh(top15["Microrregião"], valores, left=left,
                   color=cor, label=label, edgecolor="white", linewidth=0.4)
    left += valores

ax.set_title("Top 15 Micorregiões por PIB Total — RS 2021\n(Composição Setorial em R$ milhões)",
             fontsize=13, fontweight="bold")
ax.set_xlabel("PIB (R$ milhões)", fontsize=11)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
ax.legend(loc="lower right", fontsize=9, framealpha=0.85)
ax.tick_params(axis="y", labelsize=9)
fig.tight_layout()
fig.savefig("4_barras_empilhadas.png")
plt.close()
print("✔ 4_barras_empilhadas.png salvo")

print("\n✅ Todos os gráficos foram gerados com sucesso!")
