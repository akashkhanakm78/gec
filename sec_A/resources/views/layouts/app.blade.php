<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>@yield('title')</title>
</head>
<body>

<nav>
    <li><a href="/home">Home</a></li>
    <li><a href="{{ route('students.index') }}">Student</a></li>
    <li><a href="/parent">Parent</a></li>
</nav>
@include('global.search')

<div style="min-height: 50vh;">

    @yield('content')
</div>

<footer>
    <p>&copy; 2023 My App. All rights reserved.</p>
</footer>

</body>
</html>