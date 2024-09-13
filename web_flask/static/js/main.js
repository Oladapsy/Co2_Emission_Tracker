/*fetch('http://54.162.232.135:5000/api/co2/TodayCycleValue') */
async function fetchCo2dailyValue() {
    try {
        const response = await fetch('http://co2tracker.deetechwiz.tech/api/co2/TodayCycleValue');
        console.log(response, 'C02')
        if (!response.ok) {
            alert("not available")
        }
        const data = await response.json()
        console.log(data, 'C0')
        document.getElementById('co2TodayCycleValue').innerHTML = `${data.cycle} ppm`; //JSON.stringify(data.cycle, null, 2)
    }
    catch (error) {
        console.log(error, 'new error');
    }
}
fetchCo2dailyValue();

// to fetch the most rescent three days data

async function fetchCo23daysValue() {
    try {
        const res = await fetch('http://co2tracker.deetechwiz.tech/api/co2/records/3limit')
        if (!res.ok) {
            alert("last 3 days data not available")
        }
        const data = await res.json()
        console.log(data, '3 days co2')
        const tableBody = document.querySelector('#data-table tbody')
        tableBody.innerHTML = ''
        data.forEach(item => {
            const row = document.createElement('tr');

            const dateCell = document.createElement('td');
            dateCell.textContent = item.date;
            row.appendChild(dateCell)

            const cycleCell = document.createElement('td');
            cycleCell.textContent = item.cycle + "ppm";
            row.appendChild(cycleCell)

            const trendCell = document.createElement('td');
            trendCell.textContent = item.trend + "ppm";
            row.appendChild(trendCell)

            tableBody.appendChild(row);
        })

    }
    catch (error) {
        console.log(error)
    }
}

fetchCo23daysValue();

// to fetch todays record and last year record || yearly comparism

async function fetchCo2TodayLastYear() {
    try {
        const res = await fetch('http://co2tracker.deetechwiz.tech/api/co2/compare/today/lastYear')
        if (!res.ok) {
            alert("current date data not available so cant be compared with last year data")
        }
        const data = await res.json()
        console.log(data, 'todayLaastYear CO2')
        const tableBody = document.querySelector('#todayLastYear tbody')
        tableBody.innerHTML = ''
        data.forEach(item => {
            const row = document.createElement('tr');

            const dateCell = document.createElement('td');
            dateCell.textContent = item.date;
            row.appendChild(dateCell)

            const cycleCell = document.createElement('td');
            cycleCell.textContent = item.cycle + "ppm";
            row.appendChild(cycleCell)

            const trendCell = document.createElement('td');
            trendCell.textContent = item.trend + "ppm";
            row.appendChild(trendCell)

            tableBody.appendChild(row);
        })

    }
    catch (error) {
        console.log(error)
    }
}

fetchCo2TodayLastYear();

// to fetch the last 7 days co2 data

async function fetchCo27daysValue() {
    try {
        const res = await fetch('http://co2tracker.deetechwiz.tech/api/co2/records/7limit')
        if (!res.ok) {
            alert("last 7 days data not available")
        }
        const data = await res.json()
        console.log(data, '7 days co2')
        const tableBody = document.querySelector('#sevenDaysDataTable tbody')
        tableBody.innerHTML = ''
        data.forEach(item => {
            const row = document.createElement('tr');

            const idCell = document.createElement('td');
            idCell.textContent = item.id;
            row.appendChild(idCell)

            const dateCell = document.createElement('td');
            dateCell.textContent = item.date;
            row.appendChild(dateCell)

            const cycleCell = document.createElement('td');
            cycleCell.textContent = item.cycle + "ppm";
            row.appendChild(cycleCell)

            const trendCell = document.createElement('td');
            trendCell.textContent = item.trend + "ppm";
            row.appendChild(trendCell)

            tableBody.appendChild(row);
        })

    }
    catch (error) {
        console.log(error)
    }
}

fetchCo27daysValue();







// Home page graph to fetch last 7 days cycle and trend line graph



fetch('http://co2tracker.deetechwiz.tech/api/co2/records/7limit')
    .then(response => response.json())
    .then(data => {
        data.sort((a, b) => new Date(a.date) - new Date(b.date));
        // Pass the data to your plotting function
        plotGraph(data);
    });

function plotGraph(data) {
    console.log(data, '7 days')
    const ctx = document.getElementById('myChart').getContext('2d');

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.map(record => record.date),
            datasets: [
                {
                    label: '7 days Cycle',
                    data: data.map(record => record.cycle),
                    borderWidth: 3,
                    //   borderColor:"yellow"
                    tension: 0.1
                },
                {
                    label: '7 days Trend',
                    data: data.map(record => record.trend),
                    borderWidth: 3,
                    //   borderColor:"yellow"
                    tension: 0.1
                },

            ]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: false
                }
            }
        }
    });
}





//to fetch for compare data

document.getElementById('submitCompareDate').addEventListener('click', function () {
    const date1Value = document.getElementById('firstDate');
    const date1 = date1Value.value;

    const date2Value = document.getElementById('secondDate');
    const date2 = date2Value.value;

    const url = `http://co2tracker.deetechwiz.tech/api/co2/compare/${date1}/${date2}`;

    console.log(date1, date2, 'dates 1 and 2')
    // Use date1Value and date2Value here
    fetch2daysCompare(url);
});


async function fetch2daysCompare(url) {
    try {
        const res = await fetch(url)
        if (!res.ok) {
            alert("no data to compare")
        }
        const data = await res.json()
        console.log(data, 'compare data value')
        const tableBody = document.querySelector('#oneYearDataComparismTable tbody')
        tableBody.innerHTML = ''
        data.forEach(item => {
            const row = document.createElement('tr');

            const dateCell = document.createElement('td');
            dateCell.textContent = item.date;
            row.appendChild(dateCell)

            const cycleCell = document.createElement('td');
            cycleCell.textContent = item.cycle + "ppm";
            row.appendChild(cycleCell)

            const trendCell = document.createElement('td');
            trendCell.textContent = item.trend + "ppm";
            row.appendChild(trendCell)

            tableBody.appendChild(row);
        })

    }
    catch (error) {
        console.log(error)
    }
}
//fetch2daysCompare();
