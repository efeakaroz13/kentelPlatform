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

function checkLStorage(){
    fil = localStorage.getItem("filter");
    if(fil!=null){
        g("filters").value = fil
    }
}
checkLStorage()
function loadScan(){

    filter = g("filters").value;
    if(filter!=undefined){
        localStorage.setItem("filter",filter);
    }
    if(filter!="defno" && filter!=null && filter!=undefined){
        url = "/get/last/issue?filter="+filter
    }else{
        url="/get/last/issue"
    }
    /*edit the code because you werent sober writing this
    */
    $.getJSON(url,function(data){
        exchange = data.exchange
        basehtml = '<ion-item>\
        <ion-grid>\
            <ion-row>\
                <ion-col><strong>Company</strong></ion-col>\
                <ion-col><strong>Buy Score</strong></ion-col>\
                <ion-col><strong>AI-Accuracy</strong></ion-col>\
\
            </ion-row>\
        </ion-grid>\
    </ion-item>\
    '
         g("discoverList").innerHTML = basehtml
         scanTime  = new Date( data.time*1000);
         g("lastUpdate").innerHTML = scanTime.toLocaleString()

        if(exchange=="SERVER2_DAILY_NASDAQ"){
            var items = data.notifications;
            
            for (var i=0; i<items.length;i++) {
                d = items[i]
                
                chtml = '<ion-item>\
                <ion-grid>\
                    <ion-row>\
                        <ion-col>'+d.comp.ticker+'</ion-col>\
                        <ion-col>'+d.score.toFixed(2)+'%</ion-col>\
                        <ion-col>'+d.acc.toFixed(2)+'%</ion-col>\
                    </ion-row>\
                </ion-grid>\
            </ion-item>\
            '
                g("discoverList").innerHTML=g("discoverList").innerHTML+chtml;
                
            }
            //basic package
            
        }else{
            //unlimited Scans
            // add scan button.
            items = data.stockList;
            items = items.slice(0,12)
            for (var i = items.length - 1; i >= 0; i--) {
                d = items[i]
                chtml = chtml = '<ion-item>\
                <ion-grid>\
                    <ion-row>\
                        <ion-col>'+d.ticker+'</ion-col>\
                        <ion-col>'+d.score.toFixed(2)+'%</ion-col>\
                        <ion-col>'+d.acc.toFixed(2)+'%</ion-col>\
                    </ion-row>\
                </ion-grid>\
            </ion-item>\
            '
                g("discoverList").innerHTML=g("discoverList").innerHTML+chtml
            }
        }
    })
    
    
}
loadScan()
setInterval(loadScan,60000)

oldValue = g("filters").value;
function filterChangeChecker(){
    console.log(g("filters").value,oldValue)
    if(g("filters").value !=oldValue){
        loadScan();
        oldValue = g("filters").value;
    }
}
setInterval(filterChangeChecker,1000)


if(window.location.pathname=="/"){


    dji = {}
    nasdaq = {}
    function updateIndexFundStatus(){
        $.getJSON("/api/indexFunds",function(data){
            for (let index = 0; index < data.length; index++) {
                const element = data[index];
                if(element.index=="^DJI"){
                    dji = element
                }else if(element.index=="^NDX"){
                    nasdaq = element
                }
            }
            loadIndexFunds()
            setInterval(loadIndexFunds,10000);
        })
    }
    updateIndexFundStatus()
    setInterval(updateIndexFundStatus,110000)

    current = "nasdaq"

    function loadIndexFunds(){
        if(current == "dowjones"){
            document.getElementById("nasdaq").style.display = "";
            document.getElementById("dowjones").style.display = "none";
            document.getElementById("nasdaq").getElementsByTagName("a")[0].innerHTML = nasdaq.score+"%";
            if(nasdaq.signal == "BUY"){
                document.getElementById("nasdaq").style.background = "green";
        
            }else{
                document.getElementById("nasdaq").style.background="red";
            }
            current = "nasdaq";

        }else if(current == "nasdaq"){
            document.getElementById("nasdaq").style.display = "none";
            document.getElementById("dowjones").style.display = "";
            document.getElementById("dowjones").getElementsByTagName("a")[0].innerHTML = dji.score+"%";
            if(dji.signal == "BUY"){
                document.getElementById("dowjones").style.background = "green";
        
            }else{
                document.getElementById("dowjones").style.background="red";
            }
            current= "dowjones"

        }
    }

    function indexFundAlert(){
        alert("This feature you've clicked on is for showing the overall market status. Check it before participating in any trade.")
    }
}