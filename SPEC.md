
# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** One person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server.

### Expected results

Results are from the **player's perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

We agreed to build one complete round of Rock, Paper, Scissors using the existing Flask application.

**Prediction:** If the player chooses rock and the computer chooses paper, the player loses because paper covers rock.

**Implementation plan:**

1. Implement `determine_winner(player, computer)` in `game.py`.
2. Return `win`, `lose`, or `tie` for all nine possible matchups.
3. Display both moves and the correct result.
4. Allow the player to choose again for a new independent round.
5. Keep the existing interface and server without adding scores, accounts, or saved history.

**Testing plan:**

- Test all nine possible matchups.
- Verify that a valid losing round returns the correct result.
- Reject missing or unsupported moves, such as `banana`, with HTTP 400 and a helpful message.
- Test a real HTTP request and displayed result.
- Test a complete browser round and replay.
- Run Black, Pylint, pytest, and Chromium browser checks.

We review the code, tests, and actual browser behavior before merging the completed work.

### Checks

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | Nine parametrized cases verify all possible player/computer combinations. |
| Integration — positive | A real Flask POST with player rock and computer paper verifies the losing result and displayed choices. |
| Integration — negative | Existing tests verify that missing or unsupported moves return HTTP 400 instead of crashing. |
| E2E — positive | A Playwright Chromium test verifies a completed round and replay using real HTTP requests and the real rules. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `check.py` for Black, Pylint, non-browser tests, and Chromium browser checks. Review the diff and preserve the existing application structure.

### Work record

**Issue:**
https://github.com/AnabhayanA/https-github.com-AnabhayanA-my-rps/issues/1

**Pull request:**
https://github.com/AnabhayanA/https-github.com-AnabhayanA-my-rps/pull/2

**GitHub Actions:**
https://github.com/AnabhayanA/https-github.com-AnabhayanA-my-rps/actions

**Implementation:**

- Implemented `determine_winner()` in `game.py`.
- Added tests for all nine possible Rock Paper Scissors combinations.
- Added an integration test for a real completed round.
- Added a Playwright browser test for playing and replaying.
- Preserved the supplied Flask application and interface.
- Did not add scores, accounts, or saved history.

**Local test results:**

- Black formatting: Passed.
- Pylint analysis: Passed.
- Non-browser pytest tests: 23 passed.
- Game-related Chromium browser tests: 2 passed.
- Plain-mode development-refresh browser test: 1 passed.
- Full local Chromium suite: Did not complete because the development-refresh tests hung during execution on Windows. The original professor-provided test file was restored.

**GitHub verification:**

- GitHub Actions workflow `Python checks / Python checks (pull_request)`: Successful.
- GitGuardian Security Checks: Successful, no secrets detected.
- Pull Request #2: No merge conflicts reported.

**Test review:**

The unit tests catch incorrect winner determination, including the mistake of treating rock against paper as a win rather than a loss.

The Flask integration test verifies that the real server displays the correct result and both choices. The Playwright test verifies that a player can complete a round and choose again for an independent round.

**Browser observation:**

The automated Chromium game test successfully completed a round and replay. A separate manual browser-play observation should be recorded after personally checking the interface.
