import urls
import urllib2
import json
import time
import csv

with open('fc.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow([
        'Key',
        'Name',
        'Year',
        'Rank By',
        'Rank',
        'Assets',
        'Assets %',
        'Giving',
        'Giving %',
        'Gifts Received',
        'Gifts Received %',
        'State',
        'Type'])

    for url in urls.generator():
        print "Processing: %s" % url

        try:
            response = urllib2.urlopen(url)
        except urllib2.URLError, e:
            print "URLError: " + url + " " + e.reason
            time.sleep(1)
        except urllib2.HTTPError, e:
            print "HTTPError: " + url + " " + e.code
            time.sleep(1)

        raw = response.read()
        data = json.loads(raw)

        for record in data['response']['rankings']:
            writer.writerow([
                record['foundation']['gm_key'],
                record['foundation']['name'],
                data['meta']['params']['year'],
                data['meta']['params']['rank_by'],
                record['rank'],
                record['assets']['amount'],
                record['assets']['pct'],
                record['giving']['amount'],
                record['giving']['pct'],
                record['gifts_received']['amount'],
                record['gifts_received']['pct'],
                record['state']['name'],
                record['type']['name']])