from flask import Blueprint, jsonify, request
import requests
import time

api_bp = Blueprint('api', __name__)

# 國家對應貨幣代碼（部分常用，其他可擴充）
COUNTRY_CURRENCY = {
    '日本': 'JPY',
    '韓國': 'KRW',
    '泰國': 'THB',
    '新加坡': 'SGD',
    '馬來西亞': 'MYR',
    '美國': 'USD',
    '澳洲': 'AUD',
    '香港': 'HKD',
    '澳門': 'MOP',
    '中國': 'CNY',
    '越南': 'VND',
    '印尼': 'IDR',
    '菲律賓': 'PHP',
    '英國': 'GBP',
    '法國': 'EUR',
    '德國': 'EUR',
    '義大利': 'EUR',
    '加拿大': 'CAD',
    '瑞士': 'CHF',
    '紐西蘭': 'NZD',
}
UNIRATE_API_KEY = '1YEmWKXiCTbLzf3uRyHjHo30F8kCwErHiUTTWGmXcXUyx9bMDZTtJBYeJ28ODkBU'

# 簡單的後端快取（每個國家 10 分鐘）
_rate_cache = {}  # {country: (timestamp, {'rate':..., 'display':...})}
CACHE_TTL = 600  # 10 分鐘

@api_bp.route('/rate')
def get_rate():
    country = request.args.get('country')
    currency = COUNTRY_CURRENCY.get(country)
    if not currency:
        return jsonify({'rate': '', 'display': '請輸入匯率'}), 200
    now = time.time()
    # 檢查快取
    if country in _rate_cache:
        ts, data = _rate_cache[country]
        if now - ts < CACHE_TTL:
            return jsonify(data)
    # 查詢即時匯率（TWD->目標貨幣）
    try:
        url = f'https://api.unirateapi.com/api/convert?api_key={UNIRATE_API_KEY}&from=TWD&to={currency}'
        resp = requests.get(url, timeout=5)
        data = resp.json()
        rate = data.get('result')
        if rate:
            display = f'1TWD={rate:.3f}{currency}'
            result = {'rate': rate, 'display': display}
            _rate_cache[country] = (now, result)
            return jsonify(result)
        else:
            return jsonify({'rate': '', 'display': '查無匯率'}), 200
    except Exception:
        return jsonify({'rate': '', 'display': '查詢失敗'}), 200 