# Link HEROKU app
https://pbp-assignment-2-roynbb.herokuapp.com/todolist/

Daftar akun dummy:
1. ntgaming (Pass: nicetry1)
2. kokbisa (Pass: bisacuy1)

# Question and answer of this week assignment
## 1. Apa keguanaan {% csrf_token %} pada elemen <form>?
Sebelum menjawab pertanyaan itu, kita harus mengerti CSRF terlebih dahulu. CSRF(Cross-Site Request Forgery) adalah jenis serangan yang membuat pengguna memberikan request ke suatu aplikasi website (berpotensi berbahaya) melalui website yang sebenarnya sedang digunakan. Dengan demikian, bisa saja user memberikan request yang membahayakannya tanpa disadari. CSRF token mencegah serangan tersebut terjadi.

CSRF token adalah suatu nilai bersifat acak, unik, dan rahasia yang diberikan kepada tiap user di tiap sessionnya. CSRF token ini akan dicek saat user memberikan request. Jika token pada request, dalam konteks ini mengirim data melalui form, tidak sesuai dengan token yang sebenarnya, request tersebut akan ditolak.

Jika CSRF token tidak dipakai, user akan menjadi rentan terhadap serangan CSRF.

## 2. Apakah bisa membuat elemen form secara manual?
Ya, kita bisa membuat elemen form secara manual tanpa menggunakan generator. Form tersebut akan dibuat dengan menggunakan method="post" yang menggunakan CSRF token. Di dalamnya kita akan menggunakan input untuk meminta data yang dibutuhkan. Setelah input tersebut diisi dan di-submit, kita dapat mengambil data tersebut dengan menggunakan request.POST.get(name) sesuai dengan name dari input sebelumnya.

## 3. Bagaimana proses alur data dari submisi mulai dari HTML form?
Setelah user mengisi form dan submit isi form tersebut, server akan menerima HTTPRequest sesuai dengan data yang dimasukkan oleh user. Oleh karena itu, data yang telah diberikan dapat diakses melalui request.POST. Lalu, detail-detail data tersebut akan dipakai untuk membuat suatu object Task baru. Namun, program akan mengecek terlebih dahulu apakah data yang diberikan valid, jika ya, program akan melanjutkan proses penyimpanan data. Saat object dengan variable yang sesuai terbentuk, kita dapat katakan bahwa data tersebut sudah tersimpan dalam database. Setelah tersimpan dalam database, kita dapat menampilkan data tersebut melalui html pada laman yang sesuai. Kita dapat mengaksesnya dengan mengambil semua Task yang dimiliki user pada session tersebut dengan menggunakan filter seperti ini `Task.objects.filter(user = request.user)` pada method yang terhubung dengan todolist.html. Setelah itu, kita dapat menggunakan for loop pada html untuk menampilkan seluruh datanya.

## 4. Cara implementasi
1. Menjalankan `python manage.py startapp todolist` untuk membuat aplikasi, serta menambahkan urls.py dan folder templates.
2. Menambahkan path `path('', show_todolist, name='show_todolist')` pada project_django/urls.py, serta membuat function kosong bernama `show_todolist`
3. Membuat class `Task` pada todolist/models.py dengan attribute sesuai soal. Lalu menjalankan migration
4. Membuat function registrasi, login, dan logout pada todolist/views.py seperti yang telah dilakukan pada lab 3. Lalu membuat file html untuk registrasi dan login. Function registrasi akan me-redirect ke html registrasi, login ke html todolist utama (jika berhasil), serta logout menuju ke html login. 
5. Membuat sebuah html yang akan menampilkan daftar-daftar yang sudah ada dalam bentuk tabel, serta menambahkan button untuk menambahkan task dan logout. Setelah itu, mengubah function `show_todolist` yang telah dibuat di awal dan menambahkan context yang akan mengambil semua object Task yang telah di-filter sesuai User saat session tersebut. Menambahkan `@login_required(login_url='/todolist/login/')` di atas function tersebut agar hanya user yang sudah login saja dapat mengakses laman tersebut.
6. Membuat sebuah file html yang berisi form yang akan digunakan User untuk menambahkan data to do list miliknya. Lalu membuat sebuah function pada todolist/views.py yang akan mengambil data dari form html tersebut dan menyimpannya ke database. 
7. Melakukan routing dengan menambahkan path sesuai dengan url yang dibutuhkan pada todolist/urls.py.
8. Membuat 2 user dengan 3 dummy tasks.