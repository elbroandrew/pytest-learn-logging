import configparser


class Api:
    parser = configparser.ConfigParser()
    parser.read('app_config.ini')

    BASE_URL = parser.get("httpbin", "url")
    HEADERS_ISSUE = BASE_URL + "/headers"
    STATUS_CODE_ISSUE = BASE_URL + "/status/{codes}"