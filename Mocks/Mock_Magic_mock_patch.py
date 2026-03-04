"""Unit Test Cases for Mocking in Python - unittest.mock"""
from unittest.mock import Mock, MagicMock, patch


# Test Case 1: Mock with return value
def test_mock_with_return_value():
    mock_obj = Mock()
    mock_obj.return_value = 10
    assert mock_obj() == 10


# Test Case 2: Mock with side_effect iterable
def test_mock_with_side_effect_iterable():
    mock_iter = Mock(side_effect=[1, 2, 3])
    assert mock_iter() == 1
    assert mock_iter() == 2
    assert mock_iter() == 3


# Test Case 3: Mock with side_effect callable
def test_mock_with_side_effect_callable():
    def multiplier(x): return x * 2
    mock_func = Mock(side_effect=multiplier)
    assert mock_func(5) == 10


# Test Case 4: MagicMock with __len__
def test_magicmock_with_len():
    mock_list = MagicMock()
    mock_list.__len__.return_value = 5
    assert len(mock_list) == 5


# Test Case 5: MagicMock with __str__
def test_magicmock_with_str():
    mock_obj = MagicMock()
    mock_obj.__str__.return_value = "Mocked String"
    assert str(mock_obj) == "Mocked String"


# Test Case 6: MagicMock with __getitem__
def test_magicmock_with_getitem():
    mock_dict = MagicMock()
    mock_dict.__getitem__.return_value = "value"
    assert mock_dict["key"] == "value"


# Test Case 7: Patch decorator - test with a local function
def get_data():
    return "Real data"



# Test Case 8: Patch context manager
def test_patch_context_manager():
    original = get_data
    import unittest.mock
    with unittest.mock.patch('Mocks.Mock_Magic_mock_patch.get_data', return_value="Patched Data"):
        from Mocks.Mock_Magic_mock_patch import get_data as gd
        assert gd() == "Patched Data"


# Test Case 9: Mock user_service function
def test_get_user_name():
    from Mocks.user_service import get_user_name
    fake_db = Mock()
    fake_db.get_name.return_value = "Chatvika"
    result = get_user_name(fake_db)
    assert result == "Chatvika"
    fake_db.get_name.assert_called_once()


# Test Case 10: Verify call arguments
def test_verify_call_arguments():
    mock_func = Mock()
    mock_func("arg1", key="value")
    mock_func.assert_called_once_with("arg1", key="value")


# Test Case 11: Mock with attribute
def test_mock_with_attribute():
    mock_obj = Mock()
    mock_obj.name = "Test"
    assert mock_obj.name == "Test"


# Test Case 12: Mock calling multiple times
def test_mock_multiple_calls():
    mock_obj = Mock(return_value=10)
    assert mock_obj() == 10
    assert mock_obj() == 10
    assert mock_obj.call_count == 2

