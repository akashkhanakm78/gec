<div>
    <!-- When there is no desire, all things are at peace. - Laozi -->

    <form action="{{ route('search') }}" method="get">

        <input type="text" name="keywords">
        <button type="submit">Search</button>
    </form>

    @if(session('search'))

    <div>
        <li>Your Query is: {{ session('search') }}</li>
    </div>
    
    @endif
</div>
