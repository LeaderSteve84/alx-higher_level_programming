$(document).ready(function () {
  const newText = 'New Header!!!';
  $('DIV#update_header').click(function () {
    $('header').text(newText)
  });
});
