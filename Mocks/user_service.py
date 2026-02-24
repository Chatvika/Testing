'''MOCKS: A Mock is a fake object that replaces a real object during testing.'''

def get_user_name(database):
    return database.get_name()

from unittest.mock import Mock
from user_service import get_user_name

def test_get_user_name():
    
    # Create fake database
    fake_db = Mock()
    
    # Define return value
    fake_db.get_name.return_value = "Chatvika"

    # Call function
    result = get_user_name(fake_db)

    # Assert
    assert result == "Chatvika"

    # Verify method was called
    fake_db.get_name.assert_called_once()