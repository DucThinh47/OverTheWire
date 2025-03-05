# Natas Level 12 → Level 13

Username: natas13

URL: http://natas13.natas.labs.overthewire.org

# Solution

Truy cập website: 

![img](70)

Click View sourcecode:

![img](71)

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

![img](72)

Send request: 

![img](73)

Thử upload file shell.php và Intercept request: 

![img](74)

Send request: 

![img](75)

=> Website đã lọc file không phải image. 

Thử sửa Content-Type thành image/jpeg: 

![img](76)

Send request: 

![img](77)

Không bypass được. Thử sửa filename thành shell.php.jpg: 

![img](78)

Send request: 

![img](79)

Vẫn không bypass được. 

Thử thay đổi Magic number của file .php thành Magic number của file .jpg. Để nhìn rõ hơn, thêm AAAA vào đầu nội dung file shell.php: 

![img](80)

Sử dụng lệnh *hexeditor shell.php*: 

![img](81)

41 41 41 41 tượng trưng cho 4 chữ A, sửa thành ff d8 ff e0 là tượng trưng cho dạng hex của file .jpg: 

![img](82)

Kiểm tra lại định dạng file sau khi đổi magic number: 

![img](83)

Upload lại file: 

![img](84)

Sửa extension của file website tự sinh thành .php: 

![img](85)

Send request và quan sát website: 

![img](86)

Click vào link file .php này: 

![img](87)

=> Pasword natas14: z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ




