def calculate_total(data):
    try:
        ticket = float(data.get('ticket', 0))
        hotel = float(data.get('hotel', 0))
        sim = float(data.get('sim', 0))
        tickets = float(data.get('tickets', 0))
        exchange = float(data.get('exchange', 0))
        insurance = float(data.get('insurance', 0))
        card = float(data.get('card', 0))
        currency_have = float(data.get('currency_have', 0))
        currency_left = float(data.get('currency_left', 0))
        rate = float(data.get('rate', 0))
        card_twd = card / rate if rate else 0
        currency_spent = currency_have - currency_left
        currency_spent_twd = currency_spent * rate if rate else 0
        total = ticket + hotel + sim + tickets + exchange + insurance + card_twd + currency_spent_twd
        return round(total, 2)
    except Exception:
        return 0 