const forms = document.querySelectorAll('.needs-validation')

Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
        if (!form.checkValidity()) {

            event.preventDefault()
            event.stopPropagation()
        }
        form.classList.add('was-validated')
        let selectize = form.querySelectorAll('.selectize-input')
        console.log(selectize)
        form.selec
    }, false)
})