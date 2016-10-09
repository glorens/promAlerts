import yaml

class YAMLAlertParser:

	DELIMITOR = '.' 

	def __init__(self, config):
		self.config = config

	def isAMultiAlertParam(self, data):
		for key in data:
			if str(key)[0] == "_":
				return True

		return False

	def isAMulitValuesParam(self, data):
		for key in data:
			if not isinstance(key, int):
				return False

		return True

	def genMultipleValues(self, tab, key, value):
		for ruleName in tab:
			tab[ruleName][key] = []
			for n, val in value.iteritems():
				tab[ruleName][key].append(val)


	def fillTab(self, tab, key, values):
		if '_d' in values:
			for name in tab:
				tab[name][key] = values['_d']
		
		for name in values:
			if not name in tab:
				tab[name] = dict(tab['_d'])
			tab[name][key] = values[name]	

	def transformKeys(self, data):

		newData = {}
		for key, value in data.iteritems():

			key = key[1:]

			if key[0:10] == 'condition.':
				key = key[10:]
			
			nKey = key.split('.')
			newkey = None
			last = nKey[len(nKey) - 1]
			if last[-3:] == ' as':
				newkey = last[0:-3]
				key = ".".join(nKey[:-1])+"."+newkey
			elif ' as ' in last:
				newkey = last.split(' as ')[1]
				key =  ".".join(nKey[:-1])+"."+last[:-(len(newkey)+4)]

			newData[key] = value
			if newkey:
				newData[newkey] = value

		return newData


	def iterativeGenerateParams(self, data, chain, tab):
		for key, value in data.iteritems():
			if not isinstance(value, dict):
				for ruleName in tab:
					tab[ruleName][chain+self.DELIMITOR+str(key)] = value
			else:
				if self.isAMultiAlertParam(value):
					self.fillTab(tab, chain+self.DELIMITOR+str(key), value)
				elif self.isAMulitValuesParam(value):
					self.genMultipleValues(tab, chain+self.DELIMITOR+str(key), value)
				else:
					self.iterativeGenerateParams(value, chain+self.DELIMITOR+str(key), tab)

	def generateParams(self, data):
		params = {'_d' : {} }
		self.iterativeGenerateParams(data, '', params)
		if len(params) > 1:
			params.pop('_d', None)
		
		for key, data in params.iteritems():
			params[key] = self.transformKeys(data) 
		return params

	def generateRules(self, filepath):
		f = open(filepath)
		datas = yaml.safe_load(f)
		f.close()
		rules = datas['alerts']
		rulesParam = {}
		for rule, data in rules.iteritems():
			rulesParam[rule] =  self.generateParams(data)
		
		return rulesParam
