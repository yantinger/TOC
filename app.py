import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '513143646:AAEtKOcc_j2Ov12TI2IVraddArjc7LFeYM8'
WEBHOOK_URL = 'https://3a003dc6.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'state3',
        'state4',
        'state5',
        'state6',
        'state7',
        'state8',
        'state9'
    ], 
    transitions=[

        {
            'trigger': 'advance',
            'source': 'state8',
            'dest': 'state9',
            'conditions': 'is_going_to_state89'
        },
        
        {
            'trigger': 'advance',
            'source': 'state9',
            'dest': 'state9',
            'conditions': 'is_going_to_state99'
        },
        
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'user',
            'conditions': 'is_going_to_state4u'
        },
        
        {
            'trigger': 'advance',
            'source': 'state9',
            'dest': 'user',
            'conditions': 'is_going_to_state9u'
        },

        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state5',
            'conditions': 'is_going_to_state45'
        },
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state6',
            'conditions': 'is_going_to_state56'
        },
        
        {
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'state7',
            'conditions': 'is_going_to_state67'
        },
        {
            'trigger': 'advance',
            'source': 'state7',
            'dest': 'state8',
            'conditions': 'is_going_to_state78'
        },
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state5',
            'conditions': 'is_going_to_state55'
        },
        {
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'state6',
            'conditions': 'is_going_to_state66'
        },
        {
            'trigger': 'advance',
            'source': 'state7',
            'dest': 'state7',
            'conditions': 'is_going_to_state77'
        },
        {
            'trigger': 'advance',
            'source': 'state8',
            'dest': 'state8',
            'conditions': 'is_going_to_state88'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2',
                'state3'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    print(update.message.text)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
