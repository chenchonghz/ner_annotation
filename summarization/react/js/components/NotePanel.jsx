var React = require('react');
var ReactPropTypes = React.PropTypes;
var NoteList = require('./NoteList.jsx');
var NoteDetail = require('./NoteDetail.jsx');

var NotePanel = React.createClass({

  propTypes: {
    notes: ReactPropTypes.object.isRequired,
    filter: ReactPropTypes.object.isRequired,
    highlights: ReactPropTypes.object.isRequired
  },

  render: function() {
    return (
      <div className="row row-content notes">
        <NoteList notes={this.props.notes} filter={this.props.filter} highlights={this.props.highlights} />
        <NoteDetail notes={this.props.notes} filter={this.props.filter} highlights={this.props.highlights} />
      </div>
    );
  }
});

module.exports = NotePanel;
