import pytest
from src.oystercard.entity.card import Card


class TestCard:
    def test_card_should_be_ok(self):
        card = Card()
        card.set_balance(30.0)
        assert card.get_balance() == 30.0
        assert card.go_out(29.0).get_balance() == 1.0

    def test_card_should_be_ko(self):
        card = Card()
        assert card.get_balance() == 0.0
        assert card.top_up(30.0).get_balance() == 30.0
        with pytest.raises(Exception):
            assert card.go_out(31.0).get_balance()
