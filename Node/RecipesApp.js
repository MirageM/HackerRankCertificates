
//recipes.js
router.get("", (req, res) => {
	const {page, limit} = req.query;
	const pageParam = page || 1;
	const limitParam = limit || 3;
	const higherRange = pageParam * limitParam;
	const lowerRange = higherRange - limitParam;
	res.status(200).json(recipes.slice(lowerRange, higherRange));
})
module.exports = router;