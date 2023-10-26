idade = int(input('Qual sua idade? '))
if idade < 18:
    print('Vai embora!')
elif 17 < idade < 50:
    area = str(input('Qual area você tem interesse? [Química/Física/Matemática/Português/História/Geografia] ')).strip().upper()[0]
    while area not in 'QFMPHG':
        area = str(input('Area inválida, digite novamente [Química/Física/Matemática/Português/História/Geografia]: ')).strip().upper()[0]
    facul = str(input('Está cursando alguma faculdade? [Sim/Não] ')).strip().upper()[0]
    while facul not in 'SN':
        facul = str(input('Resposta inválida\n Está cursando alguma faculdade? [Sim/Não] ')).strip().upper()[0]
    if facul == 'S':
        sem = int(input('Qual semestre? [1-10] '))
        dsp = str(input('Você tem disponibilidade em qual período? [Manhã/Tarde/Noite] ')).strip().upper()[0]
        while dsp not in 'MTN':
            dsp = str(input('Periodo inválido, digite novamente [Manhã/Tarde/Noite]: ')).strip().upper()[0]
        if sem > 3 and area in 'QFM' and dsp in 'MT':
            if area == 'Q':
                area = 'Química'
            elif area == 'F':
                area = 'Física'
            elif area == 'M':
                area = 'Matemática'
            print('Tenho um emprego para você')
            print(f'Achamos uma vaga na area de {area} no periodo da {dsp}')
    else:
        print('Vai embora!')
