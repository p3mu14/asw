import requests
import json
from twilio.rest import Client
import time
import datetime
print(r"""
            _   _  _   _   ___  ___ _  ___   _____ ___ 
           /_\ | \| | /_\ | _ \/ __| || \ \ / / _ / _ \
          / _ \| .` |/ _ \|   | (__| __ |\ V /\_, \_, /
         /_/ \_|_|\_/_/ \_|_|_\\___|_||_| |_|  /_/ /_/ 
                         Twilio Get Balance And phone number
                         john.dhoe412@gmail.com
                         https://www.facebook.com/jancoxx412
                         """)
account_sid = raw_input(" [+] Input your Twilio account sid : ")
auth_token = raw_input(" [+] Input your Twilio Auth Key : ")
time.sleep(1)
print " [+] Checking ...."
time.sleep(1)


def get_balance():
    r = requests.get('https://api.twilio.com/2010-04-01/Accounts/'+account_sid+'/Balance.json', auth=(account_sid, auth_token))
    Json = json.dumps(r.json())
    resp = json.loads(Json)
    balance = resp ['balance']
    currency = resp ['currency']
    return str(balance)+' '+str(currency)

def get_phone():
    client = Client(account_sid, auth_token)
    incoming_phone_numbers = client.incoming_phone_numbers.list(limit=20)
    for record in incoming_phone_numbers:
        return record.phone_number
def get_type():
    client = Client(account_sid, auth_token)
    account = client.api.accounts.create()  
    return account.type

def send_sms():
    try:
        phone = get_phone()
        client = Client(account_sid, auth_token)
        message = client.messages.create(
                                  body='Gendeng Squad - SUCCES SEND TWILIO',
                                  from_= phone,
                                  to='+19295007090'
                              )
        return message.status
    except:
        return 'die'

def result():
    try:
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        balance = get_balance()
        number = get_phone()
        type = get_type()
        send = send_sms()
        if send == 'die':
            status = 'CANT SEND SMS'
        else:
            status = 'LIVE'
        print "================================================"
        print " [+] STATUS : {}".format(str(status))
        print " [+] Account SID : {}".format(str(account_sid))
        print " [+] Auth Key :  {}".format(str(auth_token))
        print " [+] Balance :  {}".format(str(balance))
        print " [+] Phone Number list : {}".format(str(number))
        print " [+] Account Type : {}".format(str(type))
        print " [+] Gendeng Squad Twilio Checker"
        print "================================================"
        open('twilio_result '+date+'.txt','a').write("[+] STATUS : {}\n[+] Account SID : {}\n[+] Auth Key : {}\n[+] Balance : {}\n[+] Phone number list : {}\n[+] Account Type : {} \n".format(str(status),str(account_sid),str(auth_token),str(balance),str(number),str(type)))
    except:
        print " [+] Api Invalid"

result()