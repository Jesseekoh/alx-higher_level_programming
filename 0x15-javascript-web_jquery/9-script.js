const API_URL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$.get(API_URL, (data) => {
  $('DIV#hello').append(`<p>${data.hello}</p>`);
});
