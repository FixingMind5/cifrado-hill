from django.shortcuts import render

# Create your views here.
key = [
    [1, 0, 6],
    [2, 4, 1],
    [4, 0, 3]
]

def _split_empty(word):
    array = []
    for i in word:
        if i == " ":
            continue
        else:
            array.append(i)

    return array

alphabet = _split_empty("abcdefghijklmnñopqrstuvwxyz")

def _know_scalar(vector):
    array = []
    count = 0

    for i in range(len(vector)):
        for j in alphabet:
            count += 1
            if vector[i] == j:
                array.append(count)

        count = 0

    return array


def _split_all_scalars(allScalars):
    count = 0
    temporalyArray = []
    everyScalar = []

    for i in allScalars:
        count += 1
        temporalyArray.append(i)
        if (count % 3) == 0:
            everyScalar.append(temporalyArray)
            temporalyArray = []

    if len(temporalyArray) != 0:
        everyScalar.append(temporalyArray)

    return everyScalar


def _matrix_multiplication(key, scalars):
    k = 0
    newScalar = 0
    newScalars = []

    while(k < len(scalars)):
        for i in range(3):
            for j in range(3):
                newScalar += key[i][j] * scalars[k][j]
                newScalar %= 27
            newScalars.append(newScalar + 1)
            newScalar = 0
        k += 1
    return newScalars


def _create_hill_string(newScalars):
    count = 0
    newString = ""

    for i in newScalars:
        for j in alphabet:
            count += 1
            if i == count:
                newString += j
        count = 0
    return newString


def _is_not_empty(everyScalar):
    for i in range(len(everyScalar)):
        while len(everyScalar[i]) < 3:
            everyScalar[i].append(11)


def cifrado(request):

    if request.method == 'POST':
        #myString = ""
        normalText = request.POST.get('normalText')
        cleanedVector = _split_empty(normalText)
        allOfScalars = _know_scalar(cleanedVector)
        everyScalar = _split_all_scalars(allOfScalars)
        _is_not_empty(everyScalar)
        newScalars = _matrix_multiplication(key, everyScalar)
        # myString =
        dict = [{ 'hillString' : _create_hill_string(newScalars).upper() }]


        # insertar en el html el hillString
        return render(request, 'index.html', dict[0])

    return render(request, 'index.html')
