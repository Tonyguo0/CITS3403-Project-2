

/* javascript making a clock element on the general page of the website */
var clock = document.getElementById("my-clock");

// adds a zero onto the end of a number if less than 10 (makes the clock's look consistent)
function formatZero(n) {
  return (parseInt(n,10) < 10 ? '0' : '') + n;
}

// update the page every second with the new time
function updateTime(){
  var timeNow= new Date(),
  hours = timeNow.getHours(),
  minutes = timeNow.getMinutes(),
  seconds = timeNow.getSeconds(),

  partOfDay = (hours >= 12?'PM':'AM');
  hours = hours % 12 || 12;

  clock.innerHTML = hours + "<span>:</span>" + formatZero(minutes)
                       + "<span>:</span>" + formatZero(seconds) + " " + partOfDay;

  setTimeout(updateTime,1000);
}

updateTime();