<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class SearchController extends Controller
{
    //

    public function search(Request $request){

            $query = $request->query('qurey');

        return  back()->with('query', "Your Search result is: " .$query);

    }
}
