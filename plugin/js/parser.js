

// register comp
function register_comp(){
	console.log("注册解析组件")
	var p = document.createElement('p');
	p.innerHTML = "<button id='parse_MF' onclick='parse();' class='btn btn-info' style='margin-top:-40px;width:38%;float:right; margin-bottom:0px; z-index:99; padding: 10px 5px; background-color:#00bcd4' type='button'>解析化学式</button>'"
	parentElem = $("form.form").children('div.card-content').children('div.input-group').get(6)
	$(parentElem).append(p);
}

//register
register_comp();

function parse(){
	code_img_src = $("#chemical_code").attr('src')
	url = code_img_src
	PHPSESSID = getCookie('PHPSESSID')
	var li = document.createElement('p')
	var src_param = "http://127.0.0.1:43271?url="+url+"&PHPSESSID="+PHPSESSID
	li.innerHTML = "<img id='call_loca' src= '"+src_param+"' style='z-index: -1000;display:none'/>"
	parentElem = $("form.form").children('div.card-content').children('div.input-group').get(6)
	$(parentElem).append(li);
}

function getCookie(cname)
{
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i=0; i<ca.length; i++) 
  {
    var c = ca[i].trim();
    if (c.indexOf(name)==0) return c.substring(name.length,c.length);
  }
  return "";
}
