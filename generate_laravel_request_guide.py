from pathlib import Path

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_BREAK
from docx.enum.section import WD_ORIENT

doc = Document()
sec = doc.sections[0]
sec.top_margin = Inches(0.65)
sec.bottom_margin = Inches(0.65)
sec.left_margin = Inches(0.75)
sec.right_margin = Inches(0.75)

# Theme / styles
styles = doc.styles
styles['Normal'].font.name = 'Aptos'
styles['Normal'].font.size = Pt(10)
styles['Normal'].paragraph_format.space_after = Pt(5)
for sty, size, color in [('Title', 28, '17365D'), ('Heading 1', 19, '17365D'), ('Heading 2', 14, '1F4E79'), ('Heading 3', 11, '2F5597')]:
    s = styles[sty]
    s.font.name = 'Aptos Display' if sty != 'Normal' else 'Aptos'
    s.font.size = Pt(size)
    s.font.bold = True
    s.font.color.rgb = RGBColor.from_string(color)
    s.paragraph_format.space_before = Pt(12)
    s.paragraph_format.space_after = Pt(6)

if 'Code' not in styles:
    cs = styles.add_style('Code', WD_STYLE_TYPE.PARAGRAPH)
else:
    cs = styles['Code']
cs.font.name = 'Consolas'
cs.font.size = Pt(8.5)
cs.font.color.rgb = RGBColor(35, 45, 55)
cs.paragraph_format.left_indent = Inches(0.18)
cs.paragraph_format.right_indent = Inches(0.12)
cs.paragraph_format.space_before = Pt(3)
cs.paragraph_format.space_after = Pt(7)

def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:fill'), fill)
    tcPr.append(shd)

def set_cell_text(cell, text, bold=False, color=None, size=9):
    cell.text = ''
    p = cell.paragraphs[0]
    r = p.add_run(text)
    r.bold = bold
    r.font.name = 'Aptos'
    r.font.size = Pt(size)
    if color:
        r.font.color.rgb = RGBColor.from_string(color)
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER

def para(text='', style=None, bold_prefix=None):
    p = doc.add_paragraph(style=style)
    if bold_prefix and text.startswith(bold_prefix):
        p.add_run(bold_prefix).bold = True
        p.add_run(text[len(bold_prefix):])
    else:
        p.add_run(text)
    return p

def bullet(text, level=0):
    p = doc.add_paragraph(style='List Bullet' if level == 0 else 'List Bullet 2')
    p.add_run(text)
    return p

def numbered(text):
    p = doc.add_paragraph(style='List Number')
    p.add_run(text)
    return p

def code(text):
    # one paragraph per code block, preserving line breaks
    p = doc.add_paragraph(style='Code')
    p.paragraph_format.keep_together = True
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:fill'), 'F2F4F7')
    pPr.append(shd)
    for i, line in enumerate(text.strip('\n').split('\n')):
        if i:
            p.add_run().add_break()
        p.add_run(line)
    return p

def callout(label, text, fill='EAF2F8'):
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.cell(0,0)
    shade(c, fill)
    p = c.paragraphs[0]
    r = p.add_run(label + '  ')
    r.bold = True
    r.font.color.rgb = RGBColor(31,78,121)
    p.add_run(text)
    doc.add_paragraph()

# Header/footer
header = sec.header.paragraphs[0]
header.text = "LARAVEL TEACHING GUIDE  |  REQUESTS • FORMS • CSRF • VALIDATION"
header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
for r in header.runs:
    r.font.size = Pt(8)
    r.font.color.rgb = RGBColor(100,110,120)
footer = sec.footer.paragraphs[0]
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
rr = footer.add_run("Classroom Reference • Laravel 12 • Practical Examples")
rr.font.size = Pt(8)
rr.font.color.rgb = RGBColor(100,110,120)

# Cover
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_before = Pt(65)
r = p.add_run("LARAVEL")
r.bold = True; r.font.size = Pt(18); r.font.color.rgb = RGBColor(31,78,121)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Request Handling & Form Processing")
r.bold = True; r.font.size = Pt(27); r.font.color.rgb = RGBColor(23,54,93)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("GET and POST • CSRF Protection • Old Input • Flash Data • Validation")
r.font.size = Pt(12); r.font.color.rgb = RGBColor(90,100,110)
doc.add_paragraph()
callout("Learning outcome", "By the end of this guide, students should be able to build a secure Laravel form, receive and inspect submitted data, validate it on the server, return useful feedback, and preserve user input after validation errors.")
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_before = Pt(30)
r = p.add_run("Complete teaching notes with explanations, code, examples, classroom workflow and practice tasks")
r.italic = True; r.font.size = Pt(10)
doc.add_page_break()

doc.add_heading("Contents", level=1)
contents = [
"1. Learning objectives and prerequisites",
"2. How an HTTP form request works",
"3. GET and POST methods",
"4. Routes and controller request handling",
"5. The Laravel Request object",
"6. Building a complete form",
"7. CSRF protection",
"8. Redirects, old input and flash data",
"9. Validation workflow",
"10. Built-in validation rules",
"11. Custom validation messages and attributes",
"12. Displaying validation errors in Blade",
"13. Complete practical example: student registration",
"14. File uploads and validation",
"15. Testing with browser and Thunder Client",
"16. Common errors and troubleshooting",
"17. Security and best practices",
"18. Classroom exercises and assessment questions",
"19. Quick revision sheet"
]
for x in contents: bullet(x)
doc.add_page_break()

