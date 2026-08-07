frappe.ui.form.on("employee_request", {

    refresh(frm) {

        frm.add_custom_button("Show Employee", function () {

            frm.call({
                method: "show_employee"
            });

        });

    }

});