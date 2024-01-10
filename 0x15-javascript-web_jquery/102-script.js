window.addEventListener('load', () => {
  $('INPUT#btn_translate').click(() => {
    const code = $('INPUT#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${code}`, (data) => {
      $('DIV#hello').html(data.hello);
    });
  });
});
