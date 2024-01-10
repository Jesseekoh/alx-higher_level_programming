const API_URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(API_URL, (data) => {
  $('DIV#character').text(data.name);
});
