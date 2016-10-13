def treat(params, globalParams):
	
	if 'params.source' not in params:
		return ""

	if params['params.source'] not in globalParams:
		return ""

	source = globalParams[params['params.source']]

	res = "("

	count = 0
	for key, content in source.iteritems():
		count += 1
		content['rate'] = (100.0 - float(content['params.drop'].replace('%','')))/100
		filters = []
		for param , value in content.iteritems():
			if 'params.metric.filters.' in param:
				filters.append([param,value])

		metric = content["params.metric.name"]+"{"
		for filt in filters:
			metric+=filt[0][22:]+'="'+filt[1]+'",'
		if len(filters) > 0:
			metric = metric[:-1]
		metric+="}"
		
		smooth = content['params.metric.smooth']
		if not isinstance(smooth, list):
			smooth = [smooth]
		if len(smooth) == 1:
			smooth.append(smooth[0])

		res += " (increase(%s[%s])/(increase(%s[%s] offset %s) - %s) + " % (metric, smooth[0], metric, smooth[1], content['params.offset'], str(content['rate']))  
	
	res = res[:-3] + ")/"+str(count)

	return res

def preTreat(params,globalParams):
	return params

def getRaw(params, globalParams):
	return ""