doc.add_heading("1. Learning objectives and prerequisites", level=1)
para("This guide uses Laravel 12-style syntax and Blade templates. The same core request, routing, CSRF and validation concepts apply across recent Laravel versions. Confirm version-specific details against the project installed in your classroom.")
para("Prerequisites:")
for x in ["Basic PHP syntax, arrays and functions", "HTML forms and input types", "Basic MVC understanding", "Laravel project setup, routes, controllers and Blade views", "Basic database and Eloquent knowledge (helpful for the database validation examples)"]:
    bullet(x)
para("After completing the lesson, students should be able to:")
for x in ["Explain the difference between GET and POST.", "Create routes that receive form submissions.", "Read submitted values using the Request object.", "Protect browser forms with CSRF tokens.", "Redirect users and preserve old input using flash data.", "Validate data with built-in rules and custom messages.", "Show field-level and summary validation feedback.", "Explain why server-side validation is essential even when HTML validation exists."]:
    bullet(x)

doc.add_heading("2. How an HTTP form request works", level=1)
para("A form is an HTML interface that collects information. When the user clicks Submit, the browser sends an HTTP request to a URL. Laravel matches that URL and HTTP method to a route, runs the controller or route callback, reads the request data, validates it, and then returns a response.")
code("""Browser / HTML form
        |
        |  HTTP request (GET or POST)
        v
Laravel Route
        |
        v
Controller action
        |
        +--> Read input from Request
        |
        +--> Validate input
        |
        +--> Perform action (save / update / search)
        |
        v
Response: View / Redirect / JSON""")
para("Important terms:")
for x in ["Request: data and metadata sent by the browser, such as form fields, query parameters, headers and uploaded files.", "Route: maps an HTTP method and URL to application code.", "Controller: contains the application logic for handling the request.", "Response: what Laravel sends back, such as HTML, JSON or a redirect.", "Validation: checking whether submitted data satisfies the application's rules."]:
    bullet(x)

doc.add_heading("3. GET and POST methods", level=1)
doc.add_heading("3.1 GET method", level=2)
para("GET is generally used to retrieve or display information. Search forms and filter forms commonly use GET. Submitted values usually appear in the URL as query parameters.")
code("""<!-- resources/views/products/search.blade.php -->
<form action="{{ route('products.search') }}" method="GET">
    <label for="keyword">Search product</label>
    <input type="text" id="keyword" name="keyword">
    <button type="submit">Search</button>
</form>""")
code("""// routes/web.php
use Illuminate\\Support\\Facades\\Route;
use Illuminate\\Http\\Request;

Route::get('/products/search', function (Request $request) {
    $keyword = $request->query('keyword');

    return 'Searching for: ' . e($keyword);
})->name('products.search');""")
para("Example URL after submission: /products/search?keyword=laptop")
para("GET characteristics:")
for x in ["Designed for retrieval, not for changing server data.", "Parameters are visible in the URL and may be saved in browser history or shared.", "Can be bookmarked and cached depending on the response and cache rules.", "Do not put passwords, OTPs, private tokens or sensitive personal information in a GET query string."]:
    bullet(x)
doc.add_heading("3.2 POST method", level=2)
para("POST is commonly used to submit data that creates or changes something, such as registering a student, saving a profile or creating an order. The form data is sent in the request body rather than being appended to the URL.")
code("""<!-- resources/views/students/create.blade.php -->
<form action="{{ route('students.store') }}" method="POST">
    @csrf

    <label>Name</label>
    <input type="text" name="name">

    <label>Email</label>
    <input type="email" name="email">

    <button type="submit">Save Student</button>
</form>""")
code("""// routes/web.php
use App\\Http\\Controllers\\StudentController;

Route::get('/students/create', [StudentController::class, 'create'])
    ->name('students.create');

Route::post('/students', [StudentController::class, 'store'])
    ->name('students.store');""")
para("GET versus POST:")
table = doc.add_table(rows=1, cols=3)
table.style = 'Light Shading Accent 1'
for i,h in enumerate(["Point","GET","POST"]): set_cell_text(table.rows[0].cells[i],h,True,'FFFFFF')
for row in [
("Typical purpose","Retrieve/search/filter","Submit/create/change data"),
("Data location","URL query string","Request body"),
("Bookmark/share","Often suitable","Not normally meaningful"),
("Sensitive data","Avoid","Body is less exposed in URL, but HTTPS is still mandatory"),
("Laravel route","Route::get(...)","Route::post(...)")
]:
    cells=table.add_row().cells
    for i,v in enumerate(row): set_cell_text(cells[i],v)
callout("Important correction", "POST does not automatically make data secure or encrypted. HTTPS provides transport encryption. CSRF protection and authorization solve different security problems.")

doc.add_heading("4. Routes and controller request handling", level=1)
para("For a clean MVC structure, keep route definitions in routes/web.php and put request-handling logic in a controller.")
para("Create a controller:")
code("php artisan make:controller StudentController")
para("Example controller:")
code("""<?php

namespace App\\Http\\Controllers;

use Illuminate\\Http\\Request;

class StudentController extends Controller
{
    // Display the form
    public function create()
    {
        return view('students.create');
    }

    // Receive and process submitted form data
    public function store(Request $request)
    {
        $name = $request->input('name');
        $email = $request->input('email');

        return "Name: {$name}, Email: {$email}";
    }
}""")
para("Routes:")
code("""use App\\Http\\Controllers\\StudentController;

Route::get('/students/create', [StudentController::class, 'create'])
    ->name('students.create');

Route::post('/students', [StudentController::class, 'store'])
    ->name('students.store');""")
para("The type-hinted Request parameter is injected by Laravel's service container. Laravel supplies the current HTTP request object when the route calls the controller method.")

