#!/usr/bin/env python
import urllib
import json
from urllib2 import Request, urlopen
import argparse


def create_segment(api_key, segment_name, pages):
    values = {
        "key": api_key,
        "name": segment_name,
        "pages": pages
    }

    url = "http://api.qsearch.cc/api/segment/v1/"
    url_values = urllib.urlencode(values)
    req = Request(url, data=url_values)
    response_body = urlopen(req).read()

    return json.loads(response_body)


def add_pages(api_key, segment_id, pages):
    values = {
        "key": api_key,
        "pages": pages
    }

    url = "http://api.qsearch.cc/api/segment/v1/{segment_id}".format(segment_id=segment_id)
    url_values = urllib.urlencode(values)
    req = Request(url, data=url_values)
    response_body = urlopen(req).read()

    return json.loads(response_body)


def segment_list(api_key):
    values = {
        "key": api_key,
    }
    url = "http://api.qsearch.cc/api/segment/v1/?"
    url_values = urllib.urlencode(values)
    response_body = urlopen(url + url_values).read()

    return json.loads(response_body)


def segment_info(api_key, segment_id):
    values = {
        "key": api_key,
    }
    url = "http://api.qsearch.cc/api/segment/v1/{segment_id}?".format(segment_id=segment_id)
    url_values = urllib.urlencode(values)
    response_body = urlopen(url + url_values).read()

    return json.loads(response_body)


def delete_segment_pages(api_key, segment_id, page_id):
    values = {
        "key": api_key,
    }

    url = "http://api.qsearch.cc/api/segment/v1/{segment_id}/item/{page_id}".format(segment_id=segment_id, page_id=page_id)
    url_values = urllib.urlencode(values)
    req = Request(url + '?' + url_values)
    req.get_method = lambda: 'DELETE'
    response_body = urlopen(req).read()

    return json.loads(response_body)


def delete_segment(api_key, segment_id):
    values = {
        "key": api_key
    }

    url = "http://api.qsearch.cc/api/segment/v1/{segment_id}".format(segment_id=segment_id)
    url_values = urllib.urlencode(values)
    req = Request(url + '?' + url_values)
    req.get_method = lambda: 'DELETE'
    response_body = urlopen(req).read()

    return json.loads(response_body)


def main(api_key):
    print "--- Create Segment ---"
    result = create_segment(api_key, "new_segment", "1433215316907826,https://www.facebook.com/tvbsfb/")
    print result
    segment_id = result["id"]

    print "--- Segment List ---"
    result = segment_list(api_key)

    for segment in result["data"]:
        print segment

    print "--- Add Pages ---"
    print add_pages(api_key, segment_id, "https://www.facebook.com/apple.realtimenews/")

    print "--- Segment Info ---"
    print segment_info(api_key, segment_id)

    print "--- Delete Pages in Segment ---"
    print delete_segment_pages(api_key, segment_id, "1433215316907826")
    print "--- New Segment info ---"
    print segment_info(api_key, segment_id)

    print "--- Delete segment ---"
    print delete_segment(api_key, segment_id)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--apikey', help='Your API Key.', required=True)
    args = parser.parse_args()

    main(args.apikey)
