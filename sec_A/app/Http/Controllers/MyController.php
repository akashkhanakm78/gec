<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class MyController extends Controller
{
    //
    function index()
    {
        // echo "hello this from controller";
        return view('home');
    }
}
