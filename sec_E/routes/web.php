<?php

use App\Http\Controllers\MyName;
use App\Http\Controllers\StudentController;
use App\Http\Controllers\UserController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});


Route::resource('/students', StudentController::class);

// Route::get('/home', function () {
//     return view('home');
// });
// Route::get('/blabla', [UserController::class,"getUserProfile"])->name('user');

// Route::get('/user', function () {
//     return redirect()->route('user');
// });



// Route::get('/parent', function () {
//     return view('parent.profile');
// });

// controller route
// Route::get('/home', [MyName::class,"index"]);


// Route::post('/create-user',function(){

// return response()->json([
//     'username' => "Rohit",
//     'message' => 'User created successfully',
//     'status' => 200
// ]);

// });


// Route::get('/csrf', function () {

//     return csrf_token();
// });


// Route::get('/reels/{name}/{id}', function ($name, $id) {

//     return "Video ID: " . $id . ", Name:   " . $name;
// });


// Route::delete('/delete-user/{id}', function ($id) {
//     return "User Deleted ID: " . $id;
// });
// Route::get('/hello/{name?}', function ($name = 'Friend') {
//     return "Hello, " . $name . "!";
// });



// Route::get('/admin', function () {
//     return 'Admin Page';
// });
// Route::get('/admin/dashboard', function () {
//     return 'Admin Dashboard Page';
// });
// Route::get('/admin/settings', function () {
//     return 'Admin settings Page';
// });
// Route::get('/admin/profile', function () {
//     return 'Admin profile Page';
// });


// Route::prefix('super-admin')->name('admin.')->group(function () {
//     Route::get('/', function () {
//         return 'Admin Page';
//     })->name('index');
//     Route::get('/dashboard', function () {
//         return 'Admin Dashboard Page';
//     })->name('dashboard');
//     Route::get('/settings', function () {
//         return 'Admin settings Page';
//     })->name('settings');
//     Route::get('/profile', function () {
//         return 'Admin profile Page';
//     })->name('profile');
// });


//  route(admin.dashboard)