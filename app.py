import streamlit as st
import pandas as pd
from modules import data_loader, data_analysis, data_visuals

st.set_page_config(page_title='Titanic Data Insights', layout='wide')
st.title('🚢 Titanic Data Insights')

# --- Introdução ---
st.markdown("""
**Introdução**  
O naufrágio do Titanic, em 1912, é um dos eventos mais marcantes da história moderna.  
A partir do famoso dataset “Titanic” amplamente utilizado em projetos de Ciência de Dados, este trabalho tem como objetivo analisar estatisticamente os fatores que influenciaram as chances de sobrevivência dos passageiros.  
Utilizando Python, Pandas, Matplotlib e Seaborn, foram aplicadas técnicas de Análise Exploratória de Dados (EDA) para identificar padrões relacionados à idade, gênero, classe social e valor das passagens.
""")

# --- Contextualização Histórica ---
st.markdown("""
**Contextualização Histórica**  
Em 1912, o Titanic naufragou em sua viagem inaugural após colidir com um iceberg, causando a morte de mais de 1.500 pessoas.  
A tragédia ficou marcada na história não apenas pela dimensão do desastre, mas também pelas desigualdades sociais refletidas nas taxas de sobrevivência, aspecto que o presente trabalho busca investigar por meio da análise de dados.
""")

# --- Sidebar ---
st.sidebar.header('📂 Dataset')
uploaded = st.sidebar.file_uploader('Envie um arquivo CSV (opcional)', type=['csv'])
use_default = st.sidebar.button('Usar dataset padrão (seaborn)')

st.sidebar.markdown('---')
st.sidebar.header('🎚️ Filtros')

# Opções de filtros
sex_filter = st.sidebar.multiselect('Sexo', options=['male', 'female'], default=['male', 'female'])
pclass_filter = st.sidebar.multiselect('Classe (Pclass)', options=[1, 2, 3], default=[1, 2, 3])
age_min, age_max = st.sidebar.slider('Faixa etária', 0, 100, (0, 100))

# ✅ Botão para aplicar filtros manualmente
apply_filters = st.sidebar.button('🔍 Aplicar Filtros')

# --- Carregamento dos dados ---
df = None
if uploaded:
    df = data_loader.read_csv(uploaded)
elif use_default:
    df = data_loader.load_default_dataset()
else:
    df = data_loader.load_default_dataset()

if df is None:
    st.warning('Nenhum dataset disponível. Faça upload ou use o dataset padrão.')
    st.stop()

df = data_loader.clean_dataframe(df)

# --- Aplicar filtros apenas quando o botão for clicado ---
if apply_filters:
    if 'sex' in df.columns:
        df = df[df['sex'].isin(sex_filter)]
    if 'pclass' in df.columns:
        df = df[df['pclass'].isin(pclass_filter)]
    if 'age' in df.columns:
        df = df[(df['age'].fillna(0) >= age_min) & (df['age'].fillna(0) <= age_max)]
else:
    st.info('🟡 Ajuste os filtros e clique em **Aplicar Filtros** para atualizar os resultados.')

# --- Estatísticas Gerais ---
st.markdown('---')
st.header('📊 Estatísticas Gerais')
stats = data_analysis.summary_statistics(df)
col1, col2, col3, col4 = st.columns(4)
col1.metric('Total de Passageiros', stats['Total de Passageiros'])
col2.metric('Sobreviventes', stats['Sobreviventes'])
col3.metric('Taxa de Sobrevivência', stats['Taxa de Sobrevivência (%)'])
col4.metric('Idade Média dos Passageiros', stats['Idade Média dos Passageiros'])

# --- Visualizações ---
st.markdown('---')
st.header('📈 Visualizações')

data_visuals.hist_age(df)
data_visuals.scatter_age_fare(df)
data_visuals.boxplot_age_sex_survived(df)
data_visuals.bar_survival_by_embark(df)
data_visuals.violin_age_survived(df)
data_visuals.hist_fare(df)
data_visuals.kde_age_survived(df)
data_visuals.boxplot_age_pclass(df)
data_visuals.stacked_bar_survival_class_gender(df)
data_visuals.bar_survival_by_gender(df)

# --- Amostra de Dados ---
st.markdown('---')
st.subheader('🧾 Amostra dos Dados')
st.dataframe(df.head(200))

# --- Exportar Estatísticas e Link Kaggle ---
st.markdown('---')
st.subheader('📤 Exportar e Consultar')

data_analysis.export_stats_button(stats)
data_analysis.open_dataset_link()

# --- Conclusão Geral ---
st.markdown('---')
st.header('✅ Conclusão Geral')
st.markdown("""
- Mulheres e crianças foram priorizadas nos botes salva-vidas.  
- Passageiros da 1ª classe e com tarifas mais altas sobreviveram mais.  
- A 3ª classe, composta por pessoas com menos recursos, teve as menores chances.  
- O porto de embarque 'C' (Cherbourg) concentrou o maior número de sobreviventes.  
- O padrão social e econômico teve forte influência nas chances de sobrevivência.
""")

# --- Rodapé / Assinatura ---
st.markdown('---')
st.markdown("""
#### 👨‍💻 Desenvolvido por: **Carlos Adangnihande**  
📧 Contato: [carlos.adangnihande@gmail.com](mailto:carlos.adangnihande@gmail.com)  
📅 Projeto: *Titanic Data Insights – Engenharia de Software + Ciência de Dados (2025)*
""")

st.sidebar.markdown('---')
st.sidebar.info('Projeto MVP – Titanic Data Insights (Engenharia de Software + Ciência de Dados)')
