<?php

namespace App\Http\Controllers;


use Illuminate\Http\Request;
use Illuminate\Routing\Controllers\HasMiddleware;
use Illuminate\Routing\Controllers\Middleware;
use Override;

class StudentController extends Controller
{

    // #[Override]
    // public static function middleware(): array
    // {
    //     return [
    //         new Middleware('check'),
    //     ];
    // }
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

        $validated = $request->validate([
            "name"=>'required | min:3',
            "email" =>'required | max:50',
            "password"=>'required',
            'document' => ['required', 'file', 'mimes:png,jpeg,jpg'],
        ],[
            "name.required"=> 'Naam Jaruri hain!',
            "name.min"=>" Kuch bada naam dalo yaar!",
            "email.required"=>" kyu is bar vi email dalna bhul geye",
            "password.required"=>"pasword vi to chahiye!"
        ]
        );

                $path = $request->file('document')->store('images','public' );

                return back()->with('path',$path);
                
            // return redirect()->route('home')->with('success', "Form Submited successfully!");

            // return response()->json([
            //     "data"=>$validated,
            //     "path"=> $path
            // ]);
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