doc.add_heading("5. The Laravel Request object", level=1)
para("The Request object gives access to submitted values and request information. Import it with use Illuminate\\Http\\Request; in a controller.")
doc.add_heading("5.1 Reading input", level=2)
code("""// Get one input value
$name = $request->input('name');

// Get a value with a default if it is absent
$city = $request->input('city', 'Durgapur');

// Read query-string data specifically
$keyword = $request->query('keyword');

// Read all input data
$allData = $request->all();

// Read only selected keys
$data = $request->only(['name', 'email']);

// Exclude selected keys
$data = $request->except(['password', 'password_confirmation']);

// Check whether a key is present
if ($request->has('email')) {
    // key exists in the request
}

// Check whether a key is present and not empty
if ($request->filled('name')) {
    // name has a non-empty value
}

// Check whether a checkbox/key was sent
if ($request->boolean('is_active')) {
    // interprets common truthy values as boolean
}""")
para("input() versus query():")
bullet("input('keyword') reads from the request input payload and can also account for query input.")
bullet("query('keyword') reads specifically from the URL query string.")
para("Do not confuse these two expressions:")
code("""$request->input('name');  // Correct: calls the input() method
$request->input['name'];  // Incorrect: input is a method, not an array property""")
doc.add_heading("5.2 Checking request method and path", level=2)
code("""$method = $request->method();       // GET, POST, PUT, PATCH, DELETE
$isPost = $request->isMethod('POST');
$path = $request->path();              // e.g. students
$url = $request->url();                // URL without query string
$fullUrl = $request->fullUrl();        // URL including query string""")
doc.add_heading("5.3 Safe data handling", level=2)
para("Never assume that browser-submitted data is correct. A user can modify HTML, disable JavaScript, or send a request using a tool such as curl or Thunder Client. Validate the input and pass only approved fields to the database.")
code("""// Prefer validated data
$validated = $request->validate([
    'name' => ['required', 'string', 'max:100'],
    'email' => ['required', 'email'],
]);

// Use only the validated fields for persistence
// Student::create($validated);""")

doc.add_heading("6. Building a complete form", level=1)
para("A Blade form should have a destination route, an HTTP method, named fields and a submit button. The name attribute is essential because Laravel uses it as the input key.")
code("""<!-- resources/views/students/create.blade.php -->
<!DOCTYPE html>
<html>
<head>
    <title>Student Registration</title>
</head>
<body>
    <h1>Student Registration</h1>

    <form action="{{ route('students.store') }}" method="POST">
        @csrf

        <div>
            <label for="name">Full name</label>
            <input type="text" id="name" name="name">
        </div>

        <div>
            <label for="email">Email</label>
            <input type="email" id="email" name="email">
        </div>

        <div>
            <label for="phone">Phone</label>
            <input type="text" id="phone" name="phone">
        </div>

        <button type="submit">Register</button>
    </form>
</body>
</html>""")
callout("Teaching point", "The id attribute connects a label to an HTML element. The name attribute determines the key sent to the server. An input without a name is generally not submitted as a form field.")

doc.add_heading("7. CSRF protection", level=1)
doc.add_heading("7.1 What is CSRF?", level=2)
para("CSRF means Cross-Site Request Forgery. It is an attack in which a malicious website attempts to make a user's browser send an unwanted request to another website where the user is already authenticated.")
para("Example scenario:")
for x in ["A user signs in to an online banking website.", "The browser keeps the bank's authentication cookie.", "The user visits a malicious page in another tab.", "That page tries to submit a hidden request to the bank.", "Without suitable protection, the browser may attach the bank cookie to the request."]:
    numbered(x)
para("A CSRF token helps Laravel verify that a state-changing browser request came through a form or session associated with the application.")
doc.add_heading("7.2 Adding the CSRF token", level=2)
code("""<form action="{{ route('students.store') }}" method="POST">
    @csrf

    <input type="text" name="name">
    <button type="submit">Save</button>
</form>""")
para("The @csrf Blade directive generates a hidden input similar to:")
code("""<input type="hidden" name="_token" value="generated-session-token">""")
para("The token is generated dynamically. Do not manually copy a token from one request and hard-code it into a form.")
doc.add_heading("7.3 What happens if @csrf is missing?", level=2)
para("For routes using Laravel's web middleware, a POST/PUT/PATCH/DELETE request without a valid CSRF token is normally rejected. In a typical browser request, the user may see HTTP 419 (Page Expired).")
doc.add_heading("7.4 CSRF in GET and POST", level=2)
bullet("GET requests should be read-only and should not perform actions such as deleting records or changing account settings.")
bullet("POST, PUT, PATCH and DELETE browser form requests need CSRF protection when handled through the web middleware.")
bullet("Do not change a destructive route to GET just to avoid CSRF errors. Fix the form and route correctly.")
doc.add_heading("7.5 CSRF and APIs", level=2)
para("Laravel API routes are generally stateless and do not use the same session-based CSRF flow as browser routes in routes/web.php. API authentication commonly uses bearer tokens or another API authentication mechanism. If an API uses cookie-based browser authentication, its CSRF requirements must be configured correctly; do not assume every API is automatically safe.")
doc.add_heading("7.6 CSRF versus authentication and authorization", level=2)
table = doc.add_table(rows=1, cols=3); table.style='Light Shading Accent 1'
for i,h in enumerate(["Concept","Question answered","Purpose"]): set_cell_text(table.rows[0].cells[i],h,True,'FFFFFF')
for row in [
("Authentication","Who are you?","Confirms user identity"),
("Authorization","Are you allowed to do this?","Checks permissions"),
("CSRF protection","Was this browser action intentionally initiated from the application?","Helps prevent forged cross-site requests")
]:
    cells=table.add_row().cells
    for i,v in enumerate(row): set_cell_text(cells[i],v)

