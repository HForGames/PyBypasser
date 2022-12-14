import base64
import requests


class utils:
    def __init__(self, debug=False, proxy=None):
        self.debug = debug
        self.proxy = proxy
        self.userAgent = 'Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36'

    def print_debug(self, message):
        if self.debug:
            print(message)

    def request(self, status_code_should, request_params):
        if self.proxy is not None:
            request_params["proxies"] = self.proxy
        self.print_debug(f"request : {request_params}")
        response = requests.request(**request_params)
        if status_code_should is not None and response.status_code != status_code_should:
            raise ValueError(f"status code should be 200 but is {response.status_code}")
        return response

    def change_proxy(self, proxy):
        self.proxy = proxy

    @staticmethod
    def raise_not_own():
        raise Exception("This url can't be bypass by this class")

    @staticmethod
    def encode_base64(string):
        return base64.b64encode(string.encode('ascii')).decode('utf-8')

    @staticmethod
    def decode_base64(string):
        return base64.b64decode(string.encode('ascii')).decode('utf-8')
