// Copyright (c) 2026, Monika and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Company Hierarchy", {
// 	refresh(frm) {

// 	},
// });
//get_children()
// frappe.ui.form.on("Company Hierarchy", {

//     refresh(frm) {

//         frm.add_custom_button("Show Children", function () {

//             frappe.call({

//                 method: "practice_app.practice_app.doctype.company_hierarchy.company_hierarchy.show_children",

//                 args: {
//                     docname: frm.doc.name
//                 },

//                 callback: function(r) {

//                     frappe.msgprint(r.message);

//                 }

//             });

//         });

//     }

// });


//get_parent()
frappe.ui.form.on("Company Hierarchy", {

    refresh(frm) {

        frm.add_custom_button("Show Parent", function () {

            frappe.call({

                method: "practice_app.practice_app.doctype.company_hierarchy.company_hierarchy.show_parent",

                args: {
                    docname: frm.doc.name
                },

                callback: function(r) {

                    frappe.msgprint(r.message);

                }

            });

        });

    }

});