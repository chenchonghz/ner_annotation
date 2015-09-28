var React = require('react');
var ReactPropTypes = React.PropTypes;
var $ = require('jquery');

function logout() {
  $.ajax({
    type: 'POST',
    url: 'logout',
    success: function(data, status) {
      window.location.href = "/";
    }
  });
}

var Navbar = React.createClass({

  propTypes: {
    isLandingPage: ReactPropTypes.bool.isRequired
  },

  render: function() {
    var accountInfo = null;
    if (!this.props.isLandingPage) {
      accountInfo = (
        <div className="nav-buttons">
          <div className="account-button" onMouseLeave={this.hideDropdown}>
            <div className="account-name" onMouseOver={this.showDropdown}>
              医生：许南方
            </div>
            <div className="account-dropdown" ref="accountDropdown">
              <ul>
                <div className="item" onClick={logout}>登出</div>
              </ul>
            </div>
          </div>
          <div className="help-button" data-toggle="modal" data-target="#helpModal">
            帮助
          </div>
        </div>
      );
    };
    return (
      <div className="app-header">
        <img src="/images/banner.png" />
        {accountInfo}
      </div>
    );
  },

  showDropdown: function() {
    $(React.findDOMNode(this.refs.accountDropdown)).addClass('active');
  },

  hideDropdown: function() {
    $(React.findDOMNode(this.refs.accountDropdown)).removeClass('active');
  }
});

module.exports = Navbar;
