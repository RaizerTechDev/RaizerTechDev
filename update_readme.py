import requests
import json

# Sua chave de API do Wakatime
api_key = 'SUA_CHAVE_DE_API_DO_WAKATIME'

# URL da API do Wakatime para recuperar suas estatísticas de codificação dos últimos 7 dias
url = 'https://wakatime.com/api/v1/users/current/stats/last_7_days'

# Adiciona a chave de API como um cabeçalho de autenticação
headers = {
    'Authorization': f'Basic {api_key}',
}

# Faz a solicitação GET para a API do Wakatime
response = requests.get(url, headers=headers)

# Verifica se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Parseia a resposta JSON
    data = response.json()

    # Extrai as estatísticas desejadas
    total_time = data['data']['human_readable_total']
    # Outras estatísticas que você deseja incluir

    # Formata as estatísticas em Markdown
    markdown_content = f"""
    # Estatísticas de Codificação do Wakatime

    - Tempo Total de Codificação: {total_time}
    # Outras estatísticas desejadas
    """

    # Escreve as estatísticas formatadas em um arquivo README.md local
    with open('README.md', 'w') as f:
        f.write(markdown_content)
else:
    print(f'Erro ao fazer a solicitação: {response.status_code}')
