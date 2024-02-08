$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    $.each(data.results, function (index, movie) {
      const title = movie.title;
      $('UL#list_movies').append('<li>' + title + '</li>');
    });
  });
});
