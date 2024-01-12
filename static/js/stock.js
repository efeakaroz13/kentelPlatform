function g(id){
    return document.getElementById(id);
}

async function loadGraph(stock){
    page = await fetch("/api/v1/stockGraph/"+stock)
    content = await page.json();
    
    dataset = content.out
    compinfo = content.compinfo
    price = compinfo.currentPrice
    g("price").innerHTML = price
    previousClose = compinfo.previousClose
    change = (previousClose-price)*-1
    if (change<0){
        g("trend").style.color = "red";
        g("trendIndicate").className = "fa-solid fa-angle-down";
        g("change").style.color= "red";
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
          borderColor: 'blue',
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
    acc =  Number(data.acc).toFixed(2)
    score = Number(data.score).toFixed(2)
    signal = data.signal
    if (signal=="SELL"){

        g("predictionResult").innerHTML = score+"% Sell";
        g("predictionResult").style.color = "red";
        sell = score;

    }
    if (signal=="BUY"){
        sell = 100-score
        g("predictionResult").innerHTML = score+"% Buy";
        g("predictionResult").style.color = "green"
    }
    g("accuracy").innerHTML = acc+"% Accuracy"
    AIPredictingAnimation()
}

getPrediction(document.getElementsByTagName("h1")[0].innerHTML)


