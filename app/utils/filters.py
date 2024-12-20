def format_date(date):
    return date.strftime('%m/%d/%y')
  
from datetime import datetime
(format_date(datetime.now()))

def format_url(url):
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

(format_url('http://google.com/test/'))
(format_url('https://www.google.com?q=test'))

def format_plural(amount, word):
    if amount != 1:
        return word + 's'

    return word

(format_plural(2, 'cat'))
(format_plural(1, 'dog'))