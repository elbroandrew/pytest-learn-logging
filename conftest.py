import pytest
from configparser import SafeConfigParser


@pytest.fixture(scope="function", autouse=True)
def base_url():
    config_file = 'app_config.ini'
    parser = SafeConfigParser()
    parser.read(config_file)

    return parser.get('httpbin', 'url')



