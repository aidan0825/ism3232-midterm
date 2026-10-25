"""Print the Copper Kettle Coffee Roasters shipment report."""

from business_rules import (
    calculate_shipment_total,
    format_shipment_line,
    largest_shipment,
    needs_pallet,
    requires_prepayment,
    total_shipped,
)

shipments = [
    {"buyer": "Uptown Bakery", "bag_price": 14.00, "bags": 10, "partner": False},
    {"buyer": "Vine Cafe", "bag_price": 12.50, "bags": 15, "partner": True},
    {"buyer": "Wren Hotel", "bag_price": 13.00, "bags": 40, "partner": False},
    {"buyer": "Yarrow Cafe", "bag_price": 12.00, "bags": 50, "partner": True},
    {"buyer": "Zenith Grocers", "bag_price": 11.00, "bags": 200, "partner": False},
    {"buyer": "Alder Hotel", "bag_price": 12.00, "bags": 60, "partner": False},
    {"buyer": "Birch Diner", "bag_price": 11.00, "bags": 61, "partner": False},
    {"buyer": "Cove Market", "bag_price": 13.00, "bags": 150, "partner": True},
]


def main() -> None:
    """Print individual shipment totals and the overall summary."""
    print("Copper Kettle Coffee Roasters - Shipment Report")
    prepayments_required = 0
    pallets_needed = 0
    shipment_count = 0

    for shipment in shipments:
        total = calculate_shipment_total(
            shipment["bag_price"], shipment["bags"], shipment["partner"]
        )
        prepayment = requires_prepayment(total)
        pallet = needs_pallet(shipment["bags"], total)
        print(format_shipment_line(shipment["buyer"], total, prepayment, pallet))
        shipment_count += 1
        if prepayment:
            prepayments_required += 1
        if pallet:
            pallets_needed += 1

    combined_total = total_shipped(shipments)
    average_total = combined_total / shipment_count
    print(f"Shipments: {shipment_count}")
    print(f"Total shipped: ${combined_total:.2f}")
    print(f"Average shipment total: ${average_total:.2f}")
    print(f"Largest shipment total: {largest_shipment(shipments)}")
    print(f"Prepayments required: {prepayments_required}")
    print(f"Pallets needed: {pallets_needed}")


if __name__ == "__main__":
    main()
