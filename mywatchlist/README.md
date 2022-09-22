LINK HEROKU

https://refi-tugas-2-pbp.herokuapp.com/mywatchlist/

https://refi-tugas-2-pbp.herokuapp.com/mywatchlist/html/

https://refi-tugas-2-pbp.herokuapp.com/mywatchlist/json/

https://refi-tugas-2-pbp.herokuapp.com/mywatchlist/xml/


SCREENSHOTS POSTMAN
 
-MyWatchList
 
![htmlpostman](https://user-images.githubusercontent.com/112610358/191588356-0a2bd8a6-cece-4d2e-aeff-2c7a1fd4d764.jpg)
 
-HTML
 
![mywatchlistapppostman](https://user-images.githubusercontent.com/112610358/191588124-16f1a72f-d630-48d8-8bfd-194ddc0c8995.jpg)
 
-JSON
 
![jsonpostman](https://user-images.githubusercontent.com/112610358/191588398-2a494b54-1f4b-4829-bc10-b404a42a1f5c.jpg)
 
-XML
 
![xmlpostman](https://user-images.githubusercontent.com/112610358/191588447-effb6d65-97f7-40d3-8a0d-3c24b5db0a3f.jpg)
 
 
1. Perbedaan json, html and xml
 
JSON adalah singkatan untuk JavaScript Object Notation untuk menyimpan serta melakuka penukaran data dan informasi untuk dibaca oleh user. JSON memiliki struktur berupa kumpulan value yang yang berurutan dan berpasangan layaknya sebuah object.
 
XML adalah singkatan untuk Extensible Markup Language. XML adalah sebuah cara yang menyederhanakan proses pertukaran dan penyimpanan data. XML akan menyimpan data dan informasi dengan bentuk yang sangat sederhana sehingga server dapat membaca tanpa perlu modifikasi.
 
Secara sederhana, XML dan JSON berfungsi untuk proses penyimpanan, pengiriman, dan pertukaran data sementara HTML beperan untuk menampilkan data dari database.
 
Maka dari itu, untuk lebih memfokuskan kepada perbedaan XML dan JSON. JSON adalah data-oriented dan tidak menyediakan properti display, sementara XML adalah document-oriented dan tidak menyediakan properti displat. Selain itu, terdapat beberapa perbedaan lainnya seperti JSON itu lebih less secured daripada XML.
 
 
2. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
 
Sebuah data platform adalah teknologi yang memungkinkan data untuk dikumpulkan, diubah, dikirim, dan ditukar ke user atau aplikasi. Platform memungkinkan untuk akses data, governance dan untuk security. Menurut saya, data delivery dibutuhkan di platform untuk mensinkronkan perubahan data yang ada di server dengan behaviour yang akan ditampilkan kepada user.
 
3.  Bagaimana cara mengimplementasikan checklist di atas.
 
-Membuat aplikasi mywatchlist dengan python manage.py startapp mywatchlist
-Menambahkan path mywatchlist dengan list semua kemungkinan url di url patterns yang ada di urls.py
-Membuat sebuah model dengan menambahkan class yang di extend dari models.model di models.py serta menambahkan beberapa atribut dari tabel yang dibutuhkan
-Menambahkan 10 data di database (initial_mywatchlist_data.json) yang perlu selalu di load dengan mengambil data dari models.py
-Mengimplementasikan fitur XML, HTML, dan JSON dengan menambahkan fungsi yang menerima dan menampilkan data dalam bentuk xml/json/html lewat fitur HTTP response serta menambahkan path xml/ dan json/ dan html/ di urls.py
-Membuat routing dengan menambahkan path xml, html, dan json pada list url paterns di urls.py
-Melakukan deployment sudah auto karena repositori tugas-2-refiany sudah pernah di deploy sehingga submitan yang baru di push akan auto ter deploy (sesuai dengan penjelasan yang di readme.md katalog)
