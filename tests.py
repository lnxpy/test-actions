from unittest import TestCase, main

from utils import Snippet


class SnippetTestCase(TestCase):

    def setUp(self) -> None:
        self.data = {
            'title': 'Sample Title',
            'description': 'Sample Description',
            'body':'Sample Body',
            'lang': 'python',
        }

    def testSnippetPush(self):
        code = Snippet(**self.data).push().status_code
        self.assertEqual(code, 201)


if __name__ == '__main__':
    main()