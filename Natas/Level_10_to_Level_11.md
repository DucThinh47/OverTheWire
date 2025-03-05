# Natas Level 10 → Level 11

Username: natas11

URL: http://natas11.natas.labs.overthewire.org

# Solution

Truy cập website: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image52.png?raw=true)

Click View sourcecode: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image53.png?raw=true)

Tìm được đoạn mã PHP: 

    $defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

    function xor_encrypt($in) {
        $key = '<censored>';
        $text = $in;
        $outText = '';

        // Iterate through each character
        for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
        }

        return $outText;
    }

    function loadData($def) {
        global $_COOKIE;
        $mydata = $def;
        if(array_key_exists("data", $_COOKIE)) {
        $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
        if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
            if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
            $mydata['showpassword'] = $tempdata['showpassword'];
            $mydata['bgcolor'] = $tempdata['bgcolor'];
            }
        }
        }
        return $mydata;
    }

    function saveData($d) {
        setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
    }

    $data = loadData($defaultdata);

    if(array_key_exists("bgcolor",$_REQUEST)) {
        if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
            $data['bgcolor'] = $_REQUEST['bgcolor'];
        }
    }

    saveData($data);



    ?>

    <h1>natas11</h1>
    <div id="content">
    <body style="background: <?=$data['bgcolor']?>;">
    Cookies are protected with XOR encryption<br/><br/>

    <?
    if($data["showpassword"] == "yes") {
        print "The password for natas12 is <censored><br>";
    }

    ?>

=> Đoạn code này sử dụng mã hóa XOR để bảo vệ cookie, có thể dễ dàng khai thác do biết trước dữ liệu gốc. Có thể khôi phục key bằng kỹ thuật known-plaintext attack. Sau khi có key, tạo cookie hợp lệ để bypass kiểm tra showpassword và lấy mật khẩu cho natas12.

Cookie hiện tại của trang web: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image54.png?raw=true)

=> HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg%3D

Tìm XOR key: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image55.png?raw=true)

=> eDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoe

=> eDWo

Tìm Cookie mới: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image56.png?raw=true)

=> HmYkBwozJw4WNyAAFyB1VUc9MhxHaHUNAic4Awo2dVVHZzEJAyIxCUc5

Thay cookie mới vào trang web: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image57.png?raw=true)

=> Password natas12: yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB

