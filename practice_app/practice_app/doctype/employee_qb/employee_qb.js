// Copyright (c) 2026, Monika and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Employee qb", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on("Employee qb", {
    refresh(frm) {

        let wrapper = frm.fields_dict.extra.$wrapper;

        wrapper.empty();

        let container = $('<div class="dynamic-field"></div>');
        wrapper.append(container);

        frappe.ui.form.make_control({
            parent: container,
            df: {
                label: "New one",
                fieldname: "new_one",
                fieldtype: "Data"
            },
            render_input: true
        });
    }
});


// frappe.meta.docfield_map['Employee qb'].fieldtype.formatter = (value) => {
//  if (value==='Development') return '🔵Development';
//  else return value;
// }


// frappe.ui.form.on("Employee qb",{
//     refresh(frm){
//         frm.add_custom_button("say hello",()=>{
//             frappe.msgprint("heyy")
//         })
//     }
// })


// frappe.ui.form.on("Employee qb",{
//     refresh(frm){
//         // frm.set_value("department","Development");
//         // frm.email_doc()
//         // if(frm.doc.bonus===2000){
//         //     frm.disable_save()
//         // }
        
//         //     frm.set_value("last_name","cibin").then(()=>{if(frm.is_dirty()){
//         //     frappe.show_alert("please save");
//         // }
//         // else{
//         //     frappe.show_alert("nothing")
//         // }}
//     //)
//     //frm.dirty()
//     // if(frm.is_new()){
//     //     frappe.msgprint("hello");
//     // }
//     //   if(!frm.doc.last_name){
//     //     frm.set_intro("please enter the last name","red");
//     //   }

// //     frm.add_custom_button("button",()=>{
// //     frm.set_value("salary",900);
// //     })
    
// // frm.change_custom_button_type("button",null,'danger');

// // frm.set_df_property('last_name','fieldtype','Text');
// // frm.set_df_property('last_name','reqd',1);

// // frm.toggle_reqd("last_name",frm.doc.department==="Sales")

// // frm.toggle_display(["bonus","last_name"],frm.doc.department==="Development")

// // frm.toggle_enable("joining_date",true)

// // frm.trigger('set_mandatory_fields');
// //     },
// //     set_mandatory_fields(frm){
// //         frm.toggle_reqd(["last_name","bonus"],frm.doc.department==="Sales");
// //     }


// // })

// frm.add_custom_button("scan here",()=>{
//     new frappe.ui.Scanner({
//  dialog: true, // open camera scanner in a dialog
//  multiple: false, // stop after scanning one value
//  on_scan(data) {
//   frm.set_value("salary",data.decodedText);
//  }
// });

// })



//  }

// })


frappe.ui.form.on("Employee qb", {
    get_email_recipients(frm, field) {


        if (field === "recipients") {
            return ["moni@example.com"];
        }

        return [];
    }
});



let d = new frappe.ui.Dialog({
    title: 'Enter details',
    fields: [
        {
            label: 'First Name',
            fieldname: 'first_name',
            fieldtype: 'Data'
        },
        {
            label: 'Last Name',
            fieldname: 'last_name',
            fieldtype: 'Data'
        },
        {
            label: 'Age',
            fieldname: 'age',
            fieldtype: 'Int'
        }
    ],
    size: 'small', // small, large, extra-large 
    primary_action_label: 'Submit',
    primary_action(values) {
        console.log(values);
        d.hide();
    }
});

d.show();

