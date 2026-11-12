<?php

use App\Http\Controllers\MyController;
use App\Http\Controllers\SearchController;
use App\Http\Controllers\StudentController;
use App\Http\Controllers\UserController;
use GuzzleHttp\Psr7\Request;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {


    return view('welcome');
});
Route::post('/post', function () {


    return "post successfull.";
});
Route::put('/put', function () {


    return "PUT successfull.";
})->name('put');


Route::delete('/delete', function () {


    return "Delete successfull.";
});

Route::resource('students', StudentController::class);

Route::get('/home', function () {
    return view('home');
});
Route::get('/home', [MyController::class, "index"])->name('home');


Route::get('/blabla', [StudentController::class, "getStudent"])->name("student");


// Route::get('/student',function(){

//     return redirect()->route('student');
// });

Route::get('/parent', function () {
    return view('parent.profile');
});

Route::get('/csrf', function () {
    return response()->json(['token' => csrf_token()]);
});


Route::get('/parent', function () {
    return view('parent.profile');
});


Route::get('/reels/{id}/{name}', function ($id, $name) {


    return "This is video id: $id, name: $name";
    
   } );

Route::post('/create-student', [UserController::class, "createUser"]);




Route::delete('/user/{id}', function ($id) {

    return "User deleted, id: $id";
    
   } );


   Route::get('/hello/{name?}', function ($name = "Guest") {
    return "Hello, $name!";
   } );




//    Route::get('/admin', function () {
//     return "Admin";
//    } );

//    Route::get('/admin/dashboard', function () {
//     return "Admin";
//    } );
//    Route::get('/admin/settings', function () {
//     return "Admin";
//    } );
//    Route::get('/admin/profile', function () {
//     return "Admin";
//    } );


//    Route::prefix('root')->group(function () {

//     Route::get('/', function () {
//         return "Admin";
//     });
//     Route::get('/dashboard', function () {
//         return "Admin Dashboard";
//     });
//     Route::get('/settings', function () {
//         return "Admin Settings";
//     });
//     Route::get('/profile', function () {
//         return "Admin Profile";
//     });

//    });



Route::get('/search',[SearchController::class, 'search'])->name('search');