# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

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

We will review the code, tests, and actual browser behavior before committing the completed work.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Issue: add your own issue URL.
- Issue: https://github.com/AnabhayanA/https-github.com-AnabhayanA-my-rps/issues/1
- Pull request / CI: add actual URLs when they exist.
- Implementation: **Not implemented.** The shell is supplied; `game.py` is unfinished.
- Checks: **Rules not verified.** Supplied request/browser tests cover the shell only. After implementation, record actual full-check results and your browser observations here; put detailed results in the PR. Passing formatting and analysis alone is not evidence of correct rules.
