function search() {
  fetch(
    "http://localhost/extract-twitter?word=" +
      document.getElementById("search").value
  )
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      let tweetsHTML = "";
      for (let i = 0; i < data.tweets.length; i++) {
        tweetsHTML += "<p>" + data.tweets[i].tweet + "<p>";
      }
      tweets.innerHTML = tweetsHTML;
    });
}
