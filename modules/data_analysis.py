import streamlit as st
import pandas as pd

# ==========================================================
# Resumo estatístico geral do dataset
# ==========================================================
def summary_statistics(df):
    stats = {
        'Total de Passageiros': len(df),
        'Sobreviventes': int(df['survived'].sum()) if 'survived' in df.columns else 0,
        'Taxa de Sobrevivência (%)': f"{df['survived'].mean() * 100:.2f}%" if 'survived' in df.columns else '0%',
        'Idade Média dos Passageiros': f"{df['age'].mean():.1f}" if 'age' in df.columns else 'N/A',
        'Tarifa Média (Fare)': f"{df['fare'].mean():.2f}" if 'fare' in df.columns else 'N/A',
        'Classe Mais Comum': int(df['pclass'].mode()[0]) if 'pclass' in df.columns else 'N/A',
        'Sexo Mais Frequente': df['sex'].mode()[0] if 'sex' in df.columns else 'N/A'
    }
    return stats


# ==========================================================
# Botão de exportação CSV
# ==========================================================
def export_stats_button(stats):
    df_stats = pd.DataFrame(stats.items(), columns=["Indicador", "Valor"])
    csv = df_stats.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Exportar Estatísticas (CSV)",
        data=csv,
        file_name="titanic_statistics.csv",
        mime="text/csv"
    )


# ==========================================================
# Link para o dataset original (Kaggle)
# ==========================================================
def open_dataset_link():
    kaggle_url = "https://www.kaggle.com/datasets/heptapod/titanic"
    st.markdown(f"[🌐 Acessar Dataset Original no Kaggle]({kaggle_url})", unsafe_allow_html=True)
