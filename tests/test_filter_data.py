from scripts.filter_data import FilterDates
from datetime import datetime
from unittest.mock import patch, MagicMock

SATURDAY_DATE = '2023-12-23T01:00:00'
SUNDAY_DATE = '2023-12-24T01:00:00'
MONDAY_DATE = '2023-12-25T01:00:00'


def patch_now(date):
    mock = MagicMock()
    mock.return_value = mock
    mock.now.return_value = datetime.fromisoformat(date)
    mock.fromisoformat.return_value = datetime.fromisoformat(SUNDAY_DATE)
    return mock


class TestFilterData:
    def test_not_none_false(self):
        assert FilterDates.not_none(None) is False

    def test_not_none_true(self):
        assert FilterDates.not_none('iso_date') is True

    @patch('scripts.filter_data.datetime', patch_now(SATURDAY_DATE))
    def test_remove_past_saturday(self):
        assert FilterDates.remove_past(SUNDAY_DATE) == '2023-12-24 01:00:00'

    @patch('scripts.filter_data.datetime', patch_now(SUNDAY_DATE))
    def test_remove_past_sunday(self):
        assert FilterDates.remove_past(SUNDAY_DATE) == '2023-12-24 01:00:00'

    @patch('scripts.filter_data.datetime', patch_now(MONDAY_DATE))
    def test_remove_past_monday(self):
        assert FilterDates.remove_past(SUNDAY_DATE) is None
