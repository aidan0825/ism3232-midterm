"""Tests for all eight coffee shipment business functions."""

from business_rules import (
    calculate_bean_cost,
    calculate_shipment_total,
    format_shipment_line,
    get_bulk_discount,
    largest_shipment,
    needs_pallet,
    requires_prepayment,
    total_shipped,
)


def test_bean_cost_multiplies_price_by_bags():
    assert round(calculate_bean_cost(13.50, 4), 2) == 54.00


def test_bean_cost_zero_bags():
    assert round(calculate_bean_cost(13.50, 0), 2) == 0.00


def test_discount_below_first_tier_at_19():
    assert get_bulk_discount(19) == 0.0


def test_discount_at_first_tier_20():
    assert get_bulk_discount(20) == 0.09


def test_discount_below_second_tier_at_79():
    assert get_bulk_discount(79) == 0.09


def test_discount_at_second_tier_80():
    assert get_bulk_discount(80) == 0.14


def test_partner_below_first_tier_does_not_change_discount():
    assert get_bulk_discount(19, True) == 0.0


def test_partner_at_first_tier_adds_four_points():
    assert get_bulk_discount(20, True) == 0.13
    assert get_bulk_discount(20, True) != get_bulk_discount(20, False)


def test_partner_at_second_tier_adds_four_points():
    assert round(get_bulk_discount(80, True), 2) == 0.18


def test_shipment_adds_fee_below_250_discounted_cost():
    assert round(calculate_shipment_total(249.99, 1), 2) == 284.99


def test_shipment_no_fee_exactly_at_250_discounted_cost():
    assert round(calculate_shipment_total(250.00, 1), 2) == 250.00


def test_shipment_applies_partner_discount_and_fee():
    assert round(calculate_shipment_total(10.00, 20, True), 2) == 209.00


def test_shipment_applies_discount_without_fee():
    assert round(calculate_shipment_total(12.00, 50, True), 2) == 522.00


def test_prepayment_below_1500():
    assert requires_prepayment(1499.99) is False


def test_prepayment_exactly_at_1500():
    assert requires_prepayment(1500.00) is True


def test_pallet_exactly_60_bags_even_when_total_high():
    assert needs_pallet(60, 800.00) is False


def test_pallet_61_bags_with_total_high():
    assert needs_pallet(61, 800.00) is True


def test_pallet_total_exactly_700_even_with_many_bags():
    assert needs_pallet(61, 700.00) is False


def test_pallet_total_above_700_with_many_bags():
    assert needs_pallet(61, 700.01) is True


def test_pallet_rejects_both_conditions_false():
    assert needs_pallet(60, 700.00) is False


def test_total_shipped_with_two_shipments():
    shipments = [
        {"buyer": "One", "bag_price": 10.0, "bags": 10, "partner": False},
        {"buyer": "Two", "bag_price": 10.0, "bags": 20, "partner": False},
    ]
    assert round(total_shipped(shipments), 2) == 352.00


def test_total_shipped_empty_list():
    assert round(total_shipped([]), 2) == 0.00


def test_largest_shipment_returns_highest_buyer():
    shipments = [
        {"buyer": "Small", "bag_price": 10.0, "bags": 10, "partner": False},
        {"buyer": "Large", "bag_price": 10.0, "bags": 50, "partner": False},
    ]
    assert largest_shipment(shipments) == "Large"


def test_largest_shipment_tie_keeps_first_buyer():
    shipments = [
        {"buyer": "First", "bag_price": 10.0, "bags": 10, "partner": False},
        {"buyer": "Second", "bag_price": 10.0, "bags": 10, "partner": False},
    ]
    assert largest_shipment(shipments) == "First"


def test_largest_shipment_empty_list_returns_empty_string():
    assert largest_shipment([]) == ""


def test_format_line_false_values_and_two_decimals():
    assert format_shipment_line("Cafe", 175, False, False) == (
        "Cafe: $175.00 | prepayment: no | pallet: no"
    )


def test_format_line_true_values_and_two_decimals():
    assert format_shipment_line("Hotel", 1500.5, True, True) == (
        "Hotel: $1500.50 | prepayment: yes | pallet: yes"
    )


def test_format_line_mixed_boolean_values():
    assert format_shipment_line("Shop", 700.01, False, True) == (
        "Shop: $700.01 | prepayment: no | pallet: yes"
    )
def test_shipment_zero_bags_still_adds_shipping_fee():
    assert round(calculate_shipment_total(10.00, 0), 2) == 35.00