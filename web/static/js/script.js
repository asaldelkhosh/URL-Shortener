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
    fetch("/url",
    {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
    })
        .then(response => response.json())
        .then((data) => {
            let rsp = document.getElementById('urls');
            data['urls'].forEach(element => {
                let tmp = document.createElement("li");

                let btn = document.createElement("button")
                btn.innerText = "Delete"
                btn.onclick = function() {
                    removeURL(element[0]);
                };
                btn.style.marginInlineEnd = "20px";
                btn.classList.add('btn', 'btn-red')

                let title = document.createElement("span");
                title.innerHTML = element[1] + " :";
                title.style.marginInlineEnd = "40px";

                let url = document.createElement("a");
                url.href = element[2];
                url.innerText = element[2];

                tmp.appendChild(btn)
                tmp.appendChild(title);
                tmp.appendChild(url);

                rsp.appendChild(tmp);
            });
        })
        .catch((error) => {
            console.error(error)
            alert('Failed to get URLs!')
        })
}
