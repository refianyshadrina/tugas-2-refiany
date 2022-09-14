Nama    : Refiany Shadrina,
NPM     : 2106650185,
Kelas   : PBP - F

1. Bagan MTV :

![BaganMTV_RefianyShadrina_2106650185_F](https://user-images.githubusercontent.com/112610358/190281062-658fee4c-5b46-44ff-a58a-c5ad354da597.jpg)

Teknis utamanya, misal sebuah web aplikasi yang sudah berhasil dibuat seperti URL ini;

https://refi-tugas-2-pbp.herokuapp.com/katalog/

Ketika di cari di search engine seperti web browser, hal ini sama seperti mengirim request ke server heroku app. Response nya adalah HTML.

Proses kerja django pada dasarnya di proses pertama kali pada file yang menyimpan alamat URL (route) dan fungsi yang di setiap route-nya akan di eksekusi. File yang menyimpan informasi ini adalah 'urls.py'. Cara kerja routings melalui urls.py adalah untuk melihat/mencari kepada URL yang di request dan untuk meng-invoke fungsi yang di-import dari views.py. Ketika seorang user mencari sebuah URL di search bar, URL tersebut di pass ke urls.py untuk mencari pattern URL yang sesuai. Jika  tidak ditemukan, akan ditampilkan Error 404. Jika ditemukan, di pass ke views.py untuk di invoke.  Request ini di forward ke views.py untuk ditampilkan. Kemudian, fungsi yang sudah di implementasikan di 'views.py', dalam kasus ini adalah fungsi 'takeData', memproses aktivitas-aktivitas seperti menulis data atau mengambil data dari Model ('models.py'), desain tampilan data dengan template 'HTML', dan mengirim HTTP response ke client. 

2. Penggunaan virtual environment untuk Django

Sebenarnya, penggunaan virtual environment bukan hanya dibutuhkan di Django namun di seluruh aplikasi atau project Python. Jika merujuk dari kebanyakan sumber, virtual environment memang SANGAT dianjurkan untuk semua project atau aplikasi python, meskipun ternyata sebuah aplikasi Django dapat TETAP BERJALAN tanpa menggunakan virtual environment. Virtual enviroment sendiri berupa sebuah tools--yang berisi python interpreter, library, dan script--untuk membuat lingkungan python tertutup dan tidak di akses dari dependencies. Sebuah virtual environment sangat berguna untuk me-manage python packages untuk project yang berbeda-beda, dimana cara kerjanya adalah untuk melindungi user--atau python itu sendiri--dari meng-install package python secara global yang dapat merusak sistem dan project. 

3. Implementasi tugas 2

Poin 1 : Saya membuat sebuah fungsi bernama 'takeData' untuk menampilkan data dari class CatalogItem yang di import dari models. Di sisi lain, saya mengetahui bahwa render() lah yang berperan untuk menyimpan konteks, mencetak, dan mengembalikan objek HTTP response. 

Point 2 : Melalui urls.py, menjalankan sebuah routing Django adalah dengan mengimplementasikan fungsi path() yang menerima sebuah parameter URL dan fungsi dari views.py yang di-import. Maksud dari routing di urls.py sendiri adalah untuk melihat list urls yang sekiranya akan di cari oleh user. Kita dapat menambahkan banyak url ke dalam list urlpatterns. Selain itu, saya juga menambahkan aplikasi katalog ke dalam urls.py yang ada di project_django.

point 3 : Pada katalog.html, saya melakukan iterasi (seperti yang sudah diajarkan di tutorial) untuk list_katalog yang sudah di definisikan/ikut ter-render ke HTML melalui views.py, dimana list_katalog berisi data yang diambil dari class CatalogItem di models.py. Pada dasarnya, isi dari iterasi ini hanya mengambil nama variabel beserta atribut dari objek yang sudah disimpan di list_katalog. Step ini adalah untuk menyambungkan template dengan views dan models.

point 4 : Jika melihat actions yang ada di repositori tugas 2, saya melihat bahwa kode yang sudah saya push memiliki tanda x dimana berarti masih gagal untuk dijalankan, bahkan saya mendapati notifikasi di email yang memberi tahu bahwa deployment gagal. Hal ini karena aplikasi Django sudah siap untuk deploy, dimana template sudah menyediakan dpl.yml untuk pengeksekusian deployment dan .gitignore untuk informasi ke git tentang direktori apa saja yang tidak boleh di push. Namun, status masih gagal dikarenakan terdapat parameter yang belum dikonfigurasi. Saya menyalin API key dari account saya di Heroku serta membuat aplikasi baru, kemudian mendaftarkannya di secrets sesuai dengan API key dan nama aplikasi yang dibuat tersebut. Baru saya ketahui bahwa API key ini adalah untuk autentikasi di semua permintaan API heroku.