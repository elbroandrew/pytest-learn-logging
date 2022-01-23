import configparser
import logging


class Api:
    LOGGER = logging.getLogger(__name__)
    parser = configparser.ConfigParser()
    parser.read('app_config.ini')

    BASE_URL = parser.get("httpbin", "url")
    HEADERS_ISSUE = BASE_URL + "/headers"
    STATUS_CODE_ISSUE = BASE_URL + "/status/{codes}"

    @staticmethod
    def check_connection():
        pass
