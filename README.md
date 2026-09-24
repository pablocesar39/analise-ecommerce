📊 Dashboard de Análise Estatística - E-Commerce

Aplicação web interativa desenvolvida em Python com **Dash** e **Plotly** para visualização e análise exploratória de dados do ficheiro `ecommerce_estatistica.csv`.

---

## 📌 Sobre o Projeto

Este painel interativo foi criado para facilitar a análise visual de dados de produtos de e-commerce, permitindo acompanhar distribuições de preços, estratégias de desconto, volumes de avaliações e correlações entre variáveis numéricas.

### 📈 Gráficos Incluídos no Dashboard
1. **Distribuição dos Preços dos Produtos:** Histograma indicando a frequência dos preços.
2. **Preço vs. Número de Avaliações:** Dispersão (*scatter plot*) com escala logarítmica e separação por gênero target.
3. **Matriz de Correlação (Mapa de Calor):** Correlação linear entre notas, avaliações, descontos, preços e vendas.
4. **Top 8 Materiais Mais Frequentes:** Gráfico de barras horizontais com os materiais mais utilizados.
5. **Distribuição por Gênero Target:** Gráfico de rosca (*pie chart*) da proporção por público-alvo.
6. **Curva de Densidade do Desconto:** Histograma de densidade com *box plot* marginal sobre os descontos (%).
7. **Tendência Linear (Desconto vs. Preço):** Gráfico de dispersão com linha de regressão linear (*OLS*).

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Pandas** (Leitura e tratamento do DataFrame)
- **Dash** (Framework para construção da aplicação web)
- **Plotly Express** (Criação dos gráficos interativos)
- **Statsmodels** (Cálculo da linha de tendência/regressão linear)

---

## 📂 Estrutura do Repositório

```text
├── dash/
│   └── app_dash.py            # Código-fonte da aplicação Dash
├── ecommerce_estatistica.csv   # Ficheiro de dados
├── requirements.txt            # Dependências e bibliotecas do projeto
└── README.md                   # Documentação do projeto
🚀 Como Executar o Projeto Localmente
Clonar o repositório:

Bash
git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
cd NOME_DO_REPOSITORIO
Instalar as dependências:

Bash
pip install -r requirements.txt
Executar a aplicação Dash:

Bash
python dash/app_dash.py
Acessar no navegador:
Abra o endereço exibido no terminal (geralmente http://127.0.0.1:8050/).
