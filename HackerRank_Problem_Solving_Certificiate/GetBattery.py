def getBattery(events):
	battery = 50
	for i in events:
		if i < 0:
			battery = battery - i
		else:
			battery = battery + i
			if(battery > 100):
				battery = 100
	return battery