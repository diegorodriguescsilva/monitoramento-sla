from prometheus_client import start_http_server, Gauge
import random
import time
import os

# Pega os limites mínimo e máximo da faixa da simulação das variáveis de ambiente
MIN_SLA = float(os.getenv('MIN_SLA', 10))
MAX_SLA = float(os.getenv('MAX_SLA', 50))

sla_delivery_time = Gauge('sla_delivery_time_hours', 'Tempo de entrega em horas')

def atualizar_metricas():
    tempo_entrega_simulado = random.uniform(MIN_SLA, MAX_SLA)
    sla_delivery_time.set(tempo_entrega_simulado)
    print(f"Metric updated: sla_delivery_time_hours = {tempo_entrega_simulado:.2f}")

if __name__ == '__main__':
    start_http_server(8000)
    print("Prometheus metrics server started on port 8000")
    print(f"Simulação de SLA entre {MIN_SLA} e {MAX_SLA} horas")

    while True:
        atualizar_metricas()
        time.sleep(2)
