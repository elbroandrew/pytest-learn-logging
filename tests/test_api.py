import requests


def test_get():
    try:
        res = requests.get("https://httpbin.org/headers")
    except requests.exceptions.Timeout as t:
        raise TimeoutError(t)
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(e)


    assert 200 == res.status_code

