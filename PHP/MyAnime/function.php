
<?php
require_once "config.php";

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

//function forr check if exist database on sql server
function db_exists($connection)
{
    $query = "SHOW DATABASES LIKE '" . DB_NAME . "'";
    $result = $connection->query($query);
    if ($result->num_rows > 0) {
        return true;
    } else {
        return false;
    }
}

// create database 
function db_create($connection) {
    $query = "CREATE DATABASE " . DB_NAME;
    $result = $connection->query($query);
    if (!$result) {
        throw new Exception('Could not create database');
    }
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
//in this function we create table forr animeItems
function create_table_AnimeItem($conenection) 
{
    $sql = "CREATE TABLE animeItems (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        description VARCHAR(255) NOT NULL,
        image VARCHAR(255) NOT NULL,
        link VARCHAR(255) NOT NULL,
        type VARCHAR(255) NOT NULL,
        status VARCHAR(255) NOT NULL,
        season VARCHAR(255) NOT NULL,
        year VARCHAR(255) NOT NULL,
        rating VARCHAR(255) NOT NULL,
        votes VARCHAR(255) NOT NULL,
        popularity VARCHAR(255) NOT NULL,
        last_update VARCHAR(255) NOT NULL,
        added_date VARCHAR(255) NOT NULL,
        last_check VARCHAR(255) NOT NULL,
        last_check_status VARCHAR(255) NOT NULL,
        last_check_date VARCHAR(255) NOT NULL,
        last_check_error VARCHAR(255) NOT NULL,
        last_check_error_msg VARCHAR(255) NOT NULL,
        last_check_error_code VARCHAR(255) NOT NULL,
        PRIMARY KEY (id)
    )";
    $result = $conenection->query($sql);
    if (!$result) {
        throw new Exception('Could not create table: ' . $conenection->error);
    }
}


//function forr add new record to database table
function add_record_AnimeItem($conenection, $name, $description, $image, $link, $type, $status, $season, $year, $rating, $votes, $popularity, $last_update, $added_date, $last_check, $last_check_status, $last_check_date, $last_check_error, $last_check_error_msg, $last_check_error_code) {
    //check if 
    
    $sql = "INSERT INTO animeItems (name, description, image, link, type, status, season, year, rating, votes, popularity, last_update, added_date, last_check, last_check_status, last_check_date, last_check_error, last_check_error_msg, last_check_error_code) VALUES ('$name', '$description', '$image', '$link', '$type', '$status', '$season', '$year', '$rating', '$votes', '$popularity', '$last_update', '$added_date', '$last_check', '$last_check_status', '$last_check_date', '$last_check_error', '$last_check_error_msg', '$last_check_error_code')";
    $result = $conenection->query($sql);
    if (!$result) {
        throw new Exception('Could not create record: ' . $conenection->error);
    }
}

//function forr get all records from database table animeItems
function get_all_records_AnimeItem($conenection) {
    $sql = "SELECT * FROM animeItems";
    $result = $conenection->query($sql);
    if (!$result) {
        throw new Exception('Could not get records: ' . $conenection->error);
    }
    return $result;
}


//function for ubdate record in database table animeItems
function upd_record_AnimeItem($conenection, $id, $name)
{
    $sql = "UPDATE animeItems SET name = '$name' WHERE id = '$id'";
    $result = $conenection->query($sql);
    if (!$result) {
        throw new Exception('Could not update record: ' . $conenection->error);
    }
}




// function forr delete record from database table animeItems
function del_record_AnimeItem($conenection, $id)
{
    $sql = "DELETE FROM animeItems WHERE id = '$id'";
    $result = $conenection->query($sql);
    if (!$result) {
        throw new Exception('Could not delete record: ' . $conenection->error);
    }
}

// function create table forr tags via sql query
function create_table_tags($connection)
{
    $query = "CREATE TABLE tags (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        PRIMARY KEY (id),
        
    )";
    $result = $connection->query($query);
    return $result;

}

// add new record to table tags
function add_record_tags($connection, $name, $anime_id)
{
    $query = "INSERT INTO tags (name, anime_id) VALUES ('$name', '$anime_id')";
    $result = $connection->query($query);
    return $result;
}

// update record in table tags
function upd_record_tags($connection, $id, $name, $anime_id)
{
    $query = "UPDATE tags SET name = '$name', anime_id = '$anime_id' WHERE id = '$id'";
    $result = $connection->query($query);
    return $result;
}

// delete record from table tags
function del_record_tags($connection, $id)
{
    $query = "DELETE FROM tags WHERE id = '$id'";
    $result = $connection->query($query);
    return $result;
}

function get_all_records_tags($connection)
{
    $query = "SELECT * FROM tags";
    $result = $connection->query($query);
    return $result;
}







// defain function import anime data to database from xml file parsed by php xml parser


