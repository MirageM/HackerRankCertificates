// Data Finder
function dataFinder(data){
	return function find(minRange, maxRange, value){
		console.log(data, minRange, maxRange, value);
		if(maxRange > data.length - 1){
			throw new Error("Invalid range")
		}
	}
}