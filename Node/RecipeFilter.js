// Node.js Express: Recipe Filter

//recipes.js
var recipes = require('../recipes.json');
var router = require('express').Router();

router.get('/shopping-list', (res, res) =>{
	const ids = req.query.ids || [];
	if(ids && ids.length === 0){
		res.status(400);
	}
	const ing = [];
	const idsArray = ids.split(',');
	for(const recipe of recipes){
		if(idsArray && idsArray.includes(recipe.id.toString())){
			ing = [...ing, ...recipe.ingredients]
		}
	}
	if(ing.length > 0){
		res.status(200).json(ing)
	}
	else{
		res.status(404).send('NOT_FOUND')
	}
})