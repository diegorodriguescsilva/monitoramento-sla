# Esté arquivo é responsável por coletar métricas da aplicação Python

- Prometheus irá coletar as métricas a cada 5 segundos

  `scrape_interval: 5s`  

- Nome do "trabalho" de coleta de métricas

    `job_name: 'sla_app'`  

- Endereço do serviço (o nome 'app' vem do docker-compose)

     `targets: ['app:8000']`