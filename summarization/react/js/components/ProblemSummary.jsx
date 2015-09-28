var React = require('react');
var AppActions = require('../actions/AppActions.jsx');
var ReactPropTypes = React.PropTypes;

var ProblemSummary = React.createClass({

  propTypes: {
    problemSummaries: ReactPropTypes.array.isRequired
  },

  render: function() {
    var summaryEntries = []
    for (var i = 0; i < this.props.problemSummaries.length; ++i) {
      summaryEntries.push(<div className="summary-entry" onClick={this.updateNoteSelection(this.props.problemSummaries[i].noteIndex)}><div className="summary-text">{(i + 1) + '. ' + this.props.problemSummaries[i].summary}</div><img className="summary-link" src="/images/link.png" /></div>)
    }
    return (
      <div className="col-md-6 panel-right">
        <div className="column-content problem-cloud">
          <div className="panel-title">
            <div className="panel-title-text">
              相关病症总结
              <img className="info-button" src="/images/info.png" data-toggle="tooltip" data-placement="right" title="此处将总结病人病史之中所有和所选诊断或病症相关的信息。总结的依据来自于对应病历的相关内容。点击总结的条目，可以找到该条目来源的病历。" />
            </div>
          </div>
          <div className="panel-content" ref="cloud">
            <ol>
              {summaryEntries}
            </ol>
          </div>
        </div>
      </div>
    );
  },

  updateNoteSelection: function(noteIndex) {
    return function() {
      AppActions.updateNoteSelection(noteIndex);
    }
  }
});

module.exports = ProblemSummary;
