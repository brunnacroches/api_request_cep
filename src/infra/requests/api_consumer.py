from typing import Dict, Tuple, Type
from collections import namedtuple
from requests import Request
import requests
from src.error_handling.http_request_error import HttpRequestError

class ApiConsumer():
    def __init__(self) -> None:
        self.get_ok_message_response = namedtuple('GET_Ok', 'status_code request response')

    def get_ok_message(self) -> Tuple[int, Type[Request], Dict]:
        # Preparando a requisição
        req = requests.Request(
            method='GET',
            url='http://localhost:5007/'
        )
        req_prepared = req.prepare()

        # Enviando a Requisição
        response = self.__send_http_request(req_prepared)
        status_code = response.status_code

        # Analizando a resposta e retornando os valores desejados
        if 200 <= status_code <= 299:
            return self.get_ok_message_response(
                status_code=status_code, request=req, response=response.json()
            )
        raise HttpRequestError(
            message=response.json()["error"], status_code=status_code
        )

    @classmethod
    def __send_http_request(cls, req_prepared: Type[Request]) -> any:
        http_session = requests.Session()
        response = http_session.send(req_prepared)
        return response