doc.add_heading("8. Redirects, old input and flash data", level=1)
doc.add_heading("8.1 Redirect response", level=2)
para("A redirect tells the browser to make a new request to another URL. It is commonly used after a form is processed.")
code("""return redirect()->route('students.create');""")
para("After a successful POST, redirecting instead of returning the form view directly helps prevent accidental resubmission when the user refreshes the page. This is commonly called the Post/Redirect/Get pattern.")
doc.add_heading("8.2 Flash data", level=2)
para("Flash data is session data intended to be available during the next request. It is useful for one-time messages such as success, warning or error notifications.")
code("""// Controller
return redirect()
    ->route('students.create')
    ->with('success', 'Student registered successfully.');""")
code("""<!-- Blade view -->
@if (session('success'))
    <div class="alert alert-success">
        {{ session('success') }}
    </div>
@endif""")
para("Other examples:")
code("""return back()->with('warning', 'Please review the submitted details.');
return back()->with('error', 'Unable to complete the operation.');""")
doc.add_heading("8.3 Old input", level=2)
para("When validation fails, Laravel automatically redirects back and flashes the submitted input to the session, except sensitive fields such as passwords are not flashed by default. Blade's old() helper retrieves a previously submitted value.")
code("""<input type="text" name="name" value="{{ old('name') }}">
<input type="email" name="email" value="{{ old('email') }}">""")
para("For a select box:")
code("""<select name="city">
    <option value="">Choose city</option>
    <option value="Durgapur" {{ old('city') == 'Durgapur' ? 'selected' : '' }}>
        Durgapur
    </option>
    <option value="Kolkata" {{ old('city') == 'Kolkata' ? 'selected' : '' }}>
        Kolkata
    </option>
</select>""")
para("For a checkbox:")
code("""<input type="checkbox" name="terms" value="1"
    {{ old('terms') ? 'checked' : '' }}>
<label>I accept the terms</label>""")
doc.add_heading("8.4 Old input versus flash data", level=2)
table = doc.add_table(rows=1, cols=3); table.style='Light Shading Accent 1'
for i,h in enumerate(["Feature","Old input","Flash data"]): set_cell_text(table.rows[0].cells[i],h,True,'FFFFFF')
for row in [
("What it stores","Previously submitted form values","Temporary session values"),
("Common use","Refill form fields after an error","Show one-time success/error message"),
("Blade access","old('field')","session('key')"),
("Typical lifecycle","Available after redirect for the next request","Available for the next request, then expires")
]:
    cells=table.add_row().cells
    for i,v in enumerate(row): set_cell_text(cells[i],v)

doc.add_heading("9. Validation workflow", level=1)
para("Validation is the server-side process of checking submitted data before using it. HTML attributes such as required, minlength and type=email improve the user experience, but they are not a security boundary.")
doc.add_heading("9.1 Typical validation sequence", level=2)
for x in ["User opens the form using a GET route.", "User enters values and submits the form using POST.", "Laravel receives the request.", "The controller applies validation rules.", "If validation passes, Laravel returns validated data to the controller.", "If validation fails, Laravel redirects back, stores errors in the session and flashes eligible input.", "The Blade view displays errors and restores old input."]:
    numbered(x)
doc.add_heading("9.2 Quick validation using validate()", level=2)
code("""public function store(Request $request)
{
    $validated = $request->validate([
        'name' => ['required', 'string', 'max:100'],
        'email' => ['required', 'email', 'max:255'],
        'age' => ['required', 'integer', 'min:18', 'max:60'],
    ]);

    // Use only validated values
    // Student::create($validated);

    return redirect()
        ->route('students.create')
        ->with('success', 'Student registered successfully.');
}""")
para("If the rules pass, validate() returns an array containing validated data. If they fail in a traditional web request, Laravel automatically redirects back with validation errors and eligible old input. For JSON requests, Laravel normally returns a 422 Unprocessable Entity response with validation details.")
doc.add_heading("9.3 Manual Validator", level=2)
para("Use the Validator facade when you need more control over the validation flow.")
code("""use Illuminate\\Support\\Facades\\Validator;

public function store(Request $request)
{
    $validator = Validator::make($request->all(), [
        'name' => ['required', 'string', 'max:100'],
        'email' => ['required', 'email'],
    ]);

    if ($validator->fails()) {
        return redirect()
            ->back()
            ->withErrors($validator)
            ->withInput();
    }

    $validated = $validator->validated();

    return redirect()
        ->route('students.create')
        ->with('success', 'Data is valid.');
}""")
para("Use validate() for the common case. Use Validator::make() when you need to inspect errors, add conditional rules, or control the response yourself.")
doc.add_heading("9.4 Validated data is not the same as all request data", level=2)
code("""$all = $request->all();             // Every submitted input
$validated = $request->validate([...]); // Only data that passed the rules""")
callout("Best practice", "Do not pass $request->all() directly into a model's create() or update() method. Validate first, then persist only the validated fields. Also configure model fillable/guarded properties appropriately.")

