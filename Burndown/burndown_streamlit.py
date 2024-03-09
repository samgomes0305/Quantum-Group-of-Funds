import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime, timedelta

# Dados da nossa gestão de projetos (Asana)
dias = np.arange(1, 27)
demandas_planejadas = np.array([23, 22, 22, 22, 22, 22, 21, 20, 19, 17, 16, 16, 16, 14, 14, 6, 4, 4, 4, 4, 3, 3, 3, 3, 3, 0])
demandas_concluidas = np.array([23, 22, 22, 22, 22, 22, 19, 19, 19, 16, 16, 15, 14, 7, 6, 6, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0])

# Define a data inicial
data_inicial = datetime(2024, 2, 13)

# Calcula as datas com base nos dias e na data inicial
datas = [data_inicial + timedelta(days=int(dia)) for dia in dias]

# Cria controles deslizantes para ajustar o intervalo de datas
intervalo_datas = st.slider("Escolha o intervalo de datas:", min_value=1, max_value=len(datas), value=(1, len(datas)))

# Criar o gráfico de Burndown
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(datas[intervalo_datas[0]-1:intervalo_datas[1]], demandas_planejadas[intervalo_datas[0]-1:intervalo_datas[1]], label="Planejado", color="black", marker="o")
ax.plot(datas[intervalo_datas[0]-1:intervalo_datas[1]], demandas_concluidas[intervalo_datas[0]-1:intervalo_datas[1]], label="Concluído", color="red", marker="o")

# Personaliza o gráfico
ax.set_title("Gráfico de Burndown")
ax.set_xlabel("Tempo (Dias)")
ax.set_ylabel("Demandas")
ax.set_xticks(datas[intervalo_datas[0]-1:intervalo_datas[1]])
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
plt.xticks(rotation=45, ha="right")
ax.grid(True, linestyle="--", alpha=0.5)
ax.legend()

# Mostra o gráfico usando o Streamlit
st.pyplot(fig)
