from flask import ( Blueprint, render_templates )

bp =  Blueprint('fact', __name__, url_prefix='/facts')

@bp.route('/fact')
def fact():
    return render_templates('fact.html')