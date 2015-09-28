var React = require('react');
var ReactPropTypes = React.PropTypes;
var Note = require('./Note.jsx');
var Highlight = require('react-highlighter');
var AppActions = require('../actions/AppActions.jsx');


function highlight(text, keywordsDict, targetProblem){
  if (text === undefined) {
    return "";
  }
  if (keywordsDict === undefined) {
    return text;
  }

  colorCode = {
    'active':'#FF9DFF',
    'inactive': '#FFFFFF' /*'#FFE1FF'*/
  }

  var highlightedText = text;
  
  for (var key in keywordsDict){
    var status = 'inactive';
    if (keywordsDict[key].indexOf(targetProblem) != -1){
      status = 'active';
    /*}*/
      var re = new RegExp(key,"g");

      highlightedText = highlightedText.replace(re,
          ["<mark style=\"background-color:",colorCode[status],";\">",key,"</mark>"].join('')
          );
    }
  }

  return highlightedText;
}

var NoteDetail = React.createClass({
  
  propTypes: {
    notes: ReactPropTypes.object.isRequired,
    filter: ReactPropTypes.object.isRequired,
    highlights: ReactPropTypes.object.isRequired
  },

  preNote: function(active) {
    return function() {  
      if (active > 1){   
        AppActions.updateNoteSelection(active-1);
      }
    }
  },
  nextNote: function(active,totalLen) {
    return function() { 
      if (active < totalLen){    
        AppActions.updateNoteSelection(active+1);
      }
    }
  },

  render: function() {
    var T = this.props.notes.notes;
    var A = this.props.notes.active;
    var F = this.props.filter;
    var H = this.props.highlights;

    var D = T[0];
    for (var i = T.length - 1; i >= 0; i--) {
      if (T[i].id === A){
        D = T[i];
      }
    };

    return (
      <div className="col-md-6 panel-right">
        <div className="column-content note-detail">
          <div className="panel-title">
            <div className="panel-title-text">
              病历信息
              <img className="info-button" src="/images/info.png" data-toggle="tooltip" data-placement="right" title="此处将显示在“病程记录列表”中选中的病历或病程记录的详细内容。其中，与所选取的诊断或病症相关的信息将会用粉红色自动高亮。" />
            </div>
          </div>
          <div className="panel-content">
            <p className="note-nav-button"><a onClick={this.preNote(active=this.props.notes.active)}>&lt;前一份</a>&nbsp;&nbsp;&nbsp;&nbsp;<a onClick={this.nextNote(active=this.props.notes.active, totalLen=T.length)}>后一份&gt;</a>&nbsp;&nbsp;&nbsp;&nbsp;{ D.date }</p>
            <hr className='content-hr'></hr>
            <h4><strong>基本信息 </strong></h4>
            <p>{this.props.notes.demographic}</p>
            <hr></hr>
            <div dangerouslySetInnerHTML={{__html:highlight(text=D.content,keywordsDict=H,targetProblem=F.problems[0])}} />
            <hr></hr>
          </div>
        </div>
      </div>
    );
  }
});

module.exports = NoteDetail;
