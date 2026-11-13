<div>
    <!-- Simplicity is the ultimate sophistication. - Leonardo da Vinci -->

        <h1>Student List</h1>

        @if (session('success'))
         <h4 style="color: green;">{{ session('success') }}</h4>
        @endif

        @foreach ($students as $student)

        <li> student name:{{ $student['name'] }} - Age: {{ $student['age'] }}</li>
        
        @endforeach


        <form action="{{ route('students.store') }} " method="post">
            @csrf 
            <input type="text" name="name">

            <button type="submit">Create student</button>
        </form>
        
        <form action="/students/update " method="post">
            @method("PUT")
            @csrf 
            <input type="text" name="name">
    
            <button type="submit">Update student</button>
        </form>


    </div>
    