from flask import Blueprint, render_template, request, redirect, url_for, session
from app.utils.calc import calculate_total, FORMULA_DESCRIPTION

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    result = None
    form = {}
    if request.method == 'POST':
        form = request.form.to_dict()
        if 'depart_date' in form and 'return_date' in form:
            form['date_range'] = f"{form.get('depart_date', '')} ~ {form.get('return_date', '')}"
        result = calculate_total(form)
        session['form'] = form
        session['result'] = result
        return redirect(url_for('main.index'))
    form = session.pop('form', {})
    result = session.pop('result', None)
    return render_template('form.html', result=result, form=form, formula_description=FORMULA_DESCRIPTION)

@main_bp.route('/privacy_zh.html')
def privacy():
    return render_template('privacy_zh.html')

@main_bp.route('/terms_zh.html')
def terms():
    return render_template('terms_zh.html') 