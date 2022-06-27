
<?php


//Functions for worcking with database

//defain function forr conect to db and set charset utf-8
function db_connect() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    if (!$result) {
        throw new Exception('Could not connect to database server');
    }
    $connection->set_charset('utf8');
    return $connection
    
    ;
}

//function forr close conect to db
function db_close($connection) {
    $connection->close();
}

//function for check if database table exist
function table_exists($table_name) {
    $connection = db_connect();
    $result = $connection->query("SHOW TABLES LIKE '$table_name'");
    db_close($connection);
    return $result->num_rows > 0;
}

// worcking viz table animeItems


//function forr create database table via sql query
//in this function we create table forr animeItems,
function create_table($table_name) {
    $connection = db_connect();
    $query = "CREATE TABLE $table_name (
        id INT NOT NULL AUTO_INCREMENT,
    )";
    $result = $connection->query($query);
    db_close($connection);
    return $result;
}

//function forr add new record to database table
//in this function we add new record to table forr animeItems
function add_record($table_name, $name, $path, $description, $date, $time, $reiting) {
    $connection = db_connect();
    $query = "INSERT INTO $table_name (name, path, description, date, time, reiting) VALUES ('$name', '$path', '$description', '$date', '$time', '$reiting')";
    $result = $connection->query($query);
    db_close($connection);
    return $result;
}

//function forr get all records from database table animeItems


//function for ubdate record in database table animeItems

// function forr delete record from database table animeItems




// defain function import anime data to database from xml file parsed by php xml parser


