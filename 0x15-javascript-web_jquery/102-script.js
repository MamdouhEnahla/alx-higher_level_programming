$(document).ready(function() {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('#btn_translate').click(function() {
    $.ajax({
      url: url + $.param({ lang: $('#language_code').val() }),
      method: 'GET',
      success: function(data) {
        console.log(data);
        $('#hello').html(data.hello);
      },
      error: function(xhr, status, error) {
        console.error("Failed to fetch greeting:", error);
      }
    });
  });
});
