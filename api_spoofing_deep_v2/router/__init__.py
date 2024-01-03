
from fastapi import APIRouter

start = APIRouter()


@start.get('/', summary="Welcome to to Spoofing Deep v2 API",
           status_code=200)
def welcome():
    return 'Welcome to Spoofing Deep v2 API, ' \
           'read documentation in /docs for further questions.'


@start.get('/health', summary="API is up?", status_code=200)
def health():
    return 'UP'