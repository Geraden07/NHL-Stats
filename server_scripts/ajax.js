function CreateRequestObject()
{
	var requestObject;
	
	if (window.XMLHttpRequest)
	{//Safari, Firefox, Opera...
		requestObject = new XMLHttpRequest();
	}
	else
	{//IE 5+
		requestObject = new ActiveXObject("Microsoft.XMLHTTP");
	}

	return requestObject;
}

var requestObject = CreateRequestObject();

function sendRequest(pageNum)
{
	requestObject.open('GET', 'stats.php?pageRequest=' + pageNum);
	requestObject.onreadystatechange = handleResponse;
	requestObject.send(null);
}

function handleResponse()
{
	if(requestObject.readyState ==4 && requestObject.status == 200)
	{
		var response = requestObject.responseText;
		
		if(response)
		{
			document.getElementById("dynamicTableContent").innerHTML = "";
			document.getElementById("dynamicTableContent").innerHTML = response;
		}
	}
}