console.log("this is a digital clock.")

d = new Date();
hrs = d.getHours();
min = d.getMinutes();
sec = d.getSeconds();
console.log(hrs+":"+min+":"+sec);


setInterval(() => {
    let d = new Date();
    document.getElementById('time').innerHTML = d.getHours()+":"+d.getMinutes()+":"+d.getSeconds();

}, 10);


var weekday = new Array(7);
weekday[0] = 'January';
weekday[1] = 'February';
weekday[2] = 'March';
weekday[3] = 'April';
weekday[4] = 'May';
weekday[5] = 'June';
weekday[6] = 'July';
weekday[6] = 'August';
weekday[6] = 'September';
weekday[6] = 'October';
weekday[6] = 'November';
weekday[6] = 'December';
var month = weekday[d.getMonth()];


var weekday = new Array(7);
weekday[0] = 'Sunday';
weekday[1] = 'Monday';
weekday[2] = 'Tuesday';
weekday[3] = 'Wednesday';
weekday[4] = 'Thursday';
weekday[5] = 'Friday';
weekday[6] = 'Saturday';
var day = weekday[d.getDay()];




document.getElementById('date').innerHTML = d.getDate()+"-"+ month +"-"+d.getFullYear()+" / "+day;
// document.getElementById('day').innerHTML = n;


function showNhide() {
  var x = document.getElementById("cities");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

document.getElementById('btn').addEventListener('click',function ShowAndHide() {
    var x = document.getElementById("cities");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
})