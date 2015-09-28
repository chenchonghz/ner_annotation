var React = require('react');
var $ = require('jquery');

function login() {
  $.ajax({
    type: 'POST',
    url: 'login',
    success: function(data, status) {
      window.location.href = "patients";
    }
  });
}

var Welcome = React.createClass({
  render: function() {
    return (
      <div className="welcome">
        <div className="welcome-message">
          欢迎使用舶众病历本
        </div>
        <div className="button raised" onClick={login}>
          体验账号登陆
        </div>
      </div>
    );
  }
});

module.exports = Welcome;
