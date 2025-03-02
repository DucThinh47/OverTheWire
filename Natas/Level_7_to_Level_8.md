# Natas Level 7 → Level 8

Username: natas8

URL: http://natas8.natas.labs.overthewire.org

# Solution

Truy cập URL: 

![img](41)

Click View sourcecode: 

![img](42)

=> Có thể thấy input nhập vào sẽ được so sánh với chuỗi đã được mã hóa $encodedSecret. Hàm mã hóa chuỗi:

    function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
    }

Trước tiên sẽ mã hóa chuỗi $secret bằng base64, sau đó đảo ngược chuỗi base64 đã mã hóa, cuối cùng chuyển chuỗi thành dạng mã hex. 

Viết một đoạn code đơn giản để giải mã: 

    <?php
        $encodedSecret = "3d3d516343746d4d6d6c315669563362";

        // Bước 1: Chuyển hex về nhị phân
        $binarySecret = hex2bin($encodedSecret);

        // Bước 2: Đảo ngược chuỗi
        $reversedSecret = strrev($binarySecret);

        // Bước 3: Giải mã Base64
        $decodedSecret = base64_decode($reversedSecret);

        // Kết quả
        echo "Chuỗi bí mật: " . $decodedSecret;
    ?>

![img](43)

=> Tìm được giá trị $secret: oubWYf2kBq

Quay về trang chủ, nhập giá trị và click Submit: 

![img](44)

=> Password natas9: ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t
