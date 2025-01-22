Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
        console.log('ok1');
        if (!form.checkValidity()) {
            console.log('ok');

            event.preventDefault()
            event.stopPropagation()
        }
        console.log('looooog')
        form.classList.add('was-validated')
    }, false)
})