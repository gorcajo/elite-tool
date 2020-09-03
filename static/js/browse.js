function main() {
    let request = new XMLHttpRequest();

    request.open("GET", "/api/repairments");

    request.onload = function () {
        if (request.status !== 200) {
            throw "HTTP " + request.status + ": " + request.statusText;
        }
    
        repairments = JSON.parse(request.responseText);

        let table = document.getElementById("tbl-repairments");
        let buttons = document.getElementById("div-buttons").innerHTML;

        for (let i = 0; i < repairments.length; i++) {
            let row = table.insertRow(i + 1);
            
            let j = 0;
            row.insertCell(j++).innerHTML = repairments[i].id
            row.insertCell(j++).innerHTML = repairments[i].serial_number
            row.insertCell(j++).innerHTML = repairments[i].customer_phone
            row.insertCell(j++).innerHTML = repairments[i].customer_name
            row.insertCell(j++).innerHTML = buttons
        }
    };

    request.send();
}

main();