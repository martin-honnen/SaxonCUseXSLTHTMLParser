from saxonche import *

with PySaxonProcessor(license=False) as saxon_processor:

    print(saxon_processor.version)

    xslt_proc = saxon_processor.new_xslt30_processor()

    xslt_executable = xslt_proc.compile_stylesheet(stylesheet_file='import-htmlparse-test1.xsl')

    result = xslt_executable.call_template_returning_string()

    print(result)