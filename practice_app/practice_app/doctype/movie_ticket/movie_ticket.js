// frappe.ui.form.on("Movie Ticket", {
// 	refresh(frm) {

// 		frm.add_custom_button("Book Ticket", function () {

// 			let d = new frappe.ui.Dialog({
// 				title: "Movie Ticket Booking",

// 				fields: [
// 					{
// 						label: "Movie Name",
// 						fieldname: "movie_name",
// 						fieldtype: "Data",
// 						reqd: 1
// 					},
// 					{
// 						label: "Ticket Price",
// 						fieldname: "ticket_price",
// 						fieldtype: "Currency",
// 						reqd: 1
// 					},
// 					{
// 						label: "Status",
// 						fieldname: "status",
// 						fieldtype: "Select",
// 						options: "Booked\nCancelled",
// 						default: "Booked"
// 					}
// 				],

// 				size: "small",

// 				primary_action_label: "Submit",

// 				primary_action(values) {

// 					console.log(values);

// 					frappe.msgprint(`
// 						<b>Movie Name:</b> ${values.movie_name}<br>
// 						<b>Ticket Price:</b> ${values.ticket_price}<br>
// 						<b>Status:</b> ${values.status}
// 					`);

// 					d.hide();
// 				}
// 			});

// 			d.show();

// 		});

// 	}
//  });



// frappe.msgprint({
//     title: "Booking Status",
//     indicator: 'green',
//     message: "Ticket Booked"
// });



//with primary action
// frappe.msgprint({
//     title: "Movie Ticket",
//     message: "Create a new ticket?",

//     primary_action: {

//         label: "Create",

//         action() {

//             frappe.new_doc("Movie Ticket");

//         }

//     }
// });


// with server and client action
// frappe.ui.form.on("Movie Ticket", {
// 	refresh(frm) {

// 		frm.add_custom_button("Server Action", function () {

// 			frappe.msgprint({
// 				title: "Movie Ticket",
// 				message: "Do you want to book this ticket?",

// 				primary_action: {
// 					label: "Proceed",

// 					server_action:
// 						"practice_app.practice_app.doctype.movie_ticket.movie_ticket.book_ticket",

// 					args: {
// 						movie_name: frm.doc.movie_name,
// 						price: frm.doc.ticket_price
// 					}
// 				}
// 			});

// 		});

// 	}
// });


//frappe.throw(__('This is an Error Message'))


// frappe.ui.form.on("Movie Ticket", {
// 	refresh(frm) {

// 		frm.add_custom_button("Movie Prompt", function () {

// 			frappe.prompt(
// 				"Movie Name",
// 				({ value }) => {

// 					console.log(value);

// 					frappe.msgprint({
// 						title: "Movie Details",
// 						message: "Movie Name : " + value,
// 						indicator: "green"
// 					});

// 				}
// 			);

// 		});

// 	}
// });


// frappe.ui.form.on("Movie Ticket", {
// 	refresh(frm) {

// 		frm.add_custom_button("Movie Prompt", function () {

// 			frappe.prompt(
// 				"Movie Name",
// 				console.log,
// 				"Enter Movie Name",
// 				"Book"
// 			);

// 		});

// 	}
// });


// frappe.ui.form.on("Movie Ticket", {
// 	refresh(frm) {

// 		frm.add_custom_button("Select Show Date", function () {

// 			frappe.prompt(
// 				{
// 					label: "Show Date",
// 					fieldname: "show_date",
// 					fieldtype: "Date",
// 					reqd: 1
// 				},

// 				(values) => {

// 					console.log(values.show_date);

// 					frappe.msgprint({
// 						title: "Selected Date",
// 						message: values.show_date,
// 						indicator: "green"
// 					});

// 				}

// 			);

// 		});

// 	}
// });

// frappe.ui.form.on("Movie Ticket", {
//     refresh(frm) {

//         frm.add_custom_button("Cancel Ticket", function () {

//             frappe.confirm(
//                 `Are you sure you want to cancel <b>${frm.doc.movie_name}</b>?`,

//                 () => {

