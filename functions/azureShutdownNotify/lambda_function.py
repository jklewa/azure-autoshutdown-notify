"""
Azure Auto-Shutdown Notification
A Lambda function to send a pushbullet notification to an Azure VM before its
automatically shuts down daily
"""

import os, sys
sys.path.append(os.path.join(sys.path[0],'libs'))

from pushbullet import Pushbullet
import bitly_api

pb = Pushbullet(os.environ['PUSHBULLET_API_KEY'])
bitly = bitly_api.Connection(access_token=os.getenv('BITLY_ACCESS_TOKEN'))

url_template = "{url60}"
title_template = "{vmName} will be shutting down soon..."
body_template = """
{vmName} will be shutting down in 15 minutes.

Skip this shutdown: {urlSkip}
Delay shutdown for an hour (default): {url60}
Delay shutdown for 2 hours: {url120}
"""

def lambda_handler(event, context):
    print "Event:", event
    event['url60'] = bitly.shorten(event['delayUrl60'])['url']
    event['url120'] = bitly.shorten(event['delayUrl120'])['url']
    event['urlSkip'] = bitly.shorten(event['skipUrl'])['url']

    title = title_template.format(**event)
    url = url_template.format(**event)
    body = body_template.format(**event)
    
    #push = pb.push_note(title, body=body)
    push = pb.push_link(title, url, body=body)
    return push
