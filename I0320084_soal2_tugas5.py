nama = str(input('Ketik nama Anda : '))
nilai = float(input('Masukkan nilai anda dalam angka :'))
while True:
    if nilai<60:
        print('Halo,', nama, '!', 'Nilai anda setelah dikonversi adalah E')
    elif 60<=nilai<=64:\
        print('Halo,', nama, '!', 'Nilai anda setelah dikonversi adalah C')
    elif 65<=nilai<=69:\
        print('Halo,', nama, '!', 'Nilai anda setelah dikonversi adalah C+')
    elif 70<=nilai<=74:\
        print('Halo,', nama, '!', 'Nilai anda setelah dikonversi adalah B')
    elif 75<=nilai<=79:\
        print('Halo,', nama, '!', 'Nilai anda setelah dikonversi adalah B+')
    elif 80<=nilai<=84:\
        print('Halo,', nama, '!', 'Nilai anda setelah dikonversi adalah A-')
    elif 85<=nilai<=100:\
        print('Halo,', nama, '!', 'Nilai anda setelah dikonversi adalah A')
    else:
        print('Nilai yang anda masukkan tidak valid untuk dikonversi, silahkan periksa kembali.')
    break
print('=' * 50)