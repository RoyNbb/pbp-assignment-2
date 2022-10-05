# Question and answer of week 5 assignment
## perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style
Internal CSS 
Kode CSS diletakkan di dalam bagian "head". Dengen metode ini, kode CSS hanya akan aktif di file itu saja.
Kelebihan:
- Class dan ID  dapat digunakan internal stylesheet
- perubahan terjadi pada 1 halaman saja
- Memudahkan developer untuk memiliki tampilan yang unik tiap lamannya
Kekurangan:
- Tidak dapat digunakan oleh HTML lainnya

Inline CSS
Kode CSS diletakkan pada tiap tag HTML secara langsung (style="...").
Kelebihan:
- Cocok untuk perbaikan singkat dan pengujian simpel
Kekurangan:
- Perlu menuliskan CSS secara satu-satu dari tiap elemen yang ingin di-"dekorasi"

External CSS
Kode CSS diletkkan pada file yang berbeda dari  HTML yang akan menggunakannya.
Kelebihannya:
- penulisan file menjadi lebih rapih
- CSS tersebut dapat digunakan oleh lebih dari satu file HTML
Kekurangan:
- Laman tidak akan tampil secara sempurna jika file CSS belum selesai dipanggil


## Jelaskan tag HTML5 yang kamu ketahui.
Tag pada html akan menentukan konten pada html akan ditampilkan. Ada begitu banyak tag dallam HTML5, diantaranya adalah:
- ```<div>``` menyatakan seksi/bagian dalam dokumen
- ```<form>``` menyatakan HTML form berisi input user
- ```<html>``` menyatakan root dari dokumen HTML
- ```<a>``` menyatakan hyperlink
- ```<button>``` menyatakan tombol yang dapat

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
- Selektor Tag 
```
a {
    color: blue;
}
```
selektor yang akan memilih elemen berdasarkan nama tag.
- Selektor Class
```
.class1{
    color: black;
}
```
selektor yang akan memilih elemen berdasarkan nama class yang diberikan
- Selektor ID
```
#header{
    color: white;
}
```
selektor yang akan memilih elemen berdasarkan  ID yang diberikan(ID bersifat unik).
- Selektor Universal
```
*{
    border: 2px solid cyan;
}
```
selektor yang akan memilih semua elemen dalam jangkauannya
- Selektor Atribut
```
*{
input[type=contohType] {
    padding: 5px;
    border: 2px solid cyan;
}}
```
selektor yang akan memilih elemen dengan atribut tertentu

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Dalam melakukan tugas 5 ini, saya memutuskan untuk menggunak bootstrap untuk memudahkan saya dalam mendekorasi tiap halaman situ tersebut. Oleh karena itu, yang pertama kali saya lakukan adalah mengambil CDN dan menaruhnya pada base.html. 

Setelah itu, saya mulai mengelompokkan tags yang ada dengan menggunakan ```<div>``` sesuai dengan kebutuhan saya. Lalu saya menentukan class dari tags untuk menerapkan css menggunakan bootstrap. Selain itu, saya pun juga menerapkan inline dan internal css untuk melengkapi.

Dalam menerapkan CSS, saya pun tak lupa untuk menerapkan cards untuk menampilkan tiap task dengan memodifikasi ```todolist.html```. Dalam bagian for loop tiap task, saya mengganti menambahkan baris pada list menjadi membuat sebuah card baru. Adapun tema dari tampilan laman saya yaitu monokrom minimalistik yang terinspirasi dari lugu tulus :).


