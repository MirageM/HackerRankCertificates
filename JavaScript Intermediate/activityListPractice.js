// Activity List
function Activity(amount){
	this.setAmount(amount);
}
Activity.prototype.setAmount = (amount) => {this.amount = amount; }
Activity.prototype.getAmount = () => {return this.amount;}

Payment.prototype = Object.create(Activity.prototype);
function Payment(amount, receiver){
	this.setAmount(amount);
	this.setReceiver(amount);
}
Payment.prototype.setReceiver = (receiver) => {this.receiver = receiver;}
Payment.prototype.getReceiver = () => {return this.receiver;}

Refund.prototype = Object.create(Activity.prototype);
function Refund(amount, sender){
	this.setAmount(amount);
	this.setSender(sender);
}
Refund.prototype.setSender = (sender) => {this.sender = sender;}
Refund.prototype.getSender = () => {return this.sender;}