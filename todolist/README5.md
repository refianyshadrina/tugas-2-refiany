
1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

Inline CSS :

Adalah kode CSS yang ditulis dengan mendefinisikan `<style>`. Ini berguna untuk kustomisasi design sesuai kebutuhan. 

Kelebihan dan kekurangan : Efektif untuk diterapkan kepada project-project yang berskala kecil karena tidak perlu melakukan langkah import. Lebih bisa di track untuk melakukan perubahan style. Kekurangannya adalah memberikan kontribusi beban kepada size dari file HTML sehingga bisa saja memakan waktu load yang lebih lama.


External CSS :

Adalah kode yang disimpan di luar file HTML dengan mendaftarkan/meng-import link yang mengarahkan kepada file eksternal CSS di HTML. 

Kelebihan dan kekurangan : Load untuk website dari HTML yang ditulis relatif lebih besar karena style tidak ditulis di dalam satu file HTML. Cocok untuk project-project yang besar. Kurang cocok untuk project yang kecil dikarenakan proses render dan import yang bisa saja menyebabkan gagal load.


Internal CSS :

Kode CSS yang disimpan di antara header dan footer `<style>`. Di dalam kode ini terdapat banyak class yang dapat dibuat sesuai kebutuhan yang nantinya bisa diimport ke section/body yang ingin di design di dalam kode.

Kelebihan dan kekurangan : Styling yang cocok untuk project yang kecil karena tidak perlu import-import, mudah di track, namun kurang cocok untuk diterapkan pada project yang berskala besar karena dapat menambahkan beban size file HTML yang dibuat.


2. Jelaskan tag HTML5 yang kamu ketahui

`<body>` : sesuai namanya berfungsi sebagai penopang atau badan untuk suatu dokumen yang ingin ditampilkan dalam dokumen HTML.

`<p>` : Untuk membuat suatu paragraf

`<h1-6>` : untuk membuat header

`<title>` : untuk judul halaman

`<div>` : sebagai pemisah untuk kelompok elemen yang ingin diaplikasikan style yang berbeda

`<form>` : untuk membuat form yang akan disubmit



3. Jelaskan tipe-tipe CSS selector yang kamu ketahui

* Class selector : '.'

Untuk membuat sebuah class yang akan didefinisikan style nya masing-masing oleh user.


* Elemen selector :

Untuk menunjuk kepada class bawaan dari HTML dan tidak memiliki syntax tambahan. Tinggal memanggil nama class tersebut, contohnya 
body {
    // code
}

* ID selector : "#"

Untuk menunjuk kepada sebuah id elemen yang akan di edit


4. Implementasi Checklist Box

Melakukan styling dengan memanfaatkan CSS framework berupa bootstrap. Kemudian menambahkan line `<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">` untuk menambahkan bootstrap ke file html yang di extend oleh file-file lain, yaitu base.html. Halaman login, register, dan create-task di design dengan menambahkan warna pada background pada tag `<style>` di file HTML tersebut. Kemudian, untuk bagian todolist.html menggunakan cards untuk memindahkan tabel todolist ke dalam bentuk cards. Kepada setiap section/div yang ingin mengimplementasikan cards, menambahkan potongan kode class="cards" kepada header setiap section/div tersebut dan menambahkan potongan kode lain jika ingin melakukan design yang lebih rumit.