//Kentel LTD 
// THIS CODE IS UNDER KENTEL LTD'S COPYRIGHT, CANNOT BE EDITED, REDISTRUBUTED OR PUBLISHED BY SOURCES OTHER THAN KENTEL.DEV


function g(id){
    return document.getElementById(id);

}

g("openDiscover").addEventListener("click",function(){
    g("discover").style.display="";
    g("search").style.display= "none";
    g("openSearch").className = "";
    g("openDiscover").className = "active";
})
g("openSearch").addEventListener("click",function(){
    g("discover").style.display="none";
    g("search").style.display= "";
    g("openSearch").className = "active";
    g("openDiscover").className = "";
})

g("entrySearch").addEventListener("keyup",async function(){
    searchTerm = g("entrySearch").value;
    response= await fetch("/api/ux/search?q="+searchTerm)
    data= await response.json();
    out = await data.out;
    g("searchRecommend").innerHTML = ""
    console.log(out)
    for (var i = out.length - 1; i >= 0; i--) {
        var item = out[i]
        html = '\
              <ion-item href="/stock/'+item.ticker+'">\
                <ion-label><h1>'+item.ticker+' - '+item.name+'</h1><p>'+item.summary+'</p></ion-label>\
                <ion-ripple-effect></ion-ripple-effect>\
                <ion-icon slot="end" name="search-outline" ></ion-icon>\
              </ion-item>'
        g("searchRecommend").innerHTML = g("searchRecommend").innerHTML +html
    }
})