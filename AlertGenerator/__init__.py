from YAMLAlertParser import YAMLAlertParser
from FunctionController import FunctionController
from Renderer import Renderer
import os

ymlParser = YAMLAlertParser(None)
func = FunctionController()
funcFolder =  os.path.dirname(os.path.realpath(__file__))+'/Functions/functions.yml'
func.parseFile(funcFolder)
renderer = Renderer(func)

def generate(_input, _output, alert = None):
	params = ymlParser.generateRules(_input)
	
	out = ""
	for rules, content in params.iteritems():   
		for mult, rparams in content.iteritems():
			if not alert or (alert and alert in [rules, rparams['name']]):
				out+= renderer.renderAlert(rparams) + "\n"

	f = open(_output, 'w')
	f.write(out)
	f.close()

	return out


