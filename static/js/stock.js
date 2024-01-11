async function loadGraph(stock){
    page = await fetch("/api/v1/stockGraph/"+stock)
    content = await page.json();
    
    dataset = content.out
    
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
        hover: {
          intersect: false
        },
        tooltips: {
           mode: 'dataset'
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


}
loadGraph(document.getElementsByTagName("h1")[0].innerHTML)