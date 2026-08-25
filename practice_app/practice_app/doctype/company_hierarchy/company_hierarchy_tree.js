// Copyright (c) 2026, Monika and contributors
// For license information, please see license.txt

// frappe.treeview_settings["Company Hierarchy"] = {
//     breadcrumb: "Organization",
//     title: "Company Departments"
// };

console.log("TREE JS FILE LOADED");

function handle_company_change() {
    console.log("COMPANY CHANGED");
}

// frappe.treeview_settings["Company Hierarchy"] = {
//     filters: [
//         {
//             fieldname: "company",
//             fieldtype: "Select",
//             label: "Company",
//             options: "Company 1\nCompany 2",
//             on_change: handle_company_change,
//         },
//     ],
// };


// frappe.treeview_settings["Company Hierarchy"] = {
//     get_tree_nodes: "practice_app.api.get_children",
// };

