
import requests
import re
import schedule
import time
import os
from twilio.rest import Client
from requests_html import HTMLSession

account_sid = 'XXXXXXXXXXXXXXXXXXX'
auth_token = 'XXXXXXXXXXXXXXXXXXX'
client = Client(account_sid, auth_token)

def run():
    session = HTMLSession()
    r = session.get('https://catalog.apps.asu.edu/catalog/classes/classlist?advanced=true&campusOrOnlineSelection=C&classNbr=70517&honors=F&promod=F&searchType=all&term=2227')
    r.html.render(sleep=2)

    test = r.html.find('.class-results-cell.seats', first=True).text
    test1 = re.split(' |\n',test)
    print (test1)
    int1 = int(test1[0])
    int2 = int(test1[2])
    if int1 > 0:
        print ('There are %d seats out of %d' % (int1, int2))
        message = client.messages \
            .create(
                body = 'There are %d seats out of %d' % (int1, int2),
                from_ = '(XXX)-XXX-XXXX',
                to = '(XXX)-XXX-XXXX'
            )

schedule.every(10).seconds.do(run)

while True:
    schedule.run_pending()
    time.sleep(1)

#testcommit

