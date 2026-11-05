<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class MyName extends Controller
{
    //
        function index(){
            echo "This is my first controller in laravel";
            return view('home');
        }

}
