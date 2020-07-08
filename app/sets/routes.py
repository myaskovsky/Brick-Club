from flask import Blueprint, request, render_template
from app.models import Set

sets = Blueprint('sets', __name__)


@sets.route("/show_set/<int:set_id>")
def show_set(set_id):
    set = Set.query.get_or_404(set_id)
    return render_template('public/set.html', set=set)
