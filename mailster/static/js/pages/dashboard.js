//[Dashboard Javascript]

//Project:	Lotus Admin - Responsive Admin Template
//Primary use:   Used only for the main dashboard (index.html)


$(function () {

  'use strict';
	
		
	var bar = new ProgressBar.Circle(progressbar1, {
	  color: '#5A8DEE',
	  // This has to be the same size as the maximum width to
	  // prevent clipping
	  strokeWidth: 21,
	  trailWidth: 1,
	  easing: 'easeInOut',
	  duration: 1400,
	  text: {
		autoStyleContainer: false
	  },
	  from: { color: '#5A8DEE', width: 1 },
	  to: { color: '#5A8DEE', width: 4 },
	  // Set default step function for all animate calls
	  step: function(state, circle) {
		circle.path.setAttribute('stroke', state.color);
		circle.path.setAttribute('stroke-width', state.width);

		var value = Math.round(circle.value() * 120);
		if (value === 0) {
		  circle.setText('');
		} else {
		  circle.setText(value);
		}

	  }
	});
	bar.text.style.fontFamily = '"Rubik", sans-serif';
	bar.text.style.fontSize = '2rem';

	bar.animate(0.78);
	
	
	
	var options = {
        series: [{
            name: "Visit",
            data: [189, 156, 155, 118, 167, 159, 178, 223, 195, 201, 143]
        }],
        chart: {
          height: 255,
          type: 'line',
          zoom: {
            enabled: false
          }
        },
		colors:['#cbccce'],
        dataLabels: {
          enabled: true,
			style: {
				fontSize: '16px',
				colors: ['#5A8DEE'],
			},
        },
        stroke: {
          	show: true,
			curve: 'smooth',
			lineCap: 'butt',
			colors: undefined,
			width: 4,
			dashArray: 0, 
        },		
		markers: {
			size: 6,
			colors: '#5A8DEE',
			strokeColors: '#ffffff',
			strokeWidth: 2,
			strokeOpacity: 0.9,
			strokeDashArray: 0,
			fillOpacity: 1,
			discrete: [],
			shape: "circle",
			radius: 5,
			offsetX: 0,
			offsetY: 0,
			onClick: undefined,
			onDblClick: undefined,
			hover: {
			  size: undefined,
			  sizeOffset: 3
			}
		},
        grid: {
          row: {
            colors: ['transparent'], // takes an array which will be repeated on columns
            opacity: 0
          },			
		  yaxis: {
			lines: {
			  show: false,
			},
		  },
        },
        xaxis: {
          categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
		  labels: {
			show: false,
            offsetY: -18,        
          },
          axisBorder: {
            show: false
          },
          axisTicks: {
            show: false
          },
          tooltip: {
            enabled: false,        
          },
        },
        yaxis: {
          axisBorder: {
            show: false
          },
          axisTicks: {
            show: false,
          },
          labels: {
            show: false,
            formatter: function (val) {
              return val + "k";
            }
          }
        
        },
      };
      var chart = new ApexCharts(document.querySelector("#visits-chart"), options);
      chart.render();
		
	
	
	
	var customerData = {
		labels: ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'],
		datasets: [{
			label: 'Revenue',
			data: [30, 55, 60, 50, 35, 45, 25, 60, 50, 40, 60, 55, 30, 55, 60, 50, 35, 45, 25],
			backgroundColor: [
				'#5A8DEE', '#5A8DEE', '#5A8DEE', '#5A8DEE', '#5A8DEE', '#e9e9e9', '#e9e9e9', '#5A8DEE', '#5A8DEE', '#5A8DEE', '#5A8DEE', '#5A8DEE','#e9e9e9', '#e9e9e9', '#5A8DEE', '#5A8DEE', '#5A8DEE', '#5A8DEE', '#5A8DEE',
			],
			borderColor: [
				'#5A8DEE', '#5A8DEE', '#5A8DEE', '#5A8DEE', '#5A8DEE', '#e9e9e9', '#e9e9e9', '#5A8DEE', '#5A8DEE', '#5A8DEE', '#5A8DEE', '#5A8DEE','#e9e9e9', '#e9e9e9', '#5A8DEE', '#5A8DEE', '#5A8DEE', '#5A8DEE', '#5A8DEE',
			],
			borderWidth: 1,
			fill: false
		}
		]
	};
	var customerOptions = {
		scales: {
			xAxes: [{
			barPercentage: 0.8,
			position: 'bottom',
			display: true,
			gridLines: {
				display: false,
				drawBorder: false,
			},
			ticks: {
				display: false, //this will remove only the label
				stepSize: 300,
			}
			}],
			yAxes: [{
				display: false,
				gridLines: {
					drawBorder: false,
					display: true,
					color: "#f0f3f6",
					borderDash: [8, 4],
				},
				ticks: {
					display: false,
					beginAtZero: true,
				},
			}]
		},
		legend: {
			display: false
		},
		tooltips: {
			enabled: true,
			backgroundColor: 'rgba(0, 0, 0, 1)',
		},
		plugins: {
			datalabels: {
				display: false,
				align: 'center',
				anchor: 'center'
			}
		}				
	};
	if ($("#customer").length) {
		var barChartCanvas = $("#customer").get(0).getContext("2d");
		// This will get the first returned node in the jQuery collection.
		if(screen.width>767) {
			var chartHeight = document.getElementById("customer");
			chartHeight.height = 60;
		}
		var barChart = new Chart(barChartCanvas, {
			type: 'bar',
			data: customerData,
			options: customerOptions
		});
	}
	
	
	var myConfig = {
        "type": "line",
		"utc": true,
        "plot": {
          "animation": {
            "delay": 500,
            "effect": "ANIMATION_SLIDE_LEFT"
          }
        },
        "plotarea": {
          "margin": "10px 25px 70px 46px"
        },
        "scale-y": {
          "values": "0:100:25",
          "line-color": "none",
          "guide": {
            "line-style": "solid",
            "line-color": "#566f9e",
            "line-width": "1px",
            "alpha": 0.5
          },
          "tick": {
            "visible": false
          },
          "item": {
            "font-color": "#8391a5",
            "font-family": "Arial",
            "font-size": "10px",
            "padding-right": "5px"
          }
        },
        "scale-x": {
          "line-color": "#566f9e",
          "line-width": "2px",
          "values": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
          "tick": {
            "line-color": "#566f9e",
            "line-width": "1px"
          },
          "guide": {
            "visible": false
          },
          "item": {
            "font-color": "#8391a5",
            "font-family": "Arial",
            "font-size": "10px",
            "padding-top": "5px"
          }
        },
        "legend": {
          "layout": "x4",
          "background-color": "none",
          "shadow": 0,
          "margin": "auto auto 15 auto",
          "border-width": 0,
          "item": {
            "font-color": "#707d94",
            "font-family": "Arial",
            "padding": "0px",
            "margin": "0px",
            "font-size": "9px"
          },
          "marker": {
            "show-line": "true",
            "type": "match",
            "font-family": "Arial",
            "font-size": "10px",
            "size": 4,
            "line-width": 2,
            "padding": "3px"
          }
        },
        "crosshair-x": {
          "lineWidth": 1,
          "line-color": "#707d94",
          "plotLabel": {
            "shadow": false,
            "font-color": "#000",
            "font-family": "Arial",
            "font-size": "10px",
            "padding": "5px 10px",
            "border-radius": "5px",
            "alpha": 1
          },
          "scale-label": {
            "font-color": "#ffffff",
            "background-color": "#707d94",
            "font-family": "Arial",
            "font-size": "10px",
            "padding": "5px 10px",
            "border-radius": "5px"
          }
        },
        "tooltip": {
          "visible": false
        },
        "series": [{
          "values": [69, 68, 54, 48, 70, 74, 98, 70, 72, 68, 49, 69],
          "text": "iPod",
          "line-color": "#5A8DEE",
          "line-width": "2px",
          "shadow": 0,
          "marker": {
            "background-color": "#fff",
            "size": 3,
            "border-width": 1,
            "border-color": "#5A8DEE",
            "shadow": 0
          },
          "palette": 0
        }, {
          "values": [51, 53, 47, 60, 48, 52, 75, 52, 55, 47, 60, 48],
          "text": "Mi Phone",
          "line-width": "2px",
          "line-color": "#39DA8A",
          "shadow": 0,
          "marker": {
            "background-color": "#fff",
            "size": 3,
            "border-width": 1,
            "border-color": "#39DA8A",
            "shadow": 0
          },
          "palette": 1,
          "visible": 1
        }, {
          "values": [42, 43, 30, 50, 31, 48, 55, 46, 48, 32, 50, 38],
          "text": "Mi TV",
          "line-color": "#00CFDD",
          "line-width": "2px",
          "shadow": 0,
          "marker": {
            "background-color": "#fff",
            "size": 3,
            "border-width": 1,
            "border-color": "#00CFDD",
            "shadow": 0
          },
          "palette": 2,
          "visible": 1
        }, {
          "values": [25, 15, 26, 21, 24, 26, 33, 25, 15, 25, 22, 24],
          "text": "Eco Dot",
          "line-color": "#FF5B5C",
          "line-width": "2px",
          "shadow": 0,
          "marker": {
            "background-color": "#fff",
            "size": 3,
            "border-width": 1,
            "border-color": "#FF5B5C",
            "shadow": 0
          },
          "palette": 3
        }]
      };

    zingchart.render({
      id: 'myChart',
      data: myConfig,
      height: 270,
      width: '100%'
    });
	
	
	
	
	
	
	
		var options = {
        series: [{
          name: 'This Year',
          data: [44, 55, 41, 67, 22, 43, 41, 12, 56, 51, 42, 44]
        }, {
          name: 'Past Year',
          data: [13, 23, 20, 8, 13, 27, 22, 17, 28, 14, 9, 12]
        }],
        chart: {
          type: 'bar',
          height: 313,
          stacked: true,
			foreColor: '#8a99b5',
          toolbar: {
            show: false
          },
          zoom: {
            enabled: false
          }
        },
		dataLabels: {
          enabled: false
        },
		grid: {
			show: true,
			borderColor: '#566f9e',    
		},
		colors:['#5A8DEE', '#FF5B5C'],
        responsive: [{
          breakpoint: 375,			
        }],
        plotOptions: {
          bar: {
            horizontal: false,
			  columnWidth: '30%',
			  endingShape: 'rounded',
          },
        },
        xaxis: {
          categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
			axisTicks: {
				color: '#ffffff',
			},
        },
        legend: {
          position: 'top',
           horizontalAlign: 'right',
        },
        fill: {
          opacity: 1
        }
      };

      var chart = new ApexCharts(document.querySelector("#yearly-comparison"), options);
      chart.render();
	
	
	// Apex  start
  if($('#apexChart2').length) {
    var options2 = {
      chart: {
        type: "bar",
        height: 100,
        sparkline: {
          enabled: !0
        }
      },
      plotOptions: {
        bar: {
          columnWidth: "25%"
        }
      },
      colors: ["#ffffff"],
      series: [{
        data: [36, 77, 52, 90, 74, 35, 55, 23, 47, 10, 63, 36, 77, 52, 90, 74, 35, 55, 23, 47]
      }],
      labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
      xaxis: {
        crosshairs: {
          width: 2
        }
      },
      tooltip: {
        fixed: {
          enabled: !1
        },
        x: {
          show: !1
        },
        y: {
          title: {
            formatter: function(e) {
              return ""
            }
          }
        },
        marker: {
          show: !1
        }
      }
    };
    new ApexCharts(document.querySelector("#apexChart2"),options2).render();
  }
  // Apex  end
	
	
	
	// Apex  start
  if($('#apexChart3').length) {
    var options2 = {
      chart: {
        type: "bar",
        height: 100,
        sparkline: {
          enabled: !0
        }
      },
      plotOptions: {
        bar: {
          columnWidth: "25%"
        }
      },
      colors: ["#ffffff"],
      series: [{
        data: [36, 77, 52, 90, 74, 35, 55, 23, 47, 10, 63, 36, 77, 52, 90, 74, 35, 55, 23, 47]
      }],
      labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
      xaxis: {
        crosshairs: {
          width: 2
        }
      },
      tooltip: {
        fixed: {
          enabled: !1
        },
        x: {
          show: !1
        },
        y: {
          title: {
            formatter: function(e) {
              return ""
            }
          }
        },
        marker: {
          show: !1
        }
      }
    };
    new ApexCharts(document.querySelector("#apexChart3"),options2).render();
  }
  // Apex chart2 end
	
}); // End of use strict
