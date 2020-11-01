document.addEventListener('DOMContentLoaded', function () {
    var search_input = document.querySelector('#search-place');
    addListenerMulti(search_input, 'keyup change', function () {
        refresh_page();
        });

    function refresh_page(){
        input = document.getElementById("search-vistors");
        ul = document.getElementById("myUL");
        var search_by = document.getElementById("search-form-input").value;
        var unique =document.getElementById("search-unique-check-box").checked
        search_table(ul,input.value,search_by,unique);
    }

    function search_table(table_selector,search_value,search_col,unique){
        rows =  table_selector.querySelectorAll('tr:not(:first-child)')
        rows.forEach(function (row, index){
            a = row.getElementsByTagName("td")[search_col];
            txtValue = a.innerText;
            
            if (txtValue.toUpperCase().indexOf(search_value.toUpperCase()) > -1) {
                row.style.display = "";
            } else {
                row.style.display = "none";
            }

            if(unique){
                remove_duplicates_row_in_table(row.id)
            }

        })
    }

    function remove_duplicates_row_in_table(id){
        $('tr#'+id+':not(tr#'+id+':first)').hide()
    }

    function show_duplicates_row_in_table(id){
        $('tr#'+id+':not(tr#'+id+':first)').show()
    }


/* Add one or more listeners to an element
** @param {DOMElement} element - DOM element to add listeners to
** @param {string} eventNames - space separated list of event names, e.g. 'click change'
** @param {Function} listener - function to attach for each event as a listener
*/
function addListenerMulti(element, eventNames, listener) {
  var events = eventNames.split(' ');
  for (var i=0, iLen=events.length; i<iLen; i++) {
    element.addEventListener(events[i], listener, false);
  }
}


})