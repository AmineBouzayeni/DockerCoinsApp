import pytest
import requests

def test_get_hostname():
    res = requests.get("http://__IP__:__RNG_TEST_PORT__")
    assert res.status_code == 200

def test_rng():
    res = requests.get("http://__IP__:__RNG_TEST_PORT__/32")
    assert res.status_code == 200