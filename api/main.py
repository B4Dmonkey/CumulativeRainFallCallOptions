def main():
    return True


INDEX = 18
LAYER = 8


def payout(strike: float, exit: float, notional: float):
    spread = max(INDEX - strike, 0)
    layer = min(LAYER, spread)
    return layer * notional


if __name__ == '__main__':
    main()
