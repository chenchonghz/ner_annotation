var React = require('react');
var $ = require('jquery');
global.jQuery = $;
var bootstrap = require('bootstrap');
var PatientSelection = require('./PatientSelection.jsx');
var Timeline = require('./Timeline.jsx');
var ProblemPanel = require('./ProblemPanel.jsx');
var NotePanel = require('./NotePanel.jsx');
var NoteStore = require('../stores/NoteStore.jsx');
var ProblemStore = require('../stores/ProblemStore.jsx');
var ProblemSummaryStore = require('../stores/ProblemSummaryStore.jsx');
var FilterStore = require('../stores/FilterStore.jsx');
var PatientStore = require('../stores/PatientStore.jsx');
var HighlightStore = require('../stores/HighlightStore.jsx');

function getAppState() {
  return {
    notes: NoteStore.getAll(),
    problems: ProblemStore.getAll(),
    problemSummaries: ProblemSummaryStore.getAll(),
    filter: FilterStore.getAll(),
    patients: PatientStore.getAll(),
    highlights: HighlightStore.getAll()
  };
}

var SummarizationApp = React.createClass({
  getInitialState: function() {
    return getAppState();
  },

  componentDidMount: function() {
    NoteStore.addChangeListener(this._onChange);
    ProblemStore.addChangeListener(this._onChange);
    ProblemSummaryStore.addChangeListener(this._onChange);
    FilterStore.addChangeListener(this._onChange);
    PatientStore.addChangeListener(this._onChange);
    HighlightStore.addChangeListener(this._onChange);

    $(function () {
      $('[data-toggle="tooltip"]').tooltip()
    });
  },

  componentWillUnmount: function() {
    NoteStore.removeChangeListener(this._onChange);
    ProblemStore.removeChangeListener(this._onChange);
    ProblemSummaryStore.removeChangeListener(this._onChange);
    FilterStore.removeChangeListener(this._onChange);
    PatientStore.removeChangeListener(this._onChange);
    HighlightStore.removeChangeListener(this._onChange);
  },

  render: function() {
    console.log(this.state.notes.active);
    var problemSummaries = [];
    if (this.state.filter.problems.length > 0) {
      problemSummaries = this.state.problemSummaries[this.state.filter.problems[0]];
    }
    return (
      <div>
        <PatientSelection patients={this.state.patients} />
        <div className="container-fluid patient-detail">
          <Timeline notes={this.state.notes} />
          <ProblemPanel problems={this.state.problems} problemSummaries={problemSummaries} />
          <NotePanel notes={this.state.notes} filter={this.state.filter} highlights={this.state.highlights} />
        </div>
      </div>
    );
  },

  _onChange: function() {
    this.setState(getAppState());
  }
});

module.exports = SummarizationApp;
