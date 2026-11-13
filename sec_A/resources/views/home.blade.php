@extends("layouts.app")

@section('title', "Home")

@section('content')

<div>This is home page </div>

<h1>Student Form</h1>

@if (session('path'))

<img style="width: 200px;" src="/storage/{{ session('path') }}" alt="">

@endif

<form action="{{ route('students.store') }}" enctype="multipart/form-data" method="post">
    @csrf

    <label for="file">Document</label>
    <input type="file" id="file" name="document">
    <br>
    @error('document')
    <div>{{ $message }}</div>
    @enderror

    <br>
    <input type="text" name="name" value="{{ old('name') }}" placeholder="Your Name">
    @error('name')

    {{ $message }}
    @enderror

    <br>
    <input type="email" name="email" value="{{ old('email') }}" placeholder="Email">
    @error('email')

    {{ $message }}
    @enderror
    <br>
    <input type="password" name="password" value="{{ old('password') }}" placeholder="Password">

    @error('password')

    {{ $message }}
    @enderror
    <br>
    <input type="text" name="test" placeholder="test ">
    <br>
    @if ($errors->any())
    <div class="alert alert-danger">
        <strong>Please correct the following errors:</strong>
        <ul>
            @foreach ($errors->all() as $error)
            <li>{{ $error }}</li>
            @endforeach
        </ul>
    </div>
    @endif

    <!-- <select name="city" id="city">

            <option value="">Please Select</option>
            <option value="bhubaneswar"  {{old('city') == 'bhubaneswar' ? 'selected' : ''}} >Bhubaneswar</option>
            <option value="kolkata" {{old('city') == 'kolkata' ? 'selected' : ''}}>Kolkata</option>
            <option value="durgapur" {{old('city') == 'durgapur' ? 'selected' : ''}}>Durgapur</option>
        </select> -->
    <br>

    <button type="submit">Submit</button>


</form>

@if (session('success'))

<h3 style="color: green;">{{ session('success') }}</h3>

@endif
<h3></h3>





@endsection