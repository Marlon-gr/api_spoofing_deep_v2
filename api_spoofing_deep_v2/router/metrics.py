from fastapi import APIRouter
from prometheus_client import (CollectorRegistry, generate_latest, multiprocess)

metrics_router = APIRouter()


@metrics_router.get('/metrics')
def metrics():
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
    data = generate_latest(registry)
    return data