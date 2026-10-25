"""Business calculations for Copper Kettle Coffee Roasters."""

FIRST_BULK_TIER = 20
SECOND_BULK_TIER = 80
STANDARD_BULK_DISCOUNT = 0.09
LARGE_BULK_DISCOUNT = 0.14
PARTNER_EXTRA_DISCOUNT = 0.04
NO_DISCOUNT = 0.0
SHIPPING_FEE = 35.00
FREE_SHIPPING_THRESHOLD = 250.00
PREPAYMENT_THRESHOLD = 1500.00
PALLET_BAG_THRESHOLD = 60
PALLET_TOTAL_THRESHOLD = 700.00


def calculate_bean_cost(bag_price: float, bags: int) -> float:
    """Return the bean cost before any discounts or fees."""
    return bag_price * bags


def get_bulk_discount(bags: int, partner: bool = False) -> float:
    """Return the discount based on quantity and partner status."""
    if bags >= SECOND_BULK_TIER:
        discount = LARGE_BULK_DISCOUNT
    elif bags >= FIRST_BULK_TIER:
        discount = STANDARD_BULK_DISCOUNT
    else:
    
        discount = NO_DISCOUNT


    if partner and bags >= FIRST_BULK_TIER:
        discount += PARTNER_EXTRA_DISCOUNT
    return discount


def calculate_shipment_total(
    bag_price: float, bags: int, partner: bool = False
) -> float:
    """Return the discounted shipment cost including applicable shipping."""
    bean_cost = calculate_bean_cost(bag_price, bags)
    discount = get_bulk_discount(bags, partner)
    discounted_cost = bean_cost * (1 - discount)
    if discounted_cost < FREE_SHIPPING_THRESHOLD:
        return discounted_cost + SHIPPING_FEE
    return discounted_cost


def requires_prepayment(total: float) -> bool:
    """Return whether the shipment must be prepaid."""
    return total >= PREPAYMENT_THRESHOLD


def needs_pallet(bags: int, total: float) -> bool:
    """Return whether a large, costly shipment needs a freight pallet."""
    return bags > PALLET_BAG_THRESHOLD and total > PALLET_TOTAL_THRESHOLD


def total_shipped(shipments: list) -> float:
    """Return the combined total of all shipment quotes."""
    total = 0.0
    for shipment in shipments:
        total += calculate_shipment_total(
            shipment["bag_price"], shipment["bags"], shipment["partner"]
        )
    return total


def largest_shipment(shipments: list) -> str:
    """Return the earliest buyer with the largest shipment total."""
    largest_buyer = ""
    largest_total = float("-inf")
    for shipment in shipments:
        total = calculate_shipment_total(
            shipment["bag_price"], shipment["bags"], shipment["partner"]
        )
        if total > largest_total:
            largest_total = total
            largest_buyer = shipment["buyer"]
    return largest_buyer


def format_shipment_line(
    buyer: str, total: float, prepayment: bool, pallet: bool
) -> str:
    """Format a shipment report row with money and yes/no labels."""
    prepayment_label = "yes" if prepayment else "no"
    pallet_label = "yes" if pallet else "no"
    return (
        f"{buyer}: ${total:.2f} | prepayment: {prepayment_label} "
        f"| pallet: {pallet_label}"
    )
