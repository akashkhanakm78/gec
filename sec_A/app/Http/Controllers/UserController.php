<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class UserController extends Controller
{
    function createUser(Request $request){

        $name = $request->input('name');
        $email = $request->input('email');
      

        return response()->json(['message' => 'User created successfully', 'name' => $name, 'email' => $email]);
    }
}
