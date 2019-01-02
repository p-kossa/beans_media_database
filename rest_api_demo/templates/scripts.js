var request = new XMLHttpRequest();
request.open('GET', 'http://localhost:8888/api/blog/categories', true);
request.onload = function () {
    // Begin accessing JSON data here
    var data = JSON.parse(this.response);

    if (request.status >= 200 && request.status < 400) {
        data.forEach(movie => {
            console.log(movie.name)
        });
    } else {
        console.log('error');
    }
}


request.send();