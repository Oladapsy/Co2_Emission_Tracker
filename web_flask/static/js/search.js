//to fetch data for search Range
document.getElementById('submitDateRange').addEventListener('click', function () {
    // alert("Button Clicked")
    const range1Value = document.getElementById('startDate');
    const range1 = range1Value.value;

    const range2Value = document.getElementById('endDate');
    const range2 = range2Value.value;

    const url = `http://co2tracker.deetechwiz.tech/api/co2/records/range/${range1}/${range2}`;

    console.log(range1, range2, 'range 1 and 2')
    // Use date1Value and date2Value here
    compareRange(url);
});


async function compareRange(url) {
    try {
        const res = await fetch(url)
        if (!res.ok) {
            alert("no date selected to fetch data range")
        }
        const data = await res.json()
        console.log(data, 'fetch data range')
        const tableBody = document.querySelector('#searchRangeTable tbody')
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


// search range graph

document.getElementById('submitDateRange').addEventListener('click', function () {
    
    const range1Value = document.getElementById('startDate');
    const range1 = range1Value.value;

    const range2Value = document.getElementById('endDate');
    const range2 = range2Value.value;

    const url = `http://co2tracker.deetechwiz.tech/api/co2/records/range/${range1}/${range2}`;

    fetch(url)
    .then(response => response.json())
    .then(data => {
        data.sort((a, b) => new Date(a.date) - new Date(b.date));
        // Pass the data to your plotting function
        plotGraph(data);
    });

function plotGraph(data) {
    console.log(data, 'Range days')
    const ctx = document.getElementById('searchChart').getContext('2d');

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.map(record => record.date),
            datasets: [
                {
                    label: 'Range Searched Cycle',
                    data: data.map(record => record.cycle),
                    borderWidth: 3,
                    //   borderColor:"yellow"
                    tension: 0.1
                },
                {
                    label: 'Range Searched Trend',
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
   
});

