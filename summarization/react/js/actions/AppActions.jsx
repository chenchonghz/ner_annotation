var AppDispatcher = require('../dispatcher/AppDispatcher.jsx');
var AppConstants = require('../constants/AppConstants.jsx');

var AppActions = {
  updateProblemsFilter: function(problems) {
    AppDispatcher.dispatch({
      actionType: AppConstants.PROBLEM_FILTER_UPDATE,
      problems: problems
    })
  },

  updateTimelineFilter: function(extent) {
    AppDispatcher.dispatch({
      actionType: AppConstants.TIMELINE_FILTER_UPDATE,
      extent: extent
    })
  },

  updatePatientSelection: function(selected) {
    AppDispatcher.dispatch({
      actionType: AppConstants.PATIENT_SELECTION_UPDATE,
      selected: selected
    })
  },

  updateNoteSelection: function(selected) {
    AppDispatcher.dispatch({
      actionType: AppConstants.NOTE_SELECTION_UPDATE,
      selected: selected
    })
  },

  updateSelectedProblemCategory: function(category) {
    AppDispatcher.dispatch({
      actionType: AppConstants.SELECTED_PROBLEM_CATEGORY_UPDATE,
      category: category
    })
  }
};

module.exports = AppActions;