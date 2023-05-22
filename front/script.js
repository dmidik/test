const volume = document.querySelector('#volume');
const sum = document.querySelector('#sum');

volume.addEventListener('input', (ev) => {
    sum.textContent = ev.target.value;
})