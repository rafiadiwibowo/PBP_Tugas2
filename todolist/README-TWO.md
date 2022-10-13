# README-TWO Tugas 6

## Link Aplikasi Heroku
[App To Do List](https://project2pbp.herokuapp.com/todolist/)

## Perbedaan _asynchronous_ dan _synchronous programming_
Synchronous adalah proses jalannya program secara sequential , disini yang dimaksud sequential ada berdasarkan antrian ekseskusi program. Pada dasarnya semua Bahasa pemrograman menggunakan Asynchronouse terutama PHP. Asynchronous adalah proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian. Synchronous merupakan bagian dari Asynchronous (1 antrian) dimana proses akan dieksekusi secara bersamaan dan untuk hasil tergantung lama proses suatu fungsi synchronous . Asynchronouse hampir disemua Bahasa pemrograman ada namun untuk PHP masih belum ada. PHP sebagai server side hanya menyediakan synchronous namun bisanya di WEB Developers tetap digunakan namun menggunakan AJAX (Asynchronous Javascript And XML) untuk proses Asynchronouse.
## _Event-Driven Programming_
Event-Driven Programming adalah salah satu teknik pemogramman, yang konsep kerjanya tergantung dari kejadian atau event tertentu. misalnya ketika tombol A diklik maka nilai label 2 di tambah nilai label 3 dibagi nilai label 4.  tapi jika tombol A diklik dan ternyata label satu berisikan penjumlahan. maka program yang dijalankan label 2 ditambah label 3. Konsep Event-Driven Programming sama seperti konsep pemogramman menggunakan Procedure.  pemograman yang memiliki input, proses dan output. Namun, ada satu penambahan yang berbeda, yaitu konsep pemilihan untuk mengeksekusi proses programnya. Event-Driven programming juga bisa dibilang suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan keluaran atau tindakan pengguna atau bisa berupa pesan dari program lainnya.

## _Asynchronous programming_ pada AJAX
Membuat view serta url path baru yang mereturn sebuah response JSON. Implementasi asynchronous programming AJAX dalam tugas ini terdapat pada function get serta post untuk mengambil serta mengirim data JSON ke server, serta mengatur tampilan pada Todo list secara asynchronous sesuai data yang ada pada database

## Implementasi aplikasi
- Membuat function baru yang mereturn response berupa JSON
- Menambahkan attribute onClick pada button create task yang diintegrasikan dengan AJAX serta modals pop up
- Menambahkan beberapa function javascript untuk melakukan get dan post request ke server
- Memindahkan component card menjadi response dari post request AJAX dengan data pada card yang didapat dari get request.
- AJAX GET Pada views.py ditambahkan sebuah function untuk mengembalikan Task yang sesuai dengan user logged in dalam bentuk JSON. Views tersebut dihubungkan dengan routing /todolist/json yang ditambahkan di urls.py. Ketika website selesai di-load, dilakukan pemanggilan AJAX GET untuk mendapatkan Task dalam bentuk JSON, kemudian dimasukkan ke dalam tabel.
- AJAX POST Tombol buat task yang sebelumnya melakukan redirect ke todolist/create_task diubah menjadi tidak melakukan redirect, tetapi memunculkan sebuah modal. Modal tersebut dibuat dengan memanfaatkan class pada Tailwind, yaitu hidden. Ketika button buat task diklik, atribut hidden akan dihapus. Sebaliknya, ketika button untuk menutup modal diklik, atribut hidden akan ditambahkan.
- Pada modal tersebut berisi sebuah form. Ketika form tersebut diisi dan button untuk tambah task diklik, akan dilakukan pemanggilan AJAX POST. Data pada fields form akan dikirim ke server dan kemudian diproses. Jika berhasil membuat task baru, callback function dari AJAX POST tersebut akan dipanggil dan menutup modal. 
