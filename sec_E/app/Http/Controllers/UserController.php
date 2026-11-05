<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class UserController extends Controller
{
    //

    function getUserProfile(){
        $name="Akash";
        $age=26;

        // return view('user.profile',[
        //     'name'=>$name
        //      'age'=>$age
        // ]);
        // return view('user.profile')->with('name',$name)->with('age',$age);
        return view('user.profile', compact('name','age'));
    }
}
