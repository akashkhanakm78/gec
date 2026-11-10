<?php

namespace App\Http\Controllers;


use Illuminate\Http\Request;
use Illuminate\Routing\Controllers\HasMiddleware;
use Illuminate\Routing\Controllers\Middleware;
use Override;

class StudentController extends Controller implements HasMiddleware
{

    #[Override]
    public static function middleware(): array
    {
        return [
            new Middleware('check'),
        ];
    }
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        //

        $students = [
            ['id' => 1, 'name' => 'John Doe', 'age' => 20],
            ['id' => 2, 'name' => 'Jane Smith', 'age' => 22],
            ['id' => 4, 'name' => 'Shubham', 'age' => 21],
            ['id' => 5, 'name' => 'Abhijit', 'age' => 25],
            ['id' => 3, 'name' => 'Alice Johnson', 'age' => 19],
        ];

                // return view('student.list')->with('students', $students);
                return view('student.list', compact('students'));

    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(string $id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        //
    }
}
