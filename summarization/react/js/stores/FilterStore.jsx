var AppDispatcher = require('../dispatcher/AppDispatcher.jsx');
var EventEmitter = require('events').EventEmitter;
var AppConstants = require('../constants/AppConstants.jsx');
var assign = require('object-assign');

var CHANGE_EVENT = 'change';

var _filter = {
  'timeline': {
    'start': new Date('2010-01-23 02:15:23'),
    'end': new Date('2025-05-22 08:22:09')
  },
  'problems': [
  ]
};

function updateProblems(problems) {
  _filter['problems'] = problems;
}

function updateTimelineExtent(extent) {
  _filter['timeline'] = {
    'start': extent[0],
    'end': extent[1]
  }
}

var FilterStore = assign({}, EventEmitter.prototype, {

  getAll: function() {
    return _filter;
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
    case AppConstants.PROBLEM_FILTER_UPDATE:
      updateProblems(action.problems);
      FilterStore.emitChange();
      break;

    case AppConstants.TIMELINE_FILTER_UPDATE:
      updateTimelineExtent(action.extent);
      FilterStore.emitChange();

    default:
      // no op
  }
});

module.exports = FilterStore;