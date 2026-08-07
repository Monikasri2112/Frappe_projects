// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Create Event", function () {

//             frappe.call({

//                 method: "practice_app.practice_app.doctype.event_registration.event_registration.create_event",

//                 callback: function(r) {

//                     frappe.msgprint(r.message);

//                 }

//             });

//         });

//     }

// });


//getlatest doc and getcached doc

// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Show Documents", function () {

//             frappe.call({

//                 method: "practice_app.practice_app.doctype.event_registration.event_registration.show_documents",

//                 args: {
//                     docname: frm.doc.name
//                 },

//                 callback: function (r) {

//                     frappe.msgprint(`
//                         <b>Current Doc :</b> ${r.message.current_document}<br>
//                         <b>Current Event :</b> ${r.message.current_event}<br><br>

//                         <b>Cached Doc :</b> ${r.message.cached_document}<br>
//                         <b>Cached Event :</b> ${r.message.cached_event}<br><br>

//                         <b>Last Created Doc :</b> ${r.message.last_document}<br>
//                         <b>Last Event :</b> ${r.message.last_event}
//                     `);

//                 }

//             });

//         });

//     }

// });

//rename record
// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Rename", function () {

//             frappe.call({

//                 method: "practice_app.practice_app.doctype.event_registration.event_registration.rename_event",

//                 args: {
//                     docname: frm.doc.name
//                 },

//                 callback: function(r) {

//                     console.log(r);
//                     frappe.msgprint(JSON.stringify(r));

//                    // frm.reload_doc();

//                 }

//             });

//         });

//     }

// });


// delete doc

// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Delete", function () {

//             frappe.call({

//                 method: "practice_app.practice_app.doctype.event_registration.event_registration.delete_event",

//                 args: {
//                     docname: frm.doc.name
//                 },

//                 callback: function(r) {

//                     frappe.msgprint(r.message);

//                     frappe.set_route("List", "Event Registration");

//                 }

//             });

//         });

//     }

// });


//frappe.get_meta
// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Show Meta", function () {

//             frappe.call({
//                 method: "practice_app.practice_app.doctype.event_registration.event_registration.show_meta",

//                 callback: function(r) {

//                     console.log(r.message);

//                     frappe.msgprint(r.message.join("<br>"));

//                 }

//             });

//         });

//     }

// });


//frappe.only_for

// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Manager Only", function () {

//             frappe.call({

//                 method: "practice_app.practice_app.doctype.event_registration.event_registration.manager_only",

//                 callback: function(r) {

//                     frappe.msgprint(r.message);

//                 }

//             });

//         });

//     }

// });

//doc.save()
// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Update Event", function () {

//             frappe.call({

//                 method: "practice_app.practice_app.doctype.event_registration.event_registration.update_event",

//                 args: {
//                     docname: frm.doc.name
//                 },

//                 callback: function(r) {

//                     frappe.msgprint(r.message);

//                     frm.reload_doc();

//                 }

//             });

//         });

//     }

// });

//doc.get_doc_before_save
// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Close Event", function () {

//             frm.set_value("status", "Closed");

//             frm.save();

//         });

//     }

// });

//doc.has_value_changed
// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Close Event", function () {

//             // Change the Status field
//             frm.set_value("status", "Closed");

//             // Save the document
//             frm.save();

//         });

//     }

// });

// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Reload Event", function () {

//             frappe.call({

//                 method: "practice_app.practice_app.doctype.event_registration.event_registration.reload_event",

//                 args: {
//                     docname: frm.doc.name
//                 },

//                 callback: function(r) {

//                     frappe.msgprint(r.message);

//                     frm.reload_doc();

//                 }

//             });

//         });

//     }

// });

//Check Permission

// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Check Permission", function () {

//             frappe.call({

//                 method: "practice_app.practice_app.doctype.event_registration.event_registration.check_permission",

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



//doc.get_title
// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Show Title", function () {

//             frappe.call({

//                 method: "practice_app.practice_app.doctype.event_registration.event_registration.get_event_title",

//                 args: {
//                     docname: frm.doc.name
//                 },

//                 callback: function(r) {

//                     frappe.msgprint("Title : " + r.message);

//                 }

//             });

//         });

//     }

// });

//doc.notify_update()
// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frappe.show_alert("Edit any field and click Save");

//     }

// });

