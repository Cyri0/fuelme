const consumptionEl = document.getElementById('consumption')
const refuelsEl = document.getElementById('refuels')

function loadConsumtion(consumption){
    consumptionEl.innerText = consumption ? consumption : 'N/A'
}

function fetchConsumption(){
    fetch('/api/consumption/')
    .then(res => res.json())
    .then(data => loadConsumtion(data.consumption))
}

fetchConsumption()

function loadRefuels(refuels){
    refuels.forEach(refuel => {
        refuelEl = document.createElement('div')
        inner =  `
        <h3>${refuel.amount}l</h3>
        <h4>${refuel.money}Ft</h4>
        <h5>${refuel.date} - (${refuel.gasstation.name})</h5>
        `
        refuelEl.innerHTML = inner
        refuelsEl.appendChild(refuelEl)
    })
}

function fetchRefuels(){
    fetch('/api/all/')
    .then(res => res.json())
    .then(data => loadRefuels(data))
}

fetchRefuels()