doc.add_heading("10. Built-in validation rules", level=1)
para("Rules may be written as a pipe-separated string or as an array. The array form is often easier to read, especially when rules contain parameters.")
code("""// String syntax
'name' => 'required|string|max:100',

// Array syntax
'name' => ['required', 'string', 'max:100'],""")
rules = [
("required","Field must be present and not empty."),
("nullable","Null is allowed; other rules are generally skipped for a null value."),
("sometimes","Apply rules only if the field is present in the input."),
("string","Value must be a string."),
("integer","Value must be an integer."),
("numeric","Value must be numeric."),
("boolean","Value must be a boolean-like value accepted by Laravel."),
("email","Value must be a valid email address."),
("url","Value must be a valid URL."),
("alpha","Only alphabetic characters."),
("alpha_num","Only letters and numbers."),
("alpha_dash","Letters, numbers, dashes and underscores."),
("min:5","Minimum size/value is 5; interpretation depends on the data type."),
("max:100","Maximum size/value is 100; interpretation depends on the data type."),
("between:1,10","Value must be between 1 and 10."),
("digits:10","Must contain exactly 10 digits."),
("digits_between:10,12","Must contain between 10 and 12 digits."),
("size:10","Must have exactly the specified size/value."),
("in:active,inactive","Value must be one of the listed values."),
("not_in:admin,root","Value must not be one of the listed values."),
("confirmed","Requires a matching field named field_confirmation."),
("same:password","Must match another field."),
("different:username","Must differ from another field."),
("date","Must be a valid date."),
("date_format:Y-m-d","Must match the specified date format."),
("before:today","Must be before the given date."),
("after:today","Must be after the given date."),
("accepted","Must be accepted, commonly used for terms and conditions."),
("required_if:role,admin","Required when another field equals the specified value."),
("required_with:phone","Required when the other field is present."),
("required_without:email","Required when the other field is missing."),
("unique:users,email","Value must be unique in the specified table/column."),
("exists:departments,id","Value must exist in the specified table/column."),
("regex:/pattern/","Must match a regular expression."),
("image","Uploaded file must be an image."),
("mimes:jpg,png,pdf","Uploaded file must have one of the listed extensions/types."),
("mimetypes:image/jpeg,image/png","Uploaded file must have one of the listed MIME types."),
("file","Must be a successfully uploaded file."),
("max:2048","For a file, maximum size is 2048 KB."),
]
tbl=doc.add_table(rows=1, cols=2); tbl.style='Light Shading Accent 1'
set_cell_text(tbl.rows[0].cells[0],"Rule",True,'FFFFFF')
set_cell_text(tbl.rows[0].cells[1],"Meaning",True,'FFFFFF')
for a,b in rules:
    cells=tbl.add_row().cells
    set_cell_text(cells[0],a,True)
    set_cell_text(cells[1],b)
para("Note: Some rules behave differently depending on the field type. For example, min and max can refer to string length, numeric value, array size or file size. Check the current Laravel validation documentation for edge cases and rule parameters.")
doc.add_heading("10.1 Common combinations", level=2)
code("""$validated = $request->validate([
    'name' => ['required', 'string', 'min:2', 'max:100'],
    'email' => ['required', 'email', 'max:255', 'unique:users,email'],
    'age' => ['required', 'integer', 'between:18,60'],
    'phone' => ['required', 'digits:10'],
    'password' => ['required', 'string', 'min:8', 'confirmed'],
    'terms' => ['accepted'],
]);""")
para("For the confirmed rule, the form must include password_confirmation:")
code("""<input type="password" name="password">
<input type="password" name="password_confirmation">""")
doc.add_heading("10.2 Unique and exists rules", level=2)
code("""// Email must not already exist in users.email
'email' => ['required', 'email', 'unique:users,email'],

// Department ID must exist in departments.id
'department_id' => ['required', 'exists:departments,id'],""")
para("When updating an existing record, a unique rule usually needs to ignore the current record. Prefer the fluent Rule API and pass a trusted model/record identifier rather than trusting an arbitrary request value.")
code("""use Illuminate\\Validation\\Rule;

// Example for updating a user record
'email' => [
    'required',
    'email',
    Rule::unique('users', 'email')->ignore($user->id),
],""")

doc.add_heading("11. Custom validation messages and attributes", level=1)
doc.add_heading("11.1 Custom messages in validate()", level=2)
code("""$validated = $request->validate(
    [
        'name' => ['required', 'string', 'max:100'],
        'email' => ['required', 'email'],
        'age' => ['required', 'integer', 'min:18'],
    ],
    [
        'name.required' => 'Please enter your full name.',
        'name.max' => 'Your name cannot exceed 100 characters.',
        'email.required' => 'Email address is required.',
        'email.email' => 'Enter a valid email address.',
        'age.min' => 'You must be at least 18 years old.',
    ]
);""")
para("The message key uses field.rule format. For example, email.required customizes the required rule for the email field.")
doc.add_heading("11.2 Custom attribute names", level=2)
code("""$validated = $request->validate(
    [
        'dob' => ['required', 'date'],
    ],
    [],
    [
        'dob' => 'date of birth',
    ]
);""")
para("Laravel can now use a human-friendly label such as “date of birth” in generated validation messages.")
doc.add_heading("11.3 Custom messages in a Form Request", level=2)
para("For larger forms, move validation into a dedicated Form Request class.")
code("""php artisan make:request StoreStudentRequest""")
code("""<?php

namespace App\\Http\\Requests;

use Illuminate\\Foundation\\Http\\FormRequest;

class StoreStudentRequest extends FormRequest
{
    public function authorize(): bool
    {
        return true; // Add a real permission check in protected applications
    }

    public function rules(): array
    {
        return [
            'name' => ['required', 'string', 'max:100'],
            'email' => ['required', 'email', 'max:255'],
            'phone' => ['required', 'digits:10'],
        ];
    }

    public function messages(): array
    {
        return [
            'name.required' => 'Please enter the student name.',
            'email.email' => 'Please enter a valid email address.',
            'phone.digits' => 'Phone number must contain exactly 10 digits.',
        ];
    }

    public function attributes(): array
    {
        return [
            'phone' => 'mobile number',
        ];
    }
}""")
para("Inject the Form Request into the controller. Laravel validates it before the controller action runs.")
code("""use App\\Http\\Requests\\StoreStudentRequest;

public function store(StoreStudentRequest $request)
{
    $validated = $request->validated();

    // Student::create($validated);

    return redirect()
        ->route('students.create')
        ->with('success', 'Student saved.');
}""")
callout("Important", "authorize() returning true is acceptable for a simple classroom demonstration. In a real application, implement authorization so users cannot submit records they are not permitted to create.")

