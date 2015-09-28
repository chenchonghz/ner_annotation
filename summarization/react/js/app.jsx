//require('./materialism.scss');
var React = require('react');
var Router = require('react-router');
var Route = Router.Route
var DefaultRoute = Router.DefaultRoute;
var RouteHandler = Router.RouteHandler;
var Navbar = require('./components/Navbar.jsx');
var Welcome = require('./components/Welcome.jsx');
var SummarizationApp = require('./components/SummarizationApp.jsx');
var HelpModal = require('./components/HelpModal.jsx');

var App = React.createClass({
  render: function() {
    var isLandingPage = window.location.pathname === '/';
    return (
      <div>
        <HelpModal />
        <Navbar isLandingPage={isLandingPage}/>
        <RouteHandler />
      </div>
    )
  }
});

var routes = (
  <Route handler={App}>
    <DefaultRoute handler={Welcome}/>
    <Route path="patients" handler={SummarizationApp}/>
  </Route>
);

Router.run(routes, Router.HistoryLocation, function(Handler) {
  React.render(<Handler/>, document.getElementById('react-mount'));
});