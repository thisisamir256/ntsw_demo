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


//show user avatar after select file
function previewUploadingImage(inputId, ImgId) {
    const chooseFile = document.getElementById(inputId);
    const imgPreview = document.getElementById(ImgId);
    chooseFile.addEventListener("change", function () {
        getImgData();
        console.log('ok');
    });
    function getImgData() {
        const files = chooseFile.files[0];
        if (files) {
            const fileReader = new FileReader();
            fileReader.readAsDataURL(files);
            fileReader.addEventListener("load", function () {
                imgPreview.src = this.result
            });
        }
    }
}
