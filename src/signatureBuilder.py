'''
Code signature
written: KYLiN
This is a code build string of signature code
Date: 05/07/22
'''

COMMENT_STYLES = [('/*', '*/'),
                  ('\'\'\'', '\'\'\''),
                  ('=begin', '=end'),
                  ('{-', '-}'),
                  ('<!--', '-->')]

LANGUAGES_COMMENT = {'C/C++': COMMENT_STYLES[0],
                     'Java': COMMENT_STYLES[0],
                     'Python': COMMENT_STYLES[1],
                     'Ruby': COMMENT_STYLES[2],
                     'Golang': COMMENT_STYLES[0],
                     'Haskell': COMMENT_STYLES[3],
                     'Rust': COMMENT_STYLES[1],
                     'HTML': COMMENT_STYLES[4]}


def signature_Builder(name: str, title: str, date: str, body: str, lang: str) -> str:
    if lang != None:
        commentStyle = LANGUAGES_COMMENT[lang]
    else:
        commentStyle = LANGUAGES_COMMENT['C/C++']
    out = commentStyle[0]

    if title != '':
        out += f'\nTitle:{title}\n'

    if name != '':
        out += f'Written By {name}\n'

    if body != '':
        out += body

    out += f'Date: {date}\n'
    out += commentStyle[1]

    return out
