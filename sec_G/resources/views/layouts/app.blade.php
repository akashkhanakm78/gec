<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>@yield('title')</title>
</head>
<body>

        <nav>
            <li><a href="/">Home</a></li>
            <li><a href="/parent">Parent</a></li>
            <li><a href="{{ route('student') }}">Students</a></li>
        </nav>

        <main>
            @yield('content')
        </main>

    <footer>
        <p>&copy; 2023 My App. All rights reserved.</p>
    </footer>
</body>
</html>