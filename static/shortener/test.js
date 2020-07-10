function isValidUrl(str) {
    let pattern = new RegExp('^(https?:\\/\\/)?'+
    '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+
    '((\\d{1,3}\\.){3}\\d{1,3}))'+
    '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ 
    '(\\?[;&a-z\\d%_.~+=-]*)?'+ 
    '(\\#[-a-z\\d_]*)?$','i')
    return !!pattern.test(str)
}

function ready() {
    let form_element = document.getElementById('main_form')
    let err_message_element = document.getElementById('err_message')

    form_element.addEventListener('submit', function(event) {
        let formData = new FormData(form_element)
        
        let link_text = formData.get('link')

        if (!isValidUrl(link_text)) {
            err_message_element.innerHTML = 'Некорректная ссылка'
            event.preventDefault()
            return
        }

        err_message_element.innerHTML = ''
    })
}

document.addEventListener('DOMContentLoaded', ready)
