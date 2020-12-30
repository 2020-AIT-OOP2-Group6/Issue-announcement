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

      total_score =
        data[0].hand_score +
        Number(document.getElementById("result_score").getAttribute("name"));
      console.log(total_score);
      console.log("re");

      var result_score_value = document.getElementById("result_score_value");
      result_score_value.innerHTML = total_score;

      //何ゲーム目なのか判断する変数
      var round_count =
        Number(document.getElementById("round_count").getAttribute("name")) + 1;

      var next = document.getElementById("next");

      console.log(round_count);

      
      if(data[0].hand_score != 0){
        if (round_count < 6) {
          score_i_t.innerHTML =
            "<h3 name=" +
            data[7].pname +
            'id="pname">winner ' +
            data[7].pname +
            "さん</h3><h3>スコア+" +
            data[0].hand_score +
            "点</h3>"+
            '<a href="/next?pname=' +
            data[7].pname +
            "&score=" +
            total_score +
            "&round_count=" +
            round_count +
            '"><button class="btn btn-primary btn-lg">次のゲームへ</button></a>';
          }else{
            score_i_t.innerHTML =
              "<h3 name=" +
              data[7].pname +
              'id="pname">winner ' +
              data[7].pname +
              "さん</h3><h3>スコア+" +
              data[0].hand_score +
              "点</h3>" +
              '<h3>終了です</h3> <div id="next"><a href="/title?pname=' +
              data[7].pname +
              "&result_score=" +
              total_score +
              '"><div id="title"><button type="button" class="btn btn-primary">タイトルに戻る</button></div></a></div>';

        }
      }else{
        if (round_count < 6) {
          score_i_t.innerHTML =
            "<h3 name=" +
            data[7].pname +
            'id="pname">winner ' +
            "com</h3><h3>スコア+" +
            data[0].hand_score +
            "点</h3>" +
            '<a href="/next?pname=' +
            data[7].pname +
            "&score=" +
            total_score +
            "&round_count=" +
            round_count +
            '"><button class="btn btn-primary btn-lg">次のゲームへ</button></a>';
          }else{
            score_i_t.innerHTML =
              "<h3 name=" +
              data[7].pname +
              'id="pname">winner ' +
              "com</h3><h3>スコア+" +
              data[0].hand_score +
              "点</h3>" +
              '<h3>終了です</h3> <div id="next"><a href="/title?pname=' +
              data[7].pname +
              "&result_score=" +
              total_score +
              '"><div id="title"><button type="button" class="btn btn-primary">タイトルに戻る</button></div></a></div>';

          }
      }

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
