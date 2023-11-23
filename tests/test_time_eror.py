from lib.time_error import *
from unittest.mock import Mock


def test_for_this_exercice():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime":1700750465} 
    timer_mock = Mock()
    timer_mock.time.return_value =1700750465.5
    time_error = TimeError(requester_mock, timer_mock)
    assert time_error.error() == -0.5
    
    