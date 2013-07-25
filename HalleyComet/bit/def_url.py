#-*-coding:utf8-*-
from bit.models import Url
def long_to_short(long_url):
    short_url = ""
    tuple = (
        "a","b","c","d","e","f","j","h","i","g","k","l","m","n","o",
        "p","q","r","s","t",'u','v','w','x','y','z','A','B','C','D',
        'E','F','J','H','I','G','K','L','M','N','O','P','Q','R','S',
        'T','U','V','W','X','Y','Z','0','1','2','3','4','5',"6","7","8","9"
        )

    if long_url[:4] != "http":
        long_url = "http://" + long_url

    db_url = Url.objects.filter(long_url__exact=long_url)
    if db_url:
        short_url = db_url[0].short_url
    else:
        url = Url.objects.create(long_url=long_url, short_url="")
        db_url = Url.objects.filter(long_url__exact=long_url)
        db_url_id = db_url[0].id
        while db_url_id > 0:
            short_int = db_url_id % 62
            short_var = tuple[short_int]
            short_url = short_var + short_url
            db_url_id = db_url_id / 62
    
        while len(short_url) < 6:
            short_url = "a" + short_url
    
        short_url = "localhost/" + short_url
        db_url.update(short_url=short_url)
    return short_url

def short_to_long(short_hash):
    short_url = "localhost/%s" % short_hash
    long_url = Url.objects.filter(short_url__exact=short_url)
    full_long_url = long_url[0].long_url
    return full_long_url
