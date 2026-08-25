frappe.ui.form.on("Control Demo", {
    refresh(frm) {

        // Get the HTML field
        let wrapper = $(frm.fields_dict.preview.wrapper);

        // Remove old content
        wrapper.empty();

        // Employee Name
        let employee_name = frappe.ui.form.make_control({
            parent: wrapper,
            df: {
                label: "Employee Name",
                fieldname: "employee_name",
                fieldtype: "Data"
            },
            render_input: true
        });

        // Department (Select)
        let department = frappe.ui.form.make_control({
            parent: wrapper,
            df: {
                label: "Department",
                fieldname: "department",
                fieldtype: "Select",
                options: [
                    "HR",
                    "Sales",
                    "Development",
                    "Testing"
                ]
            },
            render_input: true
        });

    }
});



frappe.ui.form.on("Control Demo", {
    refresh(frm) {

        frm.add_custom_button("Scan Barcode", () => {

            new frappe.ui.Scanner({
                dialog: true,
                multiple: false,

                on_scan(data) {
                    console.log(data.decodedText);
                }
            });

        });

    }
    
});
