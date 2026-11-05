<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class StudentController extends Controller
{
    //

    function getStudent(){
        $student = "Akash";
        return view('student.profile',[
            "student_name"=>$student
        ]);
    }


    function createStudent(Request $request){
       

        return response()->json(['message' => 'Student created successfully']);
    }
}
