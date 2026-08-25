frappe.pages["book-dashboard"].on_page_load = function (wrapper) {
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: "Book Dashboard",
        single_column: true
    });

    page.add_button("Click Me", function () {
        frappe.msgprint("Button clicked!");
    });
};
frappe.pages["book-dashboard"].on_page_load = function (wrapper) {
    frappe.utils.play_sound("ping.mp3");
};