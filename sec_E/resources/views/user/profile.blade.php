

@extends('layouts.app')


@section('title', 'User Page')


@section('content')
<div>
    <h1>
        user name: {{$name}}
        <br>
        user age: {{$age}}
        <br>
        this is user profile
        <br>
       
    </h1>
</div>
@endsection