import logging
import pytest
from _pytest.runner import CallInfo
from configparser import SafeConfigParser



@pytest.fixture(scope="function", autouse=False)
def base_url():
    config_file = 'app_config.ini'
    parser = SafeConfigParser()
    parser.read(config_file)

    return parser.get('httpbin', 'url')


def pytest_exception_interact(node, call: CallInfo, report):
    logger = logging.getLogger(__name__)
    if report.failed:
        logger.error(call.excinfo)

