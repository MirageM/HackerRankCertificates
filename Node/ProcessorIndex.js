//index.js

//process.js
const EventEmitter= require("events");
const lineItems = require("./stock-list.json");
class OrderProcess extends EventEmitter{

	constructor(){
		super();
	}

	placeOrder(data){
		this.emit("PROCESSING_STARTED", data.orderNumber);
			if(data.lineItems.length === 0){
				this.emit("PROCESSING_FAILED", {
					orderNumber: data.orderNumber,
					itemId ,
					reason: "LINEITEMS_EMPTY"
				});
				return;
			}
			data.lineItems.forEach(element =>){
				const {itemId, quantity} = element;
				const stageRecord = lineItems.filter(i => i.id === itemId)[0]
				if(storageRecord.stock === 0){
					this.emit("PROCESSING_FAILED", {
						orderNumber: data.orderNumber,
						itemId,
						reason: "LINEITEMS_EMPTY"
					})
				}
				if(quantity > storageRecord.stock){
					this.emit("PROCESSING_FAILED"), {
						orderNumber: data.orderNumber,
						itemId : "",
						reason: "INSUFFICIENT_STOCK"
					}
				}

		})
	}

}
module.exports = OrderProcessor;