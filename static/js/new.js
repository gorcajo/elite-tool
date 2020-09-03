function main() {
    document.getElementById("btn-save").onclick = function () {
        request = new XMLHttpRequest();

        request.open("POST", "/api/repairments");
        request.setRequestHeader("Content-Type", "application/json");

        request.onload = function () {
            if (request.status !== 200) {
                throw "HTTP " + request.status + ": " + request.statusText;
            }
        
            alert(request.responseText);
        };

        request.send(JSON.stringify({
            "customer_name": "Lenin Grado",
            "customer_phone": "612312312",
            "type": "Mac",
            "manufacturer": "Apple",
            "model": "MacBook Pro",
            "serial_number": "123456789",
            "reception_date": "hoy",
            "estimated_cost": "10000",
            "description": "Asd asd asd",
        }));
    }
}

main();