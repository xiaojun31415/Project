function changeImage(){
	element =document.getElementById("imageID")
		if(element.src.match("pic_bulbon")){
		element.src="./image/light/pic_bulboff.gif";
		}
		else{
		element.src="./image/light/pic_bulbon.gif";
		}
	}