function classname_normal() {
  hand00.className = "";
  hand01.className = "";
  hand02.className = "";
  hand03.className = "";
  hand04.className = "";
}

function turn_background() {
  document.getElementById("card_change").disabled = true;
  if (hand00.className == "active") {
    tmp0 = document.getElementById("hand00").src;
    document.getElementById("hand00").src = "static/card_back.png";
  }
  if (hand01.className == "active") {
    tmp1 = document.getElementById("hand01").src;
    document.getElementById("hand01").src = "static/card_back.png";
  }
  if (hand02.className == "active") {
    tmp2 = document.getElementById("hand02").src;
    document.getElementById("hand02").src = "static/card_back.png";
  }
  if (hand03.className == "active") {
    tmp3 = document.getElementById("hand03").src;
    document.getElementById("hand03").src = "static/card_back.png";
  }
  if (hand04.className == "active") {
    tmp4 = document.getElementById("hand04").src;
    document.getElementById("hand04").src = "static/card_back.png";
  }
}

function newcard_get() {
  var chenge_card_num = document.getElementsByClassName("active").length;
  var chenge_card_array = new Array(null, null, null, null, null);
  for (i = 0; i < chenge_card_num; i++) {
    chenge_card_array[i] = document
      .getElementsByClassName("active")
      [i].getAttribute("name");
  }

  fetch(
    "/change?hand0=" +
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
      "&num1=" +
      chenge_card_array[0] +
      "&num2=" +
      chenge_card_array[1] +
      "&num3=" +
      chenge_card_array[2]
  ).then((Response) => {
    console.log(Response);
    Response.json().then((data) => {
      console.log(data);
      document
        .getElementById("hand00")
        .setAttribute("src", "/static/" + data[0].hand00);
      document
        .getElementById("hand01")
        .setAttribute("src", "/static/" + data[1].hand01);
      document
        .getElementById("hand02")
        .setAttribute("src", "/static/" + data[2].hand02);
      document
        .getElementById("hand03")
        .setAttribute("src", "/static/" + data[3].hand03);
      document
        .getElementById("hand04")
        .setAttribute("src", "/static/" + data[4].hand04);
      document.getElementById("hand00").setAttribute("tag", data[0].hand00);
      document.getElementById("hand01").setAttribute("tag", data[1].hand01);
      document.getElementById("hand02").setAttribute("tag", data[2].hand02);
      document.getElementById("hand03").setAttribute("tag", data[3].hand03);
      document.getElementById("hand04").setAttribute("tag", data[4].hand04);

      '<h3>終了です</h3> <div id="next"><a href="/title?pname=' +
        data[7].pname +
        "&result_score=" +
        total_score +
        '"><div id="title"><button type="button" class="btn btn-primary">タイトルに戻る</button></div></a></div>';
      document
        .getElementsByClassName("com_card")[1]
        .setAttribute("name", data[5].ophand00);
      document
        .getElementsByClassName("com_card")[2]
        .setAttribute("name", data[6].ophand01);
      document
        .getElementsByClassName("com_card")[3]
        .setAttribute("name", data[7].ophand02);
      document
        .getElementsByClassName("com_card")[4]
        .setAttribute("name", data[8].ophand03);
      document
        .getElementsByClassName("com_card")[5]
        .setAttribute("name", data[9].ophand04);
    });
  });
}

function Alignment() {
  var card_array = [];
  card_array.push(document.getElementById("hand00").getAttribute('src').substr( 8 ));
  card_array.push(document.getElementById("hand01").getAttribute('src').substr( 8 ));
  card_array.push(document.getElementById("hand02").getAttribute('src').substr( 8 ));
  card_array.push(document.getElementById("hand03").getAttribute('src').substr( 8 ));
  card_array.push(document.getElementById("hand04").getAttribute('src').substr( 8 ));
  console.log(card_array)

  var new_card_array = [];

  for(var count = 0;count < 5; count++){
    for(var i = 0; i < card_array.length; i++){
      if(count == 0 && card_array[i].match('Joker')){
        new_card_array.push(card_array[i])
      }
      if(count == 1 && card_array[i].match('A')){
        new_card_array.push(card_array[i])
      }
      if(count == 2 && card_array[i].match('K')){
        new_card_array.push(card_array[i])
      }
      if(count == 3 && card_array[i].match('Q')){
        new_card_array.push(card_array[i])
      }
      if(count == 4 && card_array[i].match('J')){
        if(card_array[i].match('Joker')){
        }
        else{
          new_card_array.push(card_array[i])
        }
      }
    }
  }
  console.log(new_card_array)

  document
    .getElementById("hand00")
    .setAttribute("src", "/static/" + new_card_array[0]);
  document
    .getElementById("hand01")
    .setAttribute("src", "/static/" + new_card_array[1]);
  document
    .getElementById("hand02")
    .setAttribute("src", "/static/" + new_card_array[2]);
  document
    .getElementById("hand03")
    .setAttribute("src", "/static/" + new_card_array[3]);
  document
    .getElementById("hand04")
    .setAttribute("src", "/static/" + new_card_array[4]);
  document.getElementById("hand00").setAttribute("tag", new_card_array[0]);
  document.getElementById("hand01").setAttribute("tag", new_card_array[1]);
  document.getElementById("hand02").setAttribute("tag", new_card_array[2]);
  document.getElementById("hand03").setAttribute("tag", new_card_array[3]);
  document.getElementById("hand04").setAttribute("tag", new_card_array[4]);
}

document.getElementById("card_change").addEventListener("click", (e) => {
  e.preventDefault();
  turn_background();
  setTimeout(newcard_get, 1500);

  setTimeout(classname_normal, 2000);
  setTimeout(Alignment,2500);
});
