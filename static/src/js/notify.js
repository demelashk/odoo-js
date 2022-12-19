odoo.define('odoo_js.NotifyWidget', function (require) {
    "use strict";
    console.log('LOADING...')

 var FormController = require('web.FormController');

  var FormAlertController = FormController.include({
    saveRecord: function () {
      var res = this._super.apply(this, arguments);
      this.do_notify('success', 'Record Saved');
         const audio = new Audio("/odoo_js/static/src/sound/success.wav");
         audio.play();
      return res;

    },

  });
});