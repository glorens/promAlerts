import yaml
import inspect

class FunctionController:

	def __init__(self):
		self.func = {}

	def parseFile(self, filepath):
		f = open(filepath)
		datas = yaml.safe_load(f)
		f.close()
		for rule, content in datas.iteritems():
			self.func[rule] = content
	def renderPackageName(self, path):

		return "Functions.src."+path

	def renderFunc(self, name, params, globalParams):

		if name not in self.func:
			print "This function is not handled "+name
			return 0

		func = self.func[name]
		if 'treat' in func:
			pacName = self.renderPackageName(func['treat'])
		 	treat = __import__(pacName, globals(),locals(), fromlist=["treat"])
			if len(inspect.getargspec(treat.treat).args) > 1:
				return treat.treat(params, globalParams)
			return treat.treat(params)
		elif 'preTreat' in func:
			if 'raw' not in func:
				print "Missing raw"
			pacName = self.renderPackageName(func['preTreat'])
			pretreat = __import__(pacName, globals(),locals(), fromlist=["preTreat"])
			if len(inspect.getargspec(pretreat.preTreat).args) > 1:
				pretreat.preTreat(params, globalParams)
			else:
			 	pretreat.preTreat(params)
			return func['raw']
		elif 'raw' in func:
			return func['raw']

		