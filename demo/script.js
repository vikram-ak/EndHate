
const url = "https://EndHate.vikk.repl.co/input";
const button = document.getElementById("submit");
const inputElem = document.getElementById("text");
const out = document.getElementById("out");
button.onclick = () => {
    let inputText = inputElem.value;
    console.log(`Sending: ${text}`);

    let data = {text : inputText};

	console.log(data);
    const response = fetch(url, {
        method: 'POST',
		mode: 'cors',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify(data),
		json: data
    });
	console.log(response);

	response.then(r => {
		return r.json();
	})
	.then(d => {
		let label = d['label'];
		if (label == 0) {
			out.innerHTML = "Not Hate";
		} else {
			out.innerHTML = "Hate";
		}
	})
}