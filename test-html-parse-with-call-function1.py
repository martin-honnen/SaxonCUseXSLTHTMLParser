from saxonche import *

with PySaxonProcessor(license=False) as saxon_processor:

    print(saxon_processor.version)

    xslt_proc = saxon_processor.new_xslt30_processor()

    try:
        htmlparser_executable = xslt_proc.compile_stylesheet(stylesheet_file='htmlparse.xsl')
    except RuntimeError as e:
        print(f'Compiling htmlparse.xsl failed: {e}')
        exit(1)

    html = '''<p id=p1>This is a test.'''

    try:
        result = htmlparser_executable.call_function_returning_value('{data:,dpc}htmlparse', [saxon_processor.make_string_value(html), saxon_processor.make_string_value(''), saxon_processor.make_boolean_value(True)])
        print(result)
    except RuntimeError as e:
        print(f'Error parsing HTML: {e}')

    print()

    html = '''<p id=p1>This is a test.<p>This is a test.<br>This is a test.'''

    try:
        result = htmlparser_executable.call_function_returning_value('{data:,dpc}htmlparse', [saxon_processor.make_string_value(html), saxon_processor.make_string_value(''), saxon_processor.make_boolean_value(True)])
        print(result)
    except RuntimeError as e:
        print(f'Error parsing HTML: {e}')