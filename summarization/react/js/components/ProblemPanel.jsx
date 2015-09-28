var React = require('react');
var ReactPropTypes = React.PropTypes;
var ProblemCloud = require('./ProblemCloud.jsx');
var ProblemSummary = require('./ProblemSummary.jsx');

var ProblemPanel = React.createClass({

  propTypes: {
    problems: ReactPropTypes.object.isRequired,
    problemSummaries: ReactPropTypes.array.isRequired
  },

  render: function() {
    return (
      <div className="row row-content problem-panel">
        <ProblemCloud problems={this.props.problems} />
        <ProblemSummary problemSummaries={this.props.problemSummaries} />
      </div>
    );
  },
});

module.exports = ProblemPanel;
