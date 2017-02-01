// Variables
var app, canvas, chartInstance;

// Initaliase Vue
function initVue() {
    app = new Vue({
        el: '#app',
        delimiters: ['[[',']]'],
        data: {
            view: 'waterstand',
            waterstand: 0,
            animatedWaterstand: 0
        },
        computed: {
            status: function() {
                if ( this.waterstand < 20) {
                    return ['laag', '#67e267']
                } else if ( this.waterstand < 40 ) {
                    return ['normaal', '#67e267']
                } else if ( this.waterstand < 60 ) {
                    return ['hoog', '#f0ff40']
                } else if ( this.waterstand < 80 ) {
                    return ['te hoog', '#ffad40']
                } else if ( this.waterstand < 100 ) {
                    return ['kritiek', '#ff4040']
                }
            }
        },
        watch: {
            waterstand: function(newValue, oldValue) {
              var vm = this
              var animationFrame
              function animate (time) {
                TWEEN.update(time)
                animationFrame = requestAnimationFrame(animate)
              }
              new TWEEN.Tween({ tweeningNumber: oldValue }).easing(TWEEN.Easing.Quadratic.Out).to({ tweeningNumber: newValue }, 500).onUpdate(function () {
                  vm.animatedWaterstand = this.tweeningNumber.toFixed(0)
                }).onComplete(function () {
                  cancelAnimationFrame(animationFrame)
                }).start() 
               animationFrame = requestAnimationFrame(animate)
            }
        },
        methods: {
            changeView: function(view) {
                this.view = view
            },
            ajaxTesting: function(testFunction) {
                axios.post('/testing/?function=' + testFunction).then(function (response) { console.log(response); }).catch(function (error) { console.log(error); });
            }
        }
    });
} initVue();

// Initaliase ChartJS
function initChart() {

    timeList = [];
    dataList = [];
    avaragedataList = [];
    for (var i = 0; i < 60; i++) {
        time = moment().subtract(i, 'seconds').format('H:mm:ss');
        timeList.push(time);
        dataList.push(0);
        if (i % 5 == 0) {
            avaragedataList.push(0);
        }
    }

    canvas = document.getElementById('waterkering').getContext('2d');

    var gradient = canvas.createLinearGradient(0, 0, 0, 450);
    gradient.addColorStop(0, 'rgba(9,100,124, 1)');
    gradient.addColorStop(1, 'rgba(170,170,170, 0)');

    chartInstance = new Chart(canvas, {
        type: 'line',
        data: {
            xLabels: timeList,
            yLabels: [0, 20, 40, 60, 80, 100],
            datasets: [
                {
                    label: 'waterpijl', data: dataList, backgroundColor: gradient, lineTension: 0.5, borderColor: '#1fbde6', borderWidth: 2,
                }
            ]
        },
        options: {
            scales: {
                xAxes: [{
                    ticks: {},
                    gridLines: {
                        display: false,
                        drawBorder: true,
                    }
                }],
                yAxes: [{
                    ticks: {
                        min: 0,
                        max: 100,
                        stepSize: 20,
                        beginAtZero: true,
                        display: false,
                        padding: 0,
                    },
                    gridLines: {
                        color: "rgba(170, 170, 170, 0.15)",
                        drawBorder: false,
                    }
                }]
            },
            elements: { point: { radius: 1 } },
            legend: { display: false }
        }
    });

} initChart();

function updateChart(waterstand) {
    data = chartInstance.data.datasets[0].data;
    labels = chartInstance.data.xLabels;
    data.shift();
    labels.shift();
    data.push(waterstand)
    time = moment().format('H:mm:ss');
    labels.push(time);
    chartInstance.update();
}

// Initaliase Socket
function initSocket() {
    // connection gets bumped over to WebSocket consumers
    socket = new WebSocket("ws://" + window.location.host + "/waterstand/");
    socket.onmessage = function(e) {
        updateChart(e.data);
        app._data.waterstand = e.data;
    }

    socket.onopen = function() {
        console.log('start requesting:');
    }

    // Call onopen directly if socket is already open
    if (socket.readyState == WebSocket.OPEN) socket.onopen();
} initSocket();