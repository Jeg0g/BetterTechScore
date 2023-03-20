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
const hiddens =[];
const isHidden = [];
const penalties=["OCS","DSQ","DNF","DNS"]
const nonpens=["RDG","BKD"]
const scoreSets=[]
$(document).ready(function(){
  let files;
  $.ajax({
    type: 'GET',
    url: '/staticFiles/data/files.json',
    async: false,
    beforeSend: (xhr) => {
      if (xhr && xhr.overrideMimeType) {
        xhr.overrideMimeType('application/json;charset=utf-8');
      }
    },
    dataType: 'json',
    success: (data) => {
      files=data.names.slice(1,data.names.length-1).split(",");
    }
  });
  files.forEach(function(filename,ind){
    let testscore;
    $.ajax({
      type: 'GET',
      url: '/staticFiles/data/'+filename+'.json',
      async: false,
      beforeSend: (xhr) => {
        if (xhr && xhr.overrideMimeType) {
          xhr.overrideMimeType('application/json;charset=utf-8');
        }
      },
      dataType: 'json',
      success: (data) => {
        testscore = new ScoreSet(data.rank,data.name,data.imgpath,data.ascores.slice(1,data.ascores.length-1).split(","),data.bscores.slice(1,data.bscores.length-1).split(","),data.totscore,data.atot,data.btot);
      }
    });
    scoreSets.push(testscore);
  });
  sortedScoreSets=scoreSets.sort(function(a, b){return a.atot - b.atot});
  sortedScoreSets.forEach(function(ss,ind){
    ss.rank=ind+1;
  })
  sortedScoreSets.forEach(function(ss,ind){
    constructRow(ss);
  })
  $('#scores').find('.row').click( function(){
    let rank=$(this).find('.rank')[0];
    console.log(rank.innerHTML);
    let d = rank.innerHTML;

    if (isHidden[d]){
      $('#scores').find('#div'+d)[0].classList.add("open");
      isHidden[d]=false;
    }else{
      $('#scores').find('#div'+d)[0].classList.remove("open");
      isHidden[d]=true;
    }
  });
});
function constructRow(ss){
  const scoreTable=$('#scores')[0];
  hiddens.splice(ss.rank,0, '#div'+ss.rank);
  isHidden.splice(ss.rank,0, true);
  // scoreTable.insertRow($('.rows').length);
  let row =document.createElement('div');
  scoreTable.appendChild(row);
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
  td.innerHTML = '<td>'+ss.atot+'</td>';
  td.classList.add("totalscore");
  row.appendChild(td);

  hrow = document.createElement('div')
  scoreTable.appendChild(hrow);
  hrow.classList.add("hiddenrow");
  hrow.classList.add("AB");
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
    if (penalties.includes(score)){
      scoretd.classList.add("penalty");
    }else if (nonpens.includes(score)){
      scoretd.classList.add("nonpen");
    }
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
  scoretd.classList.add("boo");
  tra.appendChild(scoretd);

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
  if (Math.max(ss.ascores.length,ss.bscores.length)<6){
    for (let i=0;i<6-Math.max(ss.ascores.length,ss.bscores.length);i++){
      rtd = document.createElement('td');
      rtd.innerHTML='<td></td>';
      trr.appendChild(rtd);
    }
  }

  rtd=document.createElement('td');
  rtd.innerHTML='<td>Tot</td>';
  trr.appendChild(rtd);
}
