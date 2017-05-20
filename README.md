# API-Sample-In-Python


This repository holds the samples used in the python documentation on [http://api.qsearch.cc](http://api.qsearch.cc).

For more detailed introduction to a product, check the README.md in the corresponding folder.

## API
- Trend API
- Crawling API
- Alert API
- Segment API
- Linkbundle API


------

## Get Start

1. Get Project Key
Create a new project. [Create Project](https://api.qsearch.cc/projects)
2. Make a HTTP request

```
#-*- coding: UTF-8 -*-
#/usr/bin/env python

import urllib
import json
from urllib2 import Request, urlopen
values = {
    "key" : "7680adac5f9077b89d214dcee4a7f9e6e0a984f83f7824e",
    "q": "water security",
    "nation": "Global",
    "st": "2016-9-7",
    "et": "2016-10-7"
}

url = "http://api.qsearch.cc/api/trend/v1/series?"
url_values = urllib.urlencode(values)
response_body = urlopen(url+url_values).read()

```

----

## Premium Solutions?

We provide the stable API Connection for you. [api\_service\_support@qsearch.cc](api_service_support@qsearch.cc)

----

QSearch aims to provide a stable and reliable service.


