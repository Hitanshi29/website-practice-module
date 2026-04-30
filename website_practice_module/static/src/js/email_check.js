/** @odoo-module **/

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".toast").forEach((toastEl) => {
        if (window.bootstrap && window.bootstrap.Toast) {
            const toast = new window.bootstrap.Toast(toastEl, { delay: 4000 });
            toast.show();
        }
    });
});

// odoo.define('website_practice_module.email_check', function (require) {
//     "use strict";

//     var ajax = require('web.ajax');

//     document.addEventListener("DOMContentLoaded", function () {

//         let form = document.getElementById("partner_form");

//         form.addEventListener("submit", function (e) {
//             e.preventDefault();

//             let email = document.getElementById("email").value;

//             ajax.jsonRpc('/check_email', 'call', {
//                 email: email
//             }).then(function (result) {

//                 if (result.exists) {
//                     alert("Email already exists!");
//                 } else {
//                     form.submit(); 
//                 }

//             });
//         });

//     });

// });