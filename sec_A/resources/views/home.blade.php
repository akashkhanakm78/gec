
@extends("layouts.app")

@section('title', "Home")

@section('content')

<div>This is home page </div>

<h1>Student Form</h1>

<form action="{{ route('students.store') }}" method="post">
    @csrf

<input type="text" name="name" value="{{ old('name') }}" placeholder="Your Name">
@error('name')

{{ $message }}
@enderror

<br>
<input type="email" name="email" value="{{ old('email') }}"  placeholder="Email">
@error('email')

{{ $message }}
@enderror
<br>
<input type="password" name="password" value="{{ old('password') }}"  placeholder="Password">

@error('password')

{{ $message }}
@enderror

<input type="text" name="test" placeholder="test ">

<button type="submit">Submit</button>


</form>

@if (session('success'))

<h3 style="color: green;">{{ session('success') }}</h3>

@endif
<h3></h3>





@endsection