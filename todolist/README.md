link : https://refi-tugas-2-pbp.herokuapp.com/todolist/login/?next=/todolist/


Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

Sebelumnya, CSRF merupakan singkatan dari Cross-site Request Forgery. Dalam bahasa Indonesia, forgery merupakan pemalsuan atau tiruan. Dari arti nya ini, kita dapat mengidentifikasi CSRF sebagai suatu gangguan/ancaman sebuah site yang dapat saja disebabkan oleh malicious site atau malicious user (penjahat situs). Penyerangan ini biasanya menirukan sebuah site untuk mengincar identitas user yang ada di site tersebut. 

{% csrf_token %} adalah template yang disediakan oleh Django untuk memberikan pertahanan terhadap CSRF dengan mudah. Cara kerjanya adalah dengan menetapkan sebuah token CSRF yang berupa suatu nilai rahasia yang khas untuk site tertentu, sehingga tidak ada lebih dari satu site yang memiliki token CSRF yang sama. Token ini di set oleh CsrfViewMiddleware di dalam settings.py.

Maka dari itu, tanpa menambahkan potongan kode {% csrf_token %}, form yang do request oleh user akan lebih rentan terkena gangguan dan serangan CSRF.


Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Ya. Caranya adalah menambahkan atribut method dan action di dalam tag form yang dibuat. Kemudian membuat sebuah field untuk mengisi form dengan menambahkan tag input. 


Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Ketika user mengisi form dan menekan tombol submit, submitan tersebut dikirim sebagai request kepada views dan mencari function yang sesuai untuk mengeksekusi request user (dalam views.py di project ini adalah fungsi create_task). Fungsi tersebut kemudian memproses form yang dibuat melalui file form_todolist.py dan memproses data tersebut dengan mengambilnya dari model dan database. Disini, views kemudian mengembalikan data tersebut dalam bentuk HTTP response yang berupa halaman utama todolist namun dengan data yang ditambahkan. Namun, agar pengaksesan data pada database tidak mengembalikan data yang salah, perlu penspesifikan data siapa yang akan diambil, yaitu mengambil data dari user yang sedang login. 


Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

-Membuat aplikasi bernama todolist dengan mengeksekusi perintah python manage.py startapp todolist dan menambahkan list 'todolist' pada installed apps in project_django

-Menambahkan path todolist dengan membuat file bernama urls.py pada app dan menambahkan url tersebut kepada url patterns yang ada di project django

-Membuat model Task dengan membuat class Task yang mengimport dan memanfaatkan models di models.py. Lalu membuat atribut sesuai modelnya masing-masing kemudian di migrate.

-Menambahkan function register untuk menampilkan halaman register.html, function login untuk menampilkan halaman login user, function logout untuk memproses logout, dan halaman creat task untuk membuat task baru. Kemudian, membuat function show_todolist untuk menampilkan halaman utama todolist dengan template html todolist.

-Membuat halaman form dengan menambahkan filee create-task.html

-Melakukan push ke github sehingga sudah otomatis terdeploy