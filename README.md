# 📊 Inteligência em Faturamento: Dashboard Híbrido com IA Local (Llama 3)

Um produto de dados interativo construído em Python que conecta diretamente a um banco SQL Server para transformar dados brutos de faturamento em insights acionáveis. O sistema une filtros determinísticos de alta velocidade com uma análise qualitativa feita por Inteligência Artificial rodando 100% localmente.

## 🎯 O Desafio
O objetivo deste projeto foi criar uma ferramenta analítica para a tabela `FtFaturamento`. A necessidade era ir além do tradicional "o que aconteceu" (tabelas e gráficos) e ajudar a responder "por que aconteceu", mantendo a rigorosa privacidade dos dados financeiros da empresa (sem envio para APIs externas na nuvem). 

## 💡 A Solução (Analítica Híbrida)
Desenvolvi uma arquitetura de Analítica Híbrida dividida em duas camadas:
1. **Corte Fino (Streamlit + PyODBC):** Filtros rápidos na barra lateral permitem segmentar grandes volumes de dados (por Data de Emissão, Cliente e Representante) em milissegundos direto no SQL Server.
2. **Refino Qualitativo (Ollama + Llama 3):** Após o filtro humano, uma IA local recebe o contexto resumido dos dados em tela e atua como um "Controller Virtual", capaz de explicar anomalias, destacar os Top 5 Clientes e sugerir tendências baseadas no período selecionado.

## 🎨 Design e Usabilidade
A interface foi projetada com foco na experiência do usuário e rápida leitura de KPIs (Faturamento Líquido, Peso e Quantidade de Notas). A identidade visual foi customizada para refletir as cores corporativas, com destaque para o **laranja** do DVG GRUPO, garantindo aderência à marca.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Banco de Dados:** SQL Server (via `pyodbc`)
* **Interface & Frontend:** Streamlit
* **Processamento de Dados:** Pandas
* **Inteligência Artificial:** Ollama (rodando o modelo Llama 3 de forma local e privada)

## 🤖 Nota sobre o Desenvolvimento e Uso de IA
**Transparência e Pair Programming:** Como analista em evolução, busco sempre as melhores ferramentas para acelerar minhas entregas. Neste projeto, utilizei modelos de Inteligência Artificial como assistentes de codificação (pair programming) para me ajudar a estruturar as visualizações no Streamlit e otimizar o código Python. 

A IA foi fundamental para acelerar a construção do layout e a arquitetura visual, enquanto a minha atuação técnica focou na implementação das regras de negócio, na segurança da conexão com o banco de dados e na engenharia de prompts para que a IA local gerasse insights coerentes com a realidade comercial.

---
*Desenvolvido por Thyfani.*
