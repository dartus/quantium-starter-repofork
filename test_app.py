from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict
from dash.testing.application_runners import import_app
import chromedriver_autoinstaller


chromedriver_autoinstaller.install()

def testheaderpresent(dash_duo):
    app = import_app('app')
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal('h1', 'Pink morsel data', timeout=4)
    assert dash_duo.find_element('h1').text == 'Pink morsel data'

def testgraphpresent(dash_duo):
    app = import_app('app')
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#example-graph', timeout=4)
    assert dash_duo.find_element('#example-graph')

def testregionpickerpresent(dash_duo):
    app = import_app('app')
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#RegionFilter', timeout=4)
    assert dash_duo.find_element('#RegionFilter')