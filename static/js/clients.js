document.addEventListener('DOMContentLoaded', function() {
    loadClients();
    const form = document.getElementById('addClientForm');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        addClient();
    });
});

function loadClients() {
    fetch('http://localhost:5001/clients/list')
        .then(response => response.json())
        .then(clients => {
            const tableBody = document.getElementById('clientsTable').getElementsByTagName('tbody')[0];
            tableBody.innerHTML = '';  // Очищаем таблицу перед добавлением новых данных
            clients.forEach(client => {
                const row = tableBody.insertRow();
                row.innerHTML = `
                    <td>${client.id}</td>
                    <td>${client.first_name}</td>
                    <td>${client.last_name}</td>
                    <td>${client.email}</td>
                    <td>${client.phone}</td>
                    <td>${client.address}</td>
                `;
            });
        })
        .catch(error => console.error('Error loading clients:', error));
}

function addClient() {
    const firstName = document.getElementById('first_name').value;
    const lastName = document.getElementById('last_name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const address = document.getElementById('address').value;

    const clientData = {
        first_name: firstName,
        last_name: lastName,
        email: email,
        phone: phone,
        address: address
    };

    fetch('http://localhost:5001/client/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(clientData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "Client added successfully") {
            loadClients();  // Перезагружаем список клиентов
        }
    })
    .catch(error => {
        console.error('Error adding client:', error);
    });
}

