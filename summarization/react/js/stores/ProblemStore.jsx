var AppDispatcher = require('../dispatcher/AppDispatcher.jsx');
var EventEmitter = require('events').EventEmitter;
var AppConstants = require('../constants/AppConstants.jsx');
var assign = require('object-assign');

var CHANGE_EVENT = 'change';

/*
var _problems = [
  {
    problem: "恶心",
    weight: 0.7
  },
  {
    problem: "呕吐",
    weight: 0.5
  },
  {
    problem: "腹痛",
    weight: 0.6
  },
  {
    problem: "感冒",
    weight: 0.4
  },
  {
    problem: "咳嗽",
    weight: 0.3
  }
];
*/

var _problems = {
  'selectedCategory': 'other',
  'problems': {
    'main': [
      '吞咽困难',
      '食道恶性肿瘤'
    ],
    'other': [
      '心梗',
      '感染',
      '高血压病',
      '糖尿病',
      '肺炎',
      '肺不张'
    ]
  }
}

function updateSelectedProblemCategory(category) {
  _problems['selectedCategory'] = category;
}

var ProblemStore = assign({}, EventEmitter.prototype, {

  getAll: function() {
    return _problems;
  },

  emitChange: function() {
    this.emit(CHANGE_EVENT);
  },

  addChangeListener: function(callback) {
    this.on(CHANGE_EVENT, callback);
  },

  removeChangeListener: function(callback) {
    this.removeListener(CHANGE_EVENT, callback);
  }
});

AppDispatcher.register(function(action) {
  switch(action.actionType) {
    case AppConstants.SELECTED_PROBLEM_CATEGORY_UPDATE:
      updateSelectedProblemCategory(action.category);
      ProblemStore.emitChange();
      break;

    default:
      // no op
  }
});

module.exports = ProblemStore;