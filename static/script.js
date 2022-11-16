function search() {
  fetch(
    "http://localhost/extract_twitter?word=" +
      document.getElementById("search").value
  )
    .then(function (response) {
      return response.json();
    })
    .then(function (TweetsData) {
      let tweetsHTML = "";
      for (let i = 0; i < TweetsData.tweets.length; i++) {
        console.log(TweetsData.tweets[i].tweet);
        console.log(TweetsData.tweets[i].favorite);
        tweetsHTML += "<p>" + TweetsData.tweets[i].tweet + "<p>";
        tweets.innerHTML = tweetsHTML;
      }
    });
}
