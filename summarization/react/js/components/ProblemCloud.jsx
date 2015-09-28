var React = require('react');
var AppActions = require('../actions/AppActions.jsx');
var ReactPropTypes = React.PropTypes;
var $ = require('jquery');
global.jQuery = $;
var jQCloud = require('jqcloud-npm');

var ProblemCloud = React.createClass({

  propTypes: {
    problems: ReactPropTypes.object.isRequired
  },

  render: function() {
    var problemDOMs = [];
    var problems = this.props.problems.problems[this.props.problems.selectedCategory];
    for (var i = 0; i < problems.length; ++i) {
      problemDOMs.push(<div className="problem-word" ref={problems[i]} style={{}} onClick={this.updateProblem(problems[i])}>{problems[i]}</div>)
    }
    var categories = ['main', 'other'];
    var selectedText = {
      'main': '主诉病症',
      'other': '其他病症'
    };
    var tabDOMs = [];
    for (var i = 0; i < categories.length; ++i) {
      if (this.props.problems.selectedCategory === categories[i]) {
        tabDOMs.push(<div className="problem-cloud-tab active" ref={categories[i]} onClick={this.updateSelectedCategory(i)}>{selectedText[categories[i]]}</div>);
      } else {
        tabDOMs.push(<div className="problem-cloud-tab" ref={categories[i]} onClick={this.updateSelectedCategory(i)}>{selectedText[categories[i]]}</div>);
      }
    }

    return (
      <div className="col-md-6 panel-left">
        <div className="column-content problem-cloud">
          <div className="panel-title">
            <div className="panel-title-text">
              病症群
              <img className="info-button" src="/images/info.png" data-toggle="tooltip" data-placement="right" title="此处将显示该病人所有的主诉症状和主要诊断，并且将显示所有根据病人病历自动提取分析而推断出的可能诊断。点击相应诊断后，将自动提取和总结相关的病历内容。" />
            </div>
            {tabDOMs}
          </div>
          <div className="panel-content" ref="cloud">
            {problemDOMs}
          </div>
        </div>
      </div>
    );
  },

  componentDidMount: function() {
    /*
    var words = this.props.problems.map(function(obj, index) {
      return {
        text: obj.problem,
        weight: obj.weight,
        handlers: {
          click: function(event) {
            AppActions.updateProblemsFilter([obj.problem]);
          }
        }
      };
    });
    $(React.findDOMNode(this.refs.cloud)).jQCloud(words, {
      autoResize: true
    });
    */
  },

  componentWillUnmount: function() {
    /*
    $(React.findDOMNode(this.refs.cloud)).jQCloud('destroy');
    */
  },

  deselectAllProblems: function() {
    var problems = this.props.problems.problems[this.props.problems.selectedCategory];
    for (var i = 0; i < problems.length; ++i) {
      $(React.findDOMNode(this.refs[problems[i]])).removeClass('active');
    }
  },

  updateProblem: function(problem) {
    var that = this;
    return function() {
      that.deselectAllProblems();
      $(React.findDOMNode(that.refs[problem])).addClass('active');
      AppActions.updateProblemsFilter([problem]);
    }
  },

  deselectAllCategories: function() {
    var categories = ['main', 'other'];
    for (var i = 0; i < categories.length; ++i) {
      $(React.findDOMNode(this.refs[categories[i]])).removeClass('active');
    }
  },

  updateSelectedCategory: function(index) {
    var that = this;
    var categories = ['main', 'other'];
    return function() {
      that.deselectAllCategories();
      $(React.findDOMNode(that.refs[categories[index]])).addClass('active');
      AppActions.updateSelectedProblemCategory(categories[index]);
    }
  }
});

module.exports = ProblemCloud;
