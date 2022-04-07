/**
 * Created by admin on 02/07/2015.
 */
function test1() {
//create the table
    var oTable = document.createElement("table");
    oTable.setAttribute("border", "1");
    oTable.setAttribute("width", "100%");

//create the tbody
    var oTBody = document.createElement("tbody");
    oTable.appendChild(oTBody);

//create the first row
    oTBody.insertRow(0);
    oTBody.rows[0].insertCell(0);
    i0 = document.createElement('input');
    i0.value='';
    i0.setAttribute("tabIndex",1);
    oTBody.rows[0].cells[0].appendChild(i0);
    //oTBody.rows[0].cells[0].setAttribute("tabIndex","1");
    //oTBody.rows[0].cells[0].onfocus = function() {onFocus(this);}

    oTBody.rows[0].insertCell(1);
    i1 = document.createElement('input');
    i1.value='';
    i1.setAttribute("tabIndex",2);
    oTBody.rows[0].cells[1].appendChild(i1);


//create the second row
    oTBody.insertRow(1);
    oTBody.rows[1].insertCell(0);
    i2 = document.createElement('input');
    i2.value='';
    i2.setAttribute("tabIndex",3);
    oTBody.rows[1].cells[0].appendChild(i2);
    oTBody.rows[1].insertCell(1);
    i3 = document.createElement('input');
    i3.value='';
    i3.setAttribute("tabIndex",4);
    oTBody.rows[1].cells[1].appendChild(i3);

    document.body.appendChild(oTable);

}
