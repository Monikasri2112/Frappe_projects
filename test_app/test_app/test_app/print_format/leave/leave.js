frappe.query_reports["Leave"] = {
    filters: [
        {
            fieldname: "status",
            label: "Status",
            fieldtype: "Select",
            options: "\nOpen\nPending\nApproved\nRejected"
        },
        {
            fieldname: "from_date",
            label: "From Date",
            fieldtype: "Date"
        },
        {
            fieldname: "to_date",
            label: "To Date",
            fieldtype: "Date"
        }
    ]
};