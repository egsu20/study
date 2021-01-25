var List = {
  setColor:function (color){
    /*var li = document.querySelectorAll('li');
    var li_a = document.querySelectorAll('li a');
    var i = 0;
    while( i < li_a.length){
          li[i].style.color=color;
          li_a[i].style.color=color;
          i++;
      }*/
    $('li').css('color', color);
    $('li a').css('color', color);
  }
}

var Body = {
  setColor:function(color){
    //document.querySelector('body').style.color=color;
    $('body').css('color', color);
  },
  setBackgroundColor:function(color){
    //document.querySelector('body').style.backgroundColor=color;
    $('body').css('backgroundColor', color);
  }
}

function nightDayHandler(self){
  var title = document.querySelector('h1 a');

  if(self.value === 'night') {
    self.value = 'day';
    Body.setBackgroundColor('black');
    Body.setColor('white');
    title.style.color='rgb(74, 183, 197)';
    List.setColor('powderblue');
  } else {
    Body.setBackgroundColor('white');
    Body.setColor('black');
    self.value = 'night';
    title.style.color='rgb(206, 78, 120)';
    List.setColor('palevioletred');
  }
}