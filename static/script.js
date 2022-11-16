function search() {
  fetch(
    "http://localhost/extract_twitter?word=" +
      document.getElementById("search").value
  )
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      let tweetsHTML = "";
      for (let i = 0; i < data.tweets.length; i++) {
        console.log(data.tweets[i].tweet);
        console.log(data.tweets[i].favorite);
        tweetsHTML += "<p>" + data.tweets[i].tweet + "<p>";
        tweets.innerHTML = tweetsHTML;
      }
    });
}
