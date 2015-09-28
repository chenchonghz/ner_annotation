var React = require('react');
var ReactPropTypes = React.PropTypes;

var Note = React.createClass({

  propTypes: {
    note: ReactPropTypes.object.isRequired
  },

  render: function() {
    return (
      <div className="note">
        <div className="note-title">
          {this.props.note['title']}
        </div>
      </div>
    );
  }
});

module.exports = Note;
