# Natas Level 12 → Level 13

Username: natas13

URL: http://natas13.natas.labs.overthewire.org

# Solution

Truy cập website: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image70.png?raw=true)

Click View sourcecode:

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image71.png?raw=true)

Đoạn mã PHP: 

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

        $err=$_FILES['uploadedfile']['error'];
        if($err){
            if($err === 2){
                echo "The uploaded file exceeds MAX_FILE_SIZE";
            } else{
                echo "Something went wrong :/";
            }
        } else if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
            echo "File is too big";
        } else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
            echo "File is not an image";
        } else {
            if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
                echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
            } else{
                echo "There was an error uploading the file, please try again!";
            }
        }
    } else {
    ?>

Hàm *exif_imagetype($_FILES['uploadedfile']['tmp_name'])* check xem file upload có phải image không.

Tuy nhiên vẫn tồn tại lỗ hổng trong đoạn code: 

- Có thể bypass kiểm tra exif_imagetype() bằng header giả. 
- Không kiểm tra extension thật sự của file.
- Không chặn thực thi PHP trong thư mục upload
- Không giới hạn kích thước file từ PHP

Thử upload 1 file JPEG hợp lệ và Intercept request: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image72.png?raw=true)

Send request: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image73.png?raw=true)

Thử upload file shell.php và Intercept request: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image74.png?raw=true)

Send request: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image75.png?raw=true)

=> Website đã lọc file không phải image. 

Thử sửa Content-Type thành image/jpeg: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image76.png?raw=true)

Send request: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image77.png?raw=true)

Không bypass được. Thử sửa filename thành shell.php.jpg: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image78.png?raw=true)

Send request: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image79.png?raw=true)

Vẫn không bypass được. 

Thử thay đổi Magic number của file .php thành Magic number của file .jpg. Để nhìn rõ hơn, thêm AAAA vào đầu nội dung file shell.php: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image80.png?raw=true)

Sử dụng lệnh *hexeditor shell.php*: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image81.png?raw=true)

41 41 41 41 tượng trưng cho 4 chữ A, sửa thành ff d8 ff e0 là tượng trưng cho dạng hex của file .jpg: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image82.png?raw=true)

Kiểm tra lại định dạng file sau khi đổi magic number: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image83.png?raw=true)

Upload lại file: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image84.png?raw=true)

Sửa extension của file website tự sinh thành .php: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image85.png?raw=true)

Send request và quan sát website: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image86.png?raw=true)

Click vào link file .php này: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image87.png?raw=true)

=> Pasword natas14: z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ




