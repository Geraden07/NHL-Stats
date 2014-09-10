function prevEvent()
{
	var page = parseInt(document.getElementById("pageShown").innerHTML);
	if(page>1)
	{
		var newpage = (page-1);
		document.getElementById("jumpText").value = newpage;
		document.getElementById("pageShown").innerHTML = newpage;
		document.getElementById("resultsShown").innerHTML = ((30*newpage)-29) + "-" + (30*newpage);
		sendRequest(newpage);
	}
}

function nextEvent()
{
	var page = parseInt(document.getElementById("pageShown").innerHTML);
	
	if(page<204)
	{
		var newpage = (page+1);
		document.getElementById("jumpText").value = newpage;
		document.getElementById("pageShown").innerHTML = newpage;
		document.getElementById("resultsShown").innerHTML = ((30*newpage)-29) + "-" + (30*newpage);
		sendRequest(newpage);
	}
	

}

function jumpEvent()
{
	var page = parseInt(document.getElementById("pageShown").innerHTML);
	var target = document.getElementById("jumpText").value;
	if(target<205&&target>0)
	{
		var newpage = target;
		document.getElementById("pageShown").innerHTML = newpage;
		document.getElementById("resultsShown").innerHTML = ((30*newpage)-29) + "-" + (30*newpage);
		sendRequest(newpage);
	}
	else
	{
		document.getElementById("jumpText").value = page;
	}

}