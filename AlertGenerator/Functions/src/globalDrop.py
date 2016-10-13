def treat(params, globalParams):
	
	if 'params.source' not in params:
		return ""

	if params['params.source'] not in globalParams:
		return ""

	source = globalParams[params['params.source']]

	res = ""
	for key, content in source.iteritems():
		filters = []
		for param , value in params.iteritems():
			if 'params.metric.filters.' in param:
				filters.append(param)
		metric = content["params.metric.name"]+"{"
		for param in filters:
			metric+=param[22:]+'="#'+param+'",'
		if len(filters) > 0:
			metric = metric[:-1]
		metric+="}"

	return "lol"
	# params['rate'] = (100.0 - float(params['params.drop'].replace('%','')))/100
	# filters = []
	# for param , value in params.iteritems():
	# 	if 'params.metric.filters.' in param:
	# 		filters.append(param)
	
	# metric = "#params.metric.name{"
	# for param in filters:
	# 	metric+=param[22:]+'="#'+param+'",'
	# if len(filters) > 0:
	# 	metric = metric[:-1]
	# metric+="}"

	# smooth = params['params.metric.smooth']
	# if not isinstance(smooth, list):
	# 	smooth = [smooth]
	# if len(smooth) == 1:
	# 	smooth.append(smooth[0])
	# params['smooth1'] = smooth[0]
	# params['smooth2'] = smooth[1]


	# res = "increase("+metric+"[#smooth1]) < (#rate*increase("+metric+"[#smooth2] offset #params.offset)"
	# if 'params.from' in params and params['params.from'] != 'None':
	# 	res += " * (time() % 86400 > bool #params.from*3600)"
	# if 'params.to' in params and params['params.from'] != 'None':
	# 	res += " * (time() % 86400 < bool #params.to*3600)"
	# res += " )"
	# return res

def preTreat(params,globalParams):
	return params

def getRaw(params, globalParams):
	return ""
