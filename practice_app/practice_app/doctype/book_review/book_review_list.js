//.frappe.listview_settings["Book review"] = {

//     onload(listview) {
//        frappe.msgprint("Book Review List Loaded");
//     }

// };

//before_render
// frappe.listview_settings["Book review"] = {

//     before_render() {
//        frappe.msgprint("List is about to render");
//     }

// };

//get_indicator
frappe.listview_settings["Book review"] = {
    // hide_name_column: true,

    add_fields: ["status"],

    get_indicator(doc) {

        if (doc.status === "Completed") {
            return ["Completed", "green", "status,=,Completed"];
        } else if (doc.status === "Reading") {
            return ["Reading", "orange", "status,=,Reading"];
        } else {
            return ["Not Started", "red", "status,=,Not Started"];
        }
    }

};


//primary_action()
// frappe.listview_settings["Book review"] = {

//     primary_action() {
//         frappe.msgprint("Primary button clicked!");
//     }

// };


//  get_form_link() 
// frappe.listview_settings["Book review"] = {

//     get_form_link(doc) {
//         return "/app/user";
//     }

// };

//ading button to list view

frappe.listview_settings["Book review"] = {

    add_fields: ["status"],

    button: {

        show(doc) {
            return true;
        },

        get_label() {
            return "Details";
        },

        get_description(doc) {
            return `View ${doc.book_name}`;
        },

        action(doc) {
            frappe.msgprint(
                `Book: ${doc.book_name}<br>Status: ${doc.status}`
            );
        }

    }

};


//formatters
// frappe.listview_settings["Book review"] = {

//     formatters: {

//         rating(value) {
//             if (value == "5 Stars") {
//                 return "⭐⭐⭐⭐⭐";
//             }
//             if (value == "4 Stars") {
//                 return "⭐⭐⭐⭐";
//             }
//             return value;
//         },

//         status(value) {
//             if (value == "Completed") {
//                 return "✅ Completed";
//             }
//             if (value == "Reading") {
//                 return "📖 Reading";
//             }
//             return value;
//         }

//     }

// };

//filters
// frappe.listview_settings["Book review"] = {
// onload(listview) {
//     //add_fields: ["status"],
//     listview.filter_area.add([
//         ["Book review", "status", "=", "Completed"],
//     ]);
//     listview.refresh();
// }


//hide_name_column: true,
 
