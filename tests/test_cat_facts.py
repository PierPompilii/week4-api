from lib.cat_facts import CatFacts
from unittest.mock import Mock

def test_for_cats():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = "A cat called Dusty has the known record for the most kittens. She had more than 420 kittens in her lifetime."
    cat_facts = CatFacts(requester_mock)
    assert cat_facts._get_cat_fact() == "A cat called Dusty has the known record for the most kittens. She had more than 420 kittens in her lifetime."
    