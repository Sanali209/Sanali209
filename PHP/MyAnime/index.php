<html>
<head>
<title>Anime Example: index</title>
</head>
<body>
<h1>Anime Example: index</h1>
<p>

</p>
<!-- form for creating item tags-->
<form action="index.php" method="post">
<input type="hidden" name="action" value="create_tags">
<input type="text" name="name" value="">
<input type="submit" value="create tags">
<p>
<!-- view list of all tags-->
<h2>List of all tags</h2>
<table border="1">
<tr>
<th>id</th>
<th>name</th>
<th>anime_id</th>
</tr>
<?php
require_once('config.php');
require_once('functions.php');

// get all tags from database
$connection=db_connect();
// print connection status
echo '<p>connection status: ' . $connection->connect_errno . '</p>';
//check if database is exist on server if no create it
if (!db_exists($connection)) {
    db_create($connection);
}




$result = get_all_tags($connection);
while ($row = $result->fetch_assoc()) {
    echo "<tr>";
    echo "<td>" . $row['id'] . "</td>";
    echo "<td>" . $row['name'] . "</td>";
    echo "</tr>";
}

if (isset($_POST['action']) && $_POST['action'] == 'create_tags') {
    echo "<p>";
    echo "Creating tag: " . $_POST['name'];
    $name = $_POST['name'];
    $connection=db_connect();
    create_tag($connection, $name);
}
?>
</table>

The table of contents is created by calling the <i>index</i> function.
</p>
<!-- create table viz columns name,image,description-->
<table border="1">
<tr>
<td>name</td>
<td>image</td>
<td>description</td>
</tr>

<body>
<html>
