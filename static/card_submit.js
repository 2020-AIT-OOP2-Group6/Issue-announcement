document.querySelector("#battle").addEventListener("click", (e) => {
  e.preventDefault();
  fetch(
    "/battle?hand0=" +
      document.getElementsByClassName("play_card")[0].getAttribute("src") +
      "&hand1=" +
      document.getElementsByClassName("play_card")[1].getAttribute("src") +
      "&hand2=" +
      document.getElementsByClassName("play_card")[2].getAttribute("src") +
      "&hand3=" +
      document.getElementsByClassName("play_card")[3].getAttribute("src") +
      "&hand4=" +
      document.getElementsByClassName("play_card")[4].getAttribute("src")
  ).then((Response) => {
    

  });
});
