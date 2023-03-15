class ScoreSet{
  constructor(rank,name,imgpath,ascores,bscores,totscore,atot,btot){
    this.rank=rank;
    this.name=name;
    this.imgpath=imgpath;
    this.ascores=ascores;
    this.bscores=bscores;
    this.totscore=totscore;
    this.atot=atot;
    this.btot=btot;
  }
}
const hiddens =['#div1','#div2','#div3','#div4'];
const isHidden = [true,true,true,true];
$(document).ready(function(){
  
  $.getJSON('./data/testdict.json', function(data) {         
    alert(data);
  });
  // constructRow(testScore);
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
function constructRow(ss){
  const scoreTable=$('#scores')[0];
  let rownum=(parseInt(ss.rank)-1)*2;
  hiddens.splice(ss.rank,0, '#div'+ss.rank);
  isHidden.splice(ss.rank,0, true);
  // scoreTable.insertRow($('.rows').length);
  scoreTable.insertRow(rownum);
  let row=scoreTable.rows[rownum]
  row.classList.add("row");

  let td = document.createElement('td');
  td.innerHTML = '<td>'+ss.rank+'</td>';
  td.classList.add("rank");
  row.appendChild(td);

  td = document.createElement('td');
  td.innerHTML = '<td><img src='+ss.imgpath+' alt="'+ss.name+' Banner"></td>';
  td.classList.add("banner");
  row.appendChild(td);

  td = document.createElement('td');
  td.innerHTML = '<td>'+ss.name+'</td>';
  td.classList.add("school");
  row.appendChild(td);

  td = document.createElement('td');
  td.innerHTML = '<td>'+ss.totscore+'</td>';
  td.classList.add("totalscore");
  row.appendChild(td);

  scoreTable.insertRow(rownum+1);
  let hrow=scoreTable.rows[rownum+1]
  hrow.classList.add("hiddenrow");
  hrow.id="div"+ss.rank;

  td=document.createElement('td');
  td.classList.add("rank");
  hrow.appendChild(td);

  td=document.createElement('td');
  td.classList.add("subtd");
  td.colSpan=2;
  hrow.appendChild(td);

  let tbl=document.createElement('table');
  tbl.classList.add('subtable');
  td.appendChild(tbl);

  let tra=document.createElement('tr');
  tra.classList.add('subrow');
  tbl.appendChild(tra);
  let th=document.createElement('th');
  th.innerHTML='<th>A</th>';
  tra.appendChild(th);

  ss.ascores.forEach((score,ind) =>{
    let scoretd=document.createElement('td');
    scoretd.innerHTML='<td>'+score+'</td>';
    tra.appendChild(scoretd);
  });
  if (ss.ascores.length<6 && ss.bscores.length<6){
    for (let i=0;i<6-ss.ascores.length;i++){
      let scoretd=document.createElement('td');
      tra.appendChild(scoretd);
    }
  }else if (ss.bscores.length>ss.ascores.length){
    for (let i=0;i<ss.bscores.length-ss.ascores.length;i++){
      let scoretd=document.createElement('td');
      tra.appendChild(scoretd);
    }
  }
  let scoretd=document.createElement('td');
  scoretd.innerHTML='<td>'+ss.atot+'</td>';
  tra.appendChild(scoretd);

  tra=document.createElement('tr');
  tra.classList.add('subrow');
  tbl.appendChild(tra);
  th=document.createElement('th');
  th.innerHTML='<th>B</th>';
  tra.appendChild(th);

  ss.bscores.forEach((score,ind) =>{
    let scoretdb=document.createElement('td');
    scoretdb.innerHTML='<td>'+score+'</td>';
    tra.appendChild(scoretdb);
  });

  if (ss.bscores.length<6 && ss.ascores.length<6){
    for (let i=0;i<6-ss.bscores.length;i++){
      let scoretd=document.createElement('td');
      tra.appendChild(scoretd);
    }
  }else if (ss.ascores.length>ss.bscores.length){
    for (let i=0;i<ss.ascores.length-ss.bscores.length;i++){
      let scoretd=document.createElement('td');
      tra.appendChild(scoretd);
    }
  }

  let scoretdb=document.createElement('td');
  scoretdb.innerHTML='<td>'+ss.btot+'</td>';
  tra.appendChild(scoretdb);

  let trr = document.createElement('tr');
  trr.classList.add('racenums');
  tbl.appendChild(trr)

  let rtd = document.createElement('td');
  rtd.innerHTML='<td>Div</td>';
  trr.appendChild(rtd);

  for (let i=0;i<Math.max(ss.ascores.length,ss.bscores.length);i++){
    rtd = document.createElement('td');
    rtd.innerHTML='<td>R'+(i+1)+'</td>';
    trr.appendChild(rtd);
  }
  rtd=document.createElement('td');
  rtd.innerHTML='<td>Tot</td>';
  trr.appendChild(rtd);
}
