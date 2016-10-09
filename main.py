from AlertGenerator import generate
import getopt
import sys 

#Command arguments
del sys.argv[0]
optlist, args = getopt.getopt(sys.argv, 'i:o:a:v')

_output = ""
_input = ""
alert = None
verbose = False

for opt in optlist:
	if opt[0] == '-o':
		_output = opt[1]
	if opt[0] == '-i':
		_input = opt[1]
	elif opt[0] == '-a':
		alert = opt[1]
	elif opt[0] == '-v':
		verbose = True

if not _output or not _input:
	print "Missing arguments : -i inputpath -o outputpath"
	sys.exit(0)


render = generate(_input, _output, alert)
if verbose:
	print render
