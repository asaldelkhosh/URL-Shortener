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
            url.target = '_blank';

            el.appendChild(label);
            el.appendChild(url);

            getURLs();
        })
        .catch((error) => {
            console.error(error);
            alert('Failed to create URL!');
        })
}

// remove a url by executing a fetch
function removeURL(id) {
    fetch("/url/"+id)
        .then(() => {
            getHistory();
        })
        .catch((error) => {
            console.error(error)
            alert('Failed to remove URL!');
        })
}

// update a url by id
function updateURL(id) {
    fetch("/url/"+id, {
        method: "POST",
    })
        .then(() => {
            console.log('called ' + id);
        })
        .catch((error) => {
            console.log(error);
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
                tmp.classList.add("list-item");

                let count = document.createElement("span");
                count.style.marginInlineEnd = "25px";
                count.innerText = "Count: " + zeroPad(element[3]);

                let title = document.createElement("span");
                title.innerHTML = "URL: " + element[1];
                title.style.marginInlineEnd = "40px";

                let url = document.createElement("a");
                url.href = 'https://' + element[2];
                url.innerText = "Link: " + element[2];
                url.target = '_blank';

                url.addEventListener('click', function() {
                    updateURL(element[0]);
                });

                tmp.appendChild(title);
                tmp.appendChild(count);
                tmp.appendChild(url);

                rsp.appendChild(tmp);
            });
        })
        .catch((error) => {
            console.error(error);
            alert('Failed to get URLs!');
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

            let list = {};

            data['urls'].forEach(element => {
                let key = new Date(element[4]).toLocaleDateString();

                if (!(key in list)) {
                    list[key] = [];   
                }

                list[key].push(element);
            })

            for (const [key, value] of Object.entries(list)) {
                let tmp = document.createElement("div");

                let title = document.createElement("h2");
                title.innerText = key;

                let ul = document.createElement("ul");
                ul.style.listStyleType = 'none';

                value.forEach(element => {
                    let li = document.createElement("li");
                    li.style.marginBlockEnd = "40px";

                    let main = document.createElement("div");
                    main.style.marginBlock = "20px";
    
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

                    let modifyDate = document.createElement("span");
                    modifyDate.style.marginInlineEnd = "10px";
                    modifyDate.innerText = "Last use: " + element[5];
    
                    let title = document.createElement("span");
                    title.innerHTML = element[1] + " :";
                    title.style.marginInlineEnd = "40px";
    
                    let url = document.createElement("a");
                    url.href = 'https://' + element[2];
                    url.innerText = element[2];
                    url.target = '_blank';

                    url.addEventListener('click', function() {
                        updateURL(element[0]);
                    });

                    main.appendChild(title);
                    main.appendChild(url);
    
                    li.appendChild(main);
                    li.appendChild(count);
                    li.appendChild(btn);
                    li.appendChild(modifyDate);
    
                    ul.appendChild(li);
                });

                tmp.appendChild(title);
                tmp.appendChild(ul);
                rsp.appendChild(tmp);
            }
        })
        .catch((error) => {
            console.error(error)
            alert('Failed to get URLs!')
        })
}