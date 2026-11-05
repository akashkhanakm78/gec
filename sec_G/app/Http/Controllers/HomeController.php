<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class HomeController extends Controller
{
    //

    function index()
    {

    echo "This is from controller";
        return view('home');
    }

    function about()
    {
    echo "This is from controller";

        return view('about');
    }

}
