
@extends('layouts.app')


@section('title', 'Welcome Page')


@section('content')

<h1>This is my first web project in Laravel</h1>
 @if (session('success'))
      <h4 style="color: green;">{{session('success')}} </h4>  
        @endif

<form action="{{ route('students.store') }}" method="post">
    @csrf

    <input type="text" name="name" value="{{ old('name') }}" placeholder="Your Name">

    @error('name')
    {{ $message }}
    @enderror
    <br>
    <input type="email"  value="{{ old('email') }}"
     name="email"  placeholder="email">
    
    @error('email')
    {{ $message }}
    @enderror
    <br>
    <input type="password" value="{{ old('password') }}" name="password"  placeholder="password">
    
    @error('password')
    {{ $message }}
    @enderror
    <br>

        <input type="text" name="Test" placeholder="Test">
        

    <button type="submit">Submit</button>
</form>



@endsection