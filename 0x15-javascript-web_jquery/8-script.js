$.ajax({
  url: "https://swapi-api.alx-tools.com/api/films/?format=json",
  method: "GET",
  success: function (data) {
    $("UL#list_movies").append(
      ...data.results.map((movie) => `<li>${movie.title}</li>`)
    );
  },
  error: function (xhr, status, error) {
    console.log(error);
  },
});