//                     frappe.msgprint({
//                         title: "Cancelled",
//                         message: `${frm.doc.movie_name} has been cancelled.`,
//                         indicator: "red"
//                     });

//                 },

//                 () => {

//                     frappe.msgprint({
//                         title: "Cancelled",
//                         message: "No changes were made.",
//                         indicator: "blue"
//                     });

//                 }
//             );

//         });

//     }
// });







// frappe.ui.form.on("Movie Ticket", {

// 	refresh(frm) {

// 		frm.add_custom_button("Cancel Ticket", function () {

// 			frappe.warn(

// 				"Cancel Ticket",

// 				`You are about to cancel <b>${frm.doc.movie_name}</b>.<br><br>
// 				This action cannot be undone.`,

// 				() => {

// 					frappe.msgprint({
// 						title: "Success",
// 						message: `${frm.doc.movie_name} cancelled successfully.`,
// 						indicator: "red"
// 					});

// 				},

// 				"ok",

// 				false

// 			);

// 		});

// 	}

// });
// frappe.show_alert("Ticket Booked Successfully", 5);
// frappe.show_alert({
//     message:__('Hi, you have a new message'),
//     indicator:'green'
// }, 5);

//frappe.show_progress('Loading..', 50, 100, 'Please wait');

// frappe.new_doc(
//     "Movie Ticket",
//     {},
//     function(obj) {
//         console.log(obj);
//         console.log("Object Type:", obj.constructor.name);
//     }
// );



//when quick entry is OFF
// frappe.new_doc(
//     "Movie Ticket",
//     {},
//     function(doc) {
//         doc.movie_name = "Leo";
//         doc.ticket_price = 250;
//     }
// );


//when quick entry is ON
// frappe.new_doc("Movie Ticket", {
//     movie_name: "Leo"
// });;


//syntax
// frappe.new_doc(
//     doctype,
//     route_options,
//     init_callback
// );

// frappe.new_doc(
//     "DocType",
//     {
//         fieldname1: value1,
//         fieldname2: value2
//     },
//     (doc) => {
//         // Your code
//     }
// );


frappe.ui.form.on("Movie Ticket", {
    refresh(frm) {

        frm.add_custom_button("Open Multi Select", () => {

            new frappe.ui.form.MultiSelectDialog({

                // DocType to fetch records from
                doctype: "Movie Ticket",

                // Open dialog on current form
                target: frm,

                // Filter fields shown at the top
                setters: {
                    movie_name: "",
                    status: "Booked",
                    show_date: null
                },

                // Make these filters read-only
                read_only_setters: [
                    "status"
                ],

                // Show additional filter section
                add_filters_group: 1,

                // Date field used for date filtering
                date_field: "show_date",

                // Display these columns (works with custom query)
                columns: [
                    "name",
                    "movie_name",
                    "status",
                    "ticket_price"
                ],

                // Fetch only booked tickets
                get_query() {
                    return {
                        filters: {
                            status: "Booked"
                        }

                        // OR use custom query
                        /*
                        query: "practice_app.api.get_movie_tickets",
                        filters: {
                            status: "Booked"
                        }
                        */
                    };
                },

                // Runs after clicking the primary button
                action(selections) {

                    console.log(selections);

                    frappe.msgprint(
                        "Selected Tickets:<br><br>" +
                        selections.join("<br>")
                    );

                }

            });

        });

    }
});










//  frappe.ui.form.on("Movie Show", {
//     refresh(frm) {

//         // Add a custom button on the form
//         frm.add_custom_button("Select Tickets", () => {

//             // Open the Multi Select Dialog
//             new frappe.ui.form.MultiSelectDialog({

//                 // --------------------------------------------------
//                 // Parent DocType from which records are fetched
//                 // --------------------------------------------------
//                 doctype: "Movie Ticket",

//                 // --------------------------------------------------
//                 // Open the dialog on the current form
//                 // Usually use frm or cur_frm
//                 // --------------------------------------------------
//                 target: frm,

//                 // --------------------------------------------------
//                 // Filter fields shown at the top of the dialog.
//                 // User can change these values (unless read-only).
//                 // --------------------------------------------------
//                 setters: {
//                     movie_name: "",
//                     status: "Booked"
//                 },

