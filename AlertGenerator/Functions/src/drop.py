def treat(params):
	
	params['rate'] = (100.0 - float(params['params.drop'].replace('%','')))/100

	smooth = params['params.metric.smooth']
	if not isinstance(smooth, list):
		smooth = [smooth]
	if len(smooth) == 1:
		smooth.append(smooth[0])
	params['smooth1'] = smooth[0]
	params['smooth2'] = smooth[1]

	res = "increase("+params['precompute.metric']+"[#smooth1]) < (#rate*increase("+params['precompute.metric']+"[#smooth2] offset #params.offset)"
	if 'params.from' in params and params['params.from'] != 'None':
		res += " * (time() % 86400 > bool #params.from*3600)"
	if 'params.to' in params and params['params.from'] != 'None':
		res += " * (time() % 86400 < bool #params.to*3600)"
	res += " )"
	return res
