const movies = document.getElementById('movies');
const url = 'http://localhost:8888/api/blog/categories';

fetch(url)
.then(function(response) {
    return response.json()
})
.then(function(myJson) {
    console.log(JSON.stringify(myJson))
});
