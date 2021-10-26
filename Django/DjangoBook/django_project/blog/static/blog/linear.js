$(function () {
      var $LineChart = $("#LineChart");

      $.ajax({
        url: $LineChart.data("url"),
        success: function (data) {
          var ctx = $LineChart[0].getContext("2d");

          new Chart(ctx, {
            type: "line",
            data: {
              datasets: [
                {
                    backgroundColor: '#2A4073',
                    borderColor: '#2A4073',
                    fill: false,
                    lineTension: 0,
                    data: data.data
                },
              ],
              labels: ['2017', '2018', '2019', '2020', '2021'],
            },
            options: {
                responsive: true,
                legend: {
                    display: false,
                },
                scales: {
                    xAxes: [{
                        gridLines:{
                            display: false
                        }
                    }],
                    yAxes: [{
                        ticks: {
                            min: 0,
                            stepSize: 1
                        },
                        gridLines: {
                            display: false
                        }
                    }]
                }
            }
          });
        },
      });
    });