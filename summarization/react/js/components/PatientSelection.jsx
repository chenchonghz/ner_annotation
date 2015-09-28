var React = require('react');
var AppActions = require('../actions/AppActions.jsx');
var ReactPropTypes = React.PropTypes;

function selectPatient(i) {
  return function() {
    AppActions.updatePatientSelection(i);
  }
}

var PatientSelection = React.createClass({

  propTypes: {
    patients: ReactPropTypes.object.isRequired
  },

  render: function() {
    var selected = this.props.patients.selected;
    var patientTabs = this.props.patients.patients.map(function(patient, i) {
      if (i === selected) {
        return <div className="patient-tab selected" onClick={selectPatient(i)}>{patient}</div> 
      } else {
        return <div className="patient-tab" onClick={selectPatient(i)}>{patient}</div> 
      }
    });
    return (
      <div className="patient-selection">
          {patientTabs}
      </div>
    );
  }
});

module.exports = PatientSelection;
