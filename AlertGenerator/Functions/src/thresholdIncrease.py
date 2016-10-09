def preTreat(params):
	
	filters = []
	for param , value in params.iteritems():
		if 'params.metric.filters.' in param:
			filters.append(param)
	
	metric = ""
	for param in filters:
		metric+=param[22:]+"='#"+param+"',"
	if len(filters) > 0:
		metric = metric[:-1]
	
	params['filters'] = metric