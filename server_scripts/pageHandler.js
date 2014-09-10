//Event Handler registration for page navigation
document.getElementById("prevButton").onclick = prevEvent;
document.getElementById("nextButton").onclick = nextEvent;
document.getElementById("jumpText").onblur = jumpEvent;
document.onload = sendRequest(1);