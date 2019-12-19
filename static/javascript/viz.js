//each chart has been plotted with each function in template part

//https://www.chartjs.org/docs/latest/getting-started/
function genderPlot(data_one,data_two){

var ctx = document.getElementById('genderChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'bar',
    // The data for our dataset
    data: {
        labels: ["M", "F"],
        datasets: [{
            label: "Avarage grade based on gender",
            backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
            borderColor: 'rgb(255, 99, 132)',
            data: [data_one, data_two,5],
        }]
    },

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