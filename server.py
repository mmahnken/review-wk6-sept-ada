from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


FAKE_API = {
    'subway': {
                'name': "Subway, EAT FRESH!",
               'location':{'lat':37.8288513, 'lng':-122.4090701}
    },
    'mua': {
            'name': 'Mua Oakland',
            'location': {'lat':37.8140862, 'lng':-122.2665427}
    },
    'drakes': {
                'name': "Drake's Dealership",
                'location': {'lat':37.7638314, 'lng':-122.3638399},
    },
    'piraat':{
            'name': "Piraat",
            'location': {'lat': 37.7889406, 'lng':-122.4139837},
    },
}

@app.route('/')
def show_homepage():
    return render_template("homepage.html")

@app.route('/search')
def search():
    place_to_search = request.args.get('place_id')
    cleaned_input = place_to_search.lower()
    cleaned_input = cleaned_input.replace("'", "")

    if cleaned_input in FAKE_API:
        resp = {'data':FAKE_API[cleaned_input], 'found':True}

    else:
        resp = {'data':'NOPENOPENOPENOPE', 'found':False}

    return jsonify(resp)
        


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")