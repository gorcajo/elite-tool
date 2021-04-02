function main() {
    let id = getHashParameter("id");

    let request = new XMLHttpRequest();

    request.open("GET", "/api/repairments/" + id);

    request.onload = function () {
        if (request.status !== 200) {
            throw "HTTP " + request.status + ": " + request.statusText;
        }

        repairment = JSON.parse(request.responseText);

        document.getElementById("txt-id").value = repairment.id;
        document.getElementById("txt-customer-name").value = repairment.customer_name;
        document.getElementById("txt-customer-phone").value = repairment.customer_phone;
        document.getElementById("txt-type").value = repairment.type;
        document.getElementById("txt-manufacturer").value = repairment.manufacturer;
        document.getElementById("txt-model").value = repairment.model;
        document.getElementById("txt-sn").value = repairment.serial_number;
        document.getElementById("txt-backup").value = repairment.backup;
        document.getElementById("txt-password").value = repairment.password;
        document.getElementById("txt-reception-date").value = repairment.reception_date;
        document.getElementById("txt-withdrawal-date").value = repairment.withdrawal_date;
        document.getElementById("txt-estimated-cost").value = repairment.estimated_cost;
        document.getElementById("txt-description").value = repairment.description;
    };

    request.send();

    document.getElementById("btn-save").onclick = function() {
        let request = new XMLHttpRequest();

        request.open("PUT", "/api/repairments/" + id);
        request.setRequestHeader("Content-Type", "application/json");

        request.onload = function () {
            if (request.status !== 204) {
                throw "HTTP " + request.status + ": " + request.statusText;
            }

            alert("OK");
            console.log(request)
            window.location = "/files/repairment-" + id + ".pdf";
        };

        if (document.getElementById("txt-customer-name").value === "") {
            alert("El campo 'Nombre' es obligatorio");
        } else if (document.getElementById("txt-customer-phone").value === "") {
            alert("El campo 'Teléfono móvil' es obligatorio");
        } else if (document.getElementById("txt-type").value === "") {
            alert("El campo 'Equipo' es obligatorio");
        } else if (document.getElementById("txt-manufacturer").value === "") {
            alert("El campo 'Fabricante' es obligatorio");
        } else if (document.getElementById("txt-model").value === "") {
            alert("El campo 'Modelo' es obligatorio");
        } else if (document.getElementById("txt-sn").value === "") {
            alert("El campo 'Número de Serie' es obligatorio");
        } else if (document.getElementById("txt-backup").value === "") {
            alert("El campo 'Backup' es obligatorio");
        } else if (document.getElementById("txt-password").value === "") {
            alert("El campo 'Password' es obligatorio");
        } else if (document.getElementById("txt-reception-date").value === "") {
            alert("El campo 'Fecha de recepción' es obligatorio");
        } else if (document.getElementById("txt-withdrawal-date").value === "") {
            alert("El campo 'Fecha de retirada' es obligatorio");
        } else if (document.getElementById("txt-estimated-cost").value === "") {
            alert("El campo 'Costo aproximado de reparación' es obligatorio");
        } else if (document.getElementById("txt-description").value === "") {
            alert("El campo 'Problema del equipo' es obligatorio");
        } else {
            let response = confirm("Vas a sobreescribir la reparación, ¿estás seguro?");
    
            if (response === true) {
                request.send(JSON.stringify({
                    "customer_name": document.getElementById("txt-customer-name").value,
                    "customer_phone": document.getElementById("txt-customer-phone").value,
                    "type": document.getElementById("txt-type").value,
                    "manufacturer": document.getElementById("txt-manufacturer").value,
                    "model": document.getElementById("txt-model").value,
                    "serial_number": document.getElementById("txt-sn").value,
                    "backup": document.getElementById("txt-backup").value,
                    "password": document.getElementById("txt-password").value,
                    "reception_date": document.getElementById("txt-reception-date").value,
                    "withdrawal_date": document.getElementById("txt-withdrawal-date").value,
                    "estimated_cost": document.getElementById("txt-estimated-cost").value,
                    "description": document.getElementById("txt-description").value,
                }));
            }
        }
    };
}

function getHashParameter(parameter) {
    let pairs = getHashString().split("&");

    for (let i = 0; i < pairs.length; i++) {
        let pair = pairs[i];
        let key = pair.split("=")[0];
        let value = pair.split("=")[1];

        if (key === parameter) {
            return value;
        }
    }
}

function getHashString() {
    return window.location.hash.substr(1);
}

main();
