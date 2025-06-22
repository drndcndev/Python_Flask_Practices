function fetchGreeting() {
    const name = document.getElementById("nameInput").value;
    fetch(`/api/greet?name=${name}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("greeting").innerText = data.Greeting;
        });
}
