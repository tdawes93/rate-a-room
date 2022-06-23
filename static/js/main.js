// Code from taken and edited from Pyplane Youtube channel

//get all the stars
const one = document.getElementById('first');
const two = document.getElementById('second');
const three = document.getElementById('third');
const four = document.getElementById('fourth');
const five = document.getElementById('fifth');

const form = document.querySelector('.rate-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken');

const handleStarSelect = (size) => {
    const children = document.querySelector('.rate-btn')
    console.log(children[0])
    for (let i = 0; i < children.length; i++) {
        if (i <= size) {
            children[i].classList.add('checked')
        } else {
            children[i].classList.remove('checked')
        }
    }
}

const handleSelect = (selection) => {
    switch (selection) {
        case 'first': {
            one.classList.add('checked');
            two.classList.remove('checked');
            three.classList.remove('checked');
            four.classList.remove('checked');
            five.classList.remove('checked');
            return;
        }
        case 'second': {
            one.classList.add('checked');
            two.classList.add('checked');
            three.classList.remove('checked');
            four.classList.remove('checked');
            five.classList.remove('checked');
            return;
        }
        case 'third': {
            one.classList.add('checked');
            two.classList.add('checked');
            three.classList.add('checked');
            four.classList.remove('checked');
            five.classList.remove('checked');
            return;
        }
        case 'fourth': {
            one.classList.add('checked');
            two.classList.add('checked');
            three.classList.add('checked');
            four.classList.add('checked');
            five.classList.remove('checked');
            return;
        }
        case 'fifth': {
            one.classList.add('checked');
            two.classList.add('checked');
            three.classList.add('checked');
            four.classList.add('checked');
            five.classList.add('checked');
            return;
        }
    }
}

const getNumericValue = (stringValue) => {
    let numericValue;
    if (stringValue === 'first') {
        numericValue = 1;
    } else if (stringValue === 'second') {
        numericValue = 2;
    } else if (stringValue === 'third') {
        numericValue = 3;
    } else if (stringValue === 'fourth') {
        numericValue = 4;
    } else if (stringValue === 'fifth') {
        numericValue = 5;
    } else {
        numericValue = 0;
    }
    return numericValue;
}


const arr = [one, two, three, four, five];

arr.forEach(item => item.addEventListener('mouseover', (event) => {
    handleSelect(event.target.id)
}));

arr.forEach(item => item.addEventListener('click', (event) => {
    const val = event.target.id

    form.addEventListener('submit', e => {
        e.preventDefault
        const val_num = getNumericValue(val);
        alert(val_num)
    })
}));