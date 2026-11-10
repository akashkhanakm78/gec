<div>
    <!-- Simplicity is the ultimate sophistication. - Leonardo da Vinci -->

    Student name: {{ $student }} <br>

    <form action="{{ route('students.update', $student) }}" method="post">
    @csrf
    @method('PUT')
    <button type="submit">Update Student</button>
</form>

    <form action="{{ route('students.destroy', $student) }}" method="post">
    @csrf
    @method('DELETE')
    <button type="submit">Delete Student</button>
</form>

</div>
