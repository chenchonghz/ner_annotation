var React = require('react');
var ReactPropTypes = React.PropTypes;
var Note = require('./Note.jsx');
var Highlight = require('react-highlighter');
var AppActions = require('../actions/AppActions.jsx');
var $ = require('jquery');
global.jQuery = $;



function highlight(text, keywordsDict, targetProblem){
  if (text === undefined) {
    return "";
  }
  if (keywordsDict === undefined) {
    return text;
  }

  colorCode = {
    'active':'#FF9DFF',
    'inactive': '#F2F2F2'/*'#FFE1FF'*/
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


function convert2ISODate(dateInString, oriFormat){
  oriFormat = typeof oriFormat !== 'undefined' ? oriFormat : 'NoteDate';
  if (oriFormat == 'NoteDate'){
    return Date.parse(dateInString.replace(' ', 'T'));
  }
  else{
    throw 'Invalid format';
  }
}

function filterNoteList(oriNoteList, filter) {
  var p_filteredNoteList = [];
  var pd_filteredNoteList = [];
  //filter problem
  if (filter.problems.length !== 0){
    for (var j = 0; j < oriNoteList.length; ++j){
      for (var i = 0; i < filter.problems.length ; ++i) {
        if ((oriNoteList[j].problems.indexOf(String(filter.problems[i])) >= 0 )){
          p_filteredNoteList.push(oriNoteList[j]);
          break;
        }
      };
    };
  }
  else{
    p_filteredNoteList = oriNoteList;
  }
  //filter date
  for (var i = 0; i < p_filteredNoteList.length; ++i) {
    if((convert2ISODate(p_filteredNoteList[i].date) >= Date.parse(filter.timeline.start))
      && (convert2ISODate(p_filteredNoteList[i].date) <= Date.parse(filter.timeline.end))){
      pd_filteredNoteList.push(p_filteredNoteList[i]);
    }
  }
  return pd_filteredNoteList;
}



var NoteList = React.createClass({

  propTypes: {
    notes: ReactPropTypes.object.isRequired,
    filter: ReactPropTypes.object.isRequired,
    highlights: ReactPropTypes.object.isRequired
  },


  render: function() {

    var T = this.props.notes.notes;
    var F = this.props.filter;
    var H = this.props.highlights;
    var filteredT = filterNoteList(T, F);
    
    var noteDOMs = [];


    for (var i = 0; i < filteredT.length; ++i) {
      currT = filteredT[i]
      
      var content = "内容 - "+highlight(currT.content.substring(0,70).replace(/<br>/g,'').concat('...'),H,F.problems[0]);

      noteDOMs.push(
                    <tr>
                     <td className='note-element' ref={currT.id} onClick={this.updateNote(currT.id,T.length)}>
                      <strong>{currT.title} </strong>&nbsp;&nbsp; {currT.date}
                      <dd>
                        <div dangerouslySetInnerHTML={{__html:content}} />
                      </dd>
                     </td>
                    </tr>
                    );
    }
    return (
      <div className="col-md-6 panel-left">
        <div className="column-content note-list">
          <div className="panel-title">
            <div className="panel-title-text">
              病程记录列表
              <img className="info-button" src="/images/info.png" data-toggle="tooltip" data-placement="right" title="此处列出病人的相关病程记录或病历。点击“病症群”中的相关诊断后，此处将只显示包含该诊断相关信息的病历，并且高亮其中的相关信息。在此栏可以选择查看具体的病历，选中的病历将在“病历信息”中显示。" />
            </div>
          </div>
          <div className="panel-content">
            <table className="table table-bordered table-hover">
              <tbody>
                {noteDOMs}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    );
  },

  componentDidMount: function() {

  },

  componentWillUnmount: function() {

  },

  deselectAllNotes: function(length) {
    for (var i = 1; i <= length; i++) {
      $(React.findDOMNode(this.refs[i])).removeClass('active');
    }
  },
  updateNote: function(noteIndex,length) {
    var that = this;
    return function() {
      that.deselectAllNotes(length);
      $(React.findDOMNode(that.refs[noteIndex])).addClass('active');
      AppActions.updateNoteSelection(noteIndex);
    }
  },
});


module.exports = NoteList;
