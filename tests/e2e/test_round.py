"""Real-browser tests for Rock Paper Scissors rounds and replay."""

import pytest
from playwright.sync_api import Page, expect

import app as web

pytestmark = pytest.mark.e2e


def test_real_round_and_replay(page: Page, live_server, monkeypatch):
    """Play a losing round, then replay with a winning round."""
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")

    page.goto(live_server)

    # Round 1: Rock loses to Paper.
    page.get_by_role("button", name="Rock", exact=True).click()

    expect(page.get_by_label("This round’s choices")).to_be_visible()
    expect(page.get_by_role("region", name="Computer wins")).to_be_visible()
    expect(page.locator('[data-outcome="lose"]')).to_be_visible()
    expect(page.get_by_text("Rock", exact=True).first).to_be_visible()
    expect(page.get_by_text("Paper", exact=True).first).to_be_visible()

    # Round 2: Scissors beats Paper.
    page.get_by_role("button", name="Scissors", exact=True).click()

    expect(page.get_by_role("region", name="You win!")).to_be_visible()
    expect(page.locator('[data-outcome="win"]')).to_be_visible()
    expect(page.get_by_text("Scissors", exact=True).first).to_be_visible()
    expect(page.get_by_text("Paper", exact=True).first).to_be_visible()
