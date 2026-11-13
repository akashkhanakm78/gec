<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Routing\Controllers\HasMiddleware;
use Illuminate\Routing\Controllers\Middleware;
use Override;

class StudentController extends Controller 
{
    /**
     * Display a listing of the resource.
     */

    // #[Override]
    // public static function middleware(): array
    // {
    //     return [
    //      new Middleware("age_check", only: ['destroy'])
    //     ];
    // }

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
        $method = $request->method();
        //
        $validated = $request->validate([
            'name'=>'required | min:4',
            'email'=>['email', 'max:50'],
            'password'=>'required| min:8 | confirmed'
        ],
        [
            'name.required'=> 'naam jaruri hai!',
            'name.min'=> 'naam bada hona chahiye!',
            'email.email'=> 'sahise email dalna vi nehi ata !',
            'password.min'=>'Hack ho jayega bhai strong dal!'
            
        ]
        );
            return back()->with('success', "User Created Successfully!");
        // return redirect()->route('students.index')->with('success', "User Created Successfully!");
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
