var AppDispatcher = require('../dispatcher/AppDispatcher.jsx');
var EventEmitter = require('events').EventEmitter;
var AppConstants = require('../constants/AppConstants.jsx');
var assign = require('object-assign');

var CHANGE_EVENT = 'change';

var _patients = {
  'selected': 0,
  'patients': [
    '病人一',
    '病人二',
    '病人三'
  ]
};

function updateSelected(selected) {
  _patients['selected'] = selected;
}

var PatientStore = assign({}, EventEmitter.prototype, {

  getAll: function() {
    return _patients;
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
    case AppConstants.PATIENT_SELECTION_UPDATE:
      updateSelected(action.selected);
      PatientStore.emitChange();
      break;

    default:
      // no op
  }
});

module.exports = PatientStore;