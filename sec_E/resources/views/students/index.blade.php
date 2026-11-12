<div>
    <!-- I begin to speak only when I am certain what I will say is not better left unsaid. - Cato the Younger -->

        @if (session('success'))
      <h4 style="color: green;">{{session('success')}} </h4>  
        @endif

    <div>
        <h1>Students</h1>
        <ul>
            @foreach($students as $student)
                <li>{{ $student['name'] }} - {{ $student['email'] }}</li>
                <a href="{{ route('students.show', $student['email']) }}">View</a>
            @endforeach
        </ul>
    </div>

<form action="{{ route('students.store') }}" method="post">
    @csrf
    <input type="text" name="username">

    <button type="submit">Create Student</button>
</form>




</div>
