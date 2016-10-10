import sys
class Renderer:

	def __init__(self, functions):
		self.functions = functions

	def replaceVars(self, stri, params, chain = None):
		
		for key, value in params.iteritems():
			if "#"+key in stri:
				
				if chain and key in chain:
					print "Loop through keys : "
					chain.append(key)
					print chain
					sys.exit(0)

				if '#' in str(value):
					if not chain:
						chain = []
					chain.append(key)
					value = self.replaceVars(value, params, chain)
				stri = stri.replace(str('#'+key), str(value))

		return stri 

	def renderAlert(self, data):

		func = data['func']
		raw = self.functions.renderFunc(func, data)
		out = "ALERT #name\n"
		out += "	IF "+raw+"\n"
		out += "	FOR #for\n"

		labels = {}
		for param , value in data.iteritems():
			if 'labels.' in param:
				labels[param[7:]] = value
		if len(labels) > 0:
			out += "	LABELS {"
			labs = ""
			for label, value in labels.iteritems():
				labs += label+' = "'+value+'",'
			out += labs[:-1]
			out += '}\n'

		# out += "	LABELS #for\n"
		out += "	ANNOTATIONS {\n"
		out += "		summary='#summary'\n"
		out += "		description='#description'\n"
		out += "	}\n"

		out = self.replaceVars(out, data)

		return out