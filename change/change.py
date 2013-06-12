from decimal import Decimal


class NotFoundsError(Exception):
    pass


def give_change(cash, total):
    if cash < total:
        raise NotFoundsError()

    current_change = cash - total

    moneys = [
        100, 50, 10, 5, 1, 0.50, 0.10, 0.05, 0.01
    ]

    change = {}
    for money in moneys:
        money_amount, change_rest = divmod(Decimal(str(current_change)), Decimal(str(money)))
        current_change = change_rest
        if money_amount == 0:
            continue
        else:
            change[str(money)] = money_amount

        if change_rest == 0:
            break
    return change
