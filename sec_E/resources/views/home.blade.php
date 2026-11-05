<h2>Fruit List</h2>

<ul>
    @foreach($fruits as $fruit)
        <li>{{ $loop->iteration }}. {{ $fruit }}</li>
    @endforeach
</ul>