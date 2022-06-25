// Code from taken and edited from Pyplane Youtube channel
// This Javascript file is the code for the star rating system used in the forms

//Star rating for condition of property
const oneOne = document.getElementById('1.1');
const twoOne = document.getElementById('2.1');
const threeOne = document.getElementById('3.1');
const fourOne = document.getElementById('4.1');
const fiveOne = document.getElementById('5.1');

const formOne = document.querySelector('.rate-form')
const csrfOne = document.getElementsByName('csrfmiddlewaretoken');

const handleSelectOne = (selection) => {
    switch (selection) {
        case '1.1': {
            oneOne.classList.add('checked');
            twoOne.classList.remove('checked');
            threeOne.classList.remove('checked');
            fourOne.classList.remove('checked');
            fiveOne.classList.remove('checked');
            return;
        }
        case '2.1': {
            oneOne.classList.add('checked');
            twoOne.classList.add('checked');
            threeOne.classList.remove('checked');
            fourOne.classList.remove('checked');
            fiveOne.classList.remove('checked');
            return;
        }
        case '3.1': {
            oneOne.classList.add('checked');
            twoOne.classList.add('checked');
            threeOne.classList.add('checked');
            fourOne.classList.remove('checked');
            fiveOne.classList.remove('checked');
            return;
        }
        case '4.1': {
            oneOne.classList.add('checked');
            twoOne.classList.add('checked');
            threeOne.classList.add('checked');
            fourOne.classList.add('checked');
            fiveOne.classList.remove('checked');
            return;
        }
        case '5.1': {
            oneOne.classList.add('checked');
            twoOne.classList.add('checked');
            threeOne.classList.add('checked');
            fourOne.classList.add('checked');
            fiveOne.classList.add('checked');
            return;
        }
    }
}

const getNumericValueOne = (stringValue) => {
    let numericValue;
    if (stringValue === '1.1') {
        numericValue = 1;
    } else if (stringValue === '2.1') {
        numericValue = 2;
    } else if (stringValue === '3.1') {
        numericValue = 3;
    } else if (stringValue === '4.1') {
        numericValue = 4;
    } else if (stringValue === '5.1') {
        numericValue = 5;
    } else {
        numericValue = 0;
    }
    return numericValue;
}


const arrOne = [oneOne, twoOne, threeOne, fourOne, fiveOne];

arrOne.forEach(item => item.addEventListener('mouseover', (event) => {
    handleSelectOne(event.target.id)
}));

arrOne.forEach(item => item.addEventListener('click', (event) => {
    const valOne = event.target.id

    formOne.addEventListener('submit', e => {
        e.preventDefault
        const val_numOne = getNumericValue(valOne);
        alert(val_numOne)
    })
}));

//Star rating for quality of landlord
const oneTwo = document.getElementById('1.2');
const twoTwo = document.getElementById('2.2');
const threeTwo = document.getElementById('3.2');
const fourTwo = document.getElementById('4.2');
const fiveTwo = document.getElementById('5.2');

const formTwo = document.querySelector('.rate-form')
const csrfTwo = document.getElementsByName('csrfmiddlewaretoken');

const handleSelectTwo = (selection) => {
    switch (selection) {
        case '1.2': {
            oneTwo.classList.add('checked');
            twoTwo.classList.remove('checked');
            threeTwo.classList.remove('checked');
            fourTwo.classList.remove('checked');
            fiveTwo.classList.remove('checked');
            return;
        }
        case '2.2': {
            oneTwo.classList.add('checked');
            twoTwo.classList.add('checked');
            threeTwo.classList.remove('checked');
            fourTwo.classList.remove('checked');
            fiveTwo.classList.remove('checked');
            return;
        }
        case '3.2': {
            oneTwo.classList.add('checked');
            twoTwo.classList.add('checked');
            threeTwo.classList.add('checked');
            fourTwo.classList.remove('checked');
            fiveTwo.classList.remove('checked');
            return;
        }
        case '4.2': {
            oneTwo.classList.add('checked');
            twoTwo.classList.add('checked');
            threeTwo.classList.add('checked');
            fourTwo.classList.add('checked');
            fiveTwo.classList.remove('checked');
            return;
        }
        case '5.2': {
            oneTwo.classList.add('checked');
            twoTwo.classList.add('checked');
            threeTwo.classList.add('checked');
            fourTwo.classList.add('checked');
            fiveTwo.classList.add('checked');
            return;
        }
    }
}

