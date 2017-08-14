import logging 
import os 

import flask from Flask 
from flask_ask import Ask, request, Statement, question, render_template

app = Flask(__name__)
ask = Ask(app,'/')
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@ask.launch 
def launch():
    return get_fact()   #basically starting the act at the launch oh the application 

@ask.intent('SomethingNew')
def get_fact():
    tot_facts = 4
    fact_i = randint(0,tot_facts-1)  #random is used so that we dont have to create one exxtra question for next fact        
    fact_text = render_template('some_facts{}'.format(fact_i)) 
    card_title = render_template('card_title')
    return statement(fact_text).simple_card(card_title,fact_text)

@ask.intent('Amazon.HelpIntent') #standard alexa intent
def help_me():
    hi =  render_template('help')
    return question(hi).reprompt(hi)

@ask.intent('Amazon.StopIntent') #standard alexa intent
def stop_it():
    going = render_template('going now bye')
    return statement(going)

@ask.intent('Amazon.CancelIntent') #standard alexa Intent
def cancel_it():
    cancel_me =  render_template('ok ok exiting chill')
    return statement(cancel_me)

@ask.session_ended
def session_end:
    return "{}",200


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
