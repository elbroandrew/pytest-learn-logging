import logging
import pytest
from _pytest.runner import CallInfo


@pytest.fixture(scope="function", autouse=False)
def check_connection():
    pass


def pytest_exception_interact(node, call: CallInfo, report):
    logger = logging.getLogger(__name__)
    if report.failed:
        logger.error(call.excinfo)

