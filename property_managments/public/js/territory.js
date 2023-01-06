frappe.ui.form.on("Territory", {
	refresh: function(frm) {
		console.log("1234567890");

		},
        terrot:function(frm){
            if(frm.doc.terrot=="Country"
            || frm.doc.terrot=="City" ||
            frm.doc.terrot=="Town"
            ){
               frm.set_value("is_group", 1);
            }
        else{
             frm.set_value("is_group", 0);
             
        }
        }
});
