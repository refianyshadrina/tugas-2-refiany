1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Asinkronus programming merupakan model peorgramminng yang bersifat multi-thread. Multi thread sendiri merupakan istilah untuk memungkinkan beberapa operasi atau banyak program dapat berjalan secara bersamaaan. Model programmming ini dapat secara bersamaan menjalankan task baru sebelum task sebelumnya selesai dieksekusi. Sebaliknya, sinkronus programming merupakan model programming yang bersifat single-thread, dimana hanya satu buah operasi atau program yang bisa dijalankan dalam satu waktu. Task lain harus menunggu gilirannya dieksekusi sesuai prioritas dan semuanya tidaka berjalan secara bersamaaan.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event drive programming adalah sebuah paradigma yang menggunakan aksi user untuk melakukan sebuah tugas baru. Aksi user ini dapat berupa mouse click, key presses, dan lain-lain yag berhubungan dengan event. Salah satu contoh penerapannya pada tugas ini adalah ketika user menekan tombol addTask pada modal yang ter pop-up sehingga sebuah fungsi add_task akan segera dijalankan. 

3. Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan asynchronus programming pada AJAX adalah ketika terdapat sebuah request dari user (dalam bentuk penekanan sebuah tombol yang berfungsi atau melakukan perubahan data lainnya), halaman HTML yang dilihat oleh user tidak perlu melakukan reload seluruh page. Hal ini terjadi ketika user mengirimkan request berupa POST. Contohnya pada tugas ini adalah ketika user meminta untuk menambahkan add yang mengimplementasikan method POST maka data baru akan langsung ditampilkan tanpa mereload seluruh pagenya. 

4. Implementasi
Membuat fungsi show_json yang mengembalikan seluruh data dalam format JSON. Kemudian menambahkan path /todolist/json ke dalam urls.py sebagai path yang menyimpan informasi data user pada aplikasi todolist. Kemudian di dalam template todolist.html, melakukan iterasi kepada semua data yang dimiliki oleh user dengan pemanggilan fungsi map yang mirip seperti forloop untuk menambahkan data yang ditambahkan berupa card ke dalam tampilan user.

Kemudian membuat path /todolist/add yang berisikan fungsi di views untuk pembuatan objet baru. Di dalam template mengimplementasikan pemanggilan method post yang akan menambahkan sebuah card baru ketika user memanggil method POST lewat modal yang dibuat. Modal ini merupakan implementasi dari bootstrap dengan requirement title dan description untuk membuat sebuah task baru

