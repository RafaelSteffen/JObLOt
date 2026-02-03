import streamlit as st
from pathlib import Path

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Sistema de Análise v1.0", layout="wide")

# utilidades para localizar/abrir histórico
HISTORY_FILENAMES = ["loto.txt", "loto", "historico.txt", "historico"]
SEARCH_DIRS = [Path.cwd(), Path.cwd() / "data", Path.cwd() / "historico", Path.cwd() / "assets"]

def find_history_files():
    found = []
    for base in SEARCH_DIRS:
        for name in HISTORY_FILENAMES:
            p = base / name
            if p.exists() and p.is_file():
                found.append(p)
    # também procurar recursivamente na pasta atual por arquivos que contenham 'loto' no nome
    for p in Path.cwd().rglob("*loto*.txt"):
        if p.is_file() and p not in found:
            found.append(p)
    return found

def read_text_file(path: Path):
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            return path.read_text(encoding="latin-1")
        except Exception as e:
            return f"Erro ao ler o arquivo: {e}"

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

    st.write("O app procura automaticamente por arquivos de histórico (ex.: 'loto.txt').")
    found = find_history_files()
    uploaded_file = st.file_uploader("Ou faça upload do arquivo de histórico (txt)", type=["txt"]) 

    content = None
    selected_path = None

    if uploaded_file is not None:
        try:
            content = uploaded_file.read().decode("utf-8")
        except Exception:
            uploaded_file.seek(0)
            try:
                content = uploaded_file.read().decode("latin-1")
            except Exception as e:
                st.error(f"Não foi possível decodificar o arquivo enviado: {e}")

    elif found:
        options = [str(p) for p in found]
        selected = st.selectbox("Arquivos encontrados", options)
        if st.button("Carregar arquivo selecionado"):
            selected_path = Path(selected)
            content = read_text_file(selected_path)

    else:
        st.warning("Nenhum arquivo de histórico encontrado nos diretórios padrão. Faça upload ou coloque o arquivo em 'data/' ou 'historico/'.")

    if content:
        st.subheader("Conteúdo do Histórico")
        st.text_area("Arquivo", content, height=300)
        # Aqui você pode inserir parsing do conteúdo (ex.: converter linhas em concursos)
        # Exemplo muito simples:
        linhas = [l.strip() for l in content.splitlines() if l.strip()]
        st.write(f"Linhas encontradas: {len(linhas)}")
        if st.checkbox("Mostrar primeiras 10 linhas"):
            st.write(linhas[:10])

elif opcao == "Estatísticas de Dezenas":
    st.title("📊 Estatísticas e Tendências")
    st.write("Gráficos e tabelas de frequência aparecerão aqui.")

elif opcao == "Configurações":
    st.title("⚙️ Configurações do Sistema")
    st.checkbox("Habilitar notificações")
    st.color_picker("Escolha a cor do tema")