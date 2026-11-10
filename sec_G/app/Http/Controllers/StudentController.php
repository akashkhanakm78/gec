<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Routing\Controllers\HasMiddleware;
use Illuminate\Routing\Controllers\Middleware;
use Override;

class StudentController extends Controller implements HasMiddleware
{
    /**
     * Display a listing of the resource.
     */

    #[Override]
    public static function middleware(): array
    {
        return [
         new Middleware("age_check", only: ['destroy'])
        ];
    }

    public function index()
    {
        //

        $students = [
            ['name' => 'John Doe', 'age' => 20],
            ['name' => 'Jane Smith', 'age' => 22],
            ['name' => 'Chinmay ', 'age' => 23],
            ['name' => 'Alice Johnson', 'age' => 19],
        ];

        return view('student.index', compact('students'));
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

        return 'User created succesfully ! Name:'. $request->input('name');
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

        return "update student successfully! name: ". $request->input('name');
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        //
    }
}
