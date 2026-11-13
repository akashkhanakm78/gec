@extends('layouts.app')

@section('title', 'Home')


@section('content')


<div>
    <!-- Life is available only in the present moment. - Thich Nhat Hanh -->
     <!-- <h1>This is my first web project in laravel</h1> -->

     <a href="{{ route('student') }}">Student</a>

    <h1> Student form</h1>
       @if (session('success'))
         <h4 style="color: green;">{{ session('success') }}</h4>
        @endif

    <form action='{{route('students.store')}}' method="post">
        @csrf

            <input type="text"  name="name" value="{{ old('name') }}" placeholder="Your Name"/>
            <br>
            <!-- @error('name')
            {{ $message }}
            @enderror -->
            <br/>
            <input type="email"  name="email" value="{{ old('email') }}" placeholder="Your Email"/>

             <br>
            <!-- @error('email')
            {{ $message }}
            @enderror -->
            <br/>
            <input type="password"  name="password" value="{{ old('password') }}" placeholder="Your Password"/>
             <br>
            <!-- @error('password')
            {{ $message }}
            @enderror -->
            <br/>
            <input type="password"  name="password_confirmation" value="{{ old('password_confirmation') }}" placeholder="Your Confirm Password"/>
             <br>
            <!-- @error('password_confirmation')
            {{ $message }}
            @enderror -->
            <br/>
            <!-- <input type="text" name="unwanted" placeholder="unwanted"> -->

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


            <button type="submit">Submit</button>


    </form>
   



</div>

@endsection



