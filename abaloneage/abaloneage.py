# Add below 2 lines to display trace logs
from bottle import debug
debug(True)

from bottle import route, run, template, request, HTTPError
from abalone_predictor import AbalonePredictor
from collections import namedtuple

#_predictor = AbalonePredictor()
def calc_age(sex, length, diameter, height, weight):
    age = _predictor.predict(
        int(sex),
        int(length),
        int(diameter),
        int(height),
        int(weight)
    )
    return float(age)

READABLE_SEX = ['Female', 'UnKnown', 'Male']
INPUT_DATA = ('sex', 'length', 'diameter', 'height', 'weight')

BaseAbalone = namedtuple('BaseAbalone', INPUT_DATA + ('age',))
class Abalone(BaseAbalone):
    @property
    def sex_str(self):
        return READABLE_SEX[int(self.sex)]

@route('/')
def index():
    return template('templates/index.tpl')

@route('/abaloneage', method='POST')
def result():
    try:
        #sex         = int(request.params['sex'])
        #length      = int(request.params['length'])
        #diameter    = int(request.params['diameter'])
        #height      = int(request.params['height'])
        #weight      = int(request.params['weight'])
        #age = calc_age(**request.params)
        age = 0 #--- For debug only ---
        abalone = Abalone(age=age, **request.params)

    except (TypeError, ValueError) as e:
        raise HTTPError(status=400, body=e)

    return template('templates/result.tpl', abalone=abalone
                #sex     = READABLE_SEX[sex],
                #length  = length,
                #diameter= diameter,
                #height  = height,
                #weight  = weight,
                #age     = age
                )

# Reload the page on file update
run(host='localhost', port=8080, reloader=True)