const getNumericValueTwo = (stringValue) => {
    let numericValue;
    if (stringValue === '1.2') {
        numericValue = 1;
    } else if (stringValue === '2.2') {
        numericValue = 2;
    } else if (stringValue === '3.2') {
        numericValue = 3;
    } else if (stringValue === '4.2') {
        numericValue = 4;
    } else if (stringValue === '5.2') {
        numericValue = 5;
    } else {
        numericValue = 0;
    }
    return numericValue;
}


const arrTwo = [oneTwo, twoTwo, threeTwo, fourTwo, fiveTwo];

arrTwo.forEach(item => item.addEventListener('mouseover', (event) => {
    handleSelectTwo(event.target.id)
}));

arrTwo.forEach(item => item.addEventListener('click', (event) => {
    const valTwo = event.target.id

    formTwo.addEventListener('submit', e => {
        e.preventDefault
        const val_numTwo = getNumericValue(valTwo);
        alert(val_numTwo)
    })
}));

//Star rating for rate the neighbourhood
const oneThree = document.getElementById('1.3');
const twoThree = document.getElementById('2.3');
const threeThree = document.getElementById('3.3');
const fourThree = document.getElementById('4.3');
const fiveThree = document.getElementById('5.3');

const formThree = document.querySelector('.rate-form')
const csrfThree = document.getElementsByName('csrfmiddlewaretoken');

const handleSelectThree = (selection) => {
    switch (selection) {
        case '1.3': {
            oneThree.classList.add('checked');
            twoThree.classList.remove('checked');
            threeThree.classList.remove('checked');
            fourThree.classList.remove('checked');
            fiveThree.classList.remove('checked');
            return;
        }
        case '2.3': {
            oneThree.classList.add('checked');
            twoThree.classList.add('checked');
            threeThree.classList.remove('checked');
            fourThree.classList.remove('checked');
            fiveThree.classList.remove('checked');
            return;
        }
        case '3.3': {
            oneThree.classList.add('checked');
            twoThree.classList.add('checked');
            threeThree.classList.add('checked');
            fourThree.classList.remove('checked');
            fiveThree.classList.remove('checked');
            return;
        }
        case '4.3': {
            oneThree.classList.add('checked');
            twoThree.classList.add('checked');
            threeThree.classList.add('checked');
            fourThree.classList.add('checked');
            fiveThree.classList.remove('checked');
            return;
        }
        case '5.3': {
            oneThree.classList.add('checked');
            twoThree.classList.add('checked');
            threeThree.classList.add('checked');
            fourThree.classList.add('checked');
            fiveThree.classList.add('checked');
            return;
        }
    }
}

const getNumericValueThree = (stringValue) => {
    let numericValue;
    if (stringValue === '1.3') {
        numericValue = 1;
    } else if (stringValue === '2.3') {
        numericValue = 2;
    } else if (stringValue === '3.3') {
        numericValue = 3;
    } else if (stringValue === '4.3') {
        numericValue = 4;
    } else if (stringValue === '5.3') {
        numericValue = 5;
    } else {
        numericValue = 0;
    }
    return numericValue;
}


const arrThree = [oneThree, twoThree, threeThree, fourThree, fiveThree];

arrThree.forEach(item => item.addEventListener('mouseover', (event) => {
    handleSelectThree(event.target.id)
}));

arrThree.forEach(item => item.addEventListener('click', (event) => {
    const valThree = event.target.id

    formThree.addEventListener('submit', e => {
        e.preventDefault
        const val_numThree = getNumericValue(valThree);
        alert(val_numThree)
    })
}));

//Star rating for value for money
const oneFour = document.getElementById('1.4');
const twoFour = document.getElementById('2.4');
const threeFour = document.getElementById('3.4');
const fourFour = document.getElementById('4.4');
const fiveFour = document.getElementById('5.4');

const formFour = document.querySelector('.rate-form')
const csrfFour = document.getElementsByName('csrfmiddlewaretoken');

