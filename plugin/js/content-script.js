window.onload = function(){
	//注入js/register.js文件
	var scripts = document.createElement('script');
	scripts.src = chrome.extension.getURL('js/parser.js');
	document.body.append(scripts);
	//注入css/register.css文件
}