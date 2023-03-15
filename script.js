const hiddens =['#div1','#div2','#div3','#div4']
const isHidden = [true,true,true,true]
$(document).ready(function(){
    let isInHidden=false;
    $('#scores').find('.row').click( function(){
      if ($(this).index()%2==0){
        var index = Math.floor($(this).index()/2);
        var d = $(hiddens[index]);
        if (isHidden[index]){
          d[0].style.display='table-row';
          isHidden[index]=false;
        }else{
          d[0].style.display='none';
          isHidden[index]=true;
        }
      }
  });
});
