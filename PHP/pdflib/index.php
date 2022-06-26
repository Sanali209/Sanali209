<html>
<head>
<title>PDFlib Example: index</title>
</head>
<body>
<h1>PDFlib Example: index</h1>
<p>
<i>index</i> is a simple test page for the indexing functions.
</p>
<p>
<i>index</i> creates a PDF file with a table of contents.
</p>
<p>
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
//create html table forr show data from database
// function create_table_html($table_name) {

<?php

//add required includes once
require_once('config.php');
require_once('functions.php');

$connection = db_connect();
