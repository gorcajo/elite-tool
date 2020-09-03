function main() {
    window.onhashchange = updateTable;
    updateTable();
}

function updateTable() {
    let request = new XMLHttpRequest();

    let hashString = getHashString();

    if (hashString === "") {
        request.open("GET", "/api/repairments");
    } else {
        request.open("GET", "/api/repairments?" + hashString);
    }

    request.onload = function () {
        if (request.status !== 200) {
            throw "HTTP " + request.status + ": " + request.statusText;
        }
    
        repairments = JSON.parse(request.responseText);

        let table = document.getElementById("tbl-repairments");

        let viewButton = document.getElementById("btn-view")
        let editButton = document.getElementById("btn-edit")
        let deleteButton = document.getElementById("btn-delete")

        for (let i = 0; i < repairments.length; i++) {
            let row = table.insertRow(i + 1);
            
            let j = 0;
            row.insertCell(j++).innerHTML = repairments[i].id
            row.insertCell(j++).innerHTML = repairments[i].serial_number
            row.insertCell(j++).innerHTML = repairments[i].customer_phone
            row.insertCell(j++).innerHTML = repairments[i].customer_name
            
            let buttonsCell = row.insertCell(j++);

            let newViewButton = viewButton.cloneNode(true);
            newViewButton.removeAttribute('id');
            newViewButton.addEventListener("click", function() {
                alert("Not Implemented");
            });
            buttonsCell.appendChild(newViewButton);

            let newEditButton = editButton.cloneNode(true);
            newEditButton.removeAttribute('id');
            newEditButton.addEventListener("click", function() {
                alert("Not Implemented");
            });
            buttonsCell.appendChild(newEditButton);

            let newDeleteButton = deleteButton.cloneNode(true);
            newDeleteButton.removeAttribute('id');
            newDeleteButton.addEventListener("click", function() {
                let request = new XMLHttpRequest();
                request.open("DELETE", "/api/repairments/" + repairments[i].id);
                request.onload = function () {
                    location.reload();
                }
                request.send();
            });
            buttonsCell.appendChild(newDeleteButton);
        }
    };

    request.send();
}

function getHashString() {
    return window.location.hash.substr(1);
}

main();
