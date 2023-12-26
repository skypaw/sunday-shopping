from scripts.sunday_subpages import Config
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock

SATURDAY_DATE = '2023-12-16T00:00:00'


def patch_now(date):
    mock = MagicMock()
    mock.return_value = mock
    mock.now.return_value = datetime.fromisoformat(date)
    mock.fromisoformat.return_value = datetime.fromisoformat(SATURDAY_DATE)
    mock.strptime.return_value = datetime.strptime("January 01, 2024", "%B %d, %Y")
    mock.today.return_value = datetime.fromisoformat(date)
    return mock


class TestConfig:
    @patch('scripts.sunday_subpages.datetime', patch_now(SATURDAY_DATE))
    def test_config(self):
        config = Config()
        config.config = ["December 17, 2023", "December 31, 2023"]  # shops_open
        assert config.dates() == [datetime.fromisoformat(SATURDAY_DATE) + timedelta(1),
                                  datetime.fromisoformat(SATURDAY_DATE) + timedelta(8),
                                  datetime.fromisoformat(SATURDAY_DATE) + timedelta(15), ]

        assert config.first_sunday == datetime.fromisoformat(SATURDAY_DATE) + timedelta(1)
        assert config.last_sunday == datetime.fromisoformat(SATURDAY_DATE) + timedelta(15)

        assert config.shops_open(datetime.fromisoformat('2023-12-17T01:00:00')) is True
        assert config.shops_open(datetime.fromisoformat('2023-12-24T01:00:00')) is False
