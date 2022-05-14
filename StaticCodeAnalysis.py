#pylint --generate-rcfile | out-file -encoding utf8 .pylintrc

import pylint
from pylint import epylint as lint

#pylint.run_pylint(argv=["main.py"])
#(pylint_stdout, pylint_stderr) = lint.py_run('main.py --disable C0303', return_std=True)

from io import StringIO

from pylint.lint import Run
from pylint.reporters.text import TextReporter
from pylint.lint import pylinter

with open("Reports/report.out", "w") as f:
    reporter = TextReporter(f)
    Run(['trip_planner','--rcfile=.pylintrc'], reporter=reporter, exit=False)
    #pylint.run_pylint(argv=["trip_planner",'--rcfile=.pylintrc'])

pylinter.MANAGER.clear_cache()

