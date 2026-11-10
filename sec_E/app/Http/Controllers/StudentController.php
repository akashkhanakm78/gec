<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Routing\Controllers\HasMiddleware;
use Illuminate\Routing\Controllers\Middleware;
use Override;

class StudentController extends Controller  implements HasMiddleware
{
    /**
     * Display a listing of the resource.
     * 
     * 
     */

    #[Override]
    public static function middleware(): array
    {
        return [
            new Middleware('AgeCheck'),
        ];
    }
    public function index()
    {
        //
        $students = [
            ['id' => 1, 'name' => 'John Doe', 'email' => 'jon@gamil.com'],
            ['id' => 2, 'name' => 'Rohit', 'email' => 'rohit@gamil.com'],
            ['id' => 3, 'name' => 'Jane Doe', 'email' => 'jane@gamil.com'],
            ['id' => 4, 'name' => 'Bob Smith', 'email' => 'bob@gamil.com'],
        ];
        return view('students.index', compact('students'));
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
        return "This is the create page of StudentController";
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        //
        Return "This is the store page of StudentController";
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        //
        return view('students.show', ['student' => $id]);
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(string $id)
    {
        //
        return "This is the edit page of StudentController with ID: " . $id;
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        //
        return "This is the update page of StudentController with ID: " . $id;
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        //
        return "This is the destroy page of StudentController with ID: " . $id;
    }
}
