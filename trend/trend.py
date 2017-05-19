#coding=utf8
#!/usr/bin/env python
import urllib
import json
from urllib2 import Request, urlopen
import argparse


def timeSeries(api_key, query, st, et, nation="Global"):
    values = {
            "key" : api_key,
            "q": query,
            "nation": nation,
            "st": st,
            "et": et
        }

    url = "http://api.qsearch.cc/api/trend/v1/series?"
    url_values = urllib.urlencode(values)
    response_body = urlopen(url+url_values).read()

    return json.loads(response_body)


def influencer(api_key, query, st, et, nation="Global"):
    values = {
            "key" : api_key,
            "q": query,
            "nation": nation,
            "st": st,
            "et": et,
            "facet": "fromid"
        }

    url = "http://api.qsearch.cc/api/trend/v1/influencers?"
    url_values = urllib.urlencode(values)
    response_body = urlopen(url+url_values).read()

    return json.loads(response_body)


def hotTopic(api_key, query, st, et, nation="Global"):
    values = {
        "key" : api_key,
        "q": query,
        "nation": nation,
        "st": st,
        "et": et,
        "facet": "title_s"
    }
    url = "http://api.qsearch.cc/api/trend/v1/topics?"
    url_values = urllib.urlencode(values)
    response_body = urlopen(url+url_values).read()

    return json.loads(response_body)


def main(api_key):
    query = "食品安全"
    st = "2017-1-10"
    et = "2017-3-10"
    print "--- Time Series ---"
    print timeSeries(api_key, query, st, et, nation="Global")
    print "--- Influencer ---"
    print influencer(api_key, query, st, et, nation="Global")
    print "--- Hot Topic ---"
    print hotTopic(api_key, query, st, et, nation="Global")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--apikey', help='Your API Key.', required=True)
    args = parser.parse_args()

    main(args.apikey)
