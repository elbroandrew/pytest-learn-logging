import logging
import pytest
from _pytest.runner import CallInfo
from configparser import ConfigParser



@pytest.fixture(scope="function", autouse=False)
def base_url():
    config_file = 'app_config.ini'
    config = ConfigParser()
    config.read(config_file)

    return config['url']['httpbin']


def pytest_exception_interact(node, call: CallInfo, report):
    logger = logging.getLogger(__name__)
    if report.failed:
        logger.error(call.excinfo)

