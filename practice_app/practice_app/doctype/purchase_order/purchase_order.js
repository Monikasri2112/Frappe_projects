// Copyright (c) 2026, Monika and contributors
// For license information, please see license.txt

// frappe.ui.form.on("purchase order", {
// 	refresh(frm) {

// 	},
// });

// frappe.ui.form.on("purchase order item",{
//     product(frm,cdt,cdn){
//         let row=frappe.get_doc(cdt,cdn);
//         frappe.msgprint("you selected:"+row.product);
//     }
// })

// frappe.ui.form.on("purchase order", {
//     refresh(frm) {

//         frm.add_custom_button("Check Selected", () => {

//             let selected = frm.get_selected();

//             console.log(selected);

//         });

//     }
// });

// frappe.ui.form.on("purchase order", {

//     // When a new row is added to Items
//     // items_add(frm, cdt, cdn) {
//     //     frappe.show_alert("New item row added");
//     //     console.log("Added row:", cdn);
//     // },

//     // Before a row is removed
//     before_items_remove(frm, cdt, cdn) {
//         frappe.show_alert("Item row is about to be removed");
//         console.log("Row to remove:", cdn);
//     },

    // // After a row is removed
    // items_remove(frm, cdt, cdn) {
    //     frappe.show_alert("Item row removed");
    //     console.log("Removed row:", cdn);
    // },

    // // When a row is moved/reordered
    // items_move(frm, cdt, cdn) {
    //     frappe.show_alert("Item row moved");
    //     console.log("Moved row:", cdn);
    // },

    // // When a child row is opened as a form
    // items_on_form_rendered(frm, cdt, cdn) {
    //     frappe.show_alert("Item row opened");
    //     console.log("Opened row:", cdn);
    // }

// });