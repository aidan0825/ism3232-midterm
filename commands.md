# Terminal Record: Copper Kettle Coffee Roasters

> Complete this record using the **actual commands and unedited terminal output** from your own machine and Git repository. Do not invent outputs or commits. The steps below are prompts, not a completed record.

## 1. Building the project

Paste the commands you actually used to create the local folder, environment and files, install tools, produce `requirements.txt`, initialize Git, and connect GitHub, **in the order you ran them**, in one fenced code block.

## 2. The virtual environment
## 2. The virtual environment

Command:
```bash
which python3
Run `which python3` after activating `.venv` and paste the command and its real output in separate fenced code blocks. Explain how the path confirms the active virtual environment.

## 3. The project structure
The .venv folder is on my computer but is not included in my GitHub repository because it is listed in .gitignore.
Run `tree -L 2` and paste the command and real output in separate fenced code blocks. Explain why `.venv/` stays out of GitHub.

## 4. Every function and test
## 4. Every function and test

```bash
rg 'def '
```

```text
commands.md
23:Run `rg 'def '` and paste the command and real output in separate fenced code blocks. State how many functions `business_rules.py` defines and how many tests `tests/test_business_rules.py` defines.

business_rules.py
15:def calculate_bean_cost(bag_price: float, bags: int) -> float:
20:def get_bulk_discount(bags: int, partner: bool = False) -> float:
34:def calculate_shipment_total(
46:def requires_prepayment(total: float) -> bool:
51:def needs_pallet(bags: int, total: float) -> bool:
56:def total_shipped(shipments: list) -> float:
66:def largest_shipment(shipments: list) -> str:
80:def format_shipment_line(

main.py
24:def main() -> None:

tests/test_business_rules.py
15:def test_bean_cost_multiplies_price_by_bags():
19:def test_bean_cost_zero_bags():
23:def test_discount_below_first_tier_at_19():
27:def test_discount_at_first_tier_20():
31:def test_discount_below_second_tier_at_79():
35:def test_discount_at_second_tier_80():
39:def test_partner_below_first_tier_does_not_change_discount():
43:def test_partner_at_first_tier_adds_four_points():
48:def test_partner_at_second_tier_adds_four_points():
52:def test_shipment_adds_fee_below_250_discounted_cost():
56:def test_shipment_no_fee_exactly_at_250_discounted_cost():
60:def test_shipment_applies_partner_discount_and_fee():
64:def test_shipment_applies_discount_without_fee():
68:def test_prepayment_below_1500():
72:def test_prepayment_exactly_at_1500():
76:def test_pallet_exactly_60_bags_even_when_total_high():
80:def test_pallet_61_bags_with_total_high():
84:def test_pallet_total_exactly_700_even_with_many_bags():
88:def test_pallet_total_above_700_with_many_bags():
92:def test_pallet_rejects_both_conditions_false():
96:def test_total_shipped_with_two_shipments():
104:def test_total_shipped_empty_list():
108:def test_largest_shipment_returns_highest_buyer():
116:def test_largest_shipment_tie_keeps_first_buyer():
124:def test_largest_shipment_empty_list_returns_empty_string():
128:def test_format_line_false_values_and_two_decimals():
134:def test_format_line_true_values_and_two_decimals():
140:def test_format_line_mixed_boolean_values():
```

My business_rules.py file defines 8 functions, and my test_business_rules.py file defines 28 tests.

## 5. Which files print
```bash
rg -l 'print'
```

```text
main.py
README.md
commands.md
```

The only Python file that prints is main.py. The business_rules.py file doesn't appear because its functions return values instead of printing them.


## 6. The commit history
```bash
git log --oneline
```

```text
988045a (HEAD -> main, origin/main) Add initial Copper Kettle Coffee Roasters project
```

At this point, my repository had 1 commit, which added the initial project files.

