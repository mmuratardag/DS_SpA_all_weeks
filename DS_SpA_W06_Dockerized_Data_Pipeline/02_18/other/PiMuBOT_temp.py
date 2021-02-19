
# pip install pyjokes
import pyjokes
import requests

webhook_url = "https://hooks.slack.com/services/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"

joke = pyjokes.get_joke()

data = {'text': joke}
requests.post(url=webhook_url, json = data)