const handleSelectFour = (selection) => {
    switch (selection) {
        case '1.4': {
            oneFour.classList.add('checked');
            twoFour.classList.remove('checked');
            threeFour.classList.remove('checked');
            fourFour.classList.remove('checked');
            fiveFour.classList.remove('checked');
            return;
        }
        case '2.4': {
            oneFour.classList.add('checked');
            twoFour.classList.add('checked');
            threeFour.classList.remove('checked');
            fourFour.classList.remove('checked');
            fiveFour.classList.remove('checked');
            return;
        }
        case '3.4': {
            oneFour.classList.add('checked');
            twoFour.classList.add('checked');
            threeFour.classList.add('checked');
            fourFour.classList.remove('checked');
            fiveFour.classList.remove('checked');
            return;
        }
        case '4.4': {
            oneFour.classList.add('checked');
            twoFour.classList.add('checked');
            threeFour.classList.add('checked');
            fourFour.classList.add('checked');
            fiveFour.classList.remove('checked');
            return;
        }
        case '5.4': {
            oneFour.classList.add('checked');
            twoFour.classList.add('checked');
            threeFour.classList.add('checked');
            fourFour.classList.add('checked');
            fiveFour.classList.add('checked');
            return;
        }
    }
}

const getNumericValueFour = (stringValue) => {
    let numericValue;
    if (stringValue === '1.4') {
        numericValue = 1;
    } else if (stringValue === '2.4') {
        numericValue = 2;
    } else if (stringValue === '3.4') {
        numericValue = 3;
    } else if (stringValue === '4.4') {
        numericValue = 4;
    } else if (stringValue === '5.4') {
        numericValue = 5;
    } else {
        numericValue = 0;
    }
    return numericValue;
}


const arrFour = [oneFour, twoFour, threeFour, fourFour, fiveFour];

arrFour.forEach(item => item.addEventListener('mouseover', (event) => {
    handleSelectFour(event.target.id)
}));

arrFour.forEach(item => item.addEventListener('click', (event) => {
    const valFour = event.target.id

    formFour.addEventListener('submit', e => {
        e.preventDefault
        const val_numFour = getNumericValue(valFour);
        alert(val_numFour)
    })
}));

//Star rating for standard of amenities nearby
const oneFive = document.getElementById('1.5');
const twoFive = document.getElementById('2.5');
const threeFive = document.getElementById('3.5');
const fourFive = document.getElementById('4.5');
const fiveFive = document.getElementById('5.5');

const formFive = document.querySelector('.rate-form')
const csrfFive = document.getElementsByName('csrfmiddlewaretoken');

const handleSelectFive = (selection) => {
    switch (selection) {
        case '1.5': {
            oneFive.classList.add('checked');
            twoFive.classList.remove('checked');
            threeFive.classList.remove('checked');
            fourFive.classList.remove('checked');
            fiveFive.classList.remove('checked');
            return;
        }
        case '2.5': {
            oneFive.classList.add('checked');
            twoFive.classList.add('checked');
            threeFive.classList.remove('checked');
            fourFive.classList.remove('checked');
            fiveFive.classList.remove('checked');
            return;
        }
        case '3.5': {
            oneFive.classList.add('checked');
            twoFive.classList.add('checked');
            threeFive.classList.add('checked');
            fourFive.classList.remove('checked');
            fiveFive.classList.remove('checked');
            return;
        }
        case '4.5': {
            oneFive.classList.add('checked');
            twoFive.classList.add('checked');
            threeFive.classList.add('checked');
            fourFive.classList.add('checked');
            fiveFive.classList.remove('checked');
            return;
        }
        case '5.5': {
            oneFive.classList.add('checked');
            twoFive.classList.add('checked');
            threeFive.classList.add('checked');
            fourFive.classList.add('checked');
            fiveFive.classList.add('checked');
            return;
        }
    }
}

const getNumericValueFive = (stringValue) => {
    let numericValue;
    if (stringValue === '1.5') {
        numericValue = 1;
    } else if (stringValue === '2.5') {
        numericValue = 2;
    } else if (stringValue === '3.5') {
        numericValue = 3;
    } else if (stringValue === '4.5') {
        numericValue = 4;
    } else if (stringValue === '5.5') {
        numericValue = 5;
    } else {
        numericValue = 0;
    }
    return numericValue;
}


const arrFive = [oneFive, twoFive, threeFive, fourFive, fiveFive];

arrFive.forEach(item => item.addEventListener('mouseover', (event) => {
    handleSelectFive(event.target.id)
}));

arrFive.forEach(item => item.addEventListener('click', (event) => {
    const valFive = event.target.id

    formFive.addEventListener('submit', e => {
        e.preventDefault
        const val_numFive = getNumericValue(valFive);
        alert(val_numFive)
    })
}));