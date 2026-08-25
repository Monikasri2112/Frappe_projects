frappe.pages["book-dashboard"].on_page_load = function (wrapper) {

    window.page = frappe.ui.make_app_page({
        parent: wrapper,
        title: "Book Dashboard",
        single_column: true
    });

   //page.set_title("My Page");
   //page.set_title_sub("Manage all your book reviews");


//    page.$sub_title_area.text("Manage all your book reviews");
//    page.set_indicator('Pending', 'orange')
//    page.clear_indicator()
   page.set_primary_action("Click Me", function () {
    frappe.msgprint("Hello!");
});


//page.clear_primary_action()

// page.add_menu_item("Go to Reviews", function () {
//     frappe.set_route("List", "Book review");
// });

// page.add_menu_item("New Review", function () {
//     frappe.new_doc("Book review");
// });

// page.add_menu_item("Open Reviews", function () {
//     frappe.set_route("List", "Book review");
// });

// page.add_menu_item("Show Message", function () {
//     frappe.msgprint("Welcome!");
// });

// page.clear_menu()

// page.add_action_item("New Review", function () {
//     frappe.new_doc("Book review");
// });

// page.add_action_item("View Reviews", function () {
//     frappe.set_route("List", "Book review");
// });

// page.add_action_item("Hello", function () {
//     frappe.msgprint("Hello!");
// });

// page.clear_actions_menu()



// page.add_inner_button("Import", function () {
//     frappe.msgprint("Import");
// });

// page.add_inner_button("Export", function () {
//     frappe.msgprint("Export");
// });

// page.add_inner_button("Refresh", function () {
//     location.reload();
// });

// page.add_inner_button("Refresh", function () {
//     frappe.msgprint("Refreshing...");
// });

// page.change_custom_button_type(
//     "Refresh",
//     null,
//     "Danger"
// );

// let status = page.add_field({
//     label: "Status",
//     fieldname: "status",
//     fieldtype: "Select",
//     options: [
//         "Reading",
//         "Completed",
//         "Not Started"
//     ]
// });

 page.add_field({
        label: "Book Name",
        fieldname: "book_name",
        fieldtype: "Data"
    });

    page.set_primary_action("Read Value", function() {

        let values = page.get_form_values();

        console.log(values);

        frappe.msgprint(JSON.stringify(values));

    });



};

