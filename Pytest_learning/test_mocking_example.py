"""
Small Example of Mocking in Python 
==================================================
Mocking is used to replace real objects with fake ones during testing.
"""

from unittest.mock import Mock, patch, MagicMock


# -------------------------------------------------
# Real function (must be at module level for patch)
# -------------------------------------------------
def get_user_from_api(user_id):
    import time
    time.sleep(1)  # Simulates slow API call
    return {"id": user_id, "name": "Real User", "email": "real@example.com"}


# Example 1: Basic Mocking with Mock()
# ------------------------------------
def test_basic_mock():
    mock_obj = Mock()

    mock_obj.get_data.return_value = {"name": "John", "age": 30}

    result = mock_obj.get_data()

    assert result == {"name": "John", "age": 30}
    mock_obj.get_data.assert_called_once()


# Example 2: Mocking a function with patch()
# ------------------------------------------
def test_mock_external_api():

    # Patch using correct module reference
    with patch(__name__ + ".get_user_from_api") as mock_api:

        mock_api.return_value = {
            "id": 1,
            "name": "Test User",
            "email": "test@example.com"
        }

        result = get_user_from_api(1)

        assert result["name"] == "Test User"
        assert result["email"] == "test@example.com"

        mock_api.assert_called_with(1)


# Example 3: Mocking a class method
# ----------------------------------
class Database:
    def __init__(self):
        self.connected = False

    def connect(self):
        import time
        time.sleep(2)
        self.connected = True
        return "Connected to database"

    def get_user(self, user_id):
        return {"id": user_id, "username": "real_user"}


def test_mock_database():
    mock_db = Mock(spec=Database)

    mock_db.connect.return_value = "Mocked connection"
    mock_db.get_user.return_value = {
        "id": 1,
        "username": "mocked_user"
    }

    result = mock_db.connect()
    user = mock_db.get_user(1)

    assert result == "Mocked connection"
    assert user["username"] == "mocked_user"


# Example 4: MagicMock
# ---------------------
def test_magic_mock():
    mock_obj = MagicMock()

    mock_obj.name = "Test Object"

    mock_obj.get_user().get_profile().update_settings()

    mock_obj.get_user.assert_called_once()
    mock_obj.get_user().get_profile.assert_called_once()
    mock_obj.get_user().get_profile().update_settings.assert_called_once()


# Example 5: side_effect
# -----------------------
def test_mock_with_side_effect():
    mock_function = Mock()

    mock_function.side_effect = [
        {"status": "success", "data": [1, 2, 3]},
        {"status": "success", "data": [4, 5, 6]},
        {"status": "error", "message": "No more data"}
    ]

    result1 = mock_function()
    assert result1["data"] == [1, 2, 3]

    result2 = mock_function()
    assert result2["data"] == [4, 5, 6]

    result3 = mock_function()
    assert result3["status"] == "error"


# Example 6: Proper datetime mocking
# -----------------------------------
import datetime


@patch(__name__ + ".datetime")
def test_mock_datetime(mock_datetime):

    mock_now = Mock()
    mock_now.year = 2024
    mock_now.month = 1
    mock_now.day = 1

    mock_datetime.datetime.now.return_value = mock_now

    current_time = datetime.datetime.now()

    assert current_time.year == 2024
    assert current_time.month == 1
    assert current_time.day == 1


# -------------------------------------------------
# Run manually (optional)
# -------------------------------------------------
if __name__ == "__main__":

    print("Running Mocking Examples...")
    print("=" * 50)

    test_basic_mock()
    print("✓ Test 1 passed")

    test_mock_external_api()
    print("✓ Test 2 passed")

    test_mock_database()
    print("✓ Test 3 passed")

    test_magic_mock()
    print("✓ Test 4 passed")

    test_mock_with_side_effect()
    print("✓ Test 5 passed")

    test_mock_datetime()
    print("✓ Test 6 passed")

    print("=" * 50)
    print("All mocking examples passed!")