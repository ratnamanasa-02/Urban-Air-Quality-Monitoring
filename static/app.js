function calculateAQI() {
    var pm25 = document.getElementById('pm25').value;
    var pm10 = document.getElementById('pm10').value;
    var so2 = document.getElementById('so2').value;
    var co = document.getElementById('co').value;
    var nh3 = document.getElementById('nh3').value;
    var nox = document.getElementById('nox').value;
    var no2 = document.getElementById('no2').value;
    var no = document.getElementById('no').value;
    var o3 = document.getElementById('O3').value;
    var benzene = document.getElementById('Benzene').value;
    var toulene = document.getElementById('Toulene').value;
    var xylene = document.getElementById('Xylene').value;

    var data = {
        pm25: pm25,
        pm10: pm10,
        so2: so2,
        co: co,
        nh3: nh3,
        nox: nox,
        no2: no2,
        no: no,
        o3: o3,
        benzene: benzene,
        toulene: toulene,
        xylene: xylene
    };

    fetch('/calculate-aqi', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = 'AQI: ' + data.aqi;
    })
    .catch(error => console.error('Error:', error));
}