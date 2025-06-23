## Projeto de Monitoramento de SLA com Métricas Personalizadas


Este projeto tem como objetivo construir um monitoramento de SLA (Service Level Agreement) utilizando Prometheus, Grafana e uma aplicação Python que expõe métricas personalizadas.

## Estrutura do projeto 
```
monitoramento-sla/
│
├── app/
│   ├── app.py                # Código principal da aplicação que expõe as métricas
│   └── requirements.txt      # Dependências da aplicação 
│
├── prometheus/
│   └── prometheus.yml        # Configuração do Prometheus 
│
├── docker-compose.yml        # Orquestração dos containers (app, Prometheus, Grafana)
├── Dockerfile                # Dockerfile da aplicação Python
└── README.md                 # Documentação do projeto 
```


### Pré-requisitos:

- Docker

### O que você vai ter que fazer:

- Configurar código Python (`app/app.py`) que simula o tempo de entrega (SLA) gerando valores aleatórios dentro de uma faixa configurável via variáveis de ambiente (`MIN_SLA` e `MAX_SLA`).

- Configurar Prometheus para coletar métricas expostas pelo app no endpoint `/metrics`.

- Configurar Grafana para visualizar as métricas coletadas do Prometheus em dashboards customizados.

- Utilizar Docker Compose para orquestrar os serviços, facilitando o setup e deploy.

# Como executar o projeto: 

# 1. Instale o Docker e verifique sua versão
    
    docker --version

# 2. Faça o clone do projeto 

    git clone https://github.com/diegorodriguescsilva/monitoramento-sla.git

# 3. Execute o projeto

    docker compose up --build

# 4 -  Acesse os serviços através do navegador

| Serviço                   | URL                                                            | Função                         |
| ------------------------- | -------------------------------------------------------------- | ------------------------------ |
| **App Python (métricas)** | [http://localhost:8000/metrics](http://localhost:8000/metrics) | Mostra as métricas geradas     |
| **Prometheus**            | [http://localhost:9090](http://localhost:9090)                 | Coleta e consulta as métricas  |
| **Grafana**               | [http://localhost:3000](http://localhost:3000)                 | Visualiza os dados em gráficos |

# 5 -  Faça o login no Grafana
 
  - Acesse o localhost do Grafana e entre com usuário admin e senha admin. Logo depois altere a senha. 

# 6 - Crie Dashboard com o Grafana

- Clique em “+” > Dashboard.

 - Clique em “Add a new panel”.
 - No campo de consulta (query), escreva:
   
   `sla_delivery_time_hours`

- No topo, selecione a fonte de dados `prometheus`.

- Clique em **Apply**.

- Se você fez tudo certo, você verá os dados sendo atualizados em tempo real.


# 7 - Personalize os valores do simulador

- Edite o arquivo `docker-compose.ym`.

- No arquivo `app.py`, altere:

```environment:
  - MIN_SLA=10
  - MAX_SLA=50
```

- Após as alterações reinicie o projeto. 

`docker compose up --build`

# 8 - Quando quiser para o projeto:

 `docker compose down`


