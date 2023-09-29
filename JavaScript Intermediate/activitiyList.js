// Activity List
function Activity(amount){
	this.setAmount(amount);
}
Activity.prototype.setAmount = (amount)=>{
	if(amount<=0){
		return false;
	}
	else{
		this.amount = amount;
		return true;
	}
}
Acitivity.prototype.getAmount = ()=>{return this.amount;}

function Payment(amount, receiver){
	this.setAmount(amount);
	this.setReceiver(receiver);
}
Payment.prototype = Object.create(Activity.prototype);
Payment.prototype.setReceiver = (receiver) =>{
	this.receiver = receiver;
	return true;
}

Payment.prototype.setReceiver = (receiver) =>
function Refund(amount, sender){

}