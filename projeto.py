import streamlit as st
import pandas as pd
import pyodbc
import ollama
import os
from dotenv import load_dotenv

# Carrega as senhas do arquivo .env (que não vai para o GitHub)
load_dotenv()

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Dashboard FtFaturamento", layout="wide")

# --- CONEXÃO SQL SERVER SEGURA ---
@st.cache_data
def carregar_dados():
    # Puxa as credenciais das variáveis de ambiente
    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_DATABASE")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    conn_str = (
        "Driver={ODBC Driver 17 for SQL Server};"
        f"Server={server};"  
        f"Database={database};"
        f"UID={user};"
        f"PWD={password};"
    )
    try:
        conn = pyodbc.connect(conn_str)
        query = """
        SELECT 
            dt_emis_nota, nome_ab_cli, cod_rep, it_codigo, 
            vl_merc_liq, peso_liq_fat, nat_operacao, cod_estabel
        FROM FtFaturamento
        """
        df = pd.read_sql(query, conn)
        conn.close()
        
        df['dt_emis_nota'] = pd.to_datetime(df['dt_emis_nota'])
        return df
    except Exception as e:
        st.error(f"❌ Erro na Conexão: {e}")
        return pd.DataFrame()

# ... (Restante do seu código do Streamlit e filtros entra aqui) ...
