# SYSTEM.py

A simple algorithm in python, using dictionary.

## About Dictionary

This program is one way that we have to use the concept of dictionary in python. Then, what is a "dictionary"? Well it's very similar to lists (content index).
Although, when we use lists, python itself generate an index to us but into the dictionary we will generate this index. 

## The Algorithm

We start with the declaration of the dictionary as "perguntas", where we'll put the questions and answers. Into the dictionary each key has to have it's own value.

```py 

perguntas = {
    'Pergunta 1': { 
        'pergunta': 'Quanto é 2+2',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '14',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'quanto é 10/2?',
        'respostas': {
            'a': '3',
            'b': '5',
            'c': '2',
        },
        'resposta_certa': 'b'
    },
}

```

After that, we will declare a variable that we will use to save the number of correct answers.
As: 

```py

respostas_certas = 0

```

Okay!! Now we have to create a way to compare that answer of the usuary and the value save in the dictionary regarding the question is being asked.
For this, here comes a concept wich we will use, call 'Iterate'.
Iterate: it will be used to obtain the dictionary value and compare it with the answers, through the command "For". This commando allow us todeclare two variables, and separate them into 'variable_k' (k = key) and 'variable_v' (v = value) so that we can show the user the question and the options for the answers.

```py
for pergunta_k, pergunta_v in perguntas.items():
    print(f'{pergunta_k}: {pergunta_v["pergunta"]}')
```
This is our "For" master command, as the answers will be processed according to the iteration of this loop. It is worth remembering that within this loop there were other loopings. 
As we can see there is a function ".items()", which is used to access the key and value in the dictionary, making the user able to see if it is the first question and its content. 
Well, proceeding: 
```py

print('Respostas: ')
    for resposta_k, resposta_v in pergunta_v['respostas'].items():
        print(f'[{resposta_k}]: {resposta_v}')

    resposta_usuario = input('Sua resposta: ')
```
In this part, we will access the "reposta" key in the dictionary and later its value wich are the options for the question and also receive the answer from the user. 
Remember that this is the loop inside the loop master.
After this loop, we have a conditional that checks if the answer is correct, if yes show the user "Parabéns, você acertou!!!" else "Hmm errou em amigo".

```py
    if resposta_usuario == pergunta_v['resposta_certa']:
        print('Parabéns, você acertou!!!!')
        respostas_certas += 1
    else:
        print('Hmmmm errou em amigo')

```
Note that we also put another variable "respostas_certas" to count how many answers were correct. 
At the end we show to the user the amount of hits. 
Showing the whole loop:

```py
for pergunta_k, pergunta_v in perguntas.items():
    print(f'{pergunta_k}: {pergunta_v["pergunta"]}')

    print('Respostas: ')
    for resposta_k, resposta_v in pergunta_v['respostas'].items():
        print(f'[{resposta_k}]: {resposta_v}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pergunta_v['resposta_certa']:
        print('Parabéns, você acertou!!!!')
        respostas_certas += 1
    else:
        print('Hmmmm errou em amigo')

print(f'Você acertou {respostas_certas} pergunta(s)')

```
See you!!

