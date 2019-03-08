import pytest

from record import RecordScore


def test_new_record_on_blank_record():
    record = RecordScore()
    assert (record(10) == 10)


def test_old_record_for_lower_score():
    record = RecordScore()
    record(10)
    assert (record(9) == 10)


def test_new_record_for_higher_score():
    record = RecordScore()
    record(10)
    assert (record(11) == 11)
