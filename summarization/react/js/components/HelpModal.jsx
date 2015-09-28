var React = require('react');

var HelpModal = React.createClass({

  render: function () {
    return (
      <div className="modal fade" id="helpModal" tabIndex="-1" role="dialog" aria-hidden="true">
        <div className="modal-dialog">
          <div className="modal-content">
            <div className="modal-header">
              使用帮助
            </div>
            <div className="modal-body">
              <p>舶众智能病历是一款帮助医生快速总结浏览病人相关病史的插件，能够根据医生所关心的诊断或者症状，自动抽取、总结、和呈现病人的相关病史和检查、手术记录等，以实现对复杂病例的关键信息迅速获取。</p>
              <p>软件每一栏的功能可通过鼠标移动到栏目名旁的感叹号来参考其功能介绍。</p>
              <p>若有其他问题，请联系舶众数据：<a href="mailto:help@bosonhealthdata.com">help@bosonhealthdata.com</a></p>
            </div>
          </div>
        </div>
      </div>
    );
  }
});

module.exports = HelpModal;