doc.add_heading("12. Displaying validation errors in Blade", level=1)
doc.add_heading("12.1 Show one field's error", level=2)
code("""@error('name')
    <div class="text-danger">{{ $message }}</div>
@enderror""")
doc.add_heading("12.2 Show all errors", level=2)
code("""@if ($errors->any())
    <div class="alert alert-danger">
        <strong>Please correct the following errors:</strong>
        <ul>
            @foreach ($errors->all() as $error)
                <li>{{ $error }}</li>
            @endforeach
        </ul>
    </div>
@endif""")
doc.add_heading("12.3 Restore old values and show field errors", level=2)
code("""<div>
    <label for="name">Name</label>
    <input
        type="text"
        id="name"
        name="name"
        value="{{ old('name') }}"
        class="@error('name') is-invalid @enderror"
    >

    @error('name')
        <small class="text-danger">{{ $message }}</small>
    @enderror
</div>

<div>
    <label for="email">Email</label>
    <input
        type="email"
        id="email"
        name="email"
        value="{{ old('email') }}"
        class="@error('email') is-invalid @enderror"
    >

    @error('email')
        <small class="text-danger">{{ $message }}</small>
    @enderror
</div>""")
para("Use Blade's escaped output syntax {{ }} for user-provided values and error messages. Avoid rendering untrusted values with {!! !!} unless you have a specific, safe reason.")

doc.add_heading("13. Complete practical example: student registration", level=1)
para("This example combines routes, controller, Blade form, CSRF, validation, custom messages, old input, error feedback and a success flash message.")
doc.add_heading("Step 1 — Create the controller", level=2)
code("php artisan make:controller StudentController")
doc.add_heading("Step 2 — Add routes", level=2)
code("""// routes/web.php
use App\\Http\\Controllers\\StudentController;

Route::get('/students/create', [StudentController::class, 'create'])
    ->name('students.create');

Route::post('/students', [StudentController::class, 'store'])
    ->name('students.store');""")
