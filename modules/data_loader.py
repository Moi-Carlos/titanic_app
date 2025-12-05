import pandas as pd
import seaborn as sns

def load_default_dataset():
    try:
        df = sns.load_dataset('titanic')
        if 'alive' in df.columns and 'survived' not in df.columns:
            df['survived'] = df['alive'].map({'yes':1,'no':0})
        if 'class' in df.columns and 'pclass' not in df.columns:
            df['pclass'] = df['class'].map({'First':1,'Second':2,'Third':3})
        return df
    except Exception as e:
        print(f'Erro ao carregar dataset padrão: {e}')
        return None

def read_csv(file):
    return pd.read_csv(file)

def clean_dataframe(df):
    df = df.copy()
    df.columns = [c.lower() for c in df.columns]
    rename_map = {'survived':'survived','pclass':'pclass','sex':'sex','age':'age','fare':'fare'}
    for old, new in rename_map.items():
        if old not in df.columns and old.capitalize() in df.columns:
            df.rename(columns={old.capitalize(): new}, inplace=True)
    if 'age' in df.columns:
        df['age'] = pd.to_numeric(df['age'], errors='coerce')
    if 'sex' in df.columns:
        df['sex'] = df['sex'].astype(str).str.lower()
    if 'pclass' in df.columns:
        df['pclass'] = pd.to_numeric(df['pclass'], errors='coerce')
    return df
