/* This code was built by Daniel Roa */
const regexAlphabet = /^[a-zA-Z_ ]+$/;

let nombreValido = false, primerApellidoValido = false, segundoApellidoValido = false, cumpleaniosValido = false, lugarNacValido = false, cpValido = false, clabeValido = false, curpValido = false;

let firstSetValidate = false, secondSetValidate = false, thirdSetValidate = false, fourthSetValidate = false, allDone = false;

let nombre = '', primerApellido = '', segundoApellido = '', birthDate = '', paisNacimiento = '', cp = '', data = '', colonia = [], selColonia = '', clabeInput = '', bankName = '', curpIn = '', noTel= '';

function unhideSets() {

    if (firstSetValidate == true) {
        document.getElementById('secondSet').removeAttribute('hidden');
    } else {
        window.alert('ERROR');
    }

    if (firstSetValidate == true && secondSetValidate == true) {
        document.getElementById('thirdSet').removeAttribute('hidden');
    } else {
        //window.alert('ERROR');
    }

    if (firstSetValidate == true && secondSetValidate == true && thirdSetValidate == true) {
        document.getElementById('fourthSet').removeAttribute('hidden');
    } else {
        //window.alert('ERROR');
    }

    if (firstSetValidate == true && secondSetValidate == true && thirdSetValidate == true && fourthSetValidate == true) {
        document.getElementById('fifthSet').removeAttribute('hidden');
    } else {
        //window.alert('ERROR');
    }

    if (allDone == true) {
        document.getElementById('enviar').removeAttribute('disabled');
    } else {
        //window.alert('ERROR');
    }
}

function validarNombre(field) {

    nombre = field.value;

    if (!nombre.match(regexAlphabet)) {

        field.style.background = 'red';
        window.alert('No puede dejar campos vacios');

    } else if (field.value.length > 0) {
        nombreValido = true;

        field.style.background = 'white';

    }

}

function validarPApellido(field) {

    primerApellido = field.value;

    if (!primerApellido.match(regexAlphabet)) {

        field.style.background = 'red';

    } else if (field.value.length > 0) {
        primerApellidoValido = true;

        field.style.background = 'white';
    }
}

function validarSApellido(field) {

    segundoApellido = field.value;

    if (!segundoApellido.match(regexAlphabet)) {

        field.style.background = 'red';

    } else if (field.value.length > 0) {
        segundoApellidoValido = true;

        field.style.background = 'white';

        if (nombreValido == true && primerApellidoValido == true && segundoApellidoValido == true) {
            firstSetValidate = true;

            unhideSets();
        }

    }
}

function checkBirthDate(field) {

    birthDate = new Date(field.value);

    cumpleaniosValido = true;
}

function lugarNacimiento(field) {

    paisNacimiento = field.value;

    if (!paisNacimiento.match(regexAlphabet)) {
        window.alert('ERROR');
        field.style.background = 'red';
    } else if (paisNacimiento.length > 0) {
        lugarNacValido = true;

        field.style.background = 'white';
    }
}

async function autoFillInfo(field) {
    let cp = field.value;
    let token = '2d3686a6-4028-45aa-aa1c-c4828e7cf5bb';

    try {
        const response = await fetch(
            `https://api-sepomex.hckdrk.mx/query/info_cp/${cp}?=simplified&token=${token}`
        )

        data = await response.json();

        if (data.error !== false) {
            cpValido = true;

            const { response } = data[0];
            const fullResponse = data;

            console.log(response);

            //console.log(fullResponse);

            for (i in fullResponse) {
                colonia[i] = fullResponse[i];
            }

            console.log(colonia);

            document.getElementById('Estado').value = response.estado;
            document.getElementById('Municipio').value = response.municipio;
            //document.getElementById('Colonia').value = response.asentamiento;

            if (firstSetValidate == true && cumpleaniosValido == true && lugarNacValido == true && cpValido == true) {
                secondSetValidate = true;

                fillSelect();
                unhideSets();
            }
        }

    } catch (error) {
        console.log(error)
    }
}

function fillSelect() {

    var opts = document.getElementById('selectColonia');

    let res = '';

    for (i in colonia) {
        res = colonia[i].response;

        opts.options[opts.options.length] = new Option(res.asentamiento);
    }

}

function validaColonia(field) {
    selColonia = field.value;

    console.log(selColonia.length);

    if (!selColonia.match(regexAlphabet)) {

        field.style.background = 'red';

    } else if (selColonia.length > 0) {
        console.log('I´m here');
        field.style.background = 'white';
        thirdSetValidate = true;


        unhideSets();
    }
}

function validateBank(field) {
    let clabeDig = '';

    clabeInput = field.value;

    if (clabeInput.length != 18) {
        window.alert('El tamaño de la CLABE no es de 18 digitos!')
        console.log(clabeInput.length)
    } else {
        
        
        clabeDig = clabeInput.substring(0, 3);
        
        bankName = bankID[clabeDig];
        
        console.log(bankName);
        
        if (bankName === undefined) {
            window.alert('Verifique su CLABE una vez mas.')
        } else {
            document.getElementById('NombreBanco').value = bankName;
            clabeValido = true;
        }
        
    }
}

function validarCurp(field) {

    curpIn = field.value;

    console.log(curpIn);

    if (curpIn.length != 18) {
        window.alert('Cheque su CURP otra vez!')
    } else {
        curpValido = true;

        if (curpValido == true && clabeValido == true) {
            fourthSetValidate = true;

            unhideSets();
        }
    }
}

function verificarTel(field) {
    noTel = field.value;

    if (noTel.length !== 10) {
        window.alert('Verifique el número ingresado')
    } else {
        allDone = true;

        unhideSets();
    }
    
}

function printData() {
    
    let userLastNames = primerApellido + ' ' + segundoApellido;

    let userValues = {
        userName: nombre,
        lastName: userLastNames,
        dateOfBirth: birthDate,
        placeOfBirth: paisNacimiento,
        postalCode: cp,
        colony: selColonia,
        userClabe: clabeInput,
        userBank: bankName,
        userCurp: curpIn,
        emergencyPhoneNo: noTel
    }

    const ouptputFile = JSON.stringify(userValues);

    console.log('In file format\n', ouptputFile);
    console.log('In regular JSON format\n', userValues);


}