doc.add_heading("Step 3 — Controller code", level=2)
code("""<?php

namespace App\\Http\\Controllers;

use Illuminate\\Http\\Request;

class StudentController extends Controller
{
    public function create()
    {
        return view('students.create');
    }

    public function store(Request $request)
    {
        $validated = $request->validate(
            [
                'name' => ['required', 'string', 'min:2', 'max:100'],
                'email' => ['required', 'email', 'max:255'],
                'phone' => ['required', 'digits:10'],
                'age' => ['required', 'integer', 'between:16,60'],
                'course' => ['required', 'in:PHP,Laravel,Python,JavaScript'],
                'terms' => ['accepted'],
            ],
            [
                'name.required' => 'Student name is required.',
                'name.min' => 'Name must contain at least 2 characters.',
                'email.required' => 'Please enter an email address.',
                'email.email' => 'Please enter a valid email address.',
                'phone.digits' => 'Phone number must contain exactly 10 digits.',
                'age.between' => 'Age must be between 16 and 60.',
                'course.in' => 'Please select a valid course.',
                'terms.accepted' => 'You must accept the terms and conditions.',
            ]
        );

        // Demonstration only:
        // In a database-backed application, save $validated using a model.
        // Example: Student::create($validated);

        return redirect()
            ->route('students.create')
            ->with('success', 'Student registration completed successfully.');
    }
}""")
doc.add_heading("Step 4 — Create the Blade view", level=2)
para("Create resources/views/students/create.blade.php:")
code("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Registration</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 650px;
               margin: 30px auto; padding: 0 16px; }
        .field { margin-bottom: 14px; }
        label { display: block; margin-bottom: 5px; }
        input, select { width: 100%; padding: 9px; box-sizing: border-box; }
        .error { color: #b00020; font-size: 13px; }
        .success { background: #e6ffed; padding: 10px; }
        .summary { background: #ffe8e8; padding: 10px; }
        button { padding: 10px 18px; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Student Registration</h1>

    @if (session('success'))
        <div class="success">{{ session('success') }}</div>
    @endif

    @if ($errors->any())
        <div class="summary">
            <strong>Please fix these errors:</strong>
            <ul>
                @foreach ($errors->all() as $error)
                    <li>{{ $error }}</li>
                @endforeach
            </ul>
        </div>
    @endif

    <form action="{{ route('students.store') }}" method="POST">
        @csrf

        <div class="field">
            <label for="name">Student name</label>
            <input id="name" name="name" type="text"
                   value="{{ old('name') }}">
            @error('name') <div class="error">{{ $message }}</div> @enderror
        </div>

        <div class="field">
            <label for="email">Email</label>
            <input id="email" name="email" type="email"
                   value="{{ old('email') }}">
            @error('email') <div class="error">{{ $message }}</div> @enderror
        </div>

        <div class="field">
            <label for="phone">Phone number</label>
            <input id="phone" name="phone" type="text"
                   value="{{ old('phone') }}">
            @error('phone') <div class="error">{{ $message }}</div> @enderror
        </div>

        <div class="field">
            <label for="age">Age</label>
            <input id="age" name="age" type="number"
                   value="{{ old('age') }}">
            @error('age') <div class="error">{{ $message }}</div> @enderror
        </div>

        <div class="field">
            <label for="course">Course</label>
            <select id="course" name="course">
                <option value="">Select a course</option>
                @foreach (['PHP', 'Laravel', 'Python', 'JavaScript'] as $course)
                    <option value="{{ $course }}"
                        {{ old('course') == $course ? 'selected' : '' }}>
                        {{ $course }}
                    </option>
                @endforeach
            </select>
            @error('course') <div class="error">{{ $message }}</div> @enderror
        </div>

        <div class="field">
            <label>
                <input type="checkbox" name="terms" value="1"
                       {{ old('terms') ? 'checked' : '' }}>
                I accept the terms and conditions
            </label>
            @error('terms') <div class="error">{{ $message }}</div> @enderror
        </div>

        <button type="submit">Register Student</button>
    </form>
</body>
</html>""")
doc.add_heading("Step 5 — Run and test", level=2)
code("""php artisan serve""")
para("Open http://127.0.0.1:8000/students/create in the browser.")
para("Test cases:")
for x in ["Submit the form empty. Required-field errors should appear.", "Enter an invalid email. The email error should appear.", "Enter a phone number with fewer or more than 10 digits.", "Enter age below 16 or above 60.", "Do not accept terms and conditions.", "Submit valid values. The success flash message should appear.", "After a validation error, check that previously entered values remain in the form."]:
    numbered(x)

doc.add_heading("14. File uploads and validation", level=1)
para("To upload a file, the form must use enctype=\"multipart/form-data\". Read uploaded files through the Request object's file methods and validate them before storing.")
code("""<form action="{{ route('documents.store') }}"
      method="POST" enctype="multipart/form-data">
    @csrf

    <label>Document</label>
    <input type="file" name="document">

    @error('document')
        <div>{{ $message }}</div>
    @enderror

    <button type="submit">Upload</button>
</form>""")
code("""public function store(Request $request)
{
    $validated = $request->validate([
        'document' => ['required', 'file', 'mimes:pdf,doc,docx', 'max:5120'],
    ]);

    $path = $request->file('document')->store('documents', 'public');

    return back()->with('success', 'File uploaded successfully.');
}""")
para("This example allows PDF, DOC and DOCX files up to 5120 KB (5 MB). Configure the public storage link if files must be served from the public disk:")
code("php artisan storage:link")
callout("Security note", "Do not trust the original filename or file extension alone. Validate uploads, use controlled storage locations, limit file size, and avoid executing uploaded files as code.")

doc.add_heading("15. Testing with browser and Thunder Client", level=1)
doc.add_heading("15.1 Browser testing", level=2)
for x in ["Start the Laravel development server.", "Open the GET route that displays the form.", "Submit invalid data and inspect the error feedback.", "Submit valid data and confirm the success redirect.", "Refresh after success and confirm that the browser does not repeat the POST automatically in the usual Post/Redirect/Get flow."]:
    numbered(x)
doc.add_heading("15.2 Thunder Client testing", level=2)
para("Thunder Client is useful for testing routes directly, but it does not behave exactly like a browser form with a Laravel session.")
para("For a web POST route protected by CSRF:")
for x in ["First request the form page using GET.", "Keep the session cookie and obtain the CSRF token from the page or session flow.", "Send the POST request with the matching cookie and token.", "If you send a POST request to a web route without a valid token, a 419 response is expected."]:
    numbered(x)
para("For a stateless API route, test the API authentication and validation response appropriate to that API. Do not disable CSRF globally merely to make a manual POST request work.")
doc.add_heading("15.3 Example JSON validation response", level=2)
para("When Laravel detects a JSON request (for example, an API client sends Accept: application/json), validation errors are normally returned with HTTP status 422.")
code("""{
    "message": "The email field is required.",
    "errors": {
        "email": [
            "The email field is required."
        ]
    }
}""")
para("The exact message and response fields depend on the submitted data and validation rules.")

doc.add_heading("16. Common errors and troubleshooting", level=1)
troubles = [
("419 Page Expired","A web POST/PUT/PATCH/DELETE request has a missing, expired or mismatched CSRF token, or its session is not being preserved.","Add @csrf; preserve the session cookie; verify session configuration and domain; do not bypass CSRF as a quick fix."),
("The POST method is not supported for this route","The form method and route method do not match, or the action URL is wrong.","Check action, route URL and method. Use Route::post for POST forms."),
("The GET method is not supported","A browser or client is making GET while only a POST route exists.","Open the GET form route, then submit to the POST processing route."),
("old('name') is empty","No old input was flashed, the request did not redirect back, or the field name does not match.","Use validation redirect flow or withInput(); confirm the input name."),
("Errors are not displayed","The view is not receiving the error bag, or the wrong field key is used.","Use @error('field') and check the exact name attribute."),
("Undefined variable $request","The method does not receive the Request object or the wrong variable name is used.","Import Illuminate\\Http\\Request and type-hint Request $request."),
("Trying to access array offset on null / input access error","The code treats input() as an array property or assumes an optional value exists.","Use $request->input('name') and handle missing values."),
("Mass assignment exception","Model does not allow the fields being assigned.","Configure $fillable or $guarded, and persist only validated fields."),
("Validation passes but database insert fails","Validation rules do not cover database constraints or schema requirements.","Align validation, database constraints, casts and model configuration.")
]
tbl=doc.add_table(rows=1, cols=3); tbl.style='Light Shading Accent 1'
for i,h in enumerate(["Problem","Likely cause","Fix"]): set_cell_text(tbl.rows[0].cells[i],h,True,'FFFFFF')
for row in troubles:
    cells=tbl.add_row().cells
    for i,v in enumerate(row): set_cell_text(cells[i],v,size=8)

doc.add_heading("17. Security and best practices", level=1)
for x in [
"Use GET for reading/searching and POST/PUT/PATCH/DELETE for state-changing operations.",
"Use @csrf in every normal Blade form that submits to a web route using the web middleware.",
"Keep HTTPS enabled in production. POST alone does not encrypt information.",
"Validate on the server. Client-side validation is only a convenience.",
"Use validated data, not raw $request->all(), for database writes.",
"Use authorization policies or gates to check whether the current user may perform the action.",
"Use Blade's escaped output {{ }} when displaying user input.",
"Never flash passwords, OTPs, API secrets or other sensitive values back into a form.",
"Use password and password_confirmation fields with the confirmed rule; hash passwords before storage using Laravel's hashing facilities.",
"Use database constraints as an additional integrity layer; validation does not replace constraints.",
"Do not use GET routes for delete, payment, account changes or other state-changing actions.",
"Use Form Request classes when validation logic becomes large or reusable.",
"Give users clear, specific error messages without exposing internal stack traces or database details."
]:
    bullet(x)

doc.add_heading("18. Classroom exercises and assessment questions", level=1)
doc.add_heading("18.1 Practical exercises", level=2)
exercises = [
"Create a contact form with name, email, subject and message. Use GET to display the form and POST to process it.",
"Create a student admission form with name, email, phone, date of birth and course. Validate every field.",
"Add custom messages for required, email, digits and max rules.",
"After validation failure, preserve name, email and course using old().",
"Display all validation errors at the top and individual errors below each field.",
"Add a terms checkbox and validate it using accepted.",
"Create a profile update form that uses unique email validation while ignoring the current user's ID.",
"Create a document upload form that accepts only PDF files up to 2 MB.",
"Use flash data to display a success message after a successful submission.",
"Test a web POST route without @csrf and explain why a 419 response occurs."
]
for i,x in enumerate(exercises,1):
    p=doc.add_paragraph()
    p.add_run(f"{i}. ").bold=True
    p.add_run(x)
doc.add_heading("18.2 Short-answer questions", level=2)
questions = [
"What is the purpose of the Laravel Request object?",
"Differentiate between GET and POST.",
"What is the difference between input() and query()?",
"Why should a GET request not perform a delete operation?",
"What is CSRF? Explain a simple attack scenario.",
"What does the @csrf directive generate?",
"What is the usual meaning of HTTP 419 in a Laravel web form?",
"What is flash data? Give one example.",
"What does old('email') do?",
"What is the difference between $request->all() and $request->validated()?",
"What happens when validate() fails for a normal web request?",
"What happens when validation fails for a JSON request?",
"Explain required, nullable and sometimes.",
"What is the purpose of the confirmed validation rule?",
"How do you write a custom message for email.required?",
"What is the purpose of a Form Request class?",
"Why is server-side validation necessary even if HTML required is used?",
"Why should passwords not be flashed back as old input?"
]
for i,q in enumerate(questions,1):
    p=doc.add_paragraph()
    p.add_run(f"{i}. ").bold=True
    p.add_run(q)
doc.add_heading("18.3 Suggested practical assessment rubric", level=2)
tbl=doc.add_table(rows=1, cols=2); tbl.style='Light Shading Accent 1'
set_cell_text(tbl.rows[0].cells[0],"Assessment area",True,'FFFFFF')
set_cell_text(tbl.rows[0].cells[1],"Marks",True,'FFFFFF')
for a,b in [("Routes and HTTP methods","10"),("Correct Request handling","10"),("CSRF implementation","10"),("Validation rules and custom messages","25"),("Old input and error display","15"),("Flash success feedback and redirects","10"),("Code quality and security","10"),("Testing and explanation","10"),("Total","100")]:
    cells=tbl.add_row().cells
    set_cell_text(cells[0],a, a=="Total")
    set_cell_text(cells[1],b, a=="Total")

doc.add_heading("19. Quick revision sheet", level=1)
quick = [
("Display a form","Route::get('/form', ...);"),
("Process form","Route::post('/form', ...);"),
("Request import","use Illuminate\\Http\\Request;"),
("Read input","$request->input('name');"),
("Read query string","$request->query('search');"),
("All request input","$request->all();"),
("Selected fields","$request->only(['name', 'email']);"),
("CSRF in Blade","@csrf"),
("Validate","$validated = $request->validate([...]);"),
("Old input","old('name')"),
("One field error","@error('name') {{ $message }} @enderror"),
("All errors","$errors->all()"),
("Flash message","->with('success', 'Saved!')"),
("Manual validator","Validator::make($request->all(), [...])"),
("Validated Form Request data","$request->validated()")
]
tbl=doc.add_table(rows=1, cols=2); tbl.style='Light Shading Accent 1'
set_cell_text(tbl.rows[0].cells[0],"Task",True,'FFFFFF')
set_cell_text(tbl.rows[0].cells[1],"Syntax",True,'FFFFFF')
for a,b in quick:
    cells=tbl.add_row().cells
    set_cell_text(cells[0],a,True)
    set_cell_text(cells[1],b)

doc.add_heading("Teaching summary", level=1)
para("A secure Laravel form workflow follows a predictable pattern: show the form with GET, submit it to a state-changing route with POST, include a CSRF token, validate every field on the server, process only validated data, and redirect with useful feedback. When validation fails, Laravel provides an error bag and flashes eligible old input so the user can correct the form without starting again.")
callout("Core pattern to remember", "GET form → POST submit → CSRF check → validate → save/process validated data → redirect with flash message. If validation fails: redirect back → show errors → restore old input.")

# Metadata
doc.core_properties.title = "Laravel Request Handling and Form Processing - Complete Teaching Guide"
doc.core_properties.subject = "GET and POST, CSRF, old input, flash data, Laravel validation and feedback"
doc.core_properties.author = "OpenAI"
doc.core_properties.keywords = "Laravel, PHP, Request, Forms, CSRF, Validation, Blade"

out = "data/Laravel_Request_Handling_Form_Processing_Teaching_Guide.docx"
Path(out).parent.mkdir(parents=True, exist_ok=True)
doc.save(out)
print(out)
