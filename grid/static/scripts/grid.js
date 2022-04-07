/**
 * Created by admin on 02/06/2015.
 */


function byId(e){return document.getElementById(e);}
		function makeTable(strParentId,arr)
		{
			var table, tbody, curX, curY, curRow, curCell
			table = document.createElement('table');
            tbody = document.createElement('tbody');
			var sideLen = 20;
			table.appendChild(tbody);

			for (curY=0; curY<sideLen; curY++)
			{
				curRow = document.createElement('tr');
				for (curX=0; curX<sideLen; curX++)
				{
					curCell = document.createElement('td');
					curCell.appendChild( document.createTextNode( arr[1] ) );
					curCell.onclick = function() {onCellClick(this);}
					curRow.appendChild(curCell);
				}
				tbody.appendChild(curRow);
			}
			byId(strParentId).appendChild(table);
		}

		function onCellClick(clickedCell)
		{
			var cellTxt = clickedCell.innerHTML;
			var editBox = document.createElement('input');
			editBox.value = cellTxt;
			clickedCell.removeChild(clickedCell.childNodes[0]);
			clickedCell.appendChild(editBox);
			clickedCell.onclick = '';
			editBox.focus();
			editBox.onblur = function(){onLoseFocus(this);}
		}

		function onLoseFocus(editedCell)
		{
			var cellTxt = editedCell.value;
			parentNode = editedCell.parentNode;
			parentNode.removeChild(editedCell);
			parentNode.appendChild( document.createTextNode(cellTxt) );
			parentNode.onclick = function() {onCellClick(this);}
		}
