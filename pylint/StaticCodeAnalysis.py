

# To generate the default config file:
# pylint --generate-rcfile | out-file -encoding utf8 .pylintrc




#To run single file
import pylint
from pylint import epylint as lint

#pylint.run_pylint(argv=["main.py"])
#(pylint_stdout, pylint_stderr) = lint.py_run('main.py --disable C0303', return_std=True)




#To run whole package/project
from io import StringIO

from pylint.lint import Run
from pylint.reporters.text import TextReporter
from pylint.lint import pylinter

with open("pylint/Reports/report.out", "w") as f:
    reporter = TextReporter(f)
    Run(['./trip_planner_vmc','--rcfile=pylint/.pylintrc'], reporter=reporter, exit=False)
    #pylint.run_pylint(argv=["trip_planner",'--rcfile=.pylintrc'])

pylinter.MANAGER.clear_cache()

