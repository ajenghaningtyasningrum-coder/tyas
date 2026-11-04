print("=== SISTEM PENILAIAN MAHASISWA ===")

jumlah = int(input("Masukkan jumlah mahasiswa (5-10): "))

if 5 <= jumlah <= 10:
    total_nilai = 0
    
    for i in range(1, jumlah + 1):
        nilai = float(input(f"Masukkan nilai mahasiswa {i}: "))
        total_nilai += nilai
      
        if nilai >= 60:
            status = "lulus"
        else:
            status = "tidak lulus"
            
        print(f"Status mahasiswa {i}: {status}")
    
    rata_rata = total_nilai / jumlah
    print(f"Rata-rata nilai kelas: {rata_rata}")
    
    if rata_rata >= 90:
        print("PREDIKAT KELAS : SANGAT BAGUS")
    else:
        print("PREDIKAT KELAS : BAIK / CUKUP")
