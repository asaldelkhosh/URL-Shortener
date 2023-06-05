const host = '127.0.0.1:3000';



// create a new url by executing a fetch
function createURL() {
    let data = document.getElementById('url-input').value

    fetch(host+"/url",
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

}

// get all urls by executing a fetch
function getURLs() {

}