//                 // --------------------------------------------------
//                 // Make specific setter fields read-only.
//                 // Here, the user cannot change "Booked".
//                 // --------------------------------------------------
//                 read_only_setters: [
//                     "status"
//                 ],

//                 // --------------------------------------------------
//                 // Show the "Add Filter" section like List View.
//                 // 1 = Show
//                 // 0 = Hide
//                 // --------------------------------------------------
//                 add_filters_group: 1,

//                 // --------------------------------------------------
//                 // Date field used for the built-in date filter.
//                 // (Only if your DocType has a Date field)
//                 // --------------------------------------------------
//                 date_field: "show_date",

//                 // --------------------------------------------------
//                 // Used ONLY when using a custom Python query.
//                 // These become the table columns in the dialog.
//                 // --------------------------------------------------
//                 columns: [
//                     "movie_name",
//                     "ticket_price",
//                     "status"
//                 ],

//                 // --------------------------------------------------
//                 // Decide which records should appear.
//                 // --------------------------------------------------
//                 get_query() {
//                     return {

//                         // Default filtering
//                         filters: {
//                             status: "Booked"
//                         }

//                         /*
//                         OR use your own Python method

//                         query: "practice_app.api.get_movie_tickets",

//                         filters: {
//                             status: "Booked"
//                         }
//                         */

//                     };
//                 },

//                 // --------------------------------------------------
//                 // Allow selecting CHILD TABLE rows
//                 // instead of parent documents.
//                 // (Only if the parent DocType has a Table field)
//                 // --------------------------------------------------
//                 allow_child_item_selection: 0,

//                 // --------------------------------------------------
//                 // Name of the Table field inside the parent DocType.
//                 // Example:
//                 // Sales Order --> items
//                 // Purchase Order --> items
//                 // --------------------------------------------------
//                 child_fieldname: "items",

//                 // --------------------------------------------------
//                 // Child table columns shown in the dialog.
//                 // --------------------------------------------------
//                 child_columns: [
//                     "item_code",
//                     "qty",
//                     "rate"
//                 ],

//                 // --------------------------------------------------
//                 // Runs after clicking the primary button.
//                 // --------------------------------------------------
//                 action(selections, args) {

//                     // Parent document names
//                     console.log("Selected Parent Docs");
//                     console.log(selections);

//                     // Child table row names
//                     console.log("Selected Child Rows");
//                     console.log(args.filtered_children);

//                     frappe.msgprint(
//                         "Selected Documents:<br>" +
//                         selections.join("<br>")
//                     );
//                 }

//             });

//         });

//     }
// });

// frappe.ui.form.on("Movie Ticket", {
//     refresh(frm) {

//         frm.add_custom_button("Book Seats", () => {

//             const dialog = new frappe.ui.Dialog({
//                 title: "Movie Booking",

//                 fields: [
//                     {
//                         fieldname: "bookings",
//                         fieldtype: "Table",
//                         label: "Bookings",
//                         in_place_edit: true,

//                         fields: [
//                             {
//                                 fieldname: "customer_name",
//                                 label: "Customer",
//                                 fieldtype: "Data",
//                                 in_list_view: 1,
//                                 reqd: 1
//                             },
//                             {
//                                 fieldname: "seat_no",
//                                 label: "Seat No",
//                                 fieldtype: "Data",
//                                 in_list_view: 1,
//                                 reqd: 1
//                             },
//                             {
//                                 fieldname: "price",
//                                 label: "Price",
//                                 fieldtype: "Currency",
//                                 in_list_view: 1
//                             }
//                         ],

//                         on_add_row(idx) {

//                             let row = dialog.fields_dict.bookings.df.data[idx - 1];

//                             row.price = 200;

//                             dialog.fields_dict.bookings.grid.refresh();
//                         }

//                     }
//                 ],

//                 primary_action(values) {

//                     console.log(values);

//                     frappe.msgprint(JSON.stringify(values, null, 2));

//                     dialog.hide();
//                 },

