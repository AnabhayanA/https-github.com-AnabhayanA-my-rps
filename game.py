"""RPS-001: Rock Paper Scissors game rules."""


def determine_winner(player: str, computer: str) -> str:
    """Return 'win', 'lose', or 'tie' from the player's perspective."""

    if player == computer:
        return "tie"

    winning_combinations = {
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper"),
    }

    if (player, computer) in winning_combinations:
        return "win"

    return "lose"
