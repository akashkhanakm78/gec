<div>
    <!-- Life is available only in the present moment. - Thich Nhat Hanh -->

    <h1>Student List</h1>

    <ul>

        @foreach($students as $student)
            <li>{{ $student['name'] }} - {{ $student['age'] }}</li>
        @endforeach
        
    </ul>
</div>
