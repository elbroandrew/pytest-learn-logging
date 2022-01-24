import requests
import logging
from jsonschema import validate

LOGGER = logging.getLogger(__name__)


def test_get_headers(base_url):
    LOGGER.info("Testing status code 200 -- send request to https://httpbin.org/headers")
    res = requests.get(f"{base_url}/headers")

    try:
        assert 200 == res.status_code
    except AssertionError as e:
        LOGGER.error(e)
        raise AssertionError

    LOGGER.info(f"assert 200 == {res.status_code} status code")
    LOGGER.info("Done.")

    schema = {
        "type": "object",
        "properties": {
            "headers": {"type": "object"}
        },
        "required": ["headers"]
    }

    validate(instance=res.json(), schema=schema)

