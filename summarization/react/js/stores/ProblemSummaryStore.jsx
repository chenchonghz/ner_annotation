var AppDispatcher = require('../dispatcher/AppDispatcher.jsx');
var EventEmitter = require('events').EventEmitter;
var AppConstants = require('../constants/AppConstants.jsx');
var assign = require('object-assign');

var CHANGE_EVENT = 'change';

var _problemSummaries = {
  '吞咽困难': [
    {
      'summary': '进行性吞咽困难2月。当地医院：食管喷门癌；中国科学医学院肿瘤医院：食管下段癌，食管癌，食管胸下段癌; 食管癌',
      'noteIndex': 1
    },
    {
      'summary': '原发性食管喷门癌',
      'noteIndex': 1
    },
    {
      'summary': '2月26日，食管恶性肿瘤',
      'noteIndex': 2
    },
    {
      'summary': '3月5日，左开胸食管癌切除术，弓上吻合术。食管恶性肿瘤。常规抗炎补液抑酸化',
      'noteIndex': 4
    }
  ],
  '食道恶性肿瘤': [
    {
      'summary': '进行性吞咽困难2月。当地医院：食管喷门癌；中国科学医学院肿瘤医院：食管下段癌，食管癌，食管胸下段癌; 食管癌',
      'noteIndex': 1
    },
    {
      'summary': '原发性食管喷门癌',
      'noteIndex': 1
    },
    {
      'summary': '2月26日，食管恶性肿瘤',
      'noteIndex': 2
    },
    {
      'summary': '3月5日，左开胸食管癌切除术，弓上吻合术。食管恶性肿瘤。常规抗炎补液抑酸化',
      'noteIndex': 4
    }
  ],
  '心梗': [
    {
      'summary': '高血压病史20年，替米沙坦2片QD',
      'noteIndex': 1
    },
    {
      'summary': '糖尿病病史5年，二甲双胍itd，格列齐特qd',
      'noteIndex': 1
    },
    {
      'summary': '窦性心律过缓，无心脏病史',
      'noteIndex': 1
    },
    {
      'summary': '2月28日血压150-200/80-90mmHg，硝苯地平片，欠佳',
      'noteIndex': 3
    },
    {
      'summary': '3月6日血压145/70mmHg',
      'noteIndex': 5
    },
    {
      'summary': '3月7日心律120，气促，喘憋，体温38.0，脉搏120，呼吸20，血压120/70，喘憋貌，双肺呼吸音粗，广泛哮鸣音',
      'noteIndex': 6
    }
  ],
  '感染': [
    {
      'summary': '3月5日左开胸食管癌切除术、弓上吻合术，抗炎补液抑酸化痰',
      'noteIndex': 4
    },
    {
      'summary': '3月6日体温正常；胸引100ml',
      'noteIndex': 5
    },
    {
      'summary': '3月7日晨心律120次/分，体温38度，血压120/70mmHg',
      'noteIndex': 6
    }
  ],
  '高血压病': [
    {
      'summary': '高血压病史20年，替米沙坦2片QD。无心脏病史。无脑血管疾病',
      'noteIndex': 1
    },
    {
      'summary': '2月28日，血压150-200/80-90mmHg，硝苯地平片，缓解，欠佳',
      'noteIndex': 3
    },
    {
      'summary': '2月28日，血压160/86mmHg，心律70次/分；睡眠质量较差，精神紧张；170mmHg，硝苯地平片，160mmHg以下，停心电监护，舒乐安定改善睡眠',
      'noteIndex': 3
    },
    {
      'summary': '3月6日，血压145/70mmHg',
      'noteIndex': 5
    },
    {
      'summary': '3月7日，血压120/70mmHg',
      'noteIndex': 6
    }
  ],
  '糖尿病': [
    {
      'summary': '2月25日，糖尿病病史5年，二甲双胍tid，格列齐特qd',
      'noteIndex': 1
    }
  ],
  '肺炎': [
    {
      'summary': '2月25日，双侧清音，双侧呼吸正常，无湿罗音，无哮鸣音，无胸膜摩擦音',
      'noteIndex': 1
    },
    {
      'summary': '3月5日，抗炎补液抑酸化痰',
      'noteIndex': 4
    },
    {
      'summary': '3月7日，气促，喘憋，呼吸20次/分，憋喘貌，双肺呼吸音粗，广泛哮鸣音',
      'noteIndex': 6
    }
  ],
  '肺不张': [
    {
      'summary': '2月25日，双侧清音，双侧呼吸正常，无湿罗音，无哮鸣音，无胸膜摩擦音',
      'noteIndex': 1
    },
    {
      'summary': '3月5日，抗炎补液抑酸化痰',
      'noteIndex': 4
    },
    {
      'summary': '3月7日，气促，喘憋，呼吸20次/分，憋喘貌，双肺呼吸音粗，广泛哮鸣音',
      'noteIndex': 6
    }
  ]
}

var ProblemSummaryStore = assign({}, EventEmitter.prototype, {

  getAll: function() {
    return _problemSummaries;
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
});

module.exports = ProblemSummaryStore;