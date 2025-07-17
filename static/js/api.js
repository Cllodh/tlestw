document.addEventListener('DOMContentLoaded', function() {
    const countrySelect = document.querySelector('[name="country"]');
    const otherInputDiv = document.getElementById('other-country-div');
    const otherInput = document.getElementById('other-country-input');
    const rateInput = document.querySelector('[name="rate"]');
    const rateDisplay = document.getElementById('rate-display');

    // 頁面載入時自動判斷是否顯示自訂國家欄位
    if (countrySelect && otherInputDiv) {
        if (countrySelect.value === '其他') {
            otherInputDiv.style.display = '';
        } else {
            otherInputDiv.style.display = 'none';
        }
    }

    function fetchRate(country) {
        console.log('fetchRate called with:', country);
        if (!country || country === '其他') {
            rateInput.value = '';
            if (window.syncRateBox) window.syncRateBox('');
            if (rateDisplay) rateDisplay.textContent = '請輸入匯率';
            return;
        }
        if (rateDisplay) rateDisplay.textContent = '1TWD=即時匯率';
        fetch(`/api/rate?country=${encodeURIComponent(country)}`)
            .then(res => {
                console.log('API response status:', res.status);
                return res.json();
            })
            .then(data => {
                rateInput.value = data.rate || '';
                if (window.syncRateBox) window.syncRateBox(data.rate);
                if (rateDisplay) rateDisplay.textContent = data.display || '';
            })
            .catch((err) => {
                console.log('API fetch error:', err);
                rateInput.value = '';
                if (window.syncRateBox) window.syncRateBox('');
                if (rateDisplay) rateDisplay.textContent = '查詢失敗';
            });
    }

    if (countrySelect) {
        countrySelect.addEventListener('change', function() {
            console.log('countrySelect changed:', this.value);
            if (this.value === '其他') {
                otherInputDiv.style.display = '';
                fetchRate('');
            } else {
                otherInputDiv.style.display = 'none';
                fetchRate(this.value);
            }
        });
        // 頁面載入時自動查詢一次
        if (countrySelect.value && countrySelect.value !== '其他') {
            console.log('init fetchRate for:', countrySelect.value);
            fetchRate(countrySelect.value);
        }
    }
    if (otherInput) {
        otherInput.addEventListener('input', function() {
            console.log('other-country-input changed:', this.value);
            fetchRate('');
        });
    }

    // 出發日與回國日驗證（不跳提示，直接限制）
    const departInput = document.querySelector('[name="depart_date"]');
    const returnInput = document.querySelector('[name="return_date"]');
    const daysInput = document.querySelector('[name="days"]');
    if (departInput && returnInput) {
        function updateReturnMinAndDays() {
            if (departInput.value) {
                returnInput.min = departInput.value;
                if (returnInput.value && returnInput.value < departInput.value) {
                    returnInput.value = departInput.value;
                }
            } else {
                returnInput.min = '';
            }
            // 自動計算天數
            if (departInput.value && returnInput.value) {
                const d1 = new Date(departInput.value);
                const d2 = new Date(returnInput.value);
                if (!isNaN(d1) && !isNaN(d2) && d2 >= d1) {
                    const diff = Math.round((d2 - d1) / (1000*60*60*24)) + 1;
                    if (daysInput) daysInput.value = diff;
                }
            }
        }
        departInput.addEventListener('change', updateReturnMinAndDays);
        returnInput.addEventListener('change', updateReturnMinAndDays);
        // 初始化
        updateReturnMinAndDays();
    }
}); 