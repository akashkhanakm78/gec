<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\UserController;

Route::get('/user', function () {
    $name ="Shubham";
    return view('student.profile', compact('name'));

    
})->name('student');

Route::get('/', function () {
    return view('home');

    
});

Route::get('/parent', function () {
    return view('parent.profile');
});

Route::get('/student', function () {
    return redirect()->route('student');
});

Route::get('/home', [HomeController::class, 'index']);
Route::get('/about', [HomeController::class, 'about']);


Route::get('/contact', function () {
    return view('contact');
});

Route::get('/text', function () {
    return "This is text ";
});

Route::get('/json', function () {
    return response()->json([
        'name' => 'Mehebub Alam',
        'age' => 25,
        'address' => 'Kolkata  , India'
    ]);
});

Route::post('/create-user',[UserController::class,'createUser']);

Route::get('/csrf', function () {
    return csrf_token();
});

Route::get('/reels/{name}/{id}', function ($name, $id) {

    return "User Name: " . $name . ", Video ID: " . $id;
});

Route::get('/hello/{name?}', function ($name = 'Guest') {
    return "Hello, " . $name . "!";
});


// Route::get('/admin', function () {
//     return "This is admin page";
// });
// Route::get('/admin/dashboard', function () {
//     return "This is admin dashboard";
// });
// Route::get('/admin/settings', function () {
//     return "This is admin settings";
// });
// Route::get('/admin/profile', function () {
//     return "This is admin profile";
// });

Route::prefix('super-admin')->group(function () {
    Route::get('/', function () {
        return "This is admin page";
    });
    Route::get('/dashboard', function () {
        return "This is admin dashboard";
    });
    Route::get('/settings', function () {
        return "This is admin settings";
    });
    Route::get('/profile', function () {
        return "This is admin profile";
    });
});