// create a new url by executing a fetch
function createURL() {
    let data = document.getElementById('url-input').value

    fetch("/url",
        {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            method: "POST",
            body: JSON.stringify({'url': data})
        })
        .then(() => {
            window.location.reload()
        })
        .catch((error) => {
            console.error(error)
            alert('Failed to create URL!')
        })
}

// remove a url by executing a fetch
function removeURL(id) {
    fetch("/url/"+id)
        .then(() => {
            window.location.reload()
        })
        .catch((error) => {
            console.error(error)
            alert('Failed to remove URL!')
        })
}

// get all urls by executing a fetch
function getURLs() {
    fetch("/url")
        .then((response) => {
            console.log(response.json())
        })
        .catch((error) => {
            console.error(error)
            alert('Failed to get URLs!')
        })
}
