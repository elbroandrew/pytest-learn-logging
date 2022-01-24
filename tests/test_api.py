import requests
from configparser import ConfigParser
import pytest
from jsonschema import validate


def test_get_headers(base_url):
    res = requests.get(f"{base_url}/headers")
    assert 200 == res.status_code

