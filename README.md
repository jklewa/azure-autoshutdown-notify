# azure-autoshutdown-notify

This projex uses Apex to build the lambda function code.

```bash
apex build azureShutdownNotify > out.zip
```

Running the function requires to environment variables (configured in AWS console)

* `BITLY_ACCESS_TOKEN`: Your access token can be fetched using the following (per [pypi:bitly_api 0.3](https://pypi.python.org/pypi/bitly_api/0.3)):
  ```
curl -u “username:password” -X POST “https://api-ssl.bitly.com/oauth/access_token”
```

* `PUSHBULLET_API_KEY`: API key that can be obtained [here](https://www.pushbullet.com/account) (per [pypi:pushbullet.py 0.10.0](https://pypi.python.org/pypi/pushbullet.py/0.10.0))
