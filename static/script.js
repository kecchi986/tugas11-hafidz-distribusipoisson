document.getElementById('poissonForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    const lambda = parseFloat(document.getElementById('lambda').value);
    const k = parseInt(document.getElementById('k').value);

    if (lambda < 0 || k < 0) {
        document.getElementById('result').innerText = "Please enter valid positive numbers for λ and k.";
        return;
    }

    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ lambda, k }),
        });

        const data = await response.json();

        if (data.error) {
            document.getElementById('result').innerText = data.error;
        } else {
            document.getElementById('result').innerText = `P(X = ${k}) = ${data.result}`;
        }
    } catch (error) {
        document.getElementById('result').innerText = "An error occurred while calculating.";
    }
});
