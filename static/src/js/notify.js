odoo.define('odoo-js.NotifyWidget', function (require) {
    "use strict";
    console.log('LOADING...')

 var FormController = require('web.FormController');

  var FormAlertController = FormController.include({
    saveRecord: function () {
      var res = this._super.apply(this, arguments);
      this.do_notify('success', 'save recored');
      return res;

    },

  });
});