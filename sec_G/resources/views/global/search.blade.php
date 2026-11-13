<div>
    <!-- Breathing in, I calm body and mind. Breathing out, I smile. - Thich Nhat Hanh -->
            <form action="{{ route('search') }}" method="get">
             
            <label for="search">Search:</label>
            <input type="text" id="search" name="qurey" placeholder="Type....">
                <button type="submit">Search</button>
            </form>

            @if (session('query'))
            {{session('query')  }}
            
            @endif
</div>
