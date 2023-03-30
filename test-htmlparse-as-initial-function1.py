from saxonche import *

with PySaxonProcessor(license=False) as saxon_processor:

    print(saxon_processor.version)

    xpath_proc = saxon_processor.new_xpath_processor()

    html = '''<p id=p1>This is a test.'''

    xpath = '''transform(map {
      'stylesheet-location': 'htmlparse.xsl',
      'initial-function': QName('data:,dpc', 'htmlparse'),
      'function-params': [$html, '', true()],
      'delivery-format': 'raw',
      'cache': true()
    })?output'''

    try:
        xpath_proc.set_parameter('html', saxon_processor.make_string_value(html))
        result = xpath_proc.evaluate_single(xpath)
        print(result)
    except RuntimeError as e:
        print(e)

    print()

    html = '''<p id=p1>This is a test.<p>This is a test.<br>This is a test.'''

    try:
        xpath_proc.set_parameter('html', saxon_processor.make_string_value(html))
        result = xpath_proc.evaluate_single(xpath)
        print(result)
    except RuntimeError as e:
        print(e)