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
print()
respostas_certas = 0
for pergunta_k, pergunta_v in perguntas.items():
    print(f'{pergunta_k}: {pergunta_v["pergunta"]}')

    print('Respostas: ')
    for resposta_k, resposta_v in pergunta_v['respostas'].items():
        print(f'[{resposta_k}]: {resposta_v}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pergunta_v['resposta_certa']:
        print('DALE ACERTOU, VAMO!!!!')
        respostas_certas += 1
    else:
        print('Hmmmm faiou em amigo')

print(f'Você acertou {respostas_certas} perguntas')