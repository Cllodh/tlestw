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
        # 新公式
        card_twd = card / rate if rate else 0
        currency_have_twd = currency_have / rate if rate else 0
        currency_left_twd = currency_left / rate if rate else 0
        total = (
            ticket + hotel + insurance + sim + tickets
            + card_twd
            + (exchange + currency_have_twd - currency_left_twd)
        )
        return round(total, 2)
    except Exception:
        return 0

FORMULA_DESCRIPTION = (
    "機票＋住宿＋保險＋SIM＋票券＋刷卡（台幣）＋[換匯（台幣）＋原本有的貨幣（台幣）]－現餘（台幣）<br>"
    "※ 刷卡、原本有的貨幣、現餘皆以匯率換算成台幣，換匯直接加總台幣。"
) 