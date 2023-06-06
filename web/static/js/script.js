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
        .then(response => response.text())
        .then((data) => {
            let el = document.getElementById('url-result');
            el.innerHTML = '';

            let label = document.createElement("span");
            label.innerText = "Your URL is: ";

            let url = document.createElement("a");
            url.href = 'https://' + data;
            url.innerText = data;

            el.appendChild(label);
            el.appendChild(url);

            getURLs();
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
            getURLs();
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
            rsp.innerHTML = '';

            if (data['urls'].length == 0) {
                rsp.innerText = "No entities!";

                return
            }

            const count = (number) => number.toString().length;
            const zeroPad = (num) => String(num).padStart(count(data['urls'][0][3]), '0');

            data['urls'].forEach(element => {
                let tmp = document.createElement("li");
                tmp.style.marginBlockEnd = "20px";

                let count = document.createElement("snap");
                count.style.marginInlineEnd = "10px";
                count.innerText = zeroPad(element[3]);

                let btn = document.createElement("button");
                btn.innerText = "Delete";
                btn.onclick = function() {
                    removeURL(element[0]);
                };
                btn.style.marginInlineEnd = "20px";
                btn.classList.add('btn', 'btn-red');

                let title = document.createElement("span");
                title.innerHTML = element[1] + " :";
                title.style.marginInlineEnd = "40px";

                let url = document.createElement("a");
                url.href = 'https://' + element[2];
                url.innerText = element[2];

                tmp.appendChild(count);
                tmp.appendChild(btn);
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


function getHistory() {
    fetch("/history/data",
    {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
    })
        .then(response => response.json())
        .then((data) => {
            let rsp = document.getElementById('urls');
            rsp.innerHTML = '';

            if (data['urls'].length == 0) {
                rsp.innerText = "No entities!";

                return
            }

            const count = (number) => number.toString().length;
            const zeroPad = (num) => String(num).padStart(count(data['urls'][0][3]), '0');

            list = {}

            data['urls'].forEach(element => {
                let key = element[4];
                if (!key in list) {
                    list[key] = [];
                }

                list[key].push(element);
            })

            for (const [key, value] of Object.entries(list)) {
                let tmp = document.createElement("div");

                let title = document.createElement("h3");
                title.innerText = key;

                let ul = document.createElement("ul");

                value.forEach(element => {
                    let li = document.createElement("li");
                    li.style.marginBlockEnd = "40px";
    
                    let count = document.createElement("span");
                    count.style.marginInlineEnd = "10px";
                    count.innerText = "Used: " + zeroPad(element[3]);
    
                    let btn = document.createElement("button");
                    btn.innerText = "Delete";
                    btn.onclick = function() {
                        removeURL(element[0]);
                    };
                    btn.style.marginInlineEnd = "20px";
                    btn.classList.add('btn', 'btn-red');
    
                    let title = document.createElement("span");
                    title.innerHTML = element[1] + " :";
                    title.style.marginInlineEnd = "40px";
    
                    let url = document.createElement("a");
                    url.href = 'https://' + element[2];
                    url.innerText = element[2];
    
                    li.appendChild(count);
                    li.appendChild(btn);
                    li.appendChild(title);
                    li.appendChild(url);
    
                    ul.appendChild(tmp);
                });

                tmp.appendChild(title);
                tmp.appendChild(ul)
                rsp.appendChild(tmp);
            }
        })
        .catch((error) => {
            console.error(error)
            alert('Failed to get URLs!')
        })
}