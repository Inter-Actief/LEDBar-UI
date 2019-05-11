from json import JSONDecodeError

from flask import Flask, render_template, request, flash, json
from flask_sqlalchemy import SQLAlchemy
from moving_message_g009dh.ledbar import LEDBar

from database import db_session
from ledbar_constants import *
from models import Message

app = Flask(__name__)
app.config.from_pyfile("default_settings.cfg")
app.config.from_pyfile("local_settings.cfg", silent=True)
db = SQLAlchemy(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


def get_saved_message():
    return Message.query.first()


def update_saved(json_data):
    json_str = json.dumps(json_data)
    msg = get_saved_message()
    if msg:
        msg.message = json_str
    else:
        msg = Message(message=json_str)
    db_session.add(msg)
    db_session.commit()


def send_saved():
    json_data = get_saved_message()
    try:
        if app.config.get("LEDBAR_DEVICE", None) is not None:
            bar = LEDBar(app.config.get("LEDBAR_DEVICE", None))
        else:
            bar = LEDBar()
        bar.data_from_dict(json_data, clear=True)
        bar.send_data()
        return True, ""
    except OSError as e:
        return False, "Could not send to LEDBar. {}".format(e)


@app.route('/', methods=('GET', 'POST'))
def home():
    context = {}
    form_data = {}
    if request.method == 'POST':
        json_data = request.form['json_data']
        form_data = request.form
        if not json_data:
            flash("No data is given", 'error')
        else:
            try:
                json_data = json.loads("""{"files": [{"number": 1, "lines": %s}]}""" % (json_data,))
                valid, reasons = LEDBar.check_data(json_data)
                if not valid:
                    flash("JSON data is invalid. Reason(s):\n<ul>{}</ul>".format(
                        "".join("<li>{}</li>".format(x) for x in reasons)))
                else:
                    update_saved(json_data)

            except ValueError as e:
                flash("JSON data is invalid. {}".format(e))

    context['form_data'] = form_data
    try:
        context['message_lines'] = json.loads(get_saved_message().message)['files'][0]['lines']
    except (JSONDecodeError, KeyError, AttributeError):
        context['message_lines'] = None
    context['fade_options'] = FADE_OPTIONS
    context['speed_options'] = SPEED_OPTIONS
    context['color_options'] = COLOR_OPTIONS
    context['font_options'] = FONT_OPTIONS

    return render_template('home.html', **context)


@app.route('/custom', methods=('GET', 'POST'))
def custom_data():
    context = {}
    form_data = {}
    if request.method == 'POST':
        json_data = request.form['json_data']
        form_data = request.form
        if not json_data:
            flash("No data is given", 'error')
        else:
            try:
                json_data = json.loads(json_data)
                valid, reasons = LEDBar.check_data(json_data)
                if not valid:
                    flash("JSON data is invalid. Reason(s):\n<ul>{}</ul>".format(
                        "".join("<li>{}</li>".format(x) for x in reasons)))
                else:
                    try:
                        if app.config.get("LEDBAR_DEVICE", None) is not None:
                            bar = LEDBar(app.config.get("LEDBAR_DEVICE", None))
                        else:
                            bar = LEDBar()
                        bar.data_from_dict(json_data, clear=True)
                        bar.send_data()
                    except OSError as e:
                        flash("Could not send to LEDBar. {}".format(e))
            except ValueError as e:
                flash("JSON data is invalid. {}".format(e))

    context['form_data'] = form_data
    context['default_message'] = json.dumps({
        "files": [{
            "number": 1,
            "lines": [{
                "fade": "pacman",
                "speed": "speed_8",
                "texts": [{
                    "color": "bright_red",
                    "font": "extra_wide",
                    "text": "X"
                }, {
                    "color": "bright_orange",
                    "font": "extra_wide",
                    "text": "T"
                }, {
                    "color": "bright_yellow",
                    "font": "extra_wide",
                    "text": "R"
                }, {
                    "color": "bright_green",
                    "font": "extra_wide",
                    "text": "A"
                }]
            }, {
                "fade": "open_from_center",
                "texts": [{
                    "color": "bright_layer_mix_rainbow",
                    "font": "small",
                    "text": "smol"
                }]
            }]
        }]
    }, indent=2)

    context['fade_options'] = FADE_OPTIONS
    context['speed_options'] = SPEED_OPTIONS
    context['color_options'] = COLOR_OPTIONS
    context['font_options'] = FONT_OPTIONS

    return render_template('custom_data.html', **context)


if __name__ == '__main__':
    app.run(
        host=app.config.get("HOST"),
        port=app.config.get("PORT"),
        ssl_context=(
            app.config.get("SSL_CERTIFICATE_PATH"),
            app.config.get("SSL_KEY_PATH")
        )
    )
