function result_show() {
  result.className = "gameset";
}

document.querySelector("#battle").addEventListener("click", (e) => {
  e.preventDefault();
  fetch(
    "/battle?hand0=" +
      document.getElementById("hand00").getAttribute("tag") +
      "&hand1=" +
      document.getElementById("hand01").getAttribute("tag") +
      "&hand2=" +
      document.getElementById("hand02").getAttribute("tag") +
      "&hand3=" +
      document.getElementById("hand03").getAttribute("tag") +
      "&hand4=" +
      document.getElementById("hand04").getAttribute("tag") +
      "&ophand0=" +
      document.getElementsByClassName("com_card")[1].getAttribute("name") +
      "&ophand1=" +
      document.getElementsByClassName("com_card")[2].getAttribute("name") +
      "&ophand2=" +
      document.getElementsByClassName("com_card")[3].getAttribute("name") +
      "&ophand3=" +
      document.getElementsByClassName("com_card")[4].getAttribute("name") +
      "&ophand4=" +
      document.getElementsByClassName("com_card")[5].getAttribute("name") +
      "&pname=" +
      document.getElementById("pname").getAttribute("name") +
      "&score=" +
      document.getElementById("result_score").getAttribute("name")
  ).then((Response) => {
    console.log(Response);
    Response.json().then((data) => {
      // var handscore = document.getElementById("play_score");
      // console.log(handscore);
      // handscore.innerHTML = "<h1>player score:" + data[0].hand_score + "</h1>";

      // var ophandscore = document.getElementById("com_score");
      // console.log(ophandscore);
      // ophandscore.innerHTML = "<h1>com score:" + data[1].ophand_score + "</h1>";

      var score_i_t = document.getElementById("result");
      console.log(score_i_t);

      score_i_t.innerHTML =
        "<h3 name=" +
        data[7].pname +
        'id="pname">winner' +
        data[7].pname +
        "さん</h3><h3>スコア+" +
        data[0].hand_score +
        "点</h3>";

      total_score =
        data[0].hand_score +
        Number(document.getElementById("result_score").getAttribute("name"));
      console.log(total_score);
      console.log("re");

      // console.log(
      //   Number(document.getElementById("result_score").getAttribute("name"))
      // );
      // console.log(total_score);

      var reset = document.getElementById("reset");
      reset.innerHTML =
        '<a href="/reset?pname=' +
        data[7].pname +
        "&score=" +
        total_score +
        '">次のゲームへ</a>';

      document
        .getElementsByClassName("com_card")[1]
        .setAttribute("src", "/static/" + data[2].c0);
      document
        .getElementsByClassName("com_card")[2]
        .setAttribute("src", "/static/" + data[3].c1);
      document
        .getElementsByClassName("com_card")[3]
        .setAttribute("src", "/static/" + data[4].c2);
      document
        .getElementsByClassName("com_card")[4]
        .setAttribute("src", "/static/" + data[5].c3);
      document
        .getElementsByClassName("com_card")[5]
        .setAttribute("src", "/static/" + data[6].c4);
    });
  });
  setTimeout(result_show, 2000);
});
