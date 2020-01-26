//https://www.chartjs.org/docs/latest/getting-started/

// all of this javascript function is based on Chart.js

// chart for dataset page
function educationPlot(data_one,data_two) {
    var ctx = document.getElementById('educationChart').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',
        // The data for our dataset
        data:
        {
            labels: ['No Formal Qual.', 'Lower Than A Level', 'A Level/Equivalent', 'HE Qualification', 'Post Graduate'],
			datasets: [{
                    label: 'Distinction',
                    backgroundColor: ["#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd"],
                    data: [0, 2.11, 2.61, 3.29, 9.77]
                }, {
                    label: 'Pass',
                    backgroundColor: ["#ff5544","#ff5544","#ff5544","#ff5544","#ff5544"],
                    data: [3.95, 15.47, 20.93, 21.51, 11.73]
                }, {
                    label: "Fail",
                    backgroundColor: ["#a000cc","#a000cc","#a000cc","#a000cc","#a000cc",],
                    data: [9.38, 10.86, 9.19, 7.1, 6.84]
                }, {
                    label: "Withdrawn",
                    backgroundColor: ["#fe95cd","#fe95cd","#fe95cd","#fe95cd","#fe95cd"],
                    data: [86.67, 71.55, 67.27, 68.13, 71.66]
                }]
		},
        // configuration options go here
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
// chart for dataset page
function ageResultPlot(data_one,data_two) {
    var ctx = document.getElementById('ageResultChart').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',
        // The data for our dataset
        data:
        {
			labels: ['0-35', '35-55', '55>='],
			datasets: [{
                    label: 'Distinction',
                    backgroundColor: ["#e41a1c","#e41a1c","#e41a1c","#e41a1c","#e41a1c"],
                    borderColor: 'rgb(255, 255, 255)',
                    data: [2.38, 2.76, 15.14]
                }, {
                    label: 'Pass',
                    backgroundColor: ["#ff7f00","#ff7f00","#ff7f00","#ff7f00","#ff7f00"],
                    borderColor: 'rgb(255, 255, 255)',
                    data: [18.6, 18.31, 11.04]
                }, {
                    label: "Fail",
                    backgroundColor: ["#33a02c","#33a02c","#33a02c","#33a02c","#33a02c",],
                    borderColor: 'rgb(255, 255, 255)',
                    data: [9.33, 9.6, 9.78]
                }, {
                    label: "Withdrawn",
                    backgroundColor: ["#1f78b4","#1f78b4","#1f78b4","#1f78b4","#1f78b4"],
                    borderColor: 'rgb(255, 255, 255)',
                    data: [68.5, 69.32, 64.03]
                }]
		},
        // configuration options go here
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
// chart for dataset page
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
// chart for dataset page
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
backgroundColor: [  "#a6cee3", "#1f78b4", "#b2df8a", "#33a02c", "#fb9a99",
					"#e31a1c", "#fdbf6f", "#ff7f00", "#cab2d6", "#6a3d9a"],
                borderColor: 'rgb(255, 255, 255)',
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

        // configuration options go here
        options: {}
    });
}
// chart for tree in prediction page
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

    // configuration options go here
    options: {}
});
}
// chart for trends page
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
                    borderColor: 'rgb(255, 255, 255)',
                    borderWidth: 1,
                    data: [data_one, data_two]
                }]
        },
        // Configuration options go here
        options: {}
    });
}
// chart for trends page
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
        // configuration options go here
        options: {}
    });
}
