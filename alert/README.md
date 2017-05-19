# Qsearch Alert API
# Introduction
   QSearch Alerts is a social behavior change detection and notification service. The service sends emails to the user when it finds new results—such as new likes, new shares, or content change — that match the user's monitoring setting(s). By creating a QSearch Alert, you can get email notifications any time QSearch finds new results on a topic that interests you or receive updates in real time with webhooks. With QSearch Alert API, your app can subscribe to updates in certain pieces of data. When a change occurs, the API sends an HTTP 'POST' request to a callback URL you set up for your app.

## Prerequisites

1. Create project on the [Qsearch API Service](https://api.qsearch.cc)

## Running the samples
    $ python alert.py -k your-api-key
