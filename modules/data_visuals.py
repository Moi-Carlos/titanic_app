import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ================================================================
# 1. Histograma da Distribuição de Idade
# ================================================================
def hist_age(df):
    st.subheader('Histograma da Distribuição de Idade dos Passageiros')
    fig, ax = plt.subplots()
    ax.hist(df['age'].dropna(), bins=20, color='skyblue', edgecolor='black')
    ax.set_xlabel('Idade')
    ax.set_ylabel('Quantidade')
    ax.set_title('Distribuição de Idade dos Passageiros')
    st.pyplot(fig)
    st.markdown('**Conclusão:** A distribuição é concentrada em adultos jovens (entre 20 e 40 anos).')


# ================================================================
# 2. Dispersão Idade vs Tarifa (colorido por sobrevivência e estilo por classe)
# ================================================================
def scatter_age_fare(df):
    st.subheader('Dispersão: Idade vs Tarifa (colorido por sobrevivência e estilo por classe)')

    # Converter survived para string para aplicar corretamente o mapa de cores
    df['survived_str'] = df['survived'].astype(str)

    # Mapa de cores: 0 = vermelho, 1 = azul
    color_map = {'0': 'red', '1': 'blue'}

    # Gráfico de dispersão com cores e estilos personalizados
    fig = px.scatter(
        df,
        x='age',
        y='fare',
        color='survived_str',
        color_discrete_map=color_map,
        symbol='pclass',
        opacity=0.8,
        size_max=8,
        labels={
            'age': 'Idade',
            'fare': 'Tarifa',
            'survived_str': 'Sobreviveu',
            'pclass': 'Classe'
        },
        title='Idade vs Tarifa dos Passageiros'
    )

    st.plotly_chart(fig, use_container_width=True)
    st.markdown('**Conclusão:** Passageiros que pagaram tarifas mais altas (1ª classe) tiveram maiores chances de sobrevivência.')


# ================================================================
# 3. Boxplot de Idade por Sexo e Sobrevivência
# ================================================================
def boxplot_age_sex_survived(df):
    st.subheader('Boxplot: Idade por Sexo e Sobrevivência')
    if {'sex', 'age', 'survived'}.issubset(df.columns):
        df = df.copy()

        # Garantir ordem e cores corretas
        order = ['female', 'male']
        palette = {0: '#ff9999', 1: '#66b3ff'}

        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(
            data=df,
            x='sex',
            y='age',
            hue='survived',
            order=order,
            palette=palette,
            ax=ax
        )
        ax.set_title('Idade por Sexo e Sobrevivência')
        ax.set_xlabel('Sexo')
        ax.set_ylabel('Idade')
        ax.set_xticklabels(['Mulher', 'Homem'])
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, ['Não Sobreviveu', 'Sobreviveu'], title='Situação')

        st.pyplot(fig)
        plt.clf()
        st.markdown('**Conclusão:** Mulheres e crianças sobreviveram em maior proporção, confirmando o protocolo “mulheres e crianças primeiro”.')
    else:
        st.warning("As colunas 'sex', 'age' e 'survived' não estão disponíveis no dataset.")



# ================================================================
# 4. Taxa de Sobrevivência por Porto de Embarque
# ================================================================
def bar_survival_by_embark(df):
    st.subheader('Taxa de Sobrevivência por Porto de Embarque')
    if 'embark_town' not in df.columns:
        st.warning('Coluna de porto de embarque não disponível neste dataset.')
        return
    grouped = df.groupby('embark_town')['survived'].mean().reset_index()
    fig = px.bar(grouped, x='embark_town', y='survived',
                 labels={'embark_town':'Porto', 'survived':'Taxa de Sobrevivência'},
                 title='Sobrevivência por Porto de Embarque')
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('**Conclusão:** Passageiros que embarcaram em Cherbourg (C) apresentaram maior taxa de sobrevivência.')


# ================================================================
# 5. Gráfico de Violino – Distribuição de Idade por Sobrevivência
# ================================================================
def violin_age_survived(df):
    st.subheader('Distribuição de Idade por Sobrevivência (Gráfico de Violino)')
    fig, ax = plt.subplots()
    sns.violinplot(data=df, x='survived', y='age', palette='pastel', ax=ax)
    ax.set_title('Distribuição de Idade por Sobrevivência')
    ax.set_xlabel('Sobreviveu')
    ax.set_ylabel('Idade')
    st.pyplot(fig)
    st.markdown('**Conclusão:** Sobreviventes tendem a ter idades um pouco menores em média.')


