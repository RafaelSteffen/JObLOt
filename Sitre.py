import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Sistema de Análise v1.0", layout="wide")

# 2. CRIAÇÃO DO MENU LATERAL
with st.sidebar:
    st.title("📂 MENU PRINCIPAL")
    opcao = st.radio(
        "Selecione uma função:",
        ("Página Inicial", 
         "Analisar Novos Jogos", 
         "Consultar Histórico", 
         "Estatísticas de Dezenas",
         "Configurações")
    )
    st.markdown("---")
    st.info("Versão 1.0 - Sistema Zerado")

# 3. LÓGICA DAS PÁGINAS (O que aparece em cada opção)

if opcao == "Página Inicial":
    st.title("🚀 Bem-vindo ao Sistema de Análise")
    st.write("Selecione uma opção no menu à esquerda para começar a operar.")
    
    # Exemplo de Dashboard rápido
    col1, col2, col3 = st.columns(3)
    col1.metric("Último Concurso", "3602")
    col2.metric("Status da Base", "Atualizada")
    col3.metric("Jogos Salvos", "0")

elif opcao == "Analisar Novos Jogos":
    st.title("📝 Analisador de Jogos")
    entrada = st.text_area("Cole seus jogos abaixo:", height=150)
    if st.button("Processar Análise"):
        st.success("Lógica de processamento pronta para ser inserida aqui.")

elif opcao == "Consultar Histórico":
    st.title("🔍 Consulta de Resultados")
    num_concurso = st.number_input("Digite o número do concurso:", min_value=1)
    if st.button("Buscar"):
        st.write(f"Buscando dados do concurso {num_concurso}...")

elif opcao == "Estatísticas de Dezenas":
    st.title("📊 Estatísticas e Tendências")
    st.write("Gráficos e tabelas de frequência aparecerão aqui.")

elif opcao == "Configurações":
    st.title("⚙️ Configurações do Sistema")
    st.checkbox("Habilitar notificações")
    st.color_picker("Escolha a cor do tema")