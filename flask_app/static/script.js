
function signUp() {
    var signUp = document.querySelector('#signup-btn');
    signUp.remove();
}

function logIn() {
    var logIn = document.querySelector('#login-btn');
    logIn.remove();
}


const alertJourney = document.getElementById('journey')

const alertj = (message, type) => {
    const wrapper = document.createElement('div')
    wrapper.innerHTML = [
        `<div class="alert alert-${type} alert-dismissible" role="alert">`,
        `   <div>${message}</div>`,
        '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
        '</div>'
    ].join('')

    alertJourney.append(wrapper)
}

const journeyTrigger = document.getElementById('journeyBtn')
if (journeyTrigger) {
    journeyTrigger.addEventListener('click', () => {
        alertj('Hoorha! Your journey begins!', 'success')
    })
}

const alertquest = document.getElementById('quest')

const alertq = (message, type) => {
    const wrapper = document.createElement('div')
    wrapper.innerHTML = [
        `<div class="alert alert-${type} alert-dismissible" role="alert">`,
        `   <div>${message}</div>`,
        '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
        '</div>'
    ].join('')

    alertquest.append(wrapper)
}

const questTrigger = document.getElementById('questBtn')
if (questTrigger) {
    questTrigger.addEventListener('click', () => {
        alertq('Hoorha! Your quest begins!', 'success')
    })
}

const alerthunt = document.getElementById('hunt')

const alerth = (message, type) => {
    const wrapper = document.createElement('div')
    wrapper.innerHTML = [
        `<div class="alert alert-${type} alert-dismissible" role="alert">`,
        `   <div>${message}</div>`,
        '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
        '</div>'
    ].join('')

    alerthunt.append(wrapper)
}

const huntTrigger = document.getElementById('huntBtn')
if (huntTrigger) {
    huntTrigger.addEventListener('click', () => {
        alerth('Hoorha! Your hunt begins!', 'success')
    })
}

const alertmerc = document.getElementById('merc')

const alertm = (message, type) => {
    const wrapper = document.createElement('div')
    wrapper.innerHTML = [
        `<div class="alert alert-${type} alert-dismissible" role="alert">`,
        `   <div>${message}</div>`,
        '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
        '</div>'
    ].join('')

    alertmerc.append(wrapper)
}

const mercTrigger = document.getElementById('mercBtn')
if (mercTrigger) {
    mercTrigger.addEventListener('click', () => {
        alertj('Hoorha! Your hired a merc!', 'success')
    })
}

// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
            }

            form.classList.add('was-validated')
        }, false)
    })
})()

