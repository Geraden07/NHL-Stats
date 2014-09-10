<?php
	//Get page number being requested
	$page = $_GET["pageRequest"];
	//Open local JSON encoded list file
	$liststring = file_get_contents("jlistdata.json");
	$listobject = json_decode($liststring);
	echo "<table id=\"statTable\">";
	echo "<tr>
			<th>
				#
			</th>
			<th>
				Player
			</th>
			<th>
				Curr Team
			</th>
			<th>
				POS
			</th>
			<th>
				1st NHL Season
			</th>
			<th>
				Last NHL Season
			</th>
			<th>
				GP
			</th>
			<th>
				G
			</th>
			<th>
				A
			</th>
			<th>
				P
			</th>
			<th>
				+/-
			</th>
			<th>
				PIM
			</th>
			<th>
				PP
			</th>
			<th>
				SH
			</th>
			<th>
				GW
			</th>
			<th>
				GT
			</th>
			<th>
				OT
			</th>
			<th>
				SHOTS
			</th>
			<th>
				P/GP
			</th>
		</tr>";
	for($i=((30*$page) - 30);$i<(30*$page);$i++)
	{
		echo "<tr>";
		for($j=0;$j<19;$j++)
		{
			echo "<td>";
			echo (string)$listobject[$i][$j];
			echo "</td>";
		}
		echo "</tr>";
	}
	echo "</table>";
?>