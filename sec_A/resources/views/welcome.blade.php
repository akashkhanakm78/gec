<h1>This is my first website in laravel</h1>


<form action="/post" method="post">

@csrf
 <input type="text" name="name ">
<button type="submit">Submit Post</button>
</form>

<form action="{{ route('put') }}" method="post">

@csrf
@method('PUT')
 <input type="text" name="name ">
<button type="submit">Submit PUT</button>
</form>