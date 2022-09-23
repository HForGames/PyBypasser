from .utils import utils
from urllib.parse import urlparse


class Redirect(utils):
    def __init__(self, debug=False, proxy=None):
        super().__init__(debug, proxy)
        self.urlparse = None

    def is_own(self, url):
        self.urlparse = urlparse(url)
        self.print_debug(f"urlparse : {self.urlparse}")
        with open("redirect", "r") as f:
            all_redirect = f.read().splitlines()
        return self.urlparse.netloc in all_redirect

    def bypass(self, url):
        response = self.request(None, {
            "method": "GET",
            "url": url,
            "headers": {
                "User-Agent": self.userAgent
            }
        })
        return response.url
