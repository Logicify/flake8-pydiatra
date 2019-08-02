#    Pydiatra plugin for flake8.
#    Copyright (C) 2019 Kirill Malyshev
#    The MIT License (MIT)
#    
#    Permission is hereby granted, free of charge, to any person obtaining
#    a copy of this software and associated documentation files
#    (the "Software"), to deal in the Software without restriction,
#    including without limitation the rights to use, copy, modify, merge,
#    publish, distribute, sublicense, and/or sell copies of the Software,
#    and to permit persons to whom the Software is furnished to do so,
#    subject to the following conditions:
#    
#    The above copyright notice and this permission notice shall be
#    included in all copies or substantial portions of the Software.
#    
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from sys import stderr

from pydiatra import checks

__version__ = '0.1.0'


class PydiatraChecker():
    name = 'flake8-pydiatra'
    version = __version__

    # @formatter:off
    messages = {
        'assertion-always-true':            'PYD001',
        'async-await-used-as-name':         'PYD002',
        'embedded-code-copy':               'PYD003',
        'except-shadows-builtin':           'PYD004',
        'bare-except':                      'PYD005',
        'hardcoded-errno-value':            'PYD006',
        'inconsistent-indentation':         'PYD007',
        'mkstemp-file-descriptor-leak':     'PYD008',
        'obsolete-pil-import':              'PYD009',
        'py3k-compat-warning':              'PYD010',
        'regexp-bad-escape':                'PYD011',
        'regexp-duplicate-range':           'PYD012',
        'regexp-incompatible-flags':        'PYD013',
        'regexp-misplaced-inline-flags':    'PYD014',
        'regexp-misplaced-flags-argument':  'PYD015',
        'regexp-overlapping-ranges':        'PYD016 Overlapping regexp ranges: \'{1}\', \'{2}\'',
        'regexp-redundant-flag':            'PYD017',
        'regexp-syntax-error':              'PYD018',
        'regexp-syntax-warning':            'PYD019',
        'string-exception':                 'PYD020',
        'string-formatting-error':          'PYD021',
        'syntax-error':                     'PYD022',
        'syntax-warning':                   'PYD023 {1}',
        'sys.hexversion-comparison':        'PYD024',
        'sys.version-comparison':           'PYD025',
    }
    # @formatter:on

    def __init__(self, tree, filename, lines):
        self.filename = filename
        self.lines = lines
        checks.load_data()

    def run(self):
        for tag in checks.check_file(self.filename):
            message_template = self.messages.get(tag.name, None)

            if message_template is None:
                print(f'flake8_pydiatra warning: unsupported check: {tag}', file=stderr)
            else:
                if ' ' not in message_template:
                    # PYD005 bare except
                    message_template = '{0} {1}'.format(message_template, tag.name.replace('-', ' '))

                if '{' in message_template and '}' in message_template:
                    message = message_template.format(*tag.args)
                else:
                    message = f'{message_template}'
                    if len(tag.args) > 1:
                        message += ': ' + ' '.join(str(arg) for arg in tag.args[1:])

                yield (tag.lineno or 1, 0, message, type(self))
