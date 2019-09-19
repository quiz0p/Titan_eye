<!DOCTYPE html>
<html>
<head>
<title>Eye Titan Database</title>
<style>
table {
border-collapse: collapse;
width: 100%;
color: #588c7e;
font-family: monospace;
font-size: 25px;
text-align: left;
}
th {
background-color: #588c7e;
color: white;
}
tr:nth-child(even) {background-color: #f2f2f2}
</style>
</head>
<body>
<table>
<tr>
<th>embedding_id</th>
<th>face</th>
<th>embedding</th>
<th>start_time</th>
<th>end_time</th>
<th>cam_id</th>
</tr>
<?php
$conn = mysqli_connect("localhost", "root", "", "company");
// Check connection
if ($conn->connect_error) {
die("Connection failed: " . $conn->connect_error);
}
$sql = "SELECT id, username, password FROM login";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
// output data of each row
while($row = $result->fetch_assoc()) {
echo "<tr><td>" . $row["id"]. "</td><td>" . $row["username"] . "</td><td>"
. $row["password"]. "</td></tr>";
}
echo "</table>";
} else { echo "0 results"; }
$conn->close();
?>
</table>
</body>
</html>