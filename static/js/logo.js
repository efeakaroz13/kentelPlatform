oldstate = ""
function changeIcon(){
	var link = document.querySelector("link[rel~='icon']");
	if (!link) {
	    link = document.createElement('link');
	    link.rel = 'icon';
	    document.head.appendChild(link);
	}

	const darkThemeMq = window.matchMedia("(prefers-color-scheme: dark)");
	if (darkThemeMq.matches) {
	  // Theme set to dark.
	  link.href = "/static/images/light.png";
	} else {
	  // Theme set to light.
		link.href = "/static/images/dark.png";
	}
}
changeIcon()
setInterval(5000,changeIcon)