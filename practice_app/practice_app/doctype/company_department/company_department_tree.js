// Copyright (c) 2026, Monika and contributors
// For license information, please see license.txt
// company_department_tree.js

// frappe.treeview_settings["Company Department"] = {
//     // Navigation breadcrumb
//     breadcrumb: "Company",

//     // Heading shown at the top
//     title: "Company Department Tree",
// };



// frappe.treeview_settings["Company Department"] = {
//     title: "Company Department Tree",

//     get_tree_nodes:
//         "practice_app.practice_app.doctype.company_department.company_department.get_children"
// };

// frappe.treeview_settings["Company Department"] = {
//     title: "Company Department Tree",

//     add_tree_node:
//         "practice_app.practice_app.doctype.company_department.company_department.add_node"
// };

fields: [
    {
        fieldtype: "Data",
        fieldname: "account_name",
        label: "New Account Name",
        reqd: true,
    },
    {
        fieldtype: "Link",
        fieldname: "account_currency",
        label: "Currency",
        options: "Currency",
    },
    {
        fieldtype: "Check",
        fieldname: "is_group",
        label: "Is Group",
    },
],

//ignore_fields: ["parent_account"],