//db_set():
// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Update Status", function () {

//             frappe.call({

//                 method: "practice_app.practice_app.doctype.event_registration.event_registration.update_status",

//                 args: {
//                     docname: frm.doc.name
//                 },

//                 callback: function(r){

//                     frappe.msgprint(r.message);

//                     frm.reload_doc();

//                 }

//             });

//         });

//     }

// });

//doc.append
// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Add Participant", function () {

//             frappe.call({

//                 method: "practice_app.practice_app.doctype.event_registration.event_registration.add_participant",

//                 args: {
//                     docname: frm.doc.name
//                 },

//                 callback: function(r){

//                     frappe.msgprint(r.message);

//                     frm.reload_doc();

//                 }

//             });

//         });

//     }

// });

//doc.get_url()
// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Show URL", function () {

//             frappe.call({

//                 method: "practice_app.practice_app.doctype.event_registration.event_registration.show_document_url",

//                 args: {
//                     docname: frm.doc.name
//                 },

//                 callback: function(r) {

//                     frappe.msgprint(
//                         "Document URL:<br><br>" + r.message
//                     );

//                 }

//             });

//         });

//     }

// });

//doc.add_comment()
// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Add Comment", function () {

//             frappe.call({

//                 method: "practice_app.practice_app.doctype.event_registration.event_registration.add_comment",

//                 args: {
//                     docname: frm.doc.name
//                 },

//                 callback: function(r){

//                     frappe.msgprint(r.message);

//                     frm.reload_doc();

//                 }

//             });

//         });

//     }

// });

//doc.add_tag
// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Add Tag", function () {

//             frappe.call({

//                 method: "practice_app.practice_app.doctype.event_registration.event_registration.add_event_tag",

//                 args: {
//                     docname: frm.doc.name
//                 },

//                 callback: function(r) {

//                     frappe.msgprint(r.message);

//                     frm.reload_doc();

//                 }

//             });

//         });

//     }

// });


//doc.db_insert()
// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("DB Insert", function () {

//             frappe.prompt(
//                 [
//                     {
//                         fieldname: "event_name",
//                         label: "Event Name",
//                         fieldtype: "Data",
//                         reqd: 1
//                     },
//                     {
//                         fieldname: "organizer",
//                         label: "Organizer",
//                         fieldtype: "Data",
//                         reqd: 1
//                     },
//                     {
//                         fieldname: "status",
//                         label: "Status",
//                         fieldtype: "Data",
//                         reqd: 1
//                     }
//                 ],

//                 function(values) {

//                     frappe.call({

//                         method: "practice_app.practice_app.doctype.event_registration.event_registration.db_insert_demo",

//                         args: {
//                             event_name: values.event_name,
//                             organizer: values.organizer,
//                             status: values.status
//                         },

//                         callback: function(r) {

//                             frappe.msgprint(r.message);

//                         }

//                     });

//                 },

//                 "Create Event"

//             );

//         });

//     }

// });

//doc.db_update()
// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Update Status", function () {

//             frappe.prompt(
//                 [
//                     {
//                         fieldname: "status",
//                         label: "Status",
//                         fieldtype: "Data",
//                         reqd: 1
//                     }
//                 ],

//                 function(values){

//                     frappe.call({

//                         method: "practice_app.practice_app.doctype.event_registration.event_registration.update_status",

//                         args: {
//                             docname: frm.doc.name,
//                             status: values.status
//                         },

//                         callback: function(r){

//                             frappe.msgprint(r.message);

//                             frm.reload_doc();

//                         }

//                     });

//                 },

//                 "Update Status"

//             );

//         });

//     }

// });


//doc.get_parents()
// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Show Participants", function () {

//             frappe.call({

//                 method: "practice_app.practice_app.doctype.event_registration.event_registration.show_participants",

//                 args: {
//                     docname: frm.doc.name
//                 }

//             });

//         });

//     }

// });

// 


//get_doc
// frappe.ui.form.on("Event Registration", {

//     refresh(frm) {

//         frm.add_custom_button("Create C Workshop", function () {

//             frappe.call({

//                 method: "practice_app.practice_app.doctype.event_registration.event_registration.create_c_workshop",

//                 callback: function(r) {

//                     frappe.msgprint(r.message);

//                     frm.reload_doc();

//                 }

//             });

//         });

//     }

// });