# ================================================================
# 6. Histograma da Tarifa
# ================================================================
def hist_fare(df):
    st.subheader('Histograma da Tarifa (Fare)')
    fig, ax = plt.subplots()
    ax.hist(df['fare'].dropna(), bins=20, color='orange', edgecolor='black')
    ax.set_xlabel('Tarifa')
    ax.set_ylabel('Quantidade')
    ax.set_title('Distribuição das Tarifas Pagas')
    st.pyplot(fig)
    st.markdown('**Conclusão:** A maioria dos passageiros pagou tarifas baixas, mas há uma minoria que pagou valores muito altos (1ª classe).')


# ================================================================
# 7. Gráfico de Densidade de Idade por Sobrevivência
# ================================================================
def kde_age_survived(df):
    st.subheader("📈 Densidade de Idade por Sobrevivência")

    df = df.copy()
    if 'age' in df.columns and 'survived' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.kdeplot(data=df, x='age', hue='survived', fill=True, palette={0: 'red', 1: 'blue'})
        plt.title("Densidade de Idade por Sobrevivência")
        plt.xlabel("Idade")
        plt.ylabel("Densidade")
        plt.legend(title="Sobreviveu", labels=["Não", "Sim"])

        st.pyplot(plt)
        plt.clf()

        st.markdown("""
        **Conclusão:**  
        - Passageiros jovens (crianças) tinham maiores chances de sobrevivência.  
        - A faixa entre **20 e 40 anos** concentra a maioria das vítimas.  
        - Mostra a importância da idade no critério de resgate.
        """)
    else:
        st.warning("As colunas 'age' e 'survived' não estão disponíveis no dataset.")


# ================================================================
# 8. Boxplot – Idade por Classe (Pclass)
# ================================================================
def boxplot_age_pclass(df):
    st.subheader('Boxplot: Idade por Classe (Pclass)')
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x='pclass', y='age', ax=ax, palette='coolwarm')
    ax.set_title('Idade dos Passageiros por Classe')
    ax.set_xlabel('Classe')
    ax.set_ylabel('Idade')
    st.pyplot(fig)
    st.markdown('**Conclusão:** Passageiros da 1ª classe eram, em média, mais velhos que os da 3ª classe.')


# ================================================================
# 9. Gráfico de Barras Empilhadas – Sobreviventes por Classe e Gênero
# ================================================================
def stacked_bar_survival_class_gender(df):
    st.subheader("🧍‍♀️🧍‍♂️ Distribuição de Passageiros por Classe e Gênero")

    df = df.copy()
    if 'pclass' in df.columns and 'sex' in df.columns:
        df['Sex_pt'] = df['sex'].map({'male': 'Homem', 'female': 'Mulher'})

        plt.figure(figsize=(10, 6))
        sns.countplot(data=df, x='pclass', hue='Sex_pt', palette={'Mulher': '#ff9999', 'Homem': '#66b3ff'})
        plt.title("Distribuição de Passageiros por Classe e Gênero")
        plt.xlabel("Classe do Passageiro")
        plt.ylabel("Quantidade de Passageiros")
        plt.legend(title="Gênero")

        st.pyplot(plt)
        plt.clf()

        st.markdown("""
        **Conclusão:**  
        - A **3ª classe** tem maioria masculina.  
        - As **mulheres** predominam nas classes superiores.  
        - Reflete a divisão socioeconômica a bordo do Titanic.
        """)
    else:
        st.warning("As colunas 'pclass' e 'sex' não estão disponíveis no dataset.")


# ================================================================
# 10. Gráfico de Barras – Taxa Percentual de Sobrevivência por Gênero
# ================================================================
def bar_survival_by_gender(df):
    st.subheader('Taxa Percentual de Sobrevivência por Gênero')
    grouped = df.groupby('sex')['survived'].mean().reset_index()
    fig = px.bar(grouped, x='sex', y='survived',
                 labels={'sex':'Gênero', 'survived':'Taxa de Sobrevivência (%)'},
                 title='Taxa de Sobrevivência por Gênero')
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('**Conclusão:** Mulheres apresentaram taxa de sobrevivência muito superior à dos homens.')
