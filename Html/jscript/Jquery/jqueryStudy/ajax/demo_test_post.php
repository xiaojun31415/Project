<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Untitled Document</title>
</head>

<body>
<?php
$name = isset($_POST['name']) ? htmlspecialchars($_POST['name']) : '';
$url = isset($_POST['url']) ? htmlspecialchars($_POST['url']) : '';
echo '网站名: ' . $name;
echo "\n";
echo 'URL 地址: ' .$url;
?>
</body>
</html>