import redis
import time

# Redis bağlantısını kurun
r = redis.Redis(host='localhost', port=6379, db=0)

# Başlangıç zamanını kaydedin
start_time = time.time()

# Büyük miktarda veri oluşturun
data = {}
for i in range(1000000):
    key = f'anahtar-{i}'
    value = f'deger-{i}'
    data[key] = value

# Veriyi Redis'e yazın
r.mset(data)

# Bitiş zamanını kaydedin
end_time = time.time()

# İşlem süresini hesaplayın
execution_time = end_time - start_time

print(f"Veri Redis'e yazma süresi: {execution_time} saniye")
