# Add below 2 lines to display trace logs
from bottle import debug
debug(True)

from bottle import (
    default_app,
    run,
    route,
    template,
    request,
    HTTPError
)
from abalone_predictor import AbalonePredictor
from collections import namedtuple

from bokeh.plotting import figure
from bokeh.embed import components

_predictor = AbalonePredictor()

def get_graph(abalone):
    p = figure(plot_width=400, plot_height=400, title='実年齢と推定値の分布')
    p.xaxis.axis_label = '実年齢'
    p.yaxis.axis_label = '推定値'

    # 誤差がわかりやすいようにする
    p.line([0, 30], [0, 30], line_dash='dotted', legend='実年齢と推定値が一致するライン')

    # 実年齢と推定値のデータをプロット
    p.circle(_predictor.y_train, _predictor.prediction, legend='訓練データにおける分布')

    # ブラウザから入力したアワビの推定値をプロット
    p.line([0, 30], [abalone.age, abalone.age], legend="捕まえたアワビの推定年齢", color="green")

    # 凡例の表示位置を設定
    p.legend.location = 'top_left'

    # 凡例クリックでグラフと凡例を半透明にする
    p.legend.click_policy='mute'

    # JavaScriptコードが生成される
    script, div = components(p)
    return script, div

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
        age = calc_age(**request.params)
        abalone = Abalone(age=age, **request.params)

    except (TypeError, ValueError) as e:
        raise HTTPError(status=400, body=e)

    script, div = get_graph(abalone)
    return template(
        'templates/result.tpl',
        abalone=abalone,
        script=script,
        graph=div
    )

# Reload the page on file update
run(host='localhost', port=8080, reloader=True)
#application = default_app()
