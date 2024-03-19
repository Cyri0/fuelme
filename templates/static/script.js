
function fetchConsumption(){
    fetch('/api/consumption/')
    .then(res => res.json())
    .then(data => console.log(data))
}

fetchConsumption()

function fetchRefuels(){
    fetch('/api/all/')
    .then(res => res.json())
    .then(data => console.log(data))
}

fetchRefuels()