//                 primary_action_label: "Book"

//             });

//             dialog.show();

//         });

//     }
// });


//AJAX Server call


//No parameters
// frappe.call(
//     "practice_app.practice_app.doctype.movie_ticket.movie_ticket.ping"
// ).then(r => {

//     console.log(r);

//     frappe.msgprint(r.message);

// });


//One Parameter

// frappe.call(
//     "practice_app.practice_app.doctype.movie_ticket.movie_ticket.welcome",
//     {
//         movie_name: "Leo"
//     }
// ).then(r => {

//     console.log(r.message);

//     frappe.msgprint(r.message);

// });

// frappe.call({

//     method:
//     "practice_app.practice_app.doctype.movie_ticket.movie_ticket.calculate",

//     args: {
//         price: 200,
//         quantity: 3
//     },

//     freeze: true,

//     callback(r) {

//         console.log(r.message);

//         frappe.msgprint(
//             "Total = " + r.message.total
//         );

//     },

//     error(r) {

//         frappe.msgprint("Something went wrong");

//     }

// });


// frm.add_custom_button("", () => {

//     frappe.db.get_doc(
//         "Movie Ticket",
//         frm.doc.name
//     )
//     .then(doc => {

//         frappe.msgprint(
//             doc.movie_name
//         );

//     });

// });


// frappe.db.get_list("Movie Ticket", {
//     fields: ["movie_name", "ticket_price"],
//     filters: {
//         status: "Booked"
//     }
// }).then(records => {

//      frappe.msgprint(JSON.stringify(records, null, 2));
// });

// ===============================================
// frappe.db.get_value()
// Used to fetch one or more field values from a document
// ===============================================






// // ===============================================
// // 1. Get a Single Field using Document Name
// // ===============================================

// frappe.db.get_value(
//     "Movie Ticket",      // DocType
//     "MOV-00001",         // Document Name
//     "movie_name"         // Field to fetch
// ).then(r => {

//     // Print only the movie name
//     console.log(r.message.movie_name);

// });


// // ===============================================
// // 2. Get Ticket Price using Document Name
// // ===============================================

// frappe.db.get_value(
//     "Movie Ticket",
//     "MOV-00001",
//     "ticket_price"
// ).then(r => {

//     console.log(r.message.ticket_price);

// });


// // ===============================================
// // 3. Get Status using Document Name
// // ===============================================

// frappe.db.get_value(
//     "Movie Ticket",
//     "MOV-00001",
//     "status"
// ).then(r => {

//     console.log(r.message.status);

// });


// // ===============================================
// // 4. Get Multiple Fields
// // ===============================================

// frappe.db.get_value(
//     "Movie Ticket",
//     "MOV-00001",
//     [
//         "movie_name",
//         "ticket_price",
//         "status",
//         "show_date"
//     ]
// ).then(r => {

//     // Store all returned values
//     let values = r.message;

//     console.log(values.movie_name);
//     console.log(values.ticket_price);
//     console.log(values.status);
//     console.log(values.show_date);

// });


// // ===============================================
// // 5. Print Entire Response Object
// // ===============================================

// frappe.db.get_value(
//     "Movie Ticket",
//     "MOV-00001",
//     ["movie_name", "ticket_price"]
// ).then(r => {

//     // Shows complete response
//     console.log(r);

//     /*
//     Output:

//     {
//         message: {
//             movie_name: "Leo",
//             ticket_price: 200
//         }
//     }

//     */

// });


// // ===============================================
// // 6. Using Filter (instead of Document Name)
// // Finds the first Movie Ticket where movie_name = "Leo"
// // ===============================================

// frappe.db.get_value(
//     "Movie Ticket",
//     {
//         movie_name: "Leo"
//     },
//     "ticket_price"
// ).then(r => {

//     console.log(r.message.ticket_price);

// });


// // ===============================================
// // 7. Using Multiple Filters
// // movie_name = Leo AND status = Available
// // ===============================================

// frappe.db.get_value(
//     "Movie Ticket",
//     {
//         movie_name: "Leo",
//         status: "Available"
//     },
//     [
//         "ticket_price",
//         "show_date"
//     ]
// ).then(r => {

