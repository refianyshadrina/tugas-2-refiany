Nama    : Refiany Shadrina,
NPM     : 2106650185,
Kelas   : PBP - F

1. Bagan MTV :

![BaganMTV_RefianyShadrina_2106650185_F](https://user-images.githubusercontent.com/112610358/190288031-af6f22a9-4868-42ab-98f8-3c6521418759.jpg)

Teknis utamanya, misal sebuah web aplikasi yang sudah berhasil dibuat seperti URL ini;

https://refi-tugas-2-pbp.herokuapp.com/katalog/

Ketika di cari di search engine seperti web browser, hal ini sama seperti mengirim request ke server heroku app. Response nya adalah HTML.

Proses kerja django pada dasarnya di proses pertama kali pada file yang menyimpan alamat URL (route) dan fungsi yang di setiap route-nya akan di eksekusi. File yang menyimpan informasi ini adalah 'urls.py'. Cara kerja routings melalui urls.py adalah untuk melihat/mencari kepada URL yang di request setelah user/client mengirimkan link URL untuk dicari dan untuk meng-invoke fungsi yang di-import dari views.py. Ketika seorang user mencari sebuah URL di search bar, URL tersebut di pass ke urls.py untuk mencari pattern URL yang sesuai. Jika  tidak ditemukan, akan ditampilkan Error 404. Jika ditemukan, di pass ke views.py untuk di invoke, views.py akan bekerja untuk menampilkan tampilan url yang di request yang tersambung ke templates dan models.  Request ini di forward ke views.py untuk ditampilkan. Kemudian, fungsi yang sudah di implementasikan di 'views.py', dalam kasus ini adalah fungsi 'show_katalog', memproses aktivitas-aktivitas seperti menulis data atau mengambil data dari Model ('models.py'), desain tampilan data dengan template 'HTML', dan mengirim HTTP response ke client (HTML). View memilih template sesuai url yang di response kepada template dengan format <filename>.html, sehingga pemenuhan request client berjalan dengan baik. Di sisi lain, model (models.py) menyimpan data dan ter-connect dengan database. Model menyediakan sebuah data kepada views untuk dikirimkan kepada template.

2. Penggunaan virtual environment untuk Django

Sebenarnya, penggunaan virtual environment bukan hanya dibutuhkan di Django namun di seluruh aplikasi atau project Python. Python tidak begitu menyediakan manajemen dalam dependencies. Tidak menyalakan virtual environment bisa saja menyebabkan polusi sistem. Ketika akan menggunakan bahasa python, saya mengingat di sebuah akun youtube bahwa install python di macOS atau Linux membutuhkan virtual environment yang aktif. Baru saya ketahui baru-baru ini, jika tidak dilakukan, ketika seorang user meng-install package kepada sistem operasi global python, package-package ini akan tercampur kepada package yang relevan dengan sistem. Bahkan dapat menyebabkan package yang di-install tertumpuk (over-written) dan hilang. Sama halnya dengan Django. Jika merujuk dari kebanyakan sumber, virtual environment memang SANGAT dianjurkan untuk semua project atau aplikasi python, meskipun ternyata sebuah aplikasi Django dapat TETAP BERJALAN tanpa menggunakan virtual environment. Penggunaan virtual environment menghindari sebuah project django dari overwriting. Kesimpulannya, virtual enviroment sendiri berupa sebuah tools--yang berisi python interpreter, library, dan script--untuk membuat lingkungan python tertutup dan tidak di akses dari dependencies. Sebuah virtual environment sangat berguna untuk me-manage python packages untuk project yang berbeda-beda, dimana cara kerjanya adalah untuk melindungi user--atau python itu sendiri--dari meng-install package python secara global yang dapat merusak sistem dan project. 

3. Implementasi tugas 2

Poin 1 : Saya membuat sebuah fungsi bernama 'show_katalog' untuk menampilkan data dari class CatalogItem yang di import dari models. Di sisi lain, saya mengetahui bahwa render() lah yang berperan untuk menyimpan konteks, mencetak, dan mengembalikan objek HTTP response (HTML) sesuai request client.

Point 2 : Melalui urls.py, menjalankan sebuah routing Django adalah dengan mengimplementasikan fungsi path() yang menerima sebuah parameter URL dan fungsi dari views.py yang di-import. Maksud dari routing di urls.py sendiri adalah untuk melihat list urls yang sekiranya akan di cari oleh user. Kita dapat menambahkan banyak url ke dalam list urlpatterns. Selain itu, saya juga menambahkan aplikasi katalog ke dalam urls.py yang ada di project_django, serta menambahkan list url pattern katalog dengan menambahkan line 'path('katalog/', include('katalog.urls')),' pada urlpattern di urls.py yang terletak di file project_django

point 3 : Pada katalog.html, saya melakukan iterasi (seperti yang sudah diajarkan di tutorial) untuk list_katalog yang sudah di definisikan/ikut ter-render ke HTML melalui views.py. Disini, list_katalog menyimpan data yang diambil dari class CatalogItem di models.py. Pada dasarnya, isi dari iterasi ini hanya mengambil nama variabel beserta atribut dari objek yang sudah disimpan di list_katalog. Step ini adalah untuk menyambungkan template dengan views dan models.

point 4 : Jika melihat actions yang ada di repositori tugas 2, saya melihat bahwa kode yang sudah saya push memiliki tanda x dimana berarti masih gagal untuk dijalankan, bahkan saya mendapati notifikasi di email yang memberi tahu bahwa deployment gagal. Hal ini karena aplikasi Django sudah siap untuk deploy, dimana template sudah menyediakan dpl.yml untuk pengeksekusian deployment dan .gitignore untuk informasi ke git tentang direktori apa saja yang tidak boleh di push. Namun, status masih gagal dikarenakan terdapat parameter yang belum dikonfigurasi. Saya menyalin API key dari account saya di Heroku serta membuat aplikasi baru, kemudian mendaftarkannya di secrets sesuai dengan API key dan nama aplikasi yang dibuat tersebut. Baru saya ketahui bahwa API key ini adalah untuk autentikasi di semua permintaan API heroku. Ketika menjalankan aplikasi yang saya buat melalui heroku, by default tampilan akan menampilkan example_app yang berisi 'Hello World'. Karena kita ingin melihat aplikasi katalog yang dibuat, maka perlu menambahkan url pattern seperti yang sudah didaftarkan di urls.py, yaitu menambahkan /katalog/ di akhir url. Pada saat ini, aplikasi katalog sudah dapat dilihat. 

Sumber :
https://cupofcode.blog/intro-to-django/
https://realpython.com/python-virtual-environments-a-primer/#:~:text=One%20of%20your%20projects%20might,use%20a%20Python%20virtual%20environment.