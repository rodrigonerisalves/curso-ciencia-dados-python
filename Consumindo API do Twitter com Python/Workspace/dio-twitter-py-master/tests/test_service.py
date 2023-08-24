from unittest import mock

from src.services import _get_trends


def test_get_trends_with_success():
    # Arrange
    mock_api = mock.Mock()
    mock_api.trends_place.return_value = [
        {
            "trends": [
                {"name": "#Rodrigo%20Neris", "url": "http://twitter.com/search?q=%23Rodrigo%20Neris"},
                {"name": "Rodrigo", "url": "http://twitter.com/search?q=Rodrigo"},
            ]
        }
    ]

    # Act
    trends = _get_trends(woe_id=1000, api=mock_api)

    # Assert
    assert trends == [
        {"name": "#Rodrigo%20Neris", "url": "http://twitter.com/search?q=%23Rodrigo%20Neris"},
        {"name": "Rodrigo", "url": "http://twitter.com/search?q=Rodrigo"},
    ]


def test_get_trends_without_return_with_success():
    # Arrange
    mock_api = mock.Mock()
    mock_api.trends_place.return_value = [{"trends": []}]

    # Act
    trends = _get_trends(woe_id=1000, api=mock_api)

    # Assert
    assert trends == []
