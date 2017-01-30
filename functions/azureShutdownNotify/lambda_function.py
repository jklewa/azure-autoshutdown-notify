"""
Azure Auto-Shutdown Notification
A Lambda function to send a pushbullet notification to an Azure VM before its
automatically shuts down daily
"""

from __future__ import print_function
from libs.pushbullet import Pushbullet
import libs.bitly_api
import os

pb = Pushbullet(os.environ['PUSHBULLET_API_KEY'])
bitly = bitly_api.Connection(access_token=os.getenv(BITLY_ACCESS_TOKEN))

url_template = "{url60}"
title_template = "{vmName} will be shutting down soon..."
body_template = """
{vmName} will be shutting down in 15 minutes.

Skip this shutdown: {urlSkip}
Delay shutdown for an hour (default): {url60}
Delay shutdown for 2 hours: {url120}
"""

def lambda_handler(event, context):
    event['url60'] = bitly.shorten(event['delayUrl60'])
    event['url120'] = bitly.shorten(event['delayUrl120'])
    event['urlSkip'] = bitly.shorten(event['skipUrl'])

    push = pb.push_link(title_template.format(event), url_template.format(event), body=body_template.format(event))
    return push
