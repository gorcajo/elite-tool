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

        if (repairments.length === 0) {
            let cell = table.insertRow(1).insertCell(0);
            cell.innerHTML = "(no hay reparaciones en la base de datos)";
            cell.setAttribute("colSpan", "5");
        } else {
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
                    window.location = "/files/repairment-" +  repairments[i].id + ".pdf"
                });
                buttonsCell.appendChild(newViewButton);

                let newEditButton = editButton.cloneNode(true);
                newEditButton.removeAttribute('id');
                newEditButton.addEventListener("click", function() {
                    window.location = "/pages/edit#id=" + repairments[i].id;
                });
                buttonsCell.appendChild(newEditButton);

                let newDeleteButton = deleteButton.cloneNode(true);
                newDeleteButton.removeAttribute('id');
                newDeleteButton.addEventListener("click", function() {
                    let response = confirm("Vas a borrar la reparación, ¿estás seguro?");

                    if (response === true) {
                        let request = new XMLHttpRequest();
                        request.open("DELETE", "/api/repairments/" + repairments[i].id);
                        request.onload = function () {
                            location.reload();
                        }
                        request.send();
                    }
                });
                buttonsCell.appendChild(newDeleteButton);
            }
        }
    };

    request.send();
}

function getHashString() {
    return window.location.hash.substr(1);
}

main();
