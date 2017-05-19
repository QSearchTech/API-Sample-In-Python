#!/usr/bin/env python
import urllib
import json
from urllib2 import Request, urlopen
import argparse


def post_crawling(api_key, pageid, start_time, end_time, token, fields):
    values = {
        "key": api_key,
        "pageid": pageid,
        "start_time": start_time,
        "end_time": end_time,
        "access_token": token,
    #    "fields": fields
    }
    url = 'https://api.qsearch.cc/api/crawling/v1/posts?'
    url_values = urllib.urlencode(values)
    response_body = urlopen(url + url_values).read()

    return json.loads(response_body)


def reaction_crawling(api_key, postids, token, fields="id,type"):
    values = {
        "key": api_key,
        "postids": postids,
        "access_token": token,
       "fields": fields
    }
    url = 'https://api.qsearch.cc/api/crawling/v1/reactions?'
    url_values = urllib.urlencode(values)
    response_body = urlopen(url + url_values).read()

    return json.loads(response_body)


def main(api_key, token):
    pageid = 135989949800414
    start_time = 1356998400
    end_time = 1359676800
    print "--- Post Crawling ---"
    print post_crawling(api_key, pageid, start_time, end_time, token, fields="id")

    postids = "430401096982804_1215510185138554,430401096982804_1214767195212853"
    print "--- Reaction Crawling ---"
    print reaction_crawling(api_key, postids, token)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--apikey', help='Your API Key.', required=True)
    parser.add_argument('-t', '--token', help='Your Access Token.', required=True)
    args = parser.parse_args()

    main(args.apikey, args.token)
