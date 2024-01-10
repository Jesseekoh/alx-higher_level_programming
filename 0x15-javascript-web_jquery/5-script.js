$('DIV#add_item').click(() => {
  const newElement = $('<li></li>').text('Item');
  $('UL.my_list').append(newElement);
});
