from constants import PUSH_SNIPPET_URL

from requests import post


class Snippet:
    '''
    A class to create a snippet object and
    perform the push action to the POST API
    `more information. https://codehub.pythonanywhere.com/api/v1/docs#operation/snippet_create`_
    '''

    def __init__(self, title, body, lang, description=''):
        self.title = title
        self.body = body
        self.lang = lang
        self.description = description

    def push(self):
        
        data = {
            'title': self.title,
            'description': self.description,
            'body': self.body,
            'lang': self.lang,
        }

        r = post(
            PUSH_SNIPPET_URL,
            data=data,
        )
        return r
