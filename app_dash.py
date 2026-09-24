import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# 1. Carregar os dados
df = pd.read_csv('ecommerce_estatistica.csv')

# 2. Inicializar a aplicação Dash
app = dash.Dash(__name__, title="Dashboard E-commerce")

# 3. Criar os gráficos interativos com Plotly
# 1. Histograma
fig_hist = px.histogram(
    df, x='Preço', nbins=20,
    title="Distribuição dos Preços dos Produtos",
    labels={'Preço': 'Preço (R$)', 'count': 'Frequência'},
    color_discrete_sequence=['#3366CC']
)
fig_hist.update_layout(template="plotly_white")

# 2. Gráfico de Dispersão
fig_scatter = px.scatter(
    df, x='Preço', y='N_Avaliações', color='Gênero',
    log_y=True,
    title="Relação entre Preço e Número de Avaliações (Escala Log)",
    labels={'Preço': 'Preço (R$)', 'N_Avaliações': 'Nº de Avaliações', 'Gênero': 'Gênero Target'},
    hover_data=['Título']
)
fig_scatter.update_layout(template="plotly_white")

# 3. Mapa de Calor (Matriz de Correlação)
cols_corr = ['Nota', 'N_Avaliações', 'Desconto', 'Preço', 'Qtd_Vendidos_Cod']
corr_matrix = df[cols_corr].corr().round(2)
fig_heatmap = px.imshow(
    corr_matrix, text_auto=True, color_continuous_scale='Blues',
    title="Mapa de Calor - Correlação entre Variáveis Numéricas"
)
fig_heatmap.update_layout(template="plotly_white")

# 4. Gráfico de Barra
top_materiais = df['Material'].value_counts().head(8).reset_index()
top_materiais.columns = ['Material', 'Quantidade']
fig_bar = px.bar(
    top_materiais, x='Quantidade', y='Material', orientation='h',
    title="Top 8 Materiais Mais Frequentes",
    labels={'Quantidade': 'Quantidade de Produtos', 'Material': 'Material'},
    color='Quantidade', color_continuous_scale='Viridis'
)
fig_bar.update_layout(template="plotly_white", yaxis={'categoryorder': 'total ascending'})

# 5. Gráfico de Pizza
genero_counts = df['Gênero'].value_counts().reset_index()
genero_counts.columns = ['Gênero', 'Quantidade']
fig_pie = px.pie(
    genero_counts, names='Gênero', values='Quantidade',
    title="Distribuição de Produtos por Gênero Target",
    hole=0.3
)
fig_pie.update_layout(template="plotly_white")

# 6. Gráfico de Densidade (Aproximado via Histograma KDE)
fig_density = px.histogram(
    df, x='Desconto', histnorm='probability density', marginal='box',
    title="Curva de Densidade do Percentual de Desconto (%)",
    labels={'Desconto': 'Percentual de Desconto (%)', 'density': 'Densidade'},
    color_discrete_sequence=['#008080']
)
fig_density.update_layout(template="plotly_white")

# 7. Gráfico de Regressão / Tendência Linear
fig_reg = px.scatter(
    df, x='Desconto', y='Preço', trendline="ols",
    title="Tendência Linear: Relação entre Desconto (%) e Preço (R$)",
    labels={'Desconto': 'Desconto (%)', 'Preço': 'Preço (R$)'},
    trendline_color_override="red"
)
fig_reg.update_layout(template="plotly_white")

# 4. Definir o Layout do Dashboard
app.layout = html.Div(style={'fontFamily': 'Arial, sans-serif', 'backgroundColor': '#f4f6f9', 'padding': '20px'}, children=[
    
    html.Div(style={'textAlign': 'center', 'marginBottom': '30px'}, children=[
        html.H1("Dashboard de Análise Estatística - E-Commerce", style={'color': '#1f2c56', 'marginBottom': '10px'}),
        html.P("Visualização interativa das métricas de preços, descontos, avaliações e categorias do arquivo ecommerce_estatistica.csv", style={'color': '#666', 'fontSize': '16px'})
    ]),
    
    html.Div(style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'gap': '20px'}, children=[
        html.Div(dcc.Graph(figure=fig_hist), style={'backgroundColor': '#fff', 'padding': '15px', 'borderRadius': '8px', 'boxShadow': '0 2px 5px rgba(0,0,0,0.1)'}),
        html.Div(dcc.Graph(figure=fig_scatter), style={'backgroundColor': '#fff', 'padding': '15px', 'borderRadius': '8px', 'boxShadow': '0 2px 5px rgba(0,0,0,0.1)'}),
        html.Div(dcc.Graph(figure=fig_heatmap), style={'backgroundColor': '#fff', 'padding': '15px', 'borderRadius': '8px', 'boxShadow': '0 2px 5px rgba(0,0,0,0.1)'}),
        html.Div(dcc.Graph(figure=fig_bar), style={'backgroundColor': '#fff', 'padding': '15px', 'borderRadius': '8px', 'boxShadow': '0 2px 5px rgba(0,0,0,0.1)'}),
        html.Div(dcc.Graph(figure=fig_pie), style={'backgroundColor': '#fff', 'padding': '15px', 'borderRadius': '8px', 'boxShadow': '0 2px 5px rgba(0,0,0,0.1)'}),
        html.Div(dcc.Graph(figure=fig_density), style={'backgroundColor': '#fff', 'padding': '15px', 'borderRadius': '8px', 'boxShadow': '0 2px 5px rgba(0,0,0,0.1)'}),
    ]),
    
    html.Div(style={'marginTop': '20px'}, children=[
        html.Div(dcc.Graph(figure=fig_reg), style={'backgroundColor': '#fff', 'padding': '15px', 'borderRadius': '8px', 'boxShadow': '0 2px 5px rgba(0,0,0,0.1)'}),
    ])
])

# 5. Executar o servidor Dash
if __name__ == '__main__':
    app.run_server(debug=True)
