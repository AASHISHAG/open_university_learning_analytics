//each chart has been plotted with each function in template part

function genderBar(){
    var ctx = document.getElementById('genderBar').getContext('2d');
			window.myBar = new Chart(ctx, {
				type: 'bar',
				data: {
			labels: ['January', 'February', 'March', 'April'],
			datasets: [{
				label: 'Male',
				backgroundColor: color(window.chartColors.red).alpha(0.5).rgbString(),
				borderColor: window.chartColors.red,
				borderWidth: 1,
				data: [ 858, 6240, 2909, 20332]
			}, {
				label: 'Female',
				backgroundColor: color(window.chartColors.blue).alpha(0.5).rgbString(),
				borderColor: window.chartColors.blue,
				borderWidth: 1,
				data: [ 345, 2403, 1497, 11826]
			}]

		},
				options: {
					responsive: true,
					legend: {
						position: 'top',
					},
					title: {
						display: true,
						text: 'Chart.js Bar Chart'
					}
				}
			});

}


//https://www.chartjs.org/docs/latest/getting-started/
function genderPlot(data_one,data_two){

var ctx = document.getElementById('genderChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'bar',
    // The data for our dataset
    data:
    {
        labels: ['Distinction', 'Pass', 'Fail', 'Withdrawn'],
        datasets: [{
				label: 'Male',
				backgroundColor: ["#3e95cd","#3e95cd","#3e95cd","#3e95cd",],
				borderColor: 'rgb(0, 0, 255)',
				borderWidth: 1,
				data: [ 858, 6240, 2909, 20332]
			}, {
				label: 'Female',
				backgroundColor: ["#ff95cd","#ff95cd","#ff95cd","#ff95cd"],
				borderColor: 'rgb(255, 0, 0)',
				borderWidth: 1,
				data: [ 345, 2403, 1497, 11826]
			}]
    }
    ,

    // Configuration options go here
    options: {}
});
}

function agePlot(data_one,data_two, data_three, data_four, data_five){

var ctx = document.getElementById('ageChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'doughnut',

    // The data for our dataset
    data: {
        labels: ["15", "16","17","18","19","20"],
        datasets: [{
            label: "Avarage grade based on gender",
            backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
            borderColor: 'rgb(255, 99, 132)',
            data: [data_one,data_two, data_three, data_four, data_five,5],
        }]
    },

    // Configuration options go here
    options: {}
});
}


function testPlot(data_one,data_two, data_three, data_four, data_five){

var ctx = document.getElementById('testChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: ["15", "16","17","18","19","20"],
        datasets: [{
            label: "Avarage grade based on gender",
            backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
            borderColor: 'rgb(255, 99, 132)',
            data: [data_one,data_two, data_three, data_four, data_five,5],
        }]
    },

    // Configuration options go here
    options: {}
});
}