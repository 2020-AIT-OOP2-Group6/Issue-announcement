function result_show(){
    result.className = "gemeset";
}

function turn_front(){
    // 次のカード手札
    // document.getElementById("hand00").src =　tmp;
    // document.getElementById("hand01").src =　tmp;
    // document.getElementById("hand02").src =　tmp;
    // document.getElementById("hand03").src =　tmp;
    // document.getElementById("hand04").src =　tmp;
}

function reset(){
    result.className = "hidden"
    document.getElementById("hand00").src =　"static/card_back.png";
    document.getElementById("hand01").src =　"static/card_back.png";
    document.getElementById("hand02").src =　"static/card_back.png";
    document.getElementById("hand03").src =　"static/card_back.png";
    document.getElementById("hand04").src =　"static/card_back.png";
    setTimeout(turn_front,1000);
    document.getElementById('card_change').disabled = false;
    document.getElementById('battle').disabled = false;
}

// function battle(){
//     let gamecount = 0;

//     document.getElementById("battle").onclick = function() {
//         document.getElementById('card_change').disabled = true;
//         document.getElementById('battle').disabled = true;
//         className_normal()
//         //comの手札開示
//         // document.getElementById("com00").src = tmp;
//         // document.getElementById("com01").src = tmp;
//         // document.getElementById("com02").src = tmp;
//         // document.getElementById("com03").src = tmp;
//         // document.getElementById("com04").src = tmp;
    
//         setTimeout(result_show, 1000);
//         setTimeout(reset, 5000)
//         gamecount++;
//         console.log(gamecount);
//     }
// };

// battle();


function turn_background(){
    document.getElementById('card_change').disabled = true;
    if(hand00.className == "active"){
        tmp0 = document.getElementById("hand00").src
        document.getElementById("hand00").src =　"static/card_back.png";
    }
    if(hand01.className == "active"){
        tmp1 = document.getElementById("hand01").src
        document.getElementById("hand01").src =　"static/card_back.png";
    }
    if(hand02.className == "active"){
        tmp2 = document.getElementById("hand02").src
        document.getElementById("hand02").src =　"static/card_back.png";
    }
    if(hand03.className == "active"){
        tmp3 = document.getElementById("hand03").src
        document.getElementById("hand03").src =　"static/card_back.png";
    }
    if(hand04.className == "active"){
        tmp4 = document.getElementById("hand04").src
        document.getElementById("hand04").src =　"static/card_back.png";
    }
};

function newcard_get(){
    if(hand00.className == "active"){
        document.getElementById("hand00").src =　tmp0;//tmpに新しいカード渡す
    }
    if(hand01.className == "active"){
        document.getElementById("hand01").src =　tmp1;//tmpに新しいカード渡す
    }
    if(hand02.className == "active"){
        document.getElementById("hand02").src =　tmp2;//tmpに新しいカード渡す
    }
    if(hand03.className == "active"){
        document.getElementById("hand03").src =　tmp3;//tmpに新しいカード渡す
    }
    if(hand04.className == "active"){
        document.getElementById("hand04").src =　tmp4;//tmpに新しいカード渡す
    }
    
  
}

function className_normal(){
    hand00.className = "";
    hand01.className = "";
    hand02.className = "";
    hand03.className = "";
    hand04.className = "";
}


// function card_change(){

//     if(document.getElementById('card_change').disabled == false){
//         choose_card();
//     }
//     document.getElementById("card_change").onclick = function() {
//         if(hand00.className == "active" || hand01.className == "active" || hand02.className == "active" || hand03.className == "active" || hand04.className == "active"){
//             turn_background();
//             setTimeout(newcard_get, 1000);
//             setTimeout(className_normal,1500);
//         }
//     };

// };

// card_change();

function choose_card() {
  count = 0;

  document.getElementById("hand00").onclick = function () {
    hand00 = document.getElementById("hand00");
    if (count < 3) {
      if (hand00.className == null || hand00.className == "") {
        hand00.className = "active";
        count = count + 1;
      } else {
        hand00.className = "";
        count = count - 1;
      }
    } else if (hand00.className == "active") {
      hand00.className = "";
      count = count - 1;
    }
  };
  document.getElementById("hand01").onclick = function () {
    hand01 = document.getElementById("hand01");
    if (count < 3) {
      if (hand01.className == null || hand01.className == "") {
        hand01.className = "active";
        count = count + 1;
      } else {
        hand01.className = "";
        count = count - 1;
      }
    } else if (hand01.className == "active") {
      hand01.className = "";
      count = count - 1;
    }
  };

  document.getElementById("hand00").onclick = function () {
    hand00 = document.getElementById("hand00");
    if (count < 3) {
      if (hand00.className == null || hand00.className == "") {
        hand00.className = "active";
        count = count + 1;
      } else {
        hand00.className = "";
        count = count - 1;
      }
    } else if (hand00.className == "active") {
      hand00.className = "";
      count = count - 1;
    }
  };

  document.getElementById("hand01").onclick = function () {
    hand01 = document.getElementById("hand01");
    if (count < 3) {
      if (hand01.className == null || hand01.className == "") {
        hand01.className = "active";
        count = count + 1;
      } else {
        hand01.className = "";
        count = count - 1;
      }
    } else if (hand01.className == "active") {
      hand01.className = "";
      count = count - 1;
    }
  };

  document.getElementById("hand02").onclick = function () {
    hand02 = document.getElementById("hand02");
    if (count < 3) {
      if (hand02.className == null || hand02.className == "") {
        hand02.className = "active";
        count = count + 1;
      } else {
        hand02.className = "";
        count = count - 1;
      }
    } else if (hand02.className == "active") {
      hand02.className = "";
      count = count - 1;
    }
  };

  document.getElementById("hand03").onclick = function () {
    hand03 = document.getElementById("hand03");
    if (count < 3) {
      if (hand03.className == null || hand03.className == "") {
        hand03.className = "active";
        count = count + 1;
      } else {
        hand03.className = "";
        count = count - 1;
      }
    } else if (hand03.className == "active") {
      hand03.className = "";
      count = count - 1;
    }
  };

  document.getElementById("hand04").onclick = function () {
    hand04 = document.getElementById("hand04");
    if (count < 3) {
      if (hand04.className == null || hand04.className == "") {
        hand04.className = "active";
        count = count + 1;
      } else {
        hand04.className = "";
        count = count - 1;
      }
    } else if (hand04.className == "active") {
      hand04.className = "";
      count = count - 1;
    }
  };
}

choose_card();
