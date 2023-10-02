// Node.js Express: Find Recipe Step
// apps.js

app.use('/', indexRouter);
app.use('/recipes/step/', recipeRouter);

//recipes.js
// [1, 2, 3, 4, 5, 6, 7, 8]
function getIndex(timers, elapsedTime){
	for(let i = 0; i < timers.length; i++){
		if(timers[i] == elapsedTime){
			return i;
		}
	}

}

router.get('/:id', (req, res) => {
	const id = req.params.id;
	const elapsedTime = req.query.elapsedTime || 0;

	if(isNaN(id)){
		res.status(400).send('NOT_FOUND');
		return;
	}
	const selectedRecipe = recipes.filter( i => i.id === Number(id))[0];
	if(selectedRecipe){
		const{timers} = selectedRecipe;
		const index = getIndex(timers, elapsedTime);
		res.status(200).send(index);
		return; 
	}else{
		res.status(404).send('NOT_FOUND');
		return;
		}
})


module.exports = router;