$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    const character = data.name;
    $('DIV#character').text(character);
  });
});
