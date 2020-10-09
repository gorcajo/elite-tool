function main() {
    document.getElementById("btn-save").onclick = function () {
        let request = new XMLHttpRequest();

        request.open("POST", "/api/repairments");
        request.setRequestHeader("Content-Type", "application/json");

        request.onload = function () {
            if (request.status !== 200) {
                throw "HTTP " + request.status + ": " + request.statusText;
            }
        
            alert("OK");
            let repairmentId = JSON.parse(request.responseText).id
            window.location = "/pages/edit#id=" + repairmentId;
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
        } else if (document.getElementById("txt-estimated-cost").value === "") {
            alert("El campo 'Costo aproximado de reparación' es obligatorio");
        } else if (document.getElementById("txt-description").value === "") {
            alert("El campo 'Problema del equipo' es obligatorio");
        } else {
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
                "estimated_cost": document.getElementById("txt-estimated-cost").value,
                "description": document.getElementById("txt-description").value,
            }));
        }
    }
}

main();
