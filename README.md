# azure-autoshutdown-notify

An AWS lambda function forwards Azure's VM auto-shutdown notification (Webhook) to your Pushbullet account.

## Setup

1. Download the latest release's .zip file [here](https://github.com/jklewa/azure-autoshutdown-notify/releases)
2. Create a *Blank (Python 2.7) Function* in the [AWS Lambda Management](https://console.aws.amazon.com/lambda/home) console.
3. Upload the .zip file in place of the default code.\
4. The function *requires two environment variables* (configured in AWS console):

  * `BITLY_ACCESS_TOKEN`: Used to shorten restart delay links - Fetch your access token from Bitly's OAuth API (per [bitly_api==0.3](https://pypi.python.org/pypi/bitly_api/0.3)):
  ```
  curl -u “username:password” -X POST “https://api-ssl.bitly.com/oauth/access_token”
  ```

  * `PUSHBULLET_API_KEY`: API key can be generated from your [Account Settings](https://www.pushbullet.com/account) page (per [pushbullet.py==0.10.0](https://pypi.python.org/pypi/pushbullet.py/0.10.0))

## Building this project for development

This projex uses [Apex](https://github.com/apex/apex) to build the lambda function code. `pip` must be in your PATH to fetch external dependencies.

```bash
apex build azureShutdownNotify > out.zip
```
