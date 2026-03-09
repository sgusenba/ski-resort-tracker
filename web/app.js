fetch("../data/history.json")
.then(r=>r.json())
.then(data=>{

const latest = data[data.length-1]

let html=""

latest.resorts.forEach(r=>{

html += `
<div class="card">
<h3>${r.resort}</h3>
<p>Lifts: ${r.lifts_open}/${r.lifts_total}</p>
<p>Slopes: ${r.slopes_open}/${r.slopes_total}</p>
</div>
`

})

document.getElementById("resorts").innerHTML = html

const labels = data.map(d=>d.date)
const lifts = data.map(d=>d.resorts.reduce((a,b)=>a+b.lifts_open,0))

new Chart(
document.getElementById("chart"),
{
type:"line",
data:{
labels:labels,
datasets:[{
label:"Total open lifts",
data:lifts
}]
}
})

})
