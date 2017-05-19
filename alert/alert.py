#!/usr/bin/env python
import urllib
import json
from urllib2 import Request, urlopen
import argparse

def create_alert(api_key, alert_name, callbackurl, keyword, threshold):
    values = {
        "key": api_key,
        "name": alert_name,
        "callbackurl": callbackurl,
        "keyword": keyword,
        "threshold": threshold
    }
    data = urllib.urlencode(values)
    request = Request("http://api.qsearch.cc/api/alert/v1/", data)
    response_body = urlopen(request).read()

    return json.loads(response_body)


def alert_list(api_key):
    values = {
        "key": api_key
    }
    url = "http://api.qsearch.cc/api/alert/v1/?"
    url_values = urllib.urlencode(values)
    response_body = urlopen(url + url_values).read()

    return json.loads(response_body)


def alert_info(api_key, alert_id):
    values = {
        "key": api_key
    }
    url_data = urllib.urlencode(values)
    url = "http://api.qsearch.cc/api/alert/v1/alert/{alert_id}?".format(alert_id=alert_id)
    response_body = urlopen(url + url_data).read()

    return json.loads(response_body)


def update_alert(api_key, alert_id, field, value):
    values = {
        "key":  api_key,
        "field": field,
        "value": value
    }
    url = "http://api.qsearch.cc/api/alert/v1/alert/{alert_id}".format(alert_id=alert_id)
    data = urllib.urlencode(values)
    request = Request(url, data)
    response_body = urlopen(request).read()

    return json.loads(response_body)


def delete_alert(api_key, alert_id):
    values = {
        "key": api_key
    }
    url = "https://api.qsearch.cc/api/alert/v1/alert/{alert_id}?".format(alert_id=alert_id)
    url_values = urllib.urlencode(values)
    request = Request(url + url_values)
    request.get_method = lambda: 'DELETE'
    response_body = urlopen(request).read()

    return json.loads(response_body)


def main(api_key):
    print "---Create alert---"
    result = create_alert(api_key, "sample", "https://www.example.com/callbackurl", "keyword", json.dumps({"count":1,"share":10, "like":100}))
    print result
    alert_id = result["id"]

    print  "---Alert list---"
    result = alert_list(api_key)
    for alert in result["data"]:
        print alert

    print "---Alert info---"
    print alert_info(api_key, alert_id)

    print "---Update alert info---"
    print "Update threshold : {0}".format(update_alert(api_key, alert_id, "threshold", json.dumps({"count":5})))
    print "Update name : {0}".format(update_alert(api_key, alert_id, "name", "new_alert"))
    print "Update callbackurl : {0}".format(update_alert(api_key, alert_id, "callbackurl", "https://qsearch.cc/callbackurl"))
    print "---New alert info---"
    print alert_info(api_key, alert_id)

    print "---Delete alert---"
    print delete_alert(api_key, alert_id)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--apikey', help='Your API Key.', required=True)
    args = parser.parse_args()

    main(args.apikey)
