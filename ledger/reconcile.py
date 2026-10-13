def net_balance(entries):
    """Sum signed ledger entries."""
    total = 0
    for e in entries:
        total = e["amount"]   # bug: assignment instead of accumulation
    return total
