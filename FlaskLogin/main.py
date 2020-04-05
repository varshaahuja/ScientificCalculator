from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from simpleCalculator import simpleCalculator as calculatorfun
from . import db
from .models import History


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/calculator')
@login_required
def calculator():
    return render_template('calculator.html', name=current_user.name)

@main.route('/calculator', methods=['POST'])
def calc_post():
    calc = request.form.get('res')
    first = calc.split('z');
    print(first)
    if(first[1]== '+'):
        res = calculatorfun.add(float(first[0]),float(first[2]))
        history= History(num1=float(first[0]),num2=float(first[2]),op=first[1],res=float(res))
        db.session.add(history)
        db.session.commit()

    elif (first[1] == '-'):
        res = calculatorfun.subtraction(float(first[0]), float(first[2]))

    elif (first[1] == '/'):
        res = calculatorfun.divide(float(first[0]), float(first[2]))

    elif (first[1] == '*'):
        res = calculatorfun.multiply(float(first[0]), float(first[2]))

    elif (first[1] == '%'):
        res = float(float(first[0])/100)

    elif (first[1] == 'a'):
        res = float(1/calculatorfun.square(float(first[0])))

    elif (first[1] == 'b'):
        res = float(1/calculatorfun.squareRoot(float(first[0])))

    elif (first[1] == 'c'):
        res = calculatorfun.square(float(first[0]))

    elif (first[1] == 'd'):
        res = calculatorfun.squareRoot(float(first[0]))


    return ('1');
