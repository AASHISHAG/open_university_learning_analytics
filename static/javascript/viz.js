//https://www.chartjs.org/docs/latest/getting-started/
// dev start
// stacked bar chart
function educationPlot(data_one,data_two) {
    var ctx = document.getElementById('educationChart').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',
        // The data for our dataset
        data:
        {
			labels: ['Post Graduate', 'No Formal quals', 'Lower Than A Level', 'HE Qualification', 'A Level / Equivalent'],
			datasets: [{
                    label: 'Distinction',
                    backgroundColor: ["#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd"],
                    data: [9.77, 0, 2.11, 3.29, 2.61]
                }, {
                    label: 'Pass',
                    backgroundColor: ["#ff5544","#ff5544","#ff5544","#ff5544","#ff5544"],
                    data: [11.73, 3.95, 15.47, 21.51, 20.93]
                }, {
                    label: "Fail",
                    backgroundColor: ["#a000cc","#a000cc","#a000cc","#a000cc","#a000cc",],
                    data: [6.84, 9.38, 10.86, 7.1, 9.19]
                }, {
                    label: "Withdrawn",
                    backgroundColor: ["#fe95cd","#fe95cd","#fe95cd","#fe95cd","#fe95cd"],
                    data: [71.66, 86.67, 71.55, 68.13, 67.27]
                }]
		},
        // Configuration options go here
        options: {
            tooltips: {
						mode: 'index',
						intersect: false
					},
					responsive: true,
            scales: {
                  xAxes: [{
                    stacked: true
                  }],
                  yAxes: [{
                    stacked: true
                  }]
            }
        }
    });
}

function ageResultPlot(data_one,data_two) {
    var ctx = document.getElementById('ageResultChart').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',
        // The data for our dataset
        data:
        {
			labels: ['0-35', '35-55', '55<='],
			datasets: [{
                    label: 'Distinction',
                    backgroundColor: ["#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd"],
                    data: [2.38, 2.76, 15.14]
                }, {
                    label: 'Pass',
                    backgroundColor: ["#33cc33","#33cc33","#33cc33","#33cc33","#33cc33"],
                    data: [18.6, 18.31, 11.04]
                }, {
                    label: "Fail",
                    backgroundColor: ["#ff5544","#ff5544","#ff5544","#ff5544","#ff5544",],
                    data: [9.33, 9.6, 9.78]
                }, {
                    label: "Withdrawn",
                    backgroundColor: ["#fe95cd","#fe95cd","#fe95cd","#fe95cd","#fe95cd"],
                    data: [68.5, 69.32, 64.03]
                }]
		},
        // Configuration options go here
        options: {
            tooltips: {
						mode: 'index',
						intersect: false
					},
					responsive: true,
            scales: {
                  xAxes: [{
                    stacked: true
                  }],
                  yAxes: [{
                    stacked: true
                  }]
            }
        }
    });
}

function genderPlot(data_one,data_two) {
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
                    data: [ 2.83, 20.57, 9.59, 67.02]
                }, {
                    label: 'Female',
                    backgroundColor: ["#ff95cd","#ff95cd","#ff95cd","#ff95cd"],
                    borderColor: 'rgb(255, 0, 0)',
                    borderWidth: 1,
                    data: [ 2.15, 14.95, 9.31, 73.58]
                }]
        },
        // Configuration options go here
        options: {}
    });
}

function imdPlot(data_one,data_two, data_three, data_four, data_five){

    var ctx = document.getElementById('imdChart').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'pie',
        // The data for our dataset
        data: {
            labels: ["0-10%", "10-20%","20-30%","30-40%","40-50%","50-60%","60-70%","70-80%","80-90%","90-100%"],
            datasets: [{
                label: "Pass based on IMB-Band",
                backgroundColor: [  "#ff95ac",
                                    "#95f0ac",
                                    "#f151f0",
                                    "#9cd60c",
                                    "#bcb44b",
                                    "#f3cc33",
                                    "#8363d8",
                                    "#511e84",
                                    "#9032e6",
                                    "#ca8060"],
                borderColor: 'rgb(100, 100, 100)',
                data: ["8.94",
                        "0",
                        "11.16",
                        "13.29",
                        "12.35",
                        "11.04",
                        "9.69",
                        "10.34",
                        "13.70",
                        "9.49"],
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

function treePlot(){

var ctx = document.getElementById('featursImportance').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'horizontalBar',
    // The data for our dataset
    data: {
        datasets: [{
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

function gender_database(data_one,data_two) {
    var ctx = document.getElementById('gender_database').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'doughnut',
        // The data for our dataset
        data:
        {
            labels: ['Male', 'Female'],
            datasets: [{
                    label: ['Male','Female'],
                    backgroundColor: ["#fe95cd","#3e95cd"],
                    borderColor: 'rgb(0, 0, 255)',
                    borderWidth: 1,
                    data: [data_one, data_two]
                }]
        },
        // Configuration options go here
        options: {}
    });
}

function prediction_database(w_male, w_female, p_male, p_female, f_male, f_female, d_male, d_female) {
    var ctx = document.getElementById('prediction_database').getContext('2d');
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
                    data: [ d_male, p_male, f_male, w_male]
                }, {
                    label: 'Female',
                    backgroundColor: ["#ff95cd","#ff95cd","#ff95cd","#ff95cd"],
                    borderColor: 'rgb(255, 0, 0)',
                    borderWidth: 1,
                    data: [ d_female, p_female, f_female, w_female]
                }]
        },
        // Configuration options go here
        options: {}
    });
}
