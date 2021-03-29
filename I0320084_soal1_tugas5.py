nama = str(input('Ketik nama anda : '))
jk = str(input('wanita/pria : '))
while True:
    if jk == 'wanita':
        print('Selamat datang, Ibu', str(nama) )
    elif jk == 'pria':\
        print('Selamat datang, Bapak', str(nama) )
    else :
        print('Data yang anda masukkan salah, mohon periksa kembali')
    break
print('=' * 50)