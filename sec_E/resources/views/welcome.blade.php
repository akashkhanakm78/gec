@extends('layouts.app')


@section('title', 'Welcome Page')


@section('content')

<h1>This is my first web project in Laravel</h1>
<!-- @if (session('success'))
<h4 style="color: green;">{{session('success')}} </h4>
@endif -->

<style>
    .is-error {
        color: green;
        scale: 120%;
    }
</style>
@if (session('path'))
<img src="/storage/{{session('path')}}"  style="width: 100px;" alt="">
@endif

<form action="{{ route('students.store') }}" 
enctype="multipart/form-data" method="post">
    @csrf

    <label for="doc">Document</label>
    <input type="file" id="doc" name="document">
    <br>
    @error('document')
    <div>{{ $message }}</div>
    @enderror

    <br>

    <input type="text" name="name" class="@error('name') is-error @enderror" value="{{ old('name') }}" placeholder="Your Name">

    <!-- @error('name')
    {{ $message }}
    @enderror -->
    <br>
    <input type="email" value="{{ old('email') }}"
        name="email" placeholder="email">

    <!-- @error('email')
    {{ $message }}
    @enderror -->
    <br>
    <input type="password" value="{{ old('password') }}" name="password" placeholder="password">

    <!-- @error('password')
    {{ $message }}
    @enderror -->
    <br>
    <input type="password" value="{{ old('password_confirmation') }}" name="password_confirmation" placeholder="Confirm password">
    <!-- 
    @error('password_confirmation')
    {{ $message }}
    @enderror -->
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


    <!-- <select name="city">
        <option value="">Choose city</option>
        
        <option value="Durgapur" {{ old('city') == 'Durgapur' ? 'selected' : '' }}>
            Durgapur
        </option>


        <option value="Kolkata" {{ old('city') == 'Kolkata' ? 'selected' : '' }}>
            Kolkata
        </option> -->

    </select>


    <button type="submit">Submit</button>
</form>



@endsection