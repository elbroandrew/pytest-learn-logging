import requests
import logging
from jsonschema import validate


def test_get_headers(base_url):
    logging.info("Testing status code 200 -- send request to /headers")
    res = requests.get(f"{base_url}/headers")
    logging.info("Done.")
    assert 200 == res.status_code

    schema = {
        "type": "object",
        "properties": {
            "headers": {"type": "object"}
        },
        "required": ["headers"]
    }

    validate(instance=res.json(), schema=schema)

