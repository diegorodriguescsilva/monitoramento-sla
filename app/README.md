# Arquivo `Dockerfile`


- Esse arquivo vai construir uma imagem personalizada da aplicação Python que vai gerar as métricas simuladas do SLA

```
Dockerfile
│
├── FROM python:3.10-slim
│   └── Usa imagem base leve do Python 3.10
│
├── WORKDIR /app
│   └── Define o diretório de trabalho no container
│
├── COPY requirements.txt .
│   └── Copia o arquivo de dependências para o container
│
├── RUN pip install --no-cache-dir -r requirements.txt
│   └── Instala as bibliotecas Python listadas no requirements.txt
│
├── COPY app.py .
│   └── Copia o script da aplicação para o container
│
└── CMD ["python", "app.py"]
    └── Inicia a aplicação rodando o arquivo app.py 

```

# Arquivo `app.py`

- Esse arquivo gera os números simulando o SLA e os expõe na rota `/metrics` para que o Prometheus possa coletar e o Grafana exibir em dashboards.

```
app.py
│
├── from flask import Flask, Response
│   └── Importa o Flask para criar a API e Response para retornar dados no formato correto
│
├── import os, random
│   └── Importa módulos para pegar variáveis de ambiente e gerar números aleatórios
│
├── app = Flask(__name__)
│   └── Cria a aplicação Flask
│
├── MIN_SLA = int(os.getenv("MIN_SLA", 10))
├── MAX_SLA = int(os.getenv("MAX_SLA", 50))
│   └── Lê as variáveis de ambiente (ou usa 10 e 50 como padrão) para definir intervalo do SLA
│
├── @app.route("/metrics")
│   └── Cria uma rota da API para o Prometheus acessar as métricas
│
│   └── def metrics():
│       ├── sla_value = random.uniform(MIN_SLA, MAX_SLA)
│       │   └── Gera um valor aleatório entre MIN_SLA e MAX_SLA
│       │
│       ├── data = f"sla_simulation {sla_value:.2f}\n"
│       │   └── Formata o dado no padrão que o Prometheus entende
│       │
│       └── return Response(data, mimetype="text/plain")
│           └── Retorna o valor como texto simples (formato necessário para o Prometheus)
│
└── if __name__ == "__main__":
    └── app.run(host="0.0.0.0", port=8000)
        └── Inicia o servidor Flask acessível em todas as interfaces (porta 8000)

```

# Arquivo `requirements.txt`

- Este arquivo lista todas as bibliotecas que a aplicação precisa para ser executada corretamente. 