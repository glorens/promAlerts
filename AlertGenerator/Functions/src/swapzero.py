def preTreat(params):
	duration = params['params.metric.duration']
	if duration[-1:] == 'm':
		params['params.from'] =  round(params['params.from'] + float(duration[:-1])/60, 2)
	if duration[-1:] == 'h':
		params['params.from'] =  params['params.from'] + int(duration[:-1])
