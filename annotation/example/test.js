var $ = require('jquery');

var content = '210名胖子里只有一个能减肥成功，所以FDA新规要将肥胖扼杀在摇篮里'

$('.annotation-editor').append('<div class="text" id="text-' + 0 + '">' + content[0] + '</div>');
for (var i = 1; i < content.length; ++i) {
  $('.annotation-editor').append('<div class="separator" id="separator-' + (i - 1) + '"></div>' + '<div class="text" id="text-' + i + '">' + content[i] + '</div>');
}

var pos = 0;
$('#separator-' + pos).addClass('active');

function moveCursorTo(newPos) {
  $('#separator-' + pos).removeClass('active');
  pos = newPos;
  $('#separator-' + pos).addClass('active');
}

function moveCursorToHandler(newPos) {
  return function() {
    moveCursorTo(newPos);
  }
}

for (var i = 0; i < content.length - 1; ++i) {
  $('#separator-' + i).click(moveCursorToHandler(i));
}

for (var i = 0; i < content.length - 1; ++i) {
  $('#text-' + i).click(moveCursorToHandler(i));
}

function moveCursor(direction) {
  var newPos = pos + direction;
  if (newPos >= content.length - 1) {
    newPos = content.length - 2;
  }
  if (newPos < 0) {
    newPos = 0;
  }
  moveCursorTo(newPos);
}

function setSeparator(state) {
  if (state === true) {
    $('#separator-' + pos).addClass('separated');
  } else {
    $('#separator-' + pos).removeClass('separated');
  }
}

$("body").keydown(function (e) {
  if (e.which === 37) {
    moveCursor(-1);
  } else if (e.which === 39) {
    moveCursor(1);
  } else if (e.which === 32) {
    setSeparator(true);
  } else if (e.which === 8) {
    setSeparator(false);
  }
  e.preventDefault();
});