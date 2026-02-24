''''without Fixtures'''

def test_user_name():
    user = {"name":"Alice","age":25}  #repeated
    assert user ["name"] == "Alice"

def test_user_age():
    user = {"name":"Alice","age":25}  #repeted again 
    assert user ["age"] ==25



'''  Fixture   '''

import pytest
@pytest.fixture
def user():
    return {"name":"Alice","age":25}

# pytest sees 'user' as a parameter and automatically injects it 
def test_user_name(user):
    assert user ["name"] =="Alice"

def test_user_age(user):
    assert user["age"] ==25
    ''''You never call user() yourself — pytest handles it.'''