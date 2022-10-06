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


# Tugas 4 PBP
## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
- Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis. Cara ini kurang efisien karena setiap tag HTML yang diberikan harus memiliki style masing-masing. Anda akan lebih sulit dalam mengatur website jika hanya menggunakan inline style CSS. Sebab, Inline CSS digunakan hanya untuk mengubah satu elemen saja.
- Internal CSS adalah kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain. Cara ini akan sangat cocok dipakai untuk menciptakan halaman web dengan tampilan yang berbeda. Dengan kata lain, Internal CSS ini bisa dipakai untuk menciptakan tampilan yang unik, pada setiap halaman website.
- Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian <head> pada halaman. Cara ini lebih sederhana dan simpel daripada menambahkan kode CSS di setiap elemen HTML yang ingin Anda atur tampilannya. 

##  Jelaskan tag HTML5 yang kamu ketahui.
- ```<html>``` Tag untuk membuat sebuah dokumen HTML
- ```<h1> to <h6>``` Tag untuk membuat heading
- ```<p>``` Tag untuk membuat paragraf
- ```<br>``` Memasukan satu baris putus
- ```<hr>``` Tag untuk membuat perubahan dasar kata didalam isi
- ```<table>``` Tag untuk membuat tabel
- ```<style>``` Tag untuk membuat informasi style untuk dokumen
- ```<div>``` Tag untuk membuat sebuah bagian dalam dokumen

##  Jelaskan tipe-tipe CSS selector yang kamu ketahui.
- ```*``` Simbol bintang (*) akan fokus pada semua elemen pada halaman.
- ```:hover:``` Menerapkan styling yang aktif ketika cursor berada diatas elemen
- ```:link:``` Menerapkan styling kepada semua link yang belum dibuka user

## Proses pengimplementasian app
1. Mencari template CSS dan HTML yang akan digunakan
2. Mendefinisikan link src bootstrap ke dalam tag
2. Melakukan penyesuaian antara data yang diberikan HTML dengan data Tugas 4 kemarin lalu dimasukkan kedalam HTML tersebut, dan membuat cards untuk masing-masing todolist yang diberikan
3. Selanjutnya, mengubah style dari tampilan bootstrap dengan menambahkan Internal CSS ke dalam tag <style> 
4. Melakukan desain CSS pada halaman login, register, dan create-task
5. Lalu, melakukan ```git add .```, ```git commit```, dan juga ```git push``` yang akan langsung di deploy oleh github
