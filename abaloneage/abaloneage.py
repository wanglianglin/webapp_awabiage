# Add below 2 lines to display trace logs
from bottle import debug
debug(True)

from bottle import route, run, template, request, HTTPError

READABLE_SEX = ['Female', 'UnKnown', 'Male']

@route('/')
def index():
    return template('templates/index.tpl')

@route('/awabiage', method='POST')
def result():
    try:
        sex         = int(request.params['sex'])
        length      = int(request.params['length'])
        diameter    = int(request.params['diameter'])
        height      = int(request.params['height'])
        weight      = int(request.params['weight'])
    except (KeyError, ValueError) as e:
        raise HTTPError(status=400, body=e)

    return template('templates/result.tpl',
                sex     = READABLE_SEX[sex],
                length  = length,
                diameter= diameter,
                height  = height,
                weight  = weight,
                age     = 0
                )

# Reload the page on file update
run(host='localhost', port=8080, reloader=True)
