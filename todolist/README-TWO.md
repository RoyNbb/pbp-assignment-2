# Question and answer of assignment 6
## 1. perbedaan antara asynchronous programming dengan synchronous programming?
Dalam synchronous programming, sutu perlu diselesaikan terlebih dahulu agar operasi lainnya dapat dijalankan. Oleh karena itu, kita perlu menunggu untuk suatu operasi diselesaikan agar kita dapat menjalankan operasi lainnya. Namun dalam asynchronous programming, kita tidak perlu menunggu operasi lainnya. Dalam operasi asychronous, lebih dari 1 operasi dapat dijalankan dalam 1 waktu yang bersamaan.

## 2. Event driven programming?
Event driven programming adalah paradigma pemograman yang mengatur alur program menjadi ditentukan oleh suatu 'event' yang berasal dari pengguna/user. 'Event' tersebut dapat berupa click, hovers, dll. Setelah pengguna melakukan 'event', program akan dieksekusi sesuai dengan 'event' apa yang telah dilakukan oleh pengguna.

## 3. Penerapan asynchronous programming pada AJAX?
Kepanjangan darai AJAX sendiri adalah Asynchronous Javascript and XML. Dengan menggunakan AJAX, kita dapatt mempuat aplikasi web memporses setiap request yang masuk ke server di sisi background(secara asynchronous). Oleh karena itu, dengan AJAX, kita ddapat mengirim dan menerima data dari server tanpa perlu me-reload seluruh halaman.

## Implementasi tugas minggu ini
Dalam mengerjakan tugas minggu ini, saya menggunakan solusi dari lab sebelumnya sebagai referensi.
Agar saya masih dapat menggunakan kode saya yang sebelumnya untuk tutorial selanjutnya, hal yang pertama kali saya lakukan adalah membuat sebuah template html baru ("todolistajax.html") dan menaruh view baru bernama show_todolist_ajax pada path /todolist.

Setelah itu saya menambahkan path /todolist/json pada urls.py yang mengarah pada views berikut 
```
def get_json(request):
    tasks = Task.objects.all()
    return HttpResponse(
        serializers.serialize("json", tasks),
        content_type='application/json'
    )

```
Path ini akan mengembalikan seluruh data task dalam bentuk JSON.

Setelah itu, saya akan mengimplementasikan AJAX dalam menampilkan data tersebut pada laman "todolist.ajax" dengan menggunakan script seperti berikut
```
    $(document).ready(function(){
        refreshToDo();
    });
    
    async function get_json(){
        return fetch("{% url 'todolist:get_json' %}").then((res)=> res.json())
    }

    async function refreshToDo(){
        document.getElementById("containofcards").innerHTML = ""
        const todolist = await get_json()
        let htmlString = ``
        todolist.forEach((item)=>{
            htmlString += `\n
            <div class="containofcards mt-6" >
            <div class="row d-flex justify-content-center">
            <div class="col-md-6">
            <div class="cards">
            <div class="card px-6 py-6 text-center" style="background-color: #EEEEEE;">   
                <h5 class="card-title">${item.fields.title}</h5>
               
                {% if task.is_finished %}
                    <h6 class="card-subtitle mb-2">&#9989;</h6>
                {% else %}
                    <h6 class="card-subtitle mb-2">&#9203;</h6>
                {% endif %}

                <h6 class="card-subtitle mb-2 text-muted">${item.fields.date}</h6>
                <p class="card-text">${item.fields.description}</p>
        
            </div>
            </div>
            </div>
            </div>
            </div>
            `
        })
        document.getElementById("containofcards").innerHTML = htmlString
    }
    refreshToDo()

```
Script tersebut pun dibuat berdasarkan implementasi bootstrap card yang telah saya buat dalam assignment sebelumnya.


Setelah itu, saya membuat sebuah tombol add task dan modal yang saling terhubung berdasarkan  dokumentasi Modal pada Bootstrap. Dalam modal tersebut saya menaruh suatu form yang meminta title dan description dari task yang diinginkan

```
<!-- Button trigger modal -->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#addModal" style="background-color: #EEEEEE; color: #222222" >
            add task
        </button>
<!-- Modal -->
<div class="modal fade" id="addModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">

            <div class="modal-header">
                <h5 class="modal-title">Add To Do</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>

            <div class="modal-body">
                <form id="addform">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label class="col-form-label">Title:</label>
                        <input type="text" name="title" placeholder="Makan bakso" class="form-control" id="title">                
                    </div>
                    <div class="mb-3">
                        <label class="col-form-label">Description: </label>
                        <textarea class="form-control" id="description" name="description" placeholder="biar kenyang" ></textarea>
                    </div>
                </form>
            </div>

            <div class="modal-footer">
                <button type="button" class="btn btn-primary btn-dark" id="addtaskbtn" data-bs-dismiss="modal">add task</button>        
            </div>
        </div>
    </div>
</div>


```

Setelah itu saya menambahkan suatu view yang akan menambahkan task baru tersebut ke dalam database dan sebuah path /todolist/add yang mengarah ke view tersebut
```
@login_required(login_url='/todolist/login/')
def add_todo_ajax(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get("title")
        desc = request.POST.get("description")
        task = Task(user=user, title=title, description=desc)
        
        task.save()
        
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```

Setelah itu, saya menambahkan function pada script yang akan menggunakan view tersebut untuk menambahkan task baru lalu me-refresh todolist tanpa reload seluruh halaman.
Saya pun juga membuat .onclick pada addtaskbtn (button yang ada di modal) mengarah ke function tersebut
```
function addToDo() {
        fetch("{% url 'todolist:add_todo_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#addform'))
        }).then(refreshToDo)
        return false
    }
    document.getElementById("addtaskbtn").onclick = addToDo
```




