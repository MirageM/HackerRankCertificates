// Weekday Text
function weekdayText(weekdays){
	return function(num){
		console.log(weekdays, num);
		if(Number(num) === - 1 || Number(num) > 6){
			throw new Error("Invalid weekday number")
		}
		if(Number(num) > weekdays.length){
			throw new Error("Invalid weekday number")
		}
		return weekdays[Number(num)]
	}
}