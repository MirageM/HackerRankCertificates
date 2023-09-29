// Image Cloning
class Size{
	this.width = width;
	this.height = height;
}

class Image{
	constructor(url, size)
	{
		this.url = url;
		this.size = size;
	}
	getUrl(){return this.url;}
	setUrl(url){this.url = url;}
	setSize(w, h)
	{
		this.size.width = w;
		this.size.height = h;
	}
	getSize(){return this.size;}
	cloneImage()
	{
		return new Image(this.url, new Size(this.size.width, this.size.height));
	}
}

class Size{
	this.width = width;
	this.height = height;
}
class Image{
	constructor(url, size){
		this.url = url;
		this.size = size;
	}
	getUrl(){return this.url;}
	setUrl(url){this.url = url;}
	getSize(){return this.size;}
	setSize(w, h){
		this.size.width = w;
		this.size.height = h;
	}
	cloneImage(){
		return new Image(this.url, new Size(this.size.width, this.size.height));
	}
}


class Size{
	this.wdith = width;
	this.height = height;
}
class Iage{
	constructor(url, size){
		this.url = url;
		this.size = size;
	}
	getUrl(){return this.url;}
	setUrl(url) {this.url = url;}
	getSize(){return this.size;}
	setSize(w, h){
		this.size.width = w;
		this.size.height = h;
	}
	cloneImage(){
		return new Image(this.url, new Size(this.size.width, this.size.height));

	}
	

}