import os
import pytest

from app.robo_advisor import compile_url, transform_response, write_to_csv, to_usd, calculations

CI_ENV = os.environ.get("CI") == "true" # expect default environment variable setting of "CI=true" on Travis CI, see: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables

@pytest.mark.skipif(CI_ENV==True, reason="to avoid configuring credentials on, and issuing requests from, the CI server")

def test_compile_url():
    symbol = "NFLX"

    parsed_response = get_response(symbol)

    assert isinstance(parsed_response, dict)
    assert "Meta Data" in parsed_response.keys()
    assert "Time Series (Daily)" in parsed_response.keys()
    assert parsed_response["Meta Data"]["2. Symbol"] == symbol

