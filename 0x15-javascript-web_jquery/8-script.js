const API_URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(API_URL, (data) => {
  data.results.forEach((film) => {
    $('UL#list_movies').append(`<li>${film.title}</li>`);
  });
});
