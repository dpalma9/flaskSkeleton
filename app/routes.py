from flask import Blueprint, render_template
#from app.services.service_one import service_one_function
#from app.services.service_two import service_two_function

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    #result_one = service_one_function()
    #result_two = service_two_function()
    result_one = "Service One Result"
    result_two = "Service Two Result"
    return render_template('index.html', result_one=result_one, result_two=result_two)