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

g("entrySearch").addEventListener("keyup",async function(event){
    key = event.keyCode;
    if (key==13) {
        window.location.assign("/stock/"+g("entrySearch").value)
    }
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

function checkSearchInside(){
    if(!g("searchRecommend").innerHTML.includes("<")){
        g("searchRecommend").style.display="none";
    }else{
        g("searchRecommend").style.display="";
    }
}
checkSearchInside()

setInterval(checkSearchInside,200)


function loadScan(){
    $.getJSON("/get/last/issue",function(data){
        var exchange = data.exchange
        basehtml = '<ion-item>\
                    <div class="discoverGrid bold">\
                        <div>Company</div>\
                        <div>Signal</div>\
                        <div>Score</div>\
                        <div>Accuracy</div>\
                        <div></div>\
                    </div>\
                  </ion-item>'
         g("discoverList").innerHTML = basehtml
         scanTime  = new Date( data.time*1000);
         g("date").innerHTML = scanTime.toLocaleString()
        if(exchange=="SERVER2_DAILY_NASDAQ"){
            var items = data.notifications
            for (var i = items.length - 1; i >= 0; i--) {
                d = items[i]
                chtml = '<ion-item>\
                    <div class="discoverGrid ">\
                        <div ><a title="'+d.comp.company+'">'+d.comp.ticker+'</a></div>\
                        <div>'+d.signal+'</div>\
                        <div>'+d.score+'</div>\
                        <div style="font-weight: 500;color:darkblue">'+d.acc+'%</div>\
                    </div>\
                  </ion-item>'
                g("discoverList").innerHTML=g("discoverList").innerHTML+chtml
            }
            //basic package
            
        }else{
            //unlimited Scans
            // add scan button.
            var items = data.stockList
            for (var i = items.length - 1; i >= 0; i--) {
                d = items[i]
                chtml = '<ion-item>\
                    <div class="discoverGrid ">\
                        <div ><a >'+d.ticker+'</a></div>\
                        <div>'+d.signal+'</div>\
                        <div>'+d.score+'</div>\
                        <div style="font-weight: 500;color:darkblue">'+d.acc+'%</div>\
                    </div>\
                  </ion-item>'
                g("discoverList").innerHTML=g("discoverList").innerHTML+chtml
            }
        }
    })
}
loadScan()