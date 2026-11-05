"""Unit tests for Rock Paper Scissors rules."""

import pytest

from game import determine_winner


@pytest.mark.unit
@pytest.mark.parametrize(
    "player, computer, expected",
    [
        ("rock", "rock", "tie"),
        ("rock", "paper", "lose"),
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("paper", "paper", "tie"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("scissors", "paper", "win"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_all_matchups(player, computer, expected):
    """Verify all nine possible matchups."""
    assert determine_winner(player, computer) == expected
