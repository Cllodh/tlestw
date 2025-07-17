// 依照後端邏輯即時計算總花費
function calculateTotal() {
    function val(name) {
        return parseFloat(document.querySelector(`[name="${name}"]`).value) || 0;
    }
    let ticket = val('ticket');
    let hotel = val('hotel');
    let sim = val('sim');
    let tickets = val('tickets');
    let exchange = val('exchange');
    let insurance = val('insurance');
    let card = val('card');
    let currency_have = val('currency_have');
    let currency_left = val('currency_left');
    let rate = val('rate');
    let card_twd = rate ? card / rate : 0;
    let currency_spent = currency_have - currency_left;
    let currency_spent_twd = rate ? currency_spent * rate : 0;
    let total = ticket + hotel + sim + tickets + exchange + insurance + card_twd + currency_spent_twd;
    return Math.round(total * 100) / 100;
}

function updateTotalBox() {
    const box = document.getElementById('js-result-box');
    if (!box) return;
    const total = calculateTotal();
    box.innerHTML = `<i class='bi bi-cash-coin'></i> <span>總花費 (TWD)：</span> ${total}`;
}

['ticket','hotel','sim','tickets','exchange','insurance','card','currency_have','currency_left','rate'].forEach(name => {
    document.addEventListener('input', function(e) {
        if (e.target.name === name) updateTotalBox();
    });
});

window.addEventListener('DOMContentLoaded', updateTotalBox); 