//     console.log(r.message.ticket_price);
//     console.log(r.message.show_date);

// });


// // ===============================================
// // 8. Using Filter and Getting Multiple Fields
// // ===============================================

// frappe.db.get_value(
//     "Movie Ticket",
//     {
//         movie_name: "Leo"
//     },
//     [
//         "movie_name",
//         "ticket_price",
//         "status",
//         "show_date"
//     ]
// ).then(r => {

//     let values = r.message;

//     console.log(values.movie_name);
//     console.log(values.ticket_price);
//     console.log(values.status);
//     console.log(values.show_date);

// });


// // ===============================================
// // 9. Check if Data Exists
// // ===============================================

// frappe.db.get_value(
//     "Movie Ticket",
//     "MOV-00001",
//     "movie_name"
// ).then(r => {

//     if (r.message) {
//         console.log("Movie Found");
//         console.log(r.message.movie_name);
//     } else {
//         console.log("Movie Not Found");
//     }

// });


// // ===============================================
// // 10. Arrow Function Shortcut
// // ===============================================

// frappe.db.get_value(
//     "Movie Ticket",
//     "MOV-00001",
//     "movie_name"
// ).then(r => console.log(r.message.movie_name));


// // ===============================================
// // NOTES
// // ===============================================

// /*

// Syntax:

// frappe.db.get_value(
//     doctype,
//     name OR filters,
//     fieldname OR [fieldnames]
// )

// Parameters

// 1. doctype
//    Which DocType to search.
//    Example:
//    "Movie Ticket"

// 2. name
//    Exact document name.
//    Example:
//    "MOV-00001"

// 3. filters
//    Search using field values.
//    Example:
//    {
//        movie_name: "Leo"
//    }

// 4. fieldname
//    One field.
//    Example:
//    "ticket_price"

// 5. [fieldnames]
//    Multiple fields.
//    Example:
//    [
//        "movie_name",
//        "ticket_price",
//        "status"
//    ]

// Returns

// Single field:

// {
//     message: {
//         ticket_price: 200
//     }
// }

// Multiple fields:

// {
//     message: {
//         movie_name: "Leo",
//         ticket_price: 200,
//         status: "Available",
//         show_date: "2026-08-10"
//     }
// }

// Important:

// ✔ Returns only ONE document (the first matching record).
// ✔ Returns a Promise, so use .then().
// ✔ Use document name when you know the exact record.
// ✔ Use filters when you want to search by field values.
// ✔ If you need many records, use frappe.db.get_list() instead.

// */




// frappe.db.get_single_value(doctype, fieldname)
// .then(value => {
//     // Use the returned value here
// });

// frappe.ui.form.on("Movie Ticket", {
//     onload(frm) {

//         frm.tour.init({
//             tour_name: "Movie Ticket Tour"
//         }).then(() => {
//             frm.tour.start();
//         });

//     }
// });




//msgprint("title","message")

// frappe.ui.form.on("Movie Ticket", {
//     refresh(frm) {
// 		let dialog = new frappe.ui.Dialog({
//     title: "Enter First Name",
//     fields: [
//         {
//             label: "First Name",
//             fieldname: "first_name",
//             fieldtype: "Data"
//         }
//     ],
//     primary_action_label: "Create project",

//     primary_action(values) {
//         dialog.hide();

//         frappe.route_options = {
//             project_name: values.first_name
//         };

//         frappe.new_doc("Project");
//     }
// });

// dialog.show();
//     }
// });



//msgprint("title","message")

// frappe.ui.form.on("Movie Ticket", {
//     refresh(frm) {
// 		frm.add_custom_button("Get status", () => {
//             frm.set_value("status", "Cancelled");
//             frm.refresh_field("status");
//         });
//     }
// });

frappe.ui.form.on("Movie Ticket", {
    refresh(frm) {
        if(doc.status=='Cancelled'){
            frm.add_custom_button("Approve",()=>{
                frm.set_value("status", "Booked");
                frappe.msgprint("Employee approved succesfully")
            });
        }
    }});
