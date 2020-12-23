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

document.getElementById("card_change").onclick = function () {};

choose_card();
