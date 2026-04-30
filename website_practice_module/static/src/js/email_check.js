odoo.define('website_practice_module.email_check', function (require) {
    "use strict";

    const ajax = require('web.ajax');
    const { Notification } = require('@web/core/notifications/notification');
    const { registry } = require('@web/core/registry');

    document.addEventListener("DOMContentLoaded", function () {

        const form = document.getElementById("partner_form");

        form.addEventListener("submit", function (e) {
            e.preventDefault();

            let email = document.getElementById("email").value;

            ajax.jsonRpc('/check_email', 'call', {
                email: email
            }).then(function (result) {

                if (result.exists) {

                    const notification = new Notification(null, {
                        title: "Warning",
                        message: "Email already exists!",
                        type: "danger",
                        sticky: true,
                    });
                    notification.mount(document.body);

                } else {
                    form.submit();
                }

            });

        });

    });

});