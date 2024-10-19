import streamlit as st
import pandas as pd

# Função para calcular as emissões
def calcular_emissoes(consumo, fator_emissao):
    return consumo * fator_emissao

# Configuração da página
st.set_page_config(
    page_title="Calculadora de Pegada de Carbono Residencial",
    page_icon="🌎",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Estilo
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título e descrição
st.title("🌎 Calculadora de Pegada de Carbono Residencial")
st.write(
    "Este aplicativo calcula sua pegada de carbono anual com base no seu consumo mensal."
)

# Sidebar para inputs
st.sidebar.header("Insira seus dados mensais")

# Inputs do usuário
energia_eletrica = st.sidebar.number_input(
    "Consumo de Energia Elétrica (kWh/mês)", min_value=0.0, value=0.0, step=0.1
)

gas_natural = st.sidebar.number_input(
    "Consumo de Gás Natural (m³/mês)", min_value=0.0, value=0.0, step=0.1
)

glp = st.sidebar.number_input(
    "Consumo de GLP (kg/mês)", min_value=0.0, value=0.0, step=0.1
)

gasolina = st.sidebar.number_input(
    "Consumo de Gasolina (litros/mês)", min_value=0.0, value=0.0, step=0.1
)

diesel = st.sidebar.number_input(
    "Consumo de Diesel (litros/mês)", min_value=0.0, value=0.0, step=0.1
)

residuos = st.sidebar.number_input(
    "Resíduos Orgânicos (kg/mês)", min_value=0.0, value=0.0, step=0.1
)

agua = st.sidebar.number_input(
    "Consumo de Água (m³/mês)", min_value=0.0, value=0.0, step=0.1
)

# Fatores de emissão (kg CO2e por unidade)
fatores = {
    "energia_eletrica": 0.092,  # kg CO2e por kWh
    "gas_natural": 2.15,        # kg CO2e por m³
    "glp": 2.98,                # kg CO2e por kg
    "gasolina": 2.19,           # kg CO2e por litro
    "diesel": 2.66,             # kg CO2e por litro
    "residuos": 0.84,           # kg CO2e por kg
    "agua": 0.29,               # kg CO2e por m³
}

# Botão para calcular
if st.button("Calcular Pegada de Carbono"):
    # Calcula o consumo anual
    consumo_anual = {
        "energia_eletrica": energia_eletrica * 12,
        "gas_natural": gas_natural * 12,
        "glp": glp * 12,
        "gasolina": gasolina * 12,
        "diesel": diesel * 12,
        "residuos": residuos * 12,
        "agua": agua * 12,
    }

    # Calcula as emissões
    emissoes = {
        "energia_eletrica": calcular_emissoes(consumo_anual["energia_eletrica"], fatores["energia_eletrica"]),
        "gas_natural": calcular_emissoes(consumo_anual["gas_natural"], fatores["gas_natural"]),
        "glp": calcular_emissoes(consumo_anual["glp"], fatores["glp"]),
        "gasolina": calcular_emissoes(consumo_anual["gasolina"], fatores["gasolina"]),
        "diesel": calcular_emissoes(consumo_anual["diesel"], fatores["diesel"]),
        "residuos": calcular_emissoes(consumo_anual["residuos"], fatores["residuos"]),
        "agua": calcular_emissoes(consumo_anual["agua"], fatores["agua"]),
    }

    # Calcula a pegada total em toneladas
    pegada_total = sum(emissoes.values()) / 1000  # Converte kg para toneladas

    # Exibe os resultados
    st.header("Resultados")
    st.write(f"Sua pegada de carbono anual é **{pegada_total:.2f} toneladas de CO₂e**.")

    # Detalhamento das emissões
    st.subheader("Detalhamento das Emissões:")
    df_emissoes = pd.DataFrame({
        "Fonte": [
            "Energia Elétrica",
            "Gás Natural",
            "GLP",
            "Gasolina",
            "Diesel",
            "Resíduos Orgânicos",
            "Água",
        ],
        "Emissões Anuais (kg CO₂e)": list(emissoes.values()),
    })
    st.table(df_emissoes)

    # Gráfico de barras
    st.subheader("Distribuição das Emissões")
    st.bar_chart(df_emissoes.set_index("Fonte"))

    # Dicas para redução
    st.header("Dicas para Reduzir sua Pegada de Carbono")
    st.write("- **Eficiência Energética**: Utilize lâmpadas LED e eletrodomésticos com selo Procel A.")
    st.write("- **Transporte Sustentável**: Opte por caminhar, pedalar ou utilizar transporte público.")
    st.write("- **Consumo Consciente**: Reduza o desperdício de água e alimentos.")
    st.write("- **Energias Renováveis**: Considere a instalação de painéis solares.")
    st.write("- **Reciclagem**: Separe resíduos recicláveis e orgânicos.")

# Rodapé
st.markdown("---")
st.write("Esta calculadora fornece uma estimativa baseada em fatores médios de emissão. Para um cálculo mais preciso, consulte fontes especializadas.")


