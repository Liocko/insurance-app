const loginForm = document.getElementById('login-form');
const errorDiv = document.getElementById('error');
const clientsDiv = document.getElementById('clients');
const registerForm = document.getElementById('register-form');

let token = '';

loginForm.addEventListener('submit', async (evt) => {
    evt.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('http://localhost:5001/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: username, password: password })
        });

        const data = await response.json();

        if (response.ok) {
            token = data.access_token;
            errorDiv.textContent = '';
            fetchClients();
        } else {
            errorDiv.textContent = data.message || 'Ошибка авторизации';
        }
    } catch (error) {
        errorDiv.textContent = 'Ошибка соединения с сервером';
    }
});

async function fetchClients() {
    try {
        const response = await fetch('http://localhost:5001/clients', {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (response.ok) {
            const data = await response.json();
            renderClients(data.clients);
        } else {
            clientsDiv.textContent = 'Ошибка при загрузке клиентов';
        }
    } catch (error) {
        clientsDiv.textContent = 'Ошибка соединения с сервером';
    }
}

function renderClients(clients) {
    clientsDiv.innerHTML = '<h2>Список клиентов:</h2>';
    const list = document.createElement('ul');
    clients.forEach(client => {
        const item = document.createElement('li');
        item.textContent = `${client.id}: ${client.first_name} ${client.last_name}`;
        list.appendChild(item);
    });
    clientsDiv.appendChild(list);
}

registerForm.addEventListener('submit', async (evt) => {
    evt.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('http://localhost:5001/auth/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (response.ok) {
            errorDiv.textContent = 'Registration successful!';
            // Перенаправление на страницу логина, если нужно
        } else {
            errorDiv.textContent = data.message || 'Registration failed';
        }
    } catch (error) {
        errorDiv.textContent = 'Error connecting to server';
    }
});
