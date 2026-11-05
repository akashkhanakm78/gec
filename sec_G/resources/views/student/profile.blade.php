
@extends('layouts.app')

@section('title', 'Student Profile')


@section('content')
<div>
    <!-- Knowing is not enough; we must apply. Being willing is not enough; we must do. - Leonardo da Vinci -->
    <h1>This is student profile</h1>
    <br>
    
    <h1>Name: {{ $name }}</h1>

</div>
@endsection