
theme = localStorage.getItem("theme");
function g(id){
    return document.getElementById(id);
}

g("atp").addEventListener("click",function(){
    g("atpPopup").classList.toggle("hidden");
    g("blackout").classList.toggle("hidden")
})
g("closePopup").addEventListener("click",function(){
    g("atpPopup").classList.toggle("hidden");
    g("blackout").classList.toggle("hidden")
})

async function loadGraph(stock){
    page = await fetch("/api/v1/stockGraph/"+stock)
    content = await page.json();
    
    dataset = content.out
    compinfo = content.compinfo
    price = compinfo.currentPrice
    g("price").innerHTML = price;
    g("stockPriceP").value = price
    previousClose = compinfo.previousClose
    change = (previousClose-price)*-1
    if (change<0){
        g("trend").style.color = "red";
        g("trendIndicate").innerHTML = '<ion-icon name="caret-down-outline"></ion-icon>';
        g("trendIndicate").style.color = "red"
        g("change").style.color= "red";
    }else{
        g("trendIndicate").style.color = "green"
    }
    changePercent = Number((change/previousClose)*100).toFixed(2);
    g("change").innerHTML = Number((change).toFixed(2))+"("+changePercent+"%)";
    g("companyName").innerHTML = compinfo.longName;
    try{
        g("summary").innerHTML = compinfo.longBusinessSummary;
    }catch{
        null;
    }
    
    new Chart('chartMine', {
      type: 'line',
      data: {
        datasets: [{
          
          data: dataset ,  
          backgroundColor: 'transparent',
          borderColor: '#3880ff',
          borderWidth: 2,
          tension: 0.4
        }]
      },

      options: {
        plugins:{
            legend:{
                display:false
            }
        },
        hover: {
          intersect: false
        },
        legend: {
            display: false
        },
        tooltips: {
            mode: 'dataset',
            callbacks: {
            label: function(tooltipItem) {
            console.log(tooltipItem)
                return tooltipItem.yLabel;
            }
          }
        },
        responsive:true,
        scales: {
          x: {
            grid:{
                drawOnChartArea:false
            },
            type: 'timeseries',
            time: {
              unit: 'minute',
              displayFormats: {
                  minute: 'MMM d'
              },
              tooltipFormat: 'DD T'
            },
            title: {
              display: false,
              text: 'Date'
            }
          },
          y: {
            grid:{
                drawOnChartArea:false
            },
            title: {
              display: false,
              text: 'Price'
            }
          }
        },
        elements: {
                    point:{
                        radius: 0
                    }
                }
        }
      
    });

    g("loading").style.display="none";

}
loadGraph(document.getElementsByTagName("h1")[0].innerHTML)


buy = 100;
sell = 0;
reverse=false
function AIPredictingAnimation(){
    if (sell==100&&reverse==false){
        reverse=true
    }
    if(sell==0&&reverse==true){
        reverse=false;
    }
    if (reverse){
        sell -=1
    }else{
        sell +=1;
    }   
    
    buy = 100-sell;
    g("predictionPlace").style.gridTemplateColumns = buy+"%"+" "+sell+"%";

}
async function getPrediction(ticker){


     AIPredictingAnimation()
    loadingInterval =setInterval(AIPredictingAnimation,8)
    g("predictionResult").innerHTML = "";
    g("accuracy").innerHTML = "";
    page = await fetch("/api/ux/calculate/"+ticker);
    data = await page.json();
    if(data){
            clearInterval(loadingInterval);
    }
    if(data.err){
        g("predictionResult").style.color="red";
        g("predictionResult").innerHTML = data.err
    }else{
        
        acc =  Number(data.acc).toFixed(2)
        score = Number(data.score).toFixed(2)
        signal = data.signal
        if (signal=="SELL"){

            g("predictionResult").innerHTML = score+"% Sell";
            g("predictionResult").style.color = "red";
            sell = score;
            buy = 100-sell;
            g("predictionPlace").style.gridTemplateColumns = buy+"%"+" "+sell+"%";

        }
        if (signal=="BUY"){
            sell = 100-score
            buy = score

            g("predictionResult").innerHTML = score+"% Buy";
            g("predictionResult").style.color = "green"
            g("predictionPlace").style.gridTemplateColumns = buy+"%"+" "+sell+"%";
        }
        g("accuracy").innerHTML = acc+"% Accuracy"
        AIPredictingAnimation()
    }
    
}

getPrediction(document.getElementsByTagName("h1")[0].innerHTML)



function addToPortfolio(){
    ticker = document.getElementsByTagName("h1")[0].innerHTML;
    quantity = g("shares").value;
    price = g("stockPriceP").value;
    $.getJSON("/api/add2port/"+ticker+"?quantity="+quantity+"&fromPrice="+price,function(data){
        if (!data.err){
            alert(ticker+" has been added to portfolio!")
            console.log(data);
            g("atpPopup").classList.toggle("hidden");
            g("blackout").classList.toggle("hidden")
        }else{
            alert("Some error occured, try again.")
        }
        
    })

}
