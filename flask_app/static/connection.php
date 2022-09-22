<?php
// (A) DATABASE SETTINGS - CHANGE TO YOUR OWN!
define("DB_HOST", "localhost");
define("DB_NAME", "charinfo");
define("DB_CHARSET", "utf8");
define("DB_USER", "root");
define("DB_PASSWORD", "root");

// (B) CONNECT TO DATABASE
try {
    $pdo = new PDO(
    "mysql:host=".DB_HOST.";dbname=".DB_NAME.";charset=".DB_CHARSET,
    DB_USER, DB_PASSWORD, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
    ]
    );
} catch (Exception $ex) { exit($ex->getMessage()); }

<?php
// (B) SAVE IMAGE INTO DATABASE
if (isset($_FILES["upload"])) {
  try {
    // (B1) CONNECT To DATABASE
    require "2-connect-db.php";

    // (B2) READ IMAGE FILE & INSERT
    $stmt = $pdo->prepare("INSERT INTO `images` (`img_name`, `img_data`) VALUES (?,?)");
    $stmt->execute([$_FILES["upload"]["name"], file_get_contents($_FILES["upload"]["tmp_name"])]);
    echo "OK";
  } catch (Exception $ex) { echo $ex->getMessage(); }
}
?>

<?php
// (A) CONNECT TO DATABASE
require "2-connect-db.php";
 
// (B) GET IMAGE FROM DATABASE
$name = "potato.jpg";
$stmt = $pdo->prepare("SELECT `img_data` FROM `images` WHERE `img_name`=?");
$stmt->execute([$name]);
$img = $stmt->fetch();
$img = $img["img_data"];
 
// (C) OUTPUT IMAGE
$ext = pathinfo($name, PATHINFO_EXTENSION);
if ($ext=="jpg") { $ext = "jpeg"; }
header("Content-type: image/" . $ext);
echo $img;

<?php
// (A) CONNECT TO DATABASE
require "2-connect-db.php";
 
// (B) GET IMAGE FROM DATABASE
$name = "potato.jpg";
$stmt = $pdo->prepare("SELECT `img_data` FROM `images` WHERE `img_name`=?");
$stmt->execute([$name]);
$img = $stmt->fetch();
$img = $img["img_data"];

// (C) BASE 64 ENCODE TO OUTPUT TO <IMG> TAG
$img = base64_encode($img);
$ext = pathinfo($name, PATHINFO_EXTENSION);
echo "<img src='data:image/".$ext.";base64,".$img."'/>";
?>
