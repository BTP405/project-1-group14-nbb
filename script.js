document.getElementById('main-form').addEventListener('click', async (event) => {
    if (event.target.matches('button')) {
        const fieldset = event.target.closest('fieldset');
        const option = document.querySelector('input[name="option"]:checked').value;
        const formData = new FormData();
        formData.append('option', option);

        switch (event.target.id) {
            case 'add-student':
                formData.append('task', 'add_student');
                formData.append('name', prompt('Enter student name:'));
                formData.append('class', prompt('Enter class:'));
                formData.append('roll', prompt('Enter roll no:'));
                formData.append('address', prompt('Enter address:'));
                formData.append('phone', prompt('Enter phone:'));
                break;
            case 'remove-student':
                formData.append('task', 'remove_student');
                formData.append('class', prompt('Enter class:'));
                formData.append('roll', prompt('Enter roll no:'));
                break;
            case 'display-student':
                formData.append('task', 'display_student');
                formData.append('class', prompt('Enter class:'));
                break;
            case 'add-teacher':
                formData.append('task', 'add_teacher');
                formData.append('name', prompt('Enter teacher name:'));
                formData.append('tcode', prompt('Enter tcode:'));
                formData.append('salary', prompt('Enter salary:'));
                formData.append('address', prompt('Enter address:'));
                formData.append('phone', prompt('Enter phone:'));
                break;
            case 'remove-teacher':
                formData.append('task', 'remove_teacher');
                formData.append('tcode', prompt('Enter tcode:'));
                formData.append('name', prompt('Enter teacher:'));
                break;
            case 'update-salary':
                formData.append('task', 'update_salary');
                formData.append('name', prompt('Enter teacher:'));
                formData.append('tcode', prompt('Enter tcode:'));
                formData.append('salary', prompt('Enter salary:'));
                break;
            case 'display-teacher':
                formData.append('task', 'display_teacher');
                break;
            case 'class-attendance':
                formData.append('task', 'class_attendance');
                formData.append('class', prompt('Enter class:'));
                formData.append('clt', prompt('Enter class teacher:'));
                formData.append('t', prompt('Enter class strength:'));
                formData.append('d', prompt('Enter date:'));
                formData.append('ab', prompt('Enter no of absentees:'));
                break;
            case 'display-attendance':
                formData.append('task', 'display_class_attendance');
                break;
            case 'add-subject':
                formData.append('task', 'add_subject');
                formData.append('bid', prompt('Enter subject id:'));
                formData.append('t', prompt('Enter title:'));
                formData.append('a', prompt('Enter cost:'));
                formData.append('p', prompt('Enter timings:'));
                formData.append('g', prompt('Enter duration:'));
                break;
            case 'remove-subject':
                formData.append('task', 'remove_subject');
                formData.append('t', prompt('Enter title:'));
                break;
            case 'display-subject':
                formData.append('task', 'display_subject');
                break;
            default:
                return;
        }

        const response = await fetch('Functions.py', {
            method: 'POST',
            body: formData
        });

        const result = await response.text();
        document.getElementById('result').textContent = result;
    }
});

document.querySelectorAll('input[name="option"]').forEach((input) => {
    input.addEventListener('change', () => {
        const fieldsets = document.querySelectorAll('fieldset');
        fieldsets.forEach((fieldset) => {fieldset.style.display = 'none';
        });
        const selectedFieldset = document.getElementById(input.value + '-fieldset');
        selectedFieldset.style.display = 'block';
    });
});

document.querySelectorAll('input[name="option"]')[0].click();
