<?php
//defain constants for db conect
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'kdks6dwq');
define('DB_NAME', 'anime');

// defain constant for pdflib location
define('PDFLIB_PATH', 'W:\\Sanali209\\PHP\\MyAnime');



//database structure anime
// table animeItems
// fields: id, name, description, image, link, type, status, season, year, rating, votes, popularity, last_update, 
//  added_date, last_check, last_check_status, last_check_date, last_check_error, last_check_error_msg, last_check_error_code,
// table animeGenres
// fields: id, name, anime_id
// table animeCharacters_anime
// fields: id, name, anime_id
// table Tags
// fields: id, name, anime_id
// table list_anime
// fields: id, name, anime_id

// app structure
// main view show anime animeItems, animeGenres, animeCharacters_anime, Tags
// item view show onli one  animeItem, and items data , user can edit this data

//app description
// use case:
    // 1. import anime data to database from xml file parsed by php xml parser
    // 1.a by import add onli not exist anime to database
    // 2. show anime data in html table
    // 2.a show anime date viz filters
    // 2.a.1 show anime data not containet in eny user list (unlisted anime)
    // 2.b sort anime data by chusen fields
    // 3.add new anime to database
    // 4.edit anime data in database
    // 5.delete anime data from database
    // 6. create castom list of anime (deffault list: viewed ,vanth votch,favorite,rejected,delayed)
    // 7. add,remove anime items to/from user list
    // 8. add, edit, delete tags forr anime

