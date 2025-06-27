document.getElementById('form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const professor = document.getElementById('professorName').value;
    const school = document.getElementById('schoolName').value;
    const results = document.getElementById('results');
    const loading = document.getElementById('loading');

    console.log('Professor: ' + professor + ', School: ' + school);

    loading.classList.remove('hidden');
    results.classList.add('hidden');

    try {
        // Try to request the summary from backend
        const response = await fetch('http://127.0.1:8000/api/summarize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ professor: professor, school: school })
        })

        // Check if request worked
        if (!response.ok) {
            throw new Error('HTTP error: status: ' + response.status);
        }

        const data = await response.json();

        // add the data to the page
        document.getElementById('keywords').innerHTML = data.keywords.map(k => `<li>${k}</li>`).join('');
        document.getElementById('summary').textContent = data.summary;

        // reveal the results
        results.classList.remove('hidden');
    } catch (error) {
        if (error instanceof TypeError && error.message == 'NetworkError when attempting to fetch resource.') {
            console.error(error);
            alert('Network error: Please check your connection.');
        } else {
            console.error(error);
            alert('Something went wrong. Please try again later.');
        }
        results.classList.remove('hidden');
    } finally {
        loading.classList.add('hidden');
    }
});
