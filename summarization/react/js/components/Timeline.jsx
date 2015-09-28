var React = require('react');
var AppActions = require('../actions/AppActions.jsx');
var ReactPropTypes = React.PropTypes;
var d3Timeline = require('../misc/timeline.jsx');

function onBrush(brush) {
  return function() {
    AppActions.updateTimelineFilter(brush.extent());
  };
}

var Timeline = React.createClass({

  propTypes: {
    notes: ReactPropTypes.object.isRequired
  },

  render: function() {
    return (
      <div className="row row-content">
        <div className="col-md-12">
          <div className="column-content timeline">
            <div className="panel-title">
              <div className="panel-title-text">
                病历时间一览
                <img className="info-button" src="/images/info.png" data-toggle="tooltip" data-placement="right" title="此处将显示此病人所有病历或病程记录的时间点，并且可以通过拖曳选择关注的时间范围。选择之后，“病程记录列表”中将显示相应的记录。" />
              </div>
              <div className="zoom-icons">
                <img className="zoom-icon" src="/images/zoom-out.png" />
                <img className="zoom-icon" src="/images/zoom-in.png" />
              </div>
            </div>
            <div className="panel-content">
            </div>
          </div>
        </div>
      </div>
    );
  },

  componentDidMount: function() {
    d3Timeline.drawTimeline(this.props.notes.notes, this.props.notes.active, onBrush);
  },

  componentWillUnmount: function() {
  },

  componentDidUpdate: function() {
    d3Timeline.updateActiveNote(this.props.notes.active);
  }
});

module.exports = Timeline;
