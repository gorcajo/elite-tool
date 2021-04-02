function main() {
    document.getElementById("btn-search-id").onclick = function() {
        search("id", document.getElementById("txt-id").value)
    }

    document.getElementById("btn-search-sn").onclick = function() {
        search("serial_number", document.getElementById("txt-sn").value)
    }

    document.getElementById("btn-search-customer-phone").onclick = function() {
        search("customer_phone", document.getElementById("txt-customer-phone").value)
    }

    document.getElementById("btn-search-customer-name").onclick = function() {
        search("customer_name", document.getElementById("txt-customer-name").value)
    }
}

function search(key, value) {
    if (value !== "") {
        window.location = "/pages/browse#" + key + "=" + value;
    }
}

main();
