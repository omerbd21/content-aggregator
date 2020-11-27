async function fetchWebsites(url = 'http://celery-manager-content-aggregator.192.168.5.60.nip.io/website_names/', data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
        method: 'GET', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        headers: {
            'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
    });
    return response.json().then(data => data);
};

export default fetchWebsites;