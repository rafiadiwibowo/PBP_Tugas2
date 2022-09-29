# Tugas 4 PBP
### Muhammad Rafi Adiwibowo
### 210663855
### PBP - A

## Link aplikasi Heroku
https://project2pbp.herokuapp.com/todolist/

## Apa kegunaan ```{% csrf_token %}``` pada elemen ```<form>?``` Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen ```<form>```?
- CSRF Token sendiri merupakan sebuah random string yang di-generate setiap kali halaman form muncul. Biasanya di tiap POST request, token tersebut disisipkan sebagai header, atau form data, atau query string. Pada elemen ```<form>``` fungsi ```{% csrf_token %}``` tersebut adalah untuk memastikan user yang terautentikasi adalah benar-benar user yang mengirim data di ```<form>``` dengan cara divalidasikan oleh field ```csrfmiddlewaretoken``` sesuai dengan value tersebut. tanpa adanya ```{% csrf_token %}``` akan menjadikan user yang tidak terautentikasi dapat mengakses halaman tersebut.

## Apakah kita dapat membuat elemen ```<form>``` secara manual (tanpa menggunakan generator seperti ```{{ form.as_table }}```)? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
- Kita dapat membuat form tanpa menggunakan ```{{ form.as_table }}``` dengan cara manual yaitu membuat sebuah elemen ```<form>``` sendiri dengan memasukkan url untuk fungsi yang kita panggil dengan method ```POST```. Lalu, diberikan nama agar data yang dimasukkan dapat dipanggil dengan ```request.POST.get(<nama_field_form>)```.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
- Alur yang dilakukan oleh pengguna yaitu dengan melakukan request pada browser, lalu browser tersebut akan merespon dengan mengirim ```POST``` ke server saat user membuat request. Setelah itu akan ada perubahan pada server dengan event ```POST```. Lalu, ```views.py``` akan merespon dengan mengupdate data dengan melakukan mereturn data sehingga data akan ditampilkan.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat directory baru dengan melakukan ```python manage.py startapp todolist```
2. Melakukan routing app pada ```project_django/urls.py```, dan juga ```todolist/urls.py```
3. Membuat template yang dapat diakses url pada file ```templates``` yang akan diisi seperti ```login.html```, ```create_task.hml```, ```register.html```, dan juga ```todolist.html```.
4. Membuat file baru yaitu ```todolist/forms.py``` untuk menampilkan ```create_task.html``` yang digunakan untuk mensubmit data yang akan ditampilkan
5. Membuat fungsi yang dibutuhkan pada ```todolist/views.py``` untuk login, logout, register, dan juga membuat task dan lain lain. Lalu fungsi-fungsi tersebut ditampilkan pada ```templates/todolist.html```
6. Melakukan deploy project dengan cara ```git add .```, ```git commit```, dan juga ```git push``` yang akan langsung ke deploy oleh github
