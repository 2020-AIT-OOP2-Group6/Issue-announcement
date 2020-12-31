// ホーム画面にランキングを表示させる
fetch("/name").then((response) => {
  console.log(response);
  response.json().then((data) => {
    console.log(data); // 取得されたレスポンスデータをデバッグ表示
    // データを表示させる
    const tableBody = document.querySelector("#ranking-list > tbody");
    i = 1;
    data.forEach((elm) => {
      // 1行づつ処理を行う
      let tr = document.createElement("tr");
      let td = document.createElement("td");
      td.innerText = i;
      // 順位
      tr.appendChild(td);
      td = document.createElement("td");
      td.innerText = elm.player_name;
      // player_name
      tr.appendChild(td);
      td = document.createElement("td");
      td.innerText = elm.score;
      // score
      tr.appendChild(td);

      // 1行分をtableタグ内のtbodyへ追加する
      tableBody.appendChild(tr);
      i++;
    });
  });
});

function loadFinish() {
  if (window.performance) {
    if (performance.navigation.type === 1) {
      new_url = "http://127.0.0.1:5000/title?pname=null&result_score=0";

      window.location.href = new_url;
    }
  }
}

window.addEventListener("load", loadFinish);
