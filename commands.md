# Terminal Record: Copper Kettle Coffee Roasters

> Complete this record using the **actual commands and unedited terminal output** from your own machine and Git repository. Do not invent outputs or commits. The steps below are prompts, not a completed record.

## 1. Building the project

Paste the commands you actually used to create the local folder, environment and files, install tools, produce `requirements.txt`, initialize Git, and connect GitHub, **in the order you ran them**, in one fenced code block.

## 2. The virtual environment

Run `which python3` after activating `.venv` and paste the command and its real output in separate fenced code blocks. Explain how the path confirms the active virtual environment.

## 3. The project structure

Run `tree -L 2` and paste the command and real output in separate fenced code blocks. Explain why `.venv/` stays out of GitHub.

## 4. Every function and test

Run `rg 'def '` and paste the command and real output in separate fenced code blocks. State how many functions `business_rules.py` defines and how many tests `tests/test_business_rules.py` defines.

## 5. Which files print

Run `rg -l 'print'` and paste the command and real output in separate fenced code blocks. Explain why `business_rules.py` has no print calls.

## 6. The commit history

Run `git log --oneline` just before committing this file. Paste the command and the unedited output in separate fenced code blocks and say how many commits existed then.
