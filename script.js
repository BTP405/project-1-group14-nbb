<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teaching Management System</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Teaching Management System</h1>
    <form id="main-form">
        <fieldset>
            <legend>Select an option:</legend>
            <label><input type="radio" name="option" value="student" checked> Student</label>
            <label><input type="radio" name="option" value="teacher"> Teacher</label>
            <label><input type="radio" name="option" value="attendance"> Class Attendance</label>
            <label><input type="radio" name="option" value="subject"> Subject</label>
        </fieldset>
        <fieldset id="student-fieldset" style="display: block;">
            <legend>Student</legend>
            <button type="button" id="add-student">Add Student</button>
            <button type="button" id="remove-student">Remove Student</button>
            <button type="button" id="display-student">Display Student Details</button>
        </fieldset>
        <fieldset id="teacher-fieldset" style="display: none;">
            <legend>Teacher</legend>
            <button type="button" id="add-teacher">Add Teacher</button>
            <button type="button" id="remove-teacher">Remove Teacher</button>
            <button type="button" id="update-salary">Update Salary</button>
            <button type="button" id="display-teacher">Display Teacher Details</button>
        </fieldset>
         <fieldset id="attendance-fieldset" style="display: none;">
            <legend>Class Attendance</legend>
            <button type="button" id="class-attendance">Class Attendance</button>
            <button type="button" id="display-attendance">Display Class Attendance Details</button>
        </fieldset>
        <fieldset id="subject-fieldset" style="display: none;">
            <legend>Subject</legend>
            <button type="button" id="add-subject">Add Subject</button>
            <button type="button" id="remove-subject">Remove Subject</button>
            <button type="button" id="display-subject">Display Subject Details</button>
        </fieldset>
    </form>
    <div id="result"></div>
    <script src="script.js"></script>
</body>
</html>
