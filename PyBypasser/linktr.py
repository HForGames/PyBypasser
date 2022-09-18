from urllib.parse import urlparse
from PyBypasser.utils import utils


class Linktr(utils):
    def __init__(self, debug=False, proxy=None):
        super().__init__(debug, proxy)
        self.urlparse = None

    def is_own(self, url):
        self.urlparse = urlparse(url)
        self.print_debug(f"urlparse : {self.urlparse}")
        return self.urlparse.netloc == "Linktr.ee"

    def bypass(self, url):
        response = self.request(None, {
            "method": "GET",
            "url": url,
            "headers": {
                "User-Agent": self.userAgent
            }
        })
        print(response.text)
