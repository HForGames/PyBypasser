from .utils import utils
from urllib.parse import urlparse

class Redirect:
    def __init__(self, debug=False, proxy=None):
        self.urlparse = None
        self.__utils = utils(debug=debug, proxy=proxy)

    def is_own(self, url):
        self.urlparse = urlparse(url)
        self.__utils.print_debug(f"urlparse : {self.urlparse}")
        with open("redirect", "r") as f:
            all_redirect = f.read().splitlines()
        return self.urlparse.netloc in all_redirect

    def bypass(self, url):
        response = self.__utils.request(None, {
            "method": "GET",
            "url": url,
            "headers": {
                "User-Agent" : self.__utils.userAgent
            }
        })
        return response.url


