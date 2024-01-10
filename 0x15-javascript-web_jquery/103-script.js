window.addEventListener('load', () => {
  const translate = () => {
    const code = $('INPUT#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${code}`, (data) => {
      $('DIV#hello').html(data.hello);
    });
  };

  $('INPUT#btn_translate').click(translate);

  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').keydown((ev) => {
    if (ev.key === 'Enter') translate();
  });
});
