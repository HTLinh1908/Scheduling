window.onload = function() {
    fetch('output.txt')
        .then(response => response.text())
        .then(data => {
            const tables = data.split("end"); 
            days=['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']
            for (let k = 0; k < tables.length - 1; k++) 
            {
                table = tables[k];
                tableHTML = "";
                tableHTML += `<div>${days[k]}</div>`;
                tableHTML += `<table>`;
                rows = table.split("row");
                for (let i = 0; i < rows.length - 1; i++)
                {
                    row = rows[i];
                    tableHTML += "<tr>";
                    items = row.split(" ");
                    for (let j = 0; j < items.length ; j++) 
                    {
                        item = items[j];
                        tableHTML += (i == 0) ? `<th>${item}</th>` : `<td>${item}</td>`;
                    }
                    tableHTML += "</tr>";
                }
                tableHTML += `</table>`;
                console.log(tableHTML);
                document.body.innerHTML += tableHTML;
            }
        });
};