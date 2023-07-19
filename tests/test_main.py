import pytest
from fastapi import HTTPException

from course_test.main import authorize_token, get_token, salary, next_promotion, get_salary


def test_authorize_token_with_valid_token():
    token = "your_access_token"
    response = authorize_token(token)
    assert response == token


def test_authorize_token_with_invalid_token():
    token = "invalid_token"
    with pytest.raises(HTTPException):
        authorize_token(token)


def test_get_token_with_valid_credentials():
    username = "user"
    password = "password"
    response = get_token(username, password)
    assert response["access_token"] == "your_access_token"
    assert response["token_type"] == "bearer"


def test_get_token_with_invalid_credentials():
    username = "invalid_user"
    password = "invalid_password"
    with pytest.raises(HTTPException):
        get_token(username, password)


def test_get_salary():
    expected_salary = {"salary": salary, "next_promotion": next_promotion.strftime("%Y-%m-%d")}
    response = get_salary()
    assert response == expected_salary
