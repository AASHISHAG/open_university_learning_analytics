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
            datasets: [
            {
                label: 'Male',
                backgroundColor: ["#3e95cd","#3e95cd","#3e95cd","#3e95cd",],
                borderColor: 'rgb(0, 0, 255)',
                borderWidth: 1,
                data: [ 858, 6240, 2909, 20332]
            },
            {
                label: 'Female',
                backgroundColor: ["#ff95cd","#ff95cd","#ff95cd","#ff95cd"],
                borderColor: 'rgb(255, 0, 0)',
                borderWidth: 1,
                data: [ 345, 2403, 1497, 11826]
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




function treePlot(data_one,data_two){
    var ctx = document.getElementById('featursImportance').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'horizontalBar',
        // The data for our dataset
        data: {
            datasets: [
            {
                label: "Gender",
                backgroundColor: ["#3e95cd"],
                borderColor: 'rgb(255, 99, 132)',
                data: [1.346817814],
            },
            {
                label: "Age Band",
                backgroundColor: ["#8e5ea2"],
                borderColor: 'rgb(255, 99, 132)',
                data: [0.262031797],
            },
            {
                label: "Semester",
                backgroundColor: ["#3cba9f"],
                borderColor: 'rgb(255, 99, 132)',
                data: [0.19188812],
            },
            {
                label: "Region",
                backgroundColor: ["#e8c3b9"],
                borderColor: 'rgb(255, 99, 132)',
                data: [0.179155034],
            },
            {
                label: "Semester (First Module)",
                backgroundColor: ["#c45850"],
                borderColor: 'rgb(255, 99, 132)',
                data: [0.155225322],
            },
            {
                label: "Highest Education",
                backgroundColor: ["#fe9dcd"],
                borderColor: 'rgb(255, 99, 132)',
                data: [0.118247178],
            },
            {
                label: "Imd Band",
                backgroundColor: ["#8a5ea2"],
                borderColor: 'rgb(255, 99, 132)',
                data: [0.11134633],
            },
            {
                label: "First Module",
                backgroundColor: ["#300a9f"],
                borderColor: 'rgb(255, 99, 132)',
                data: [0.081328867],
            },
            {
                label: "Second Module",
                backgroundColor: ["#7883b9"],
                borderColor: 'rgb(255, 99, 132)',
                data: [0.059469076],
            },
            {
                label: "Number Of Previous Attempts",
                backgroundColor: ["#235850"],
                borderColor: 'rgb(255, 99, 132)',
                data: [0.042821206],
            },
            {
                label: "Semester (Second Module)",
                backgroundColor: ["#b45850"],
                borderColor: 'rgb(255, 99, 132)',
                data: [0.038979394],
            }]
        },
        // Configuration options go here
        options: {}
    });
}