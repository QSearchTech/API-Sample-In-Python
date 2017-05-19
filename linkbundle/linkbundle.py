#!/usr/bin/env python
import urllib
import json
from urllib2 import Request, urlopen
import argparse


def create_bundle(api_key, data):
    payload = {
        "key" : api_key,
        "data": data
    }
    url = "http://api.qsearch.cc/api/linkbundle/v1/create"
    rq = requests.post(url, data=payload)
    response_body = rq.text

    return json.loads(response_body)


def bundle_list(api_key):
    payload = {
        "key" : APIKEY
    }
    url = "http://api.qsearch.cc/api/linkbundle/v1/list"
    rq = requests.get(url, params=payload)
    response_body = rq.text

    return json.loads(response_body)


def api_quota(api_key):
    payload = {
        "key" : APIKEY
    }
    url = "http://api.qsearch.cc/api/linkbundle/v1/quota"
    rq = requests.get(url, params=payload)
    response_body = rq.text

    return json.loads(response_body)


def reporting(api_key, codes):
    payload = {
        "key" : api_key,
        "codes": codes
    }
    url = "http://api.qsearch.cc/api/linkbundle/v1/reporting"
    rq = requests.get(url, params=payload)
    response_body = rq.text


def archive(api_key):
    payload = {
        "key" : APIKEY,
        "codes": CODES
    }
    url = "http://api.qsearch.cc/api/linkbundle/v1/archive"
    rq = requests.get(url, params=payload)
    response_body = rq.text


def main(api_key):
    print "--- Create Bundle ---"
    result = create_segment(api_key, "new_segment", "1433215316907826,https://www.facebook.com/tvbsfb/")
    print "--- Bundle List ---"
    bundle_list(api_key)
    print "--- API Quota ---"
    api_quota(api_key)
    print "--- Reporting ---"
    reporting(api_key, codes)
    print "--- Archive Bundle ---"
    archive(api_key)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--apikey', help='Your API Key.', required=True)
    args = parser.parse_args()

    main(args.apikey)
