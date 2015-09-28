var AppDispatcher = require('../dispatcher/AppDispatcher.jsx');
var EventEmitter = require('events').EventEmitter;
var AppConstants = require('../constants/AppConstants.jsx');
var assign = require('object-assign');

var CHANGE_EVENT = 'change';

var _notes = [
  {
    "id":1,
    "title": "首次病程记录",
    "content": "一、病历特点：\
                1、一般情况：男，慢性病程\
                2、简要病史：进行性吞咽困难2月，1月前于当地医院进行胃镜检查，提示：“食管喷门癌”。随后就诊于中国科学医学院肿瘤医院，行胸部CT提示：“食管下段癌；纵膈、喷门周围多发淋巴结；右肺上叶炎症？双侧胸膜增厚\",随后行胃镜检查，提示：“食管癌”,上消化道造影提示：“食管胸下段癌”，病理回报：“食管（30-45cm），食管分化差的癌”。未行特殊处理。随后就诊于我院，门诊以食管癌收入院，患者自发病来，无咳嗽、咳痰、发热、咳血、喘憋、胸痛、无力，精神良好，饮食良好，睡眠欠佳，大小便正常，体重未见明显减轻。\
                3、高血压病史20年，自服替米沙坦2片QD；糖尿病病史5年，口服二甲双胍tid，格列齐特qd;睡眠较差1年；窦性心律过缓；否认肝炎、结合、疟疾病史，否认心脏病史，否认脑血管疾病、精疾病史，否认手术、外伤、输血史，否认食物、药物过敏史，预防接种史不详。\
                4、查体：心脏正常，双肺正常。口唇无紫绀，气管居中，胸廓外形正常。三凹征无，双侧呼吸动度一致，瘀点一致，叩诊双侧清音，听诊双侧呼吸正常，湿罗音无，固定，哮鸣音无，胸膜摩擦音无。四肢关节无肿痛，无杵状指趾。\
                <br><br>\
                二、诊断及鉴别诊断：\
                1,、食管喷门占位：患者胃镜发现（食管胸下段）占位病变，考虑病变性质为：\
                （1）原发性食管喷门癌：患者老年，男性，胃镜或消化道造影表现，考虑原发性食管喷门癌可能性大；\
                （2）喷门失迟缓症：暂不考虑\
                （3）食管喷门良性狭窄：根据病理结果，可能性小\
                <br><br>\
                三、诊疗计划：\
                1. 完善相关术前检查\
                2. 择期行手术治疗\
                <br><br>\
                主治医师签名：\
                记录者：",
    "problems": ["吞咽困难","食道恶性肿瘤","心梗","高血压病","糖尿病","肺炎","肺不张"],
    "date": "2015-02-25 11:43:00"
  },
  {
    "id":2,
    "title": "查房记录",
    "content": "患者病情平稳，查体：生命体征平稳、神志清、精神可、查体同前。<br>XX副主任医师查房，病史如前，查体同前，诊断为：食管恶性肿瘤 原治疗计划不变。",
    "problems": ["吞咽困难","食道恶性肿瘤"],
    "date": "2015-02-26 07:34:00"
  },
  {
    "id":3,
    "title": "病程记录",
    "content": "患者今日下午至夜间心电监测示血压波动于150-200/80-90mmHg，予硝苯地平片舌下含服缓解欠佳，请心内科会诊，测血压为160/86mmHg，心律70次/分，指示患者目前夜间血压高可能与患者睡眠质量较差、精神紧张相关，收缩压高于170mmHg时可予硝苯地平片临时处理，待患者收缩压稳定于160mmHg以下可停心电监护，必要时可予舒乐安定改善睡眠。遵嘱执行。",
    "problems": ["心梗","高血压病"],
    "date": "2015-02-28 22:41:00"
  },
  {
    "id":4,
    "title": "术后病程",
    "content": "患者2015年3月5日在全麻下行左开胸食管癌切除术、弓上吻合术。手术经过如下：见手术记录。术后诊断：食管恶性肿瘤，目前患者生命体征平稳，返回病房，常规抗炎补液抑酸化痰治疗。术后应该特别注意观察事项：注意监测血压，关注胸腔引流、胃肠减压、出入量、Glu、体温及化验检查结果。",
    "problems": ["吞咽困难","食道恶性肿瘤","感染","肺炎","肺不张"],
    "date": "2015-03-05 14:35:00"
  },
  {
    "id":5,
    "title": "查房记录",
    "content": "今日患者晨起未诉特殊不适，一般情况可，生命体征：体温正常，血压145/70mmHg，NGT 300ml， 胸引100mg。副主任医师查房，注意复查血常规电解质，注意NGT引流情况。今日起予患者500ml牛奶空肠灌注。注意控制血糖。注意对症控制血压。",
    "problems": ["心梗","感染","高血压病"],
    "date": "2015-03-06 09:09:00"
  },
  {
    "id":6,
    "title": "查房记录",
    "content": "患者今晨心律120次/分，诉气促，喘憋。体温38.0，脉搏120次/分，呼吸20次/分，血压120/70mmHg，憋喘貌，双肺呼吸音粗，可闻及广泛哮鸣音。XXX副主任医师、XXX主治医师查房，请内科会诊，完善床旁胸片、超声心动、心肌酶、TNI、NBP、心电图、血气分析等检查。",
    "problems": ["心梗","感染","高血压病","肺炎","肺不张"],
    "date": "2015-03-07 13:38:00"
  }
];

var _active = 0;
var _demographic = '患者XXX，男，73岁，进行性吞咽困难2月';

function updateSelectedNote(selected) {
  _active = selected;
}

var NoteStore = assign({}, EventEmitter.prototype, {

  getAll: function() {
    return {
      "notes":_notes,
      "active":_active,
      'demographic':_demographic
      }
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
    case AppConstants.NOTE_SELECTION_UPDATE:
      updateSelectedNote(action.selected);
      NoteStore.emitChange();
      break;

    default:
      // no op
  }
});

module.exports = NoteStore;