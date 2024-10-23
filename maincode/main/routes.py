from flask import render_template, request, Blueprint, flash, url_for, jsonify
from maincode import db
import random
main = Blueprint('main', __name__)
K = 32

tiktoker_tags = ["urdadella","sonosempreiris","alessia_basile_","iriss.vallaranii", "aliseabruno","martina_os", "bunnybunny924","777.siria_","elisa.radulescu","lisa_luchetta","lucreziagrande_"]
class TikToker:
    ELO = 1500
    def __init__(self, tag):
        self.tag = tag
tiktokers = []
for tiktoker in tiktoker_tags:
    tiktokers.append(TikToker(tiktoker))

@main.route('/')
def home():
    return render_template('homepage.html')

@main.route('/get_fregne', methods = ['GET'])
def get_fregne():
    fregna1 = random.choice(tiktoker_tags)
    fregna2 = random.choice(tiktoker_tags)
    while fregna2 == fregna1:
        fregna2 = random.choice(tiktoker_tags)
    return jsonify({
        'left': fregna1,
        'left_path': url_for('static', filename=f'imgs/{fregna1}.jpg'),
        'right': fregna2,
        'right_path': url_for('static', filename=f'imgs/{fregna2}.jpg')
    })

@main.route('/post_fregna', methods = ["POST"])
def post_fregna():
    data= request.get_json()
    vincitrice = data['vincitrice'].split("/")[-1].replace(".jpg", "")
    print(vincitrice)
    perdente = data['perdente'].split("/")[-1].replace(".jpg", "")
    vincitrice = list(filter(lambda x: x.tag == vincitrice, tiktokers))[0]
    perdente = list(filter(lambda x: x.tag == perdente, tiktokers))[0]
    expected_perdente = 1/ (1+10**((vincitrice.ELO - perdente.ELO)/400))
    expected_vincitrice = 1/ (1+10**((perdente.ELO - vincitrice.ELO)/400))
    vincitrice.ELO += K*(1-expected_vincitrice)
    perdente.ELO += K*(0-expected_perdente)
    return jsonify({"status": "success"})

@main.route('/classifica')
def classifica():
    tiktokers.sort(key = lambda x: x.ELO, reverse=True)
    classificalist = ""
    for num, tiktoker in enumerate(tiktokers):
        classificalist += f"{num+1}a: {tiktoker.tag}, ELO: {tiktoker.ELO} <br>"
    classificalist += '<a href="/">home</a>'
    return classificalist