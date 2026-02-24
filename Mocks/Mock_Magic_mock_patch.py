'''What is Mocking?

Mocking means replacing a real object (API, database, file, etc.) with a fake object during testing.
'''
from unittest.mock import Mock, MagicMock, patch


'''mock: Basic Fake object'''

from unittest.mock import Mock
mock_obj=Mock()
mock_obj.return_value =10
print(mock_obj())


'''MagicMock:   __len__
                __str__
                __getitem__'''

from unittest.mock import MagicMock
mock_list =MagicMock()
mock_list.__len__.return_value =5

print(len(mock_list))


'''patch :patch() temporarily replaces a real object.'''

from unittest.mock import patch
def get_data():
    return "Real data"

@patch('__main__.get_data')
def test_get_data(mock_func):
    mock_func.return_value = "Fake Data"
    assert get_data() =="Fake Data"