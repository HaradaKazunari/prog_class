function myGame(){
  $('.button').on('click', function(){
    var myNumber =  $(this).data('id');

    hisNumber = Math.floor(Math.random()*3);
    if( hisNumber == 0 ){
      hisHand = '<img src="./img/gu.png" alt="">';
    }
    else if( hisNumber == 1 ){
      hisHand = '<img src="./img/tyoki.png" alt="">';
    }
    else if( hisNumber == 2 ){
      hisHand = '<img src="./img/pa.png" alt="">';
    }

    let judgeNumber = myNumber - hisNumber;
    if( (judgeNumber == -2 ) || ( judgeNumber == 1 ) ){
      judge = "あなたの 負け";
    }
    else if(( judgeNumber == -1 ) || ( judgeNumber == 2 )){
      judge = "あなたの 勝ち";
    }
    else if( myNumber - hisNumber == 0 ){
      judge = "両者の 引き分け";
    }
    $("#message1").empty();
    $("#message1").append(hisHand);
    $("#message2").text(judge);

  });
}
