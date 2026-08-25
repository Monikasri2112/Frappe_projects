import frappe

def student_timeline(doctype, docname):

    doc = frappe.get_doc(doctype, docname)

    return [
        {
            "creation": doc.modified,
            "content": f"""
                <div>
                    <strong>Student Event</strong>
                   
                   <h1>helloooo</h1>
                
                </div>
            """
        }